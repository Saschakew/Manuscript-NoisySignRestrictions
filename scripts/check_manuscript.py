"""Mechanical checks for a standalone manuscript repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")
REQUIRED_PATHS = [
    "AGENTS.md",
    "knowledge-vault-link.json",
    "bibliography/references.bib",
    "manuscript/project-dashboard.md",
    "manuscript/source-packet.md",
    "manuscript/paper-map.md",
    "manuscript/task-board.md",
    "manuscript/draft.md",
    "manuscript/manuscript-rules.md",
    "manuscript/formal-object-registry.json",
    "manuscript/citation-provenance.md",
    "manuscript/replication/README.md",
    "manuscript/transparency/README.md",
    "manuscript/transparency/timeline.json",
    "manuscript/transparency/user-input.jsonl",
    "manuscript/transparency/agent-actions.jsonl",
    "manuscript/transparency/schema/milestone.schema.json",
    "scripts/transparency_milestone.py",
]
TEXT_SUFFIXES = {".bib", ".css", ".html", ".js", ".json", ".md", ".py", ".txt", ".yml", ".yaml"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on template placeholders even when template_mode is true.",
    )
    return parser.parse_args()


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report parse failures cleanly.
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return {}


def load_jsonl(path: Path, errors: list[str]) -> list[dict]:
    items: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception as exc:  # noqa: BLE001 - report read failures cleanly.
        errors.append(f"{path.relative_to(ROOT)} could not be read: {exc}")
        return items
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)} line {line_number} is not valid JSON: {exc}")
            continue
        if not isinstance(item, dict):
            errors.append(f"{path.relative_to(ROOT)} line {line_number} must be a JSON object.")
            continue
        items.append(item)
    return items


def iter_text_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__", ".venv"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.name == "initialize_manuscript.py":
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def validate_transparency(link: dict, errors: list[str], warnings: list[str]) -> None:
    transparency = link.get("transparency", {}) if link else {}
    if not transparency:
        errors.append("knowledge-vault-link.json must define transparency metadata.")
        return
    if transparency.get("schema_version") != 1:
        errors.append("knowledge-vault-link.json transparency.schema_version must be 1.")

    timeline_rel = transparency.get("timeline", "manuscript/transparency/timeline.json")
    timeline_path = ROOT / timeline_rel
    timeline = load_json(timeline_path, errors)
    if timeline:
        if timeline.get("schema_version") != 1:
            errors.append("manuscript/transparency/timeline.json must have schema_version 1.")
        if not isinstance(timeline.get("milestones"), list):
            errors.append("manuscript/transparency/timeline.json must contain a milestones list.")
        if timeline.get("snapshot_tag_prefix") != transparency.get("snapshot_tag_prefix"):
            warnings.append("Transparency timeline and link file should use the same snapshot_tag_prefix.")

    user_input_rel = transparency.get("user_input_log", "manuscript/transparency/user-input.jsonl")
    action_rel = transparency.get("agent_action_log", "manuscript/transparency/agent-actions.jsonl")
    user_inputs = load_jsonl(ROOT / user_input_rel, errors)
    actions = load_jsonl(ROOT / action_rel, errors)
    user_input_ids = {item.get("id") for item in user_inputs}
    action_ids = {item.get("id") for item in actions}

    milestones_dir = ROOT / transparency.get("milestones_dir", "manuscript/transparency/milestones")
    if milestones_dir.exists():
        for path in sorted(milestones_dir.glob("*.json")):
            milestone = load_json(path, errors)
            if not milestone:
                continue
            missing = [
                key
                for key in [
                    "schema_version",
                    "id",
                    "sequence",
                    "title",
                    "kind",
                    "status",
                    "opened_at",
                    "start_commit",
                    "snapshot_ref",
                    "user_inputs",
                    "agent_actions",
                    "checks",
                    "changed_files",
                ]
                if key not in milestone
            ]
            if missing:
                errors.append(f"{path.relative_to(ROOT)} missing required fields: {', '.join(missing)}")
            if milestone.get("schema_version") != 1:
                errors.append(f"{path.relative_to(ROOT)} must have schema_version 1.")
            if milestone.get("status") not in {"open", "closed"}:
                errors.append(f"{path.relative_to(ROOT)} status must be open or closed.")
            if milestone.get("kind") not in {"user-request", "progress", "review", "release", "maintenance"}:
                errors.append(f"{path.relative_to(ROOT)} has an unknown kind.")
            for item in milestone.get("user_inputs", []):
                if item.get("id") and item.get("id") not in user_input_ids:
                    warnings.append(f"{path.relative_to(ROOT)} user input {item.get('id')} is not in user-input.jsonl.")
            for item in milestone.get("agent_actions", []):
                if item.get("id") and item.get("id") not in action_ids:
                    warnings.append(f"{path.relative_to(ROOT)} action {item.get('id')} is not in agent-actions.jsonl.")

    active_path = ROOT / "manuscript" / "transparency" / "active-milestone.json"
    if active_path.exists():
        warnings.append("A transparency milestone is open; close it before publishing a milestone snapshot.")


def validate_computational_package(
    link: dict,
    vault_path: Path | None,
    template_mode: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    package = link.get("computational_package", {}) if link else {}
    if not package:
        errors.append("knowledge-vault-link.json must define computational_package metadata.")
        return
    if package.get("name") != "svar-python":
        warnings.append("computational_package.name should be svar-python.")
    if package.get("import_name") != "svar_toolkit":
        warnings.append("computational_package.import_name should be svar_toolkit.")
    if not package.get("required", False):
        warnings.append("computational_package.required should be true.")

    candidates = package.get("path_candidates", [])
    if not isinstance(candidates, list) or not candidates:
        errors.append("computational_package.path_candidates must be a non-empty list.")
        return

    if template_mode:
        return

    if not vault_path or not vault_path.exists():
        warnings.append("Cannot validate svar-python because the KnowledgeVault local path is unavailable.")
        return

    resolved = ""
    for rel in candidates:
        if (vault_path / rel).exists():
            resolved = rel
            break
    if not resolved:
        warnings.append(
            "KnowledgeVault local path does not contain the required svar-python package candidates: "
            + ", ".join(str(item) for item in candidates)
        )
        return

    recorded = package.get("resolved_path", "")
    if recorded and recorded.rstrip("/\\") != resolved.rstrip("/\\"):
        warnings.append(
            "computational_package.resolved_path differs from the detected svar-python path: "
            + resolved.rstrip("/\\")
        )
    if package.get("status") != "validated":
        warnings.append("computational_package.status should be validated after package orientation.")


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required path: {rel}")

    link = load_json(ROOT / "knowledge-vault-link.json", errors)
    registry = load_json(ROOT / "manuscript" / "formal-object-registry.json", errors)

    template_mode = bool(link.get("template_mode", False))
    slug = link.get("manuscript_slug", "")
    if link and link.get("schema_version") != 1:
        errors.append("knowledge-vault-link.json must have schema_version 1.")
    if link and not slug:
        errors.append("knowledge-vault-link.json must define manuscript_slug.")
    if registry:
        if registry.get("schema_version") != 1:
            errors.append("formal-object-registry.json must have schema_version 1.")
        if not isinstance(registry.get("objects"), list):
            errors.append("formal-object-registry.json must contain an objects list.")
        if slug and registry.get("manuscript") != slug:
            errors.append("formal-object-registry.json manuscript must match knowledge-vault-link.json.")

    if link:
        vault = link.get("knowledge_vault", {})
        orientation = link.get("vault_orientation", {})
        local_hint = vault.get("local_path_hint", "")
        required_surfaces = orientation.get("required_surfaces", [])
        vault_path: Path | None = None
        if not template_mode:
            if not local_hint:
                warnings.append("KnowledgeVault local_path_hint is empty; Codex will need to ask for the vault path.")
            else:
                vault_path = Path(local_hint)
                if not vault_path.is_absolute():
                    vault_path = (ROOT / vault_path).resolve()
                if not vault_path.exists():
                    warnings.append(f"KnowledgeVault local_path_hint does not exist: {local_hint}")
                else:
                    missing = [rel for rel in required_surfaces if not (vault_path / rel).exists()]
                    if missing:
                        warnings.append(
                            "KnowledgeVault local_path_hint is missing required surfaces: "
                            + ", ".join(missing)
                        )
            if orientation.get("source_packet") != "manuscript/source-packet.md":
                warnings.append("vault_orientation.source_packet should be manuscript/source-packet.md.")
            if orientation.get("status") != "validated":
                warnings.append("KnowledgeVault orientation has not been marked validated.")
        validate_computational_package(link, vault_path, template_mode, errors, warnings)
        validate_transparency(link, errors, warnings)

    unresolved: list[str] = []
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        if PLACEHOLDER_RE.search(text):
            unresolved.append(str(path.relative_to(ROOT)))
    if unresolved:
        message = "Template placeholders remain in: " + ", ".join(sorted(unresolved))
        if template_mode and not args.strict:
            warnings.append(message)
        else:
            errors.append(message)

    if errors:
        print("Manuscript check failed:")
        for item in errors:
            print(f"- {item}")
        if warnings:
            print("\nWarnings:")
            for item in warnings:
                print(f"- {item}")
        return 1

    print("Manuscript check passed.")
    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

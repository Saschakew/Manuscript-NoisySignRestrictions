"""Initialize a repository copied from the manuscript template."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TEXT_SUFFIXES = {
    ".bib",
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yml",
    ".yaml",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="Lowercase hyphen-case manuscript slug.")
    parser.add_argument("--title", required=True, help="Working manuscript title.")
    parser.add_argument("--vault-url", default="", help="KnowledgeVault repository URL.")
    parser.add_argument(
        "--vault-local-path",
        default="",
        help="Local KnowledgeVault path hint. If omitted, common sibling paths are detected.",
    )
    parser.add_argument("--vault-commit", default="", help="KnowledgeVault commit SHA used for the initial source snapshot.")
    parser.add_argument(
        "--skip-vault-validation",
        action="store_true",
        help="Initialize even when no local KnowledgeVault checkout can be validated.",
    )
    parser.add_argument(
        "--source",
        action="append",
        default=[],
        help="KnowledgeVault path or external URL that started the manuscript. May be repeated.",
    )
    return parser.parse_args()


def run_git(path: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def required_vault_surfaces() -> list[str]:
    link_path = ROOT / "knowledge-vault-link.json"
    data = json.loads(link_path.read_text(encoding="utf-8"))
    return list(data.get("vault_orientation", {}).get("required_surfaces", []))


def computational_package_candidates() -> list[str]:
    link_path = ROOT / "knowledge-vault-link.json"
    data = json.loads(link_path.read_text(encoding="utf-8"))
    package = data.get("computational_package", {})
    return list(package.get("path_candidates", []))


def vault_missing_surfaces(path: Path) -> list[str]:
    missing: list[str] = []
    for rel in required_vault_surfaces():
        if not (path / rel).exists():
            missing.append(rel)
    return missing


def detect_vault_path() -> Path | None:
    candidates = [
        ROOT.parent / "KnowledgeVault",
        ROOT.parent.parent / "KnowledgeVault",
        ROOT / "KnowledgeVault",
    ]
    for candidate in candidates:
        if candidate.exists() and not vault_missing_surfaces(candidate):
            return candidate
    return None


def resolve_vault_path_hint(local_hint: str) -> Path | None:
    if not local_hint:
        return None
    path = Path(local_hint)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    return path


def normalize_local_hint(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(ROOT.resolve())
        return rel.as_posix()
    except ValueError:
        try:
            rel = path.resolve().relative_to(ROOT.parent.resolve())
            return f"../{rel.as_posix()}"
        except ValueError:
            return str(path)


def prepare_vault_link(args: argparse.Namespace) -> tuple[str, str, str, str]:
    local_hint = args.vault_local_path
    vault_path: Path | None = None

    if local_hint:
        candidate = Path(local_hint)
        if not candidate.is_absolute():
            candidate = (ROOT / candidate).resolve()
        vault_path = candidate
    else:
        vault_path = detect_vault_path()
        if vault_path:
            local_hint = normalize_local_hint(vault_path)

    if vault_path:
        missing = vault_missing_surfaces(vault_path)
        if missing and not args.skip_vault_validation:
            missing_text = ", ".join(missing)
            raise SystemExit(
                f"KnowledgeVault path could not be validated: {vault_path}\n"
                f"Missing required surfaces: {missing_text}\n"
                "Pass --vault-local-path with the correct checkout or "
                "--skip-vault-validation to initialize without local vault access."
            )

    if not local_hint and not args.skip_vault_validation:
        raise SystemExit(
            "No local KnowledgeVault checkout was found. Pass --vault-local-path "
            "or use --skip-vault-validation if this manuscript will connect later."
        )

    vault_url = args.vault_url
    vault_commit = args.vault_commit
    orientation_status = "not-validated"
    if vault_path and not vault_missing_surfaces(vault_path):
        orientation_status = "validated"
        if not vault_url:
            vault_url = run_git(vault_path, "remote", "get-url", "origin")
        if not vault_commit:
            vault_commit = run_git(vault_path, "rev-parse", "HEAD")

    return local_hint, vault_url, vault_commit, orientation_status


def find_computational_package(vault_path: Path | None) -> tuple[str, str]:
    if not vault_path or not vault_path.exists():
        return "", "not-validated"
    for rel in computational_package_candidates():
        candidate = vault_path / rel
        if candidate.exists():
            return rel.rstrip("/\\"), "validated"
    return "", "missing"


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


def replace_placeholders(replacements: dict[str, str]) -> None:
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        updated = text
        for key, value in replacements.items():
            updated = updated.replace(key, value)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")


def update_link_file(
    args: argparse.Namespace,
    today: str,
    vault_local_path: str,
    vault_url: str,
    vault_commit: str,
    orientation_status: str,
    package_path: str,
    package_status: str,
) -> None:
    path = ROOT / "knowledge-vault-link.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["template_mode"] = False
    data["manuscript_slug"] = args.slug
    data["working_title"] = args.title
    data["knowledge_vault"]["repository"] = vault_url
    data["knowledge_vault"]["local_path_hint"] = vault_local_path
    data["knowledge_vault"]["commit"] = vault_commit
    data["vault_orientation"]["last_validated"] = today if orientation_status == "validated" else ""
    data["vault_orientation"]["status"] = orientation_status
    if args.source:
        data["knowledge_vault"]["source_material"] = [
            {
                "type": "vault-path" if not re.match(r"^https?://", source) else "url",
                "path_or_url": source,
                "title": "",
                "note": "Initial source material supplied during repository initialization.",
            }
            for source in args.source
        ]
    data["citation_snapshot"]["last_synced"] = today
    if "computational_package" in data:
        data["computational_package"]["resolved_path"] = package_path
        data["computational_package"]["version_or_commit"] = vault_commit
        data["computational_package"]["status"] = package_status
    if "transparency" in data:
        data["transparency"]["status"] = "initialized"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    args = parse_args()
    if not SLUG_RE.match(args.slug):
        raise SystemExit("Slug must be lowercase hyphen case, e.g. proxy-exogeneity-note.")

    today = dt.date.today().isoformat()
    vault_local_path, vault_url, vault_commit, orientation_status = prepare_vault_link(args)
    package_path, package_status = find_computational_package(resolve_vault_path_hint(vault_local_path))
    replacements = {
        "{{MANUSCRIPT_SLUG}}": args.slug,
        "{{WORKING_TITLE}}": args.title,
        "{{KNOWLEDGE_VAULT_REPOSITORY_URL}}": vault_url,
        "{{KNOWLEDGE_VAULT_LOCAL_PATH}}": vault_local_path,
        "{{KNOWLEDGE_VAULT_COMMIT}}": vault_commit,
        "{{KNOWLEDGE_VAULT_ORIENTATION_STATUS}}": orientation_status,
        "{{TODAY}}": today,
    }
    update_link_file(
        args,
        today,
        vault_local_path,
        vault_url,
        vault_commit,
        orientation_status,
        package_path,
        package_status,
    )
    replace_placeholders(replacements)

    print(f"Initialized manuscript repository: {args.slug}")
    print(f"Working title: {args.title}")
    print(f"KnowledgeVault local path: {vault_local_path or 'not connected'}")
    print(f"KnowledgeVault orientation status: {orientation_status}")
    print(f"svar-python package status: {package_status}")
    print("Next: edit manuscript/project-dashboard.md and run python scripts/check_manuscript.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

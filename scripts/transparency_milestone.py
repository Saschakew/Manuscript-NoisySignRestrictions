"""Create and close machine-readable manuscript transparency milestones."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSPARENCY_DIR = ROOT / "manuscript" / "transparency"
MILESTONES_DIR = TRANSPARENCY_DIR / "milestones"
TIMELINE_PATH = TRANSPARENCY_DIR / "timeline.json"
ACTIVE_PATH = TRANSPARENCY_DIR / "active-milestone.json"
USER_INPUT_PATH = TRANSPARENCY_DIR / "user-input.jsonl"
AGENT_ACTION_PATH = TRANSPARENCY_DIR / "agent-actions.jsonl"
TAG_PREFIX = "manuscript-milestones/"


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:48].strip("-") or "milestone"


def run_git(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def ensure_dirs() -> None:
    MILESTONES_DIR.mkdir(parents=True, exist_ok=True)


def read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path.relative_to(ROOT)} is not valid JSON: {exc}") from exc


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")


def append_jsonl(path: Path, item: dict) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(item, ensure_ascii=True) + "\n")


def load_timeline() -> dict:
    link = read_json(ROOT / "knowledge-vault-link.json", {})
    default = {
        "schema_version": 1,
        "manuscript_slug": link.get("manuscript_slug", ""),
        "working_title": link.get("working_title", ""),
        "snapshot_tag_prefix": TAG_PREFIX,
        "updated_at": "",
        "milestones": [],
    }
    return read_json(TIMELINE_PATH, default)


def next_sequence(timeline: dict) -> int:
    sequences = [int(item.get("sequence", 0)) for item in timeline.get("milestones", [])]
    return max(sequences, default=0) + 1


def milestone_path(milestone_id: str) -> Path:
    return MILESTONES_DIR / f"{milestone_id}.json"


def read_request_text(args: argparse.Namespace) -> str:
    if args.request_file:
        return Path(args.request_file).read_text(encoding="utf-8").strip()
    return args.request.strip()


def timeline_entry_from_milestone(milestone: dict) -> dict:
    return {
        "id": milestone["id"],
        "sequence": milestone["sequence"],
        "title": milestone["title"],
        "kind": milestone["kind"],
        "status": milestone["status"],
        "opened_at": milestone["opened_at"],
        "closed_at": milestone.get("closed_at", ""),
        "start_commit": milestone.get("start_commit", ""),
        "snapshot_ref": milestone.get("snapshot_ref", ""),
        "summary": milestone.get("summary", ""),
        "user_input_ids": [item["id"] for item in milestone.get("user_inputs", [])],
        "milestone_path": f"manuscript/transparency/milestones/{milestone['id']}.json",
        "github": milestone.get("github", {}),
    }


def upsert_timeline_entry(timeline: dict, milestone: dict) -> None:
    entry = timeline_entry_from_milestone(milestone)
    entries = timeline.setdefault("milestones", [])
    for index, existing in enumerate(entries):
        if existing.get("id") == milestone["id"]:
            entries[index] = entry
            break
    else:
        entries.append(entry)
    entries.sort(key=lambda item: item.get("sequence", 0))
    timeline["updated_at"] = utc_now()
    if "snapshot_tag_prefix" not in timeline:
        timeline["snapshot_tag_prefix"] = TAG_PREFIX


def changed_files_since(start_commit: str) -> list[str]:
    changed: set[str] = set()
    if start_commit:
        diff = run_git("diff", "--name-only", start_commit, "--")
        changed.update(line.strip() for line in diff.splitlines() if line.strip())
    untracked = run_git("ls-files", "--others", "--exclude-standard")
    changed.update(line.strip() for line in untracked.splitlines() if line.strip())
    return sorted(changed)


def begin(args: argparse.Namespace) -> int:
    ensure_dirs()
    if ACTIVE_PATH.exists() and not args.allow_nested:
        active = read_json(ACTIVE_PATH, {})
        raise SystemExit(
            "A transparency milestone is already open: "
            f"{active.get('id', 'unknown')}. Close it or pass --allow-nested."
        )

    request_text = read_request_text(args)
    if not request_text:
        raise SystemExit("Provide --request or --request-file so the user input is captured.")

    now = utc_now()
    timeline = load_timeline()
    sequence = next_sequence(timeline)
    milestone_id = f"M{sequence:04d}-{slugify(args.title)}"
    snapshot_ref = args.snapshot_ref or f"{TAG_PREFIX}{milestone_id}"
    user_input = {
        "id": f"U{sequence:04d}-001",
        "milestone_id": milestone_id,
        "captured_at": now,
        "source": args.source,
        "text": request_text,
    }
    milestone = {
        "schema_version": 1,
        "id": milestone_id,
        "sequence": sequence,
        "title": args.title,
        "kind": args.kind,
        "status": "open",
        "opened_at": now,
        "closed_at": "",
        "start_commit": run_git("rev-parse", "HEAD"),
        "snapshot_ref": snapshot_ref,
        "summary": "",
        "user_inputs": [user_input],
        "agent_actions": [],
        "checks": [],
        "changed_files": [],
        "github": {
            "repository": args.github_repository,
            "milestone_number": args.github_milestone_number,
            "milestone_url": args.github_milestone_url,
            "tag_name": snapshot_ref,
        },
    }

    write_json(milestone_path(milestone_id), milestone)
    append_jsonl(USER_INPUT_PATH, user_input)
    upsert_timeline_entry(timeline, milestone)
    write_json(TIMELINE_PATH, timeline)
    write_json(ACTIVE_PATH, {"id": milestone_id, "path": str(milestone_path(milestone_id).relative_to(ROOT))})

    print(f"Opened transparency milestone {milestone_id}")
    print(f"Snapshot ref to tag after closing: {snapshot_ref}")
    return 0


def close(args: argparse.Namespace) -> int:
    ensure_dirs()
    if args.id:
        milestone_id = args.id
    elif ACTIVE_PATH.exists():
        milestone_id = read_json(ACTIVE_PATH, {}).get("id", "")
    else:
        raise SystemExit("No active milestone found. Pass --id to close a specific milestone.")
    if not milestone_id:
        raise SystemExit("Could not determine milestone id.")

    path = milestone_path(milestone_id)
    milestone = read_json(path, {})
    if not milestone:
        raise SystemExit(f"Milestone manifest not found: {path.relative_to(ROOT)}")
    if milestone.get("status") == "closed" and not args.reopen:
        raise SystemExit(f"Milestone {milestone_id} is already closed. Pass --reopen to update it.")

    now = utc_now()
    milestone["status"] = "closed"
    milestone["closed_at"] = now
    milestone["summary"] = args.summary.strip()
    if args.snapshot_ref:
        milestone["snapshot_ref"] = args.snapshot_ref
        milestone.setdefault("github", {})["tag_name"] = args.snapshot_ref
    if args.github_repository:
        milestone.setdefault("github", {})["repository"] = args.github_repository
    if args.github_milestone_url:
        milestone.setdefault("github", {})["milestone_url"] = args.github_milestone_url
    if args.github_milestone_number is not None:
        milestone.setdefault("github", {})["milestone_number"] = args.github_milestone_number

    action_offset = len(milestone.get("agent_actions", [])) + 1
    for index, description in enumerate(args.action, start=action_offset):
        action = {
            "id": f"A{milestone['sequence']:04d}-{index:03d}",
            "milestone_id": milestone_id,
            "captured_at": now,
            "description": description,
        }
        milestone.setdefault("agent_actions", []).append(action)
        append_jsonl(AGENT_ACTION_PATH, action)

    for description in args.check:
        milestone.setdefault("checks", []).append(
            {
                "captured_at": now,
                "description": description,
            }
        )

    milestone["changed_files"] = changed_files_since(milestone.get("start_commit", ""))
    write_json(path, milestone)

    timeline = load_timeline()
    upsert_timeline_entry(timeline, milestone)
    write_json(TIMELINE_PATH, timeline)
    if ACTIVE_PATH.exists() and read_json(ACTIVE_PATH, {}).get("id") == milestone_id:
        ACTIVE_PATH.unlink()

    print(f"Closed transparency milestone {milestone_id}")
    print(f"Snapshot ref: {milestone.get('snapshot_ref', '')}")
    print("Commit these changes, then tag that commit with the snapshot ref.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    begin_parser = subparsers.add_parser("begin", help="Open a transparency milestone.")
    begin_parser.add_argument("--title", required=True, help="Short milestone title.")
    begin_parser.add_argument("--request", default="", help="User request or close paraphrase.")
    begin_parser.add_argument("--request-file", default="", help="UTF-8 text file containing the request.")
    begin_parser.add_argument(
        "--kind",
        choices=["user-request", "progress", "review", "release", "maintenance"],
        default="user-request",
    )
    begin_parser.add_argument("--source", default="chat", help="Input source label.")
    begin_parser.add_argument("--snapshot-ref", default="", help="Git ref that will snapshot this milestone.")
    begin_parser.add_argument("--github-repository", default="", help="GitHub repository in owner/name form.")
    begin_parser.add_argument("--github-milestone-url", default="", help="Optional GitHub milestone URL.")
    begin_parser.add_argument("--github-milestone-number", type=int, default=None)
    begin_parser.add_argument("--allow-nested", action="store_true", help="Allow opening while another is active.")
    begin_parser.set_defaults(func=begin)

    close_parser = subparsers.add_parser("close", help="Close a transparency milestone.")
    close_parser.add_argument("--id", default="", help="Milestone id. Defaults to the active milestone.")
    close_parser.add_argument("--summary", required=True, help="Short summary of the completed work.")
    close_parser.add_argument("--action", action="append", default=[], help="Codex action taken. May repeat.")
    close_parser.add_argument("--check", action="append", default=[], help="Check run and outcome. May repeat.")
    close_parser.add_argument("--snapshot-ref", default="", help="Override the Git ref for this snapshot.")
    close_parser.add_argument("--github-repository", default="", help="GitHub repository in owner/name form.")
    close_parser.add_argument("--github-milestone-url", default="", help="Optional GitHub milestone URL.")
    close_parser.add_argument("--github-milestone-number", type=int, default=None)
    close_parser.add_argument("--reopen", action="store_true", help="Allow updating a closed milestone.")
    close_parser.set_defaults(func=close)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

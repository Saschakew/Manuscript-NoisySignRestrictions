"""Launch the M74 sample-size Monte Carlo as a detached background process."""

from __future__ import annotations

import argparse
import ctypes
import json
import os
import signal
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SIM_SCRIPT = ROOT / "manuscript" / "simulations" / "m69_extended_three_block_mc.py"
OUTPUT_DIR = ROOT / "manuscript" / "simulations" / "output"
NOTE_OUTPUT = ROOT / "manuscript" / "simulations" / "m74_sample_size_mc_500_grid27.md"
JSON_OUTPUT = OUTPUT_DIR / "m74_sample_size_mc_500_grid27.json"
PROGRESS_OUTPUT = OUTPUT_DIR / "m74_sample_size_mc_500_grid27.progress.json"
PROGRESS_LOG = OUTPUT_DIR / "m74_sample_size_mc_500_grid27.log"
ERR_LOG = OUTPUT_DIR / "m74_sample_size_mc_500_grid27.err.log"
PID_FILE = OUTPUT_DIR / "m74_sample_size_mc_500_grid27.pid"
LAUNCH_MANIFEST = OUTPUT_DIR / "m74_sample_size_mc_500_grid27.launch.json"


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def is_pid_running(pid: int) -> bool:
    if pid <= 0:
        return False
    if os.name != "nt":
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        return True

    process_query_limited_information = 0x1000
    still_active = 259
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.OpenProcess(process_query_limited_information, False, pid)
    if not handle:
        return False
    try:
        exit_code = ctypes.c_ulong()
        if not kernel32.GetExitCodeProcess(handle, ctypes.byref(exit_code)):
            return False
        return exit_code.value == still_active
    finally:
        kernel32.CloseHandle(handle)


def read_existing_pid() -> int | None:
    for path in (PID_FILE, PROGRESS_OUTPUT):
        if not path.exists():
            continue
        try:
            if path == PID_FILE:
                return int(path.read_text(encoding="utf-8").strip())
            payload = json.loads(path.read_text(encoding="utf-8"))
            pid = payload.get("pid")
            if pid is not None:
                return int(pid)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
    return None


def command() -> list[str]:
    return [
        sys.executable,
        str(SIM_SCRIPT),
        "--block",
        "sample_size_grid",
        "--evaluation-reps",
        "500",
        "--projection-points",
        "27",
        "--profile-points",
        "7",
        "--lambda-points",
        "5",
        "--json-output",
        str(JSON_OUTPUT),
        "--note-output",
        str(NOTE_OUTPUT),
        "--progress-output",
        str(PROGRESS_OUTPUT),
        "--progress-log-output",
        str(PROGRESS_LOG),
    ]


def clean_monitor_files() -> None:
    for path in (PROGRESS_OUTPUT, PROGRESS_LOG, ERR_LOG, PID_FILE, LAUNCH_MANIFEST):
        try:
            path.unlink()
        except FileNotFoundError:
            continue


def launch(force: bool) -> dict[str, object]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    existing_pid = read_existing_pid()
    if existing_pid is not None and is_pid_running(existing_pid) and not force:
        raise SystemExit(f"M74 appears to be running already as PID {existing_pid}.")
    if force:
        clean_monitor_files()

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    creationflags = 0
    popen_kwargs: dict[str, object] = {
        "cwd": str(ROOT),
        "stdin": subprocess.DEVNULL,
        "stdout": subprocess.DEVNULL,
        "stderr": None,
        "close_fds": True,
        "env": env,
    }
    if os.name == "nt":
        creationflags |= getattr(subprocess, "DETACHED_PROCESS", 0)
        creationflags |= getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
        creationflags |= getattr(subprocess, "CREATE_NO_WINDOW", 0)
        popen_kwargs["creationflags"] = creationflags
    else:
        popen_kwargs["start_new_session"] = True
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    cmd = command()
    with ERR_LOG.open("a", encoding="utf-8") as err_handle:
        popen_kwargs["stderr"] = err_handle
        process = subprocess.Popen(cmd, **popen_kwargs)

    PID_FILE.write_text(f"{process.pid}\n", encoding="utf-8", newline="\n")
    manifest = {
        "schema_version": 1,
        "launched_at": now_iso(),
        "pid": process.pid,
        "command": cmd,
        "cwd": str(ROOT),
        "grid": {
            "projection_points": 27,
            "profile_points": 7,
            "lambda_points": 5,
        },
        "reps_per_scenario": 500,
        "block": "sample_size_grid",
        "outputs": {
            "json": str(JSON_OUTPUT),
            "note": str(NOTE_OUTPUT),
            "progress": str(PROGRESS_OUTPUT),
            "progress_log": str(PROGRESS_LOG),
            "error_log": str(ERR_LOG),
            "pid": str(PID_FILE),
        },
    }
    LAUNCH_MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8", newline="\n")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Discard stale monitor files before launching.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = launch(force=args.force)
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

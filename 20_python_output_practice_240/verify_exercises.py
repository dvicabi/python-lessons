#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run all 242 exercises and compare stdout with their embedded final answer."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
START = "# >>> EXPECTED OUTPUT"
END = "# <<< END EXPECTED OUTPUT"

def check(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        first = lines.index(START)
        last = lines.index(END, first + 1)
    except ValueError:
        return "Missing solution markers"

    target_lines = lines[first + 1:last]
    if not target_lines or any(not line.startswith("# ") for line in target_lines):
        return "Malformed solution comments"

    expected = "\n".join(line[2:] for line in target_lines)
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=5,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "Timeout (possible infinite loop)"

    if result.returncode:
        return "Python error: " + result.stderr[:500]
    # Python print(..., end="!") may legitimately omit the last newline.
    actual = result.stdout.rstrip("\n")
    if actual != expected:
        return f"Expected {expected!r}, got {actual!r}"
    return None

def main():
    exercises = sorted(ROOT.glob("0[1-7]_*/exercise_*.py"))
    failures = []
    for file in exercises:
        error = check(file)
        if error is not None:
            failures.append((file.relative_to(ROOT), error))
    for path, reason in failures:
        print(f"FAIL {path}: {reason}")
    print(f"Checked: {len(exercises)} | Passed: {len(exercises) - len(failures)} | Failed: {len(failures)}")
    if len(exercises) != 242 or failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()

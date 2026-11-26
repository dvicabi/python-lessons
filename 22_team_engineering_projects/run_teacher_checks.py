"""Run the teacher reference verifiers for all published team projects."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
verifiers = sorted(root.glob("*/teacher/verify.py"))
if len(verifiers) == 0:
    raise SystemExit("No project verifiers found")
for verifier in verifiers:
    print("\nPROJECT:", verifier.parent.parent.name, flush=True)
    subprocess.run([sys.executable, str(verifier)], check=True)
print("\nPASS:", len(verifiers), "projects")

"""Check the exact Python examples in the graded engineering labs."""
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

TEACHER = Path(__file__).resolve().parent
BASE = TEACHER.parent

def code_blocks(path):
    return re.findall(r"```python\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S)

def check(code, input_text, expected, label):
    if any(isinstance(node, (ast.Break, ast.Continue)) for node in ast.walk(ast.parse(code))):
        raise AssertionError(label + ": forbidden loop-control statement")
    result = subprocess.run(
        [sys.executable, "-c", code],
        input=input_text, capture_output=True, text=True, timeout=5
    )
    if result.returncode != 0 or result.stdout != expected + "\n":
        raise AssertionError(
            f"{label}: expected {expected!r}; got {result.stdout!r}; "
            f"stderr={result.stderr!r}"
        )

def main():
    cases = json.loads((TEACHER / "cases.json").read_text(encoding="utf-8"))
    count = 0
    for name, levels in cases:
        student = code_blocks(BASE / (name + ".md"))
        solutions = code_blocks(TEACHER / (name + "_solution.md"))
        if len(student) != 8 or len(solutions) != 8 or len(levels) != 8:
            raise AssertionError(name + ": incomplete levels")
        for i in range(8):
            given_input, given_output, written_input, written_output = levels[i]
            check(student[i], given_input, given_output, f"{name} level {i+1} trace")
            check(solutions[i], written_input, written_output, f"{name} level {i+1} solution")
            count += 2
        print(name, "16 checks passed")
    print("PASS:", count, "Python output checks")

if __name__ == "__main__":
    main()

"""Verify graded aviation, space and robotics exercises using Python's actual runtime."""
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

def code_blocks(path):
    return re.findall(r"```python\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S)

def check_level(code, level, label):
    tree = ast.parse(code)
    prohibited = (ast.Dict, ast.Set, ast.Tuple, ast.DictComp, ast.SetComp, ast.Break, ast.Continue)
    if level < 8:
        prohibited += (ast.ClassDef,)
    if level < 7:
        prohibited += (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.Return)
    if level < 6:
        prohibited += (ast.List, ast.ListComp, ast.Subscript)
    if level < 5:
        prohibited += (ast.For, ast.While, ast.AsyncFor)
    if level < 4:
        prohibited += (ast.If, ast.IfExp, ast.BoolOp, ast.Compare)
    allowed = {"print"}
    if level >= 3:
        allowed.update(("input", "int"))
    if level >= 5:
        allowed.add("range")
    if level >= 6:
        allowed.add("len")
    for node in ast.walk(tree):
        if isinstance(node, prohibited):
            raise AssertionError(f"{label}: early or forbidden syntax {type(node).__name__}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            name = node.func.id
            if name in ("set", "dict", "tuple", "enumerate", "zip"):
                raise AssertionError(f"{label}: forbidden {name}")
            if level < 7 and name not in allowed:
                raise AssertionError(f"{label}: early call {name}")
    if level == 1:
        for statement in tree.body:
            if not isinstance(statement, ast.Expr) or not isinstance(statement.value, ast.Call) or not isinstance(statement.value.func, ast.Name) or statement.value.func.id != "print":
                raise AssertionError(f"{label}: only print allowed")

def check(code, input_text, expected, level, label):
    check_level(code, level, label)
    result = subprocess.run(
        [sys.executable, "-c", code],
        input=input_text, text=True, capture_output=True, timeout=5
    )
    if result.returncode != 0 or result.stdout != expected:
        raise AssertionError(
            f"{label}: expected {expected!r}, got {result.stdout!r}; stderr={result.stderr!r}"
        )

def main():
    records = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    assert len(records) == 8
    count = 0
    for record in records:
        name = record["id"]
        traces = code_blocks(BASE / (name + ".md"))
        solutions = code_blocks(HERE / (name + "_solution.md"))
        assert len(traces) == len(solutions) == len(record["levels"]) == 8
        for i, case in enumerate(record["levels"]):
            label = f"{name} level {i+1}"
            original = traces[i]
            changed = original
            for old, new in case["edits"]:
                assert changed.count(old) == 1, label
                changed = changed.replace(old, new, 1)
            check(original, case["input"], case["out"], i+1, label + " trace")
            check(changed, case["alt_input"], case["alt_out"], i+1, label + " alternate")
            check(solutions[i], case["solution_input"], case["solution_out"], i+1, label + " solution")
            count += 3
        print(name, "24 checks passed")
    print("PASS:", count, "Python output and prerequisite checks")

if __name__ == "__main__":
    main()

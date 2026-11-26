"""Teacher-only integration checks for the six student components."""
import ast
from pathlib import Path

HERE = Path(__file__).resolve().parent
reference = (HERE / "reference.py").read_text(encoding="utf-8")
base, code = reference.split("# TEAM_CODE\n", 1)
code = code.split("# FINAL_REPORT\n", 1)[0]
tree = ast.parse(code)
for node in ast.walk(tree):
    if isinstance(node, (ast.Break, ast.Continue, ast.Dict, ast.Set, ast.Tuple, ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)):
        raise AssertionError("Unexpected syntax in student-level reference: " + type(node).__name__)
cases = [
    ("תיקון מאושר", "", "result = \"OK\"\ntech = 2\nbay = 0\ntotal = 70\nstock_after = [1, 2, 3]\ntech_after = [40, 60, 30]\nbay_after = [10, 60, 60]\nused_after = [40, 41]"),
    ("חלקים חסרים", "stock = [2, 1, 3]", "result = \"PARTS\"\ntech = -1\nbay = -1\ntotal = -1\nstock_after = [2, 1, 3]\ntech_after = [40, 60, 60]\nbay_after = [40, 60, 60]\nused_after = [40]"),
    ("טכנאים לא פנויים", "tech_time = [29, 60, 29]", "result = \"TECH\"\ntech = -1\nbay = -1\ntotal = -1\nstock_after = [2, 4, 3]\ntech_after = [29, 60, 29]\nbay_after = [40, 60, 60]\nused_after = [40]"),
    ("עמדות מלאות", "bay_time = [29, 29, 60]", "result = \"BAY\"\ntech = -1\nbay = -1\ntotal = -1\nstock_after = [2, 4, 3]\ntech_after = [40, 60, 60]\nbay_after = [29, 29, 60]\nused_after = [40]"),
    ("תקציב חסר", "budget = 69", "result = \"BUDGET\"\ntech = -1\nbay = -1\ntotal = -1\nstock_after = [2, 4, 3]\ntech_after = [40, 60, 60]\nbay_after = [40, 60, 60]\nused_after = [40]"),
]
for name, changes, expected_code in cases:
    ns = {}
    exec(base, ns)
    exec(changes, ns)
    exec(code, ns)
    expected = {}
    exec(expected_code, expected)
    for key, value in expected.items():
        if key != "__builtins__":
            assert ns[key] == value, (name, key, ns[key], value)
    print("PASS:", name)
print("PASS:", len(cases), "integration scenarios")

# Test the second request on the committed state of the first request.
ns = {}
exec(base, ns)
exec(code, ns)
exec("stock = stock_after\ntech_time = tech_after\nbay_time = bay_after\nused = used_after\nticket = 42", ns)
exec(code, ns)
expected = {}
exec("result = \"OK\"\ntech = 2\nbay = 1\ntotal = 75\nstock_after = [0, 0, 3]\ntech_after = [40, 60, 0]\nbay_after = [10, 30, 60]\nused_after = [40, 41, 42]", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

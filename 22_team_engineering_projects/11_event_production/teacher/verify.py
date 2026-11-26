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
    ("אישור", "", "result = \"OK\"\nhall = 2\ntotal = 138\navailable_after = [True, True, False]\nequipment_after = 3\nstaff_after = 2\nused_after = [20, 21]"),
    ("חוסר ציוד", "equipment = 0", "result = \"EQUIPMENT\"\nhall = -1\ntotal = -1\navailable_after = [True, True, True]\nequipment_after = 0\nstaff_after = 4\nused_after = [20]"),
    ("חוסר צוות", "staff = 1", "result = \"STAFF\"\nhall = -1\ntotal = -1\navailable_after = [True, True, True]\nequipment_after = 4\nstaff_after = 1\nused_after = [20]"),
    ("מחיר חורג", "budget = 137", "result = \"BUDGET\"\nhall = -1\ntotal = -1\navailable_after = [True, True, True]\nequipment_after = 4\nstaff_after = 4\nused_after = [20]"),
    ("אין אולם", "guests = 61", "result = \"HALL\"\nhall = -1\ntotal = -1\navailable_after = [True, True, True]\nequipment_after = 4\nstaff_after = 4\nused_after = [20]"),
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
exec("available = available_after\nequipment = equipment_after\nstaff = staff_after\nused = used_after\nevent_id = 22", ns)
exec(code, ns)
expected = {}
exec("result = \"STAFF\"\nhall = -1\ntotal = -1\navailable_after = [True, True, False]\nequipment_after = 3\nstaff_after = 2\nused_after = [20, 21]", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

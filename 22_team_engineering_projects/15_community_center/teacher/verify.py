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
    ("חוג מתאים", "", "result = \"OK\"\ncourse = 1\ntotal = 70\nbusy_after = [[False, True, True, True], [False, False, False, False]]\nseats_after = [2, 2, 1, 4]\ncredits_after = [80, 90]\nused_after = [60, 61]"),
    ("אין יתרה", "credits = [69, 90]", "result = \"CREDIT\"\ncourse = -1\ntotal = -1\nbusy_after = [[False, True, False, False], [False, False, False, False]]\nseats_after = [2, 3, 1, 4]\ncredits_after = [69, 90]\nused_after = [60]"),
    ("חוג מלא", "seats = [2, 0, 1, 4]", "result = \"SEAT\"\ncourse = -1\ntotal = -1\nbusy_after = [[False, True, False, False], [False, False, False, False]]\nseats_after = [2, 0, 1, 4]\ncredits_after = [150, 90]\nused_after = [60]"),
    ("אין פעילות", "activity = 9", "result = \"COURSE\"\ncourse = -1\ntotal = -1\nbusy_after = [[False, True, False, False], [False, False, False, False]]\nseats_after = [2, 3, 1, 4]\ncredits_after = [150, 90]\nused_after = [60]"),
    ("משתתף שני", "person = 102", "result = \"OK\"\ncourse = 0\ntotal = 60\nbusy_after = [[False, True, False, False], [True, True, False, False]]\nseats_after = [1, 3, 1, 4]\ncredits_after = [150, 30]\nused_after = [60, 61]"),
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
exec("busy = busy_after\nseats = seats_after\ncredits = credits_after\nused = used_after\nregistration = 62", ns)
exec(code, ns)
expected = {}
exec("result = \"TIME\"\ncourse = -1\ntotal = -1\nbusy_after = [[False, True, True, True], [False, False, False, False]]\nseats_after = [2, 2, 1, 4]\ncredits_after = [80, 90]\nused_after = [60, 61]", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

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
    ("חדר זול מתאים", "", "result = \"OK\"\nroom = 2\ntotal = 230\nrevenue = 230\nrefund = 30\ncalendar_after = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 21, 21, 21, 20]]\nused_after = [20, 21]"),
    ("אין תקציב", "budget = 229", "result = \"BUDGET\"\nroom = -1\ntotal = -1\nrevenue = 0\nrefund = 260\ncalendar_after = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 20]]\nused_after = [20]"),
    ("לילה אחרון מחוץ ללוח", "start = 3", "result = \"DATES\"\nroom = -1\ntotal = -1\nrevenue = 0\nrefund = 260\ncalendar_after = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 20]]\nused_after = [20]"),
    ("תשלום חסר", "paid = 229", "result = \"PAYMENT\"\nroom = 2\ntotal = 230\nrevenue = 0\nrefund = 229\ncalendar_after = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 20]]\nused_after = [20]"),
    ("קבוצה גדולה", "guests = 5", "result = \"ROOM\"\nroom = -1\ntotal = -1\nrevenue = 0\nrefund = 260\ncalendar_after = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 20]]\nused_after = [20]"),
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
exec("calendar = calendar_after\nused = used_after\nbooking = 22", ns)
exec(code, ns)
expected = {}
exec("result = \"OK\"\nroom = 1\ntotal = 260\nrevenue = 260\nrefund = 0\ncalendar_after = [[0, 0, 0, 0, 0], [0, 22, 22, 22, 0], [0, 21, 21, 21, 20]]\nused_after = [20, 21, 22]", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

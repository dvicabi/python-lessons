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
    ("מהיר", "", "result = \"OK\"\nchosen = [3, 4]\neta = 19\ntotal = 18\nseats_after = [3, 3, 4, 0, 0]\nused_after = [30, 31]\nrevenue = 18\nrefund = 0"),
    ("תקציב", "budget = 14", "result = \"OK\"\nchosen = [0, 1]\neta = 20\ntotal = 14\nseats_after = [1, 1, 4, 2, 2]\nused_after = [30, 31]\nrevenue = 14\nrefund = 4"),
    ("אין מקום", "group_size = 5", "result = \"SEATS\"\nchosen = []\neta = -1\ntotal = -1\nseats_after = [3, 3, 4, 2, 2]\nused_after = [30]\nrevenue = 0\nrefund = 18"),
    ("אין זמן", "latest = 18", "result = \"ROUTE\"\nchosen = []\neta = -1\ntotal = -1\nseats_after = [3, 3, 4, 2, 2]\nused_after = [30]\nrevenue = 0\nrefund = 18"),
    ("אין תשלום", "paid = 17", "result = \"PAYMENT\"\nchosen = [3, 4]\neta = 19\ntotal = 18\nseats_after = [3, 3, 4, 2, 2]\nused_after = [30]\nrevenue = 0\nrefund = 17"),
    ("תקציב נמוך", "budget = 13", "result = \"BUDGET\"\nchosen = []\neta = -1\ntotal = -1\nseats_after = [3, 3, 4, 2, 2]\nused_after = [30]\nrevenue = 0\nrefund = 18"),
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
exec("seats = seats_after\nused = used_after\nticket = 32", ns)
exec(code, ns)
expected = {}
exec("result = \"OK\"\nchosen = [0, 1]\neta = 20\ntotal = 14\nseats_after = [1, 1, 4, 0, 0]\nused_after = [30, 31, 32]\nrevenue = 14\nrefund = 4", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

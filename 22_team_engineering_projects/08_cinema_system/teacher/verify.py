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
    ("הקרנה שנייה מתאימה", "", "result = \"OK\"\nshow = 1\nrow_index = 0\nstart_col = 0\ntotal = 90\ndiscount = 15\nrevenue = 90\nrefund = 10\nused_after = [7, 8, 11]\nhalls_after = [[[0, 0, 7, 0], [7, 0, 8, 0]], [[11, 11, 11, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]"),
    ("קבוצה קטנה", "group_size = 2", "result = \"OK\"\nshow = 0\nrow_index = 0\nstart_col = 0\ntotal = 60\ndiscount = 0\nrevenue = 60\nrefund = 40\nused_after = [7, 8, 11]\nhalls_after = [[[11, 11, 7, 0], [7, 0, 8, 0]], [[0, 0, 0, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]"),
    ("אין רצף", "group_size = 4", "result = \"SEATS\"\nshow = -1\nrow_index = -1\nstart_col = -1\ntotal = -1\ndiscount = 0\nrevenue = 0\nrefund = 100\nused_after = [7, 8]\nhalls_after = [[[0, 0, 7, 0], [7, 0, 8, 0]], [[0, 0, 0, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]"),
    ("אין הקרנה בזמן", "earliest_start = 130", "result = \"SHOW\"\nshow = -1\nrow_index = -1\nstart_col = -1\ntotal = -1\ndiscount = 0\nrevenue = 0\nrefund = 100\nused_after = [7, 8]\nhalls_after = [[[0, 0, 7, 0], [7, 0, 8, 0]], [[0, 0, 0, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]"),
    ("תשלום חסר", "paid = 89", "result = \"PAYMENT\"\nshow = 1\nrow_index = 0\nstart_col = 0\ntotal = 90\ndiscount = 15\nrevenue = 0\nrefund = 89\nused_after = [7, 8]\nhalls_after = [[[0, 0, 7, 0], [7, 0, 8, 0]], [[0, 0, 0, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]"),
    ("מזהה כפול", "booking_code = 7", "result = \"REQUEST\"\nshow = -1\nrow_index = -1\nstart_col = -1\ntotal = -1\ndiscount = 0\nrevenue = 0\nrefund = 100\nused_after = [7, 8]\nhalls_after = [[[0, 0, 7, 0], [7, 0, 8, 0]], [[0, 0, 0, 8], [7, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]"),
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

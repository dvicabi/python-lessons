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
    ("סל מאושר", "", "result = \"OK\"\ntotal = 36\nstock_after = [4, 1, 4]\nstation_after = [2, 2]\nused_after = [50, 51]\nrevenue = 36\nrefund = 4"),
    ("תפריט לא מתאים", "cart = [[2, 1]]", "result = \"MENU\"\ntotal = -1\nstock_after = [8, 5, 8]\nstation_after = [8, 6]\nused_after = [50]\nrevenue = 0\nrefund = 40"),
    ("רכיב חסר", "stock = [8, 3, 8]", "result = \"INGREDIENTS\"\ntotal = -1\nstock_after = [8, 3, 8]\nstation_after = [8, 6]\nused_after = [50]\nrevenue = 0\nrefund = 40"),
    ("עמדה עמוסה", "station_free = [5, 6]", "result = \"KITCHEN\"\ntotal = -1\nstock_after = [8, 5, 8]\nstation_after = [5, 6]\nused_after = [50]\nrevenue = 0\nrefund = 40"),
    ("כסף חסר", "paid = 35", "result = \"PAYMENT\"\ntotal = 36\nstock_after = [8, 5, 8]\nstation_after = [8, 6]\nused_after = [50]\nrevenue = 0\nrefund = 35"),
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
exec("stock = stock_after\nstation_free = station_after\nused = used_after\norder_id = 52", ns)
exec(code, ns)
expected = {}
exec("result = \"INGREDIENTS\"\ntotal = -1\nstock_after = [4, 1, 4]\nstation_after = [2, 2]\nused_after = [50, 51]\nrevenue = 0\nrefund = 40", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

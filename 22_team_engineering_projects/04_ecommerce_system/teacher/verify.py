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
    ("עסקה מלאה", "", "result = \"OK\"\ntotal = 44\ndiscount = 6\nslot = 2\nstock_after = [2, 2, 7]\ndelivery_after = [2, 0, 2]\nrevenue = 44\nrefund = 6"),
    ("סל כפול חורג", "cart = [[0, 3], [0, 3]]", "result = \"STOCK\"\ntotal = -1\ndiscount = 0\nslot = -1\nstock_after = [5, 4, 7]\ndelivery_after = [2, 0, 3]\nrevenue = 0\nrefund = 50"),
    ("כסף חסר", "paid = 43", "result = \"PAYMENT\"\ntotal = 44\ndiscount = 6\nslot = -1\nstock_after = [5, 4, 7]\ndelivery_after = [2, 0, 3]\nrevenue = 0\nrefund = 43"),
    ("משלוח חסר", "delivery_free = [2, 0, 0]", "result = \"DELIVERY\"\ntotal = 44\ndiscount = 6\nslot = -1\nstock_after = [5, 4, 7]\ndelivery_after = [2, 0, 0]\nrevenue = 0\nrefund = 50"),
    ("לקוח לא פעיל", "customer = 102", "result = \"CUSTOMER\"\ntotal = -1\ndiscount = 0\nslot = -1\nstock_after = [5, 4, 7]\ndelivery_after = [2, 0, 3]\nrevenue = 0\nrefund = 50"),
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

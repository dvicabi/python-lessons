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
    ("משלוח אפשרי", "", "result = \"OK\"\nvehicle = 1\nroute = 1\neta = 9\nstock_after = [6, 2, 2]\nrange_after = [15, 2, 9]"),
    ("מלאי חסר", "quantity = 6", "result = \"STOCK\"\nvehicle = -1\nroute = -1\neta = -1\nstock_after = [6, 5, 2]\nrange_after = [15, 20, 9]"),
    ("אריזה כבדה", "pack_limit = 8", "result = \"PACK\"\nvehicle = -1\nroute = -1\neta = -1\nstock_after = [6, 5, 2]\nrange_after = [15, 20, 9]"),
    ("אין טווח מספיק", "vehicle_range = [8, 8, 8]", "result = \"ROUTE\"\nvehicle = -1\nroute = -1\neta = -1\nstock_after = [6, 5, 2]\nrange_after = [8, 8, 8]"),
    ("שוויון זמן", "route_delay = [2, 0]", "result = \"OK\"\nvehicle = 1\nroute = 0\neta = 9\nstock_after = [6, 2, 2]\nrange_after = [15, 6, 9]"),
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

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
    ("חבילה חוקית", "", "result = \"OK\"\npower_need = 22\nbus = 1\nwater_after = [6, 8]\npower_after = [2, 15]\nbus_after = [5, 0, 6]\nparking_after = [1, 5]"),
    ("חוסר חשמל", "power_available = [21, 15]", "result = \"POWER\"\npower_need = 22\nbus = -1\nwater_after = [10, 8]\npower_after = [21, 15]\nbus_after = [5, 3, 6]\nparking_after = [3, 5]"),
    ("חוסר חניה", "cars = 4", "result = \"PARKING\"\npower_need = 22\nbus = 1\nwater_after = [10, 8]\npower_after = [24, 15]\nbus_after = [5, 3, 6]\nparking_after = [3, 5]"),
    ("בלי נסיעות", "trips = 0", "result = \"OK\"\npower_need = 16\nbus = -1\nwater_after = [6, 8]\npower_after = [8, 15]\nbus_after = [5, 3, 6]\nparking_after = [1, 5]"),
    ("אין מים", "water_need = 11", "result = \"WATER\"\npower_need = 0\nbus = -1\nwater_after = [10, 8]\npower_after = [24, 15]\nbus_after = [5, 3, 6]\nparking_after = [3, 5]"),
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

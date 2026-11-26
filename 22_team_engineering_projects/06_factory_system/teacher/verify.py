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
    ("אצווה אפשרית", "", "result = \"OK\"\nmachine = 2\nminutes = 6\nbad_count = 0\nshipping = 2\nmaterials_after = [5, 9, 7]\nminutes_after = [12, 20, 2]\nshipping_after = [2, 5, 0]\nfulfilled = 3"),
    ("חומר חסר", "materials = [8, 5, 10]", "result = \"MATERIALS\"\nmachine = -1\nminutes = 0\nbad_count = 0\nshipping = -1\nmaterials_after = [8, 5, 10]\nminutes_after = [12, 20, 8]\nshipping_after = [2, 5, 3]\nfulfilled = 0"),
    ("זמן מכונה חסר", "machine_minutes = [12, 8, 5]", "result = \"MACHINE\"\nmachine = -1\nminutes = 0\nbad_count = 0\nshipping = -1\nmaterials_after = [8, 15, 10]\nminutes_after = [12, 8, 5]\nshipping_after = [2, 5, 3]\nfulfilled = 0"),
    ("איכות נדחית", "quality_scores = [80, 69, 90]", "result = \"QUALITY\"\nmachine = 2\nminutes = 6\nbad_count = 1\nshipping = -1\nmaterials_after = [8, 15, 10]\nminutes_after = [12, 20, 8]\nshipping_after = [2, 5, 3]\nfulfilled = 0"),
    ("אין הפצה", "shipping_free = [2, 2, 2]", "result = \"SHIPPING\"\nmachine = 2\nminutes = 6\nbad_count = 0\nshipping = -1\nmaterials_after = [8, 15, 10]\nminutes_after = [12, 20, 8]\nshipping_after = [2, 2, 2]\nfulfilled = 0"),
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

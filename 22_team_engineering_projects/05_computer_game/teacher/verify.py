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
    ("איסוף אנרגיה", "", "result = \"OK\"\nnext_level = 3\nrows_after = [1, 2]\ncols_after = [1, 0]\nenergies_after = [6, 10]\nscores_after = [21, 5]\ngrid_after = [[0, 3, -1, 0], [0, 0, 0, 3], [0, 0, -1, 0]]"),
    ("איסוף מטבע", "rows = [0, 2]", "result = \"OK\"\nnext_level = 4\nrows_after = [0, 2]\ncols_after = [1, 0]\nenergies_after = [3, 10]\nscores_after = [31, 5]\ngrid_after = [[0, 0, -1, 0], [0, 2, 0, 3], [0, 0, -1, 0]]"),
    ("מכשול", "rows = [0, 2]\ncols = [1, 0]", "result = \"BLOCKED\"\nnext_level = 3\nrows_after = [0, 2]\ncols_after = [1, 0]\nenergies_after = [5, 10]\nscores_after = [20, 5]\ngrid_after = [[0, 3, -1, 0], [0, 2, 0, 3], [0, 0, -1, 0]]"),
    ("אנרגיה חסרה", "energies = [1, 10]", "result = \"ENERGY\"\nnext_level = 3\nrows_after = [1, 2]\ncols_after = [0, 0]\nenergies_after = [1, 10]\nscores_after = [20, 5]\ngrid_after = [[0, 3, -1, 0], [0, 2, 0, 3], [0, 0, -1, 0]]"),
    ("מחוץ ללוח", "direction = 4", "result = \"OUTSIDE\"\nnext_level = 3\nrows_after = [1, 2]\ncols_after = [0, 0]\nenergies_after = [5, 10]\nscores_after = [20, 5]\ngrid_after = [[0, 3, -1, 0], [0, 2, 0, 3], [0, 0, -1, 0]]"),
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

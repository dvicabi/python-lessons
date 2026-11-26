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
    ("שיבוץ ראשון", "", "result = \"OK\"\nslot = 0\nteacher = 1\nroom = 2\nteacher_after = [[False, True, True], [False, False, True], [True, True, True]]\nroom_after = [[True, True, True], [False, True, True], [False, True, False]]\ngroup_after = [[False, True, True], [True, False, True]]\ntquota_after = [2, 0, 3]\ngquota_after = [1, 2]"),
    ("מורים ללא מכסה", "teacher_quota = [0, 0, 3]", "result = \"TEACHER\"\nslot = -1\nteacher = -1\nroom = -1\nteacher_after = [[False, True, True], [True, False, True], [True, True, True]]\nroom_after = [[True, True, True], [False, True, True], [True, True, False]]\ngroup_after = [[True, True, True], [True, False, True]]\ntquota_after = [0, 0, 3]\ngquota_after = [2, 2]"),
    ("חדרים קטנים", "room_caps = [24, 25, 27]", "result = \"ROOM\"\nslot = -1\nteacher = -1\nroom = -1\nteacher_after = [[False, True, True], [True, False, True], [True, True, True]]\nroom_after = [[True, True, True], [False, True, True], [True, True, False]]\ngroup_after = [[True, True, True], [True, False, True]]\ntquota_after = [2, 1, 3]\ngquota_after = [2, 2]"),
    ("אין זמן משותף", "group_free = [[False, False, False], [True, False, True]]", "result = \"TIME\"\nslot = -1\nteacher = -1\nroom = -1\nteacher_after = [[False, True, True], [True, False, True], [True, True, True]]\nroom_after = [[True, True, True], [False, True, True], [True, True, False]]\ngroup_after = [[False, False, False], [True, False, True]]\ntquota_after = [2, 1, 3]\ngquota_after = [2, 2]"),
    ("מכסת קבוצה נגמרה", "group_quota = [0, 2]", "result = \"QUOTA\"\nslot = 0\nteacher = 1\nroom = 2\nteacher_after = [[False, True, True], [True, False, True], [True, True, True]]\nroom_after = [[True, True, True], [False, True, True], [True, True, False]]\ngroup_after = [[True, True, True], [True, False, True]]\ntquota_after = [2, 1, 3]\ngquota_after = [0, 2]"),
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

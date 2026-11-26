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
    ("השאלה חוקית", "", "result = \"OK\"\ncopy_index = 2\ndue = 24\nholders_after = [0, 0, 101, 0]\nreserved_after = [102, 0, 0, 0]\nlimits_after = [1, 1]\nused_after = [50, 51]"),
    ("מכסה נגמרה", "limits = [0, 1]", "result = \"LIMIT\"\ncopy_index = 2\ndue = -1\nholders_after = [0, 0, 0, 0]\nreserved_after = [102, 0, 101, 0]\nlimits_after = [0, 1]\nused_after = [50]"),
    ("עותק מרוחק", "holders = [0, 0, 102, 0]", "result = \"OK\"\ncopy_index = 1\ndue = 17\nholders_after = [0, 101, 102, 0]\nreserved_after = [102, 0, 101, 0]\nlimits_after = [1, 1]\nused_after = [50, 51]"),
    ("מזהה חוזר", "loan_id = 50", "result = \"MEMBER\"\ncopy_index = -1\ndue = -1\nholders_after = [0, 0, 0, 0]\nreserved_after = [102, 0, 101, 0]\nlimits_after = [2, 1]\nused_after = [50]"),
    ("אין עותק זמין", "holders = [0, 102, 102, 0]", "result = \"COPY\"\ncopy_index = -1\ndue = -1\nholders_after = [0, 102, 102, 0]\nreserved_after = [102, 0, 101, 0]\nlimits_after = [2, 1]\nused_after = [50]"),
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
exec("holders = holders_after\nreserved = reserved_after\nlimits = limits_after\nused_ids = used_after\nloan_id = 52", ns)
exec(code, ns)
expected = {}
exec("result = \"OK\"\ncopy_index = 1\ndue = 17\nholders_after = [0, 101, 101, 0]\nlimits_after = [0, 1]\nused_after = [50, 51, 52]", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

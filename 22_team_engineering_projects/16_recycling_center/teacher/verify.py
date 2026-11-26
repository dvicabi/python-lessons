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
    ("קליטה מלאה", "", "result = \"OK\"\nplan = [3, 4, 2, 2]\ncredit = 24\nfree_after = [0, 1, 2, 1]\nfund_after = 6\nused_after = [70, 71]\npaid_credit = 24"),
    ("מיון שגוי", "items = [[3, 2, 0]]", "result = \"SORT\"\nplan = [0, 0, 0, 0]\ncredit = 0\nfree_after = [3, 5, 4, 3]\nfund_after = 30\nused_after = [70]\npaid_credit = 0"),
    ("איכות נדחית", "bad_limit = [1, 0, 1]", "result = \"QUALITY\"\nplan = [0, 0, 0, 0]\ncredit = 0\nfree_after = [3, 5, 4, 3]\nfund_after = 30\nused_after = [70]\npaid_credit = 0"),
    ("קיבולת חסרה", "free = [2, 5, 2, 3]", "result = \"CAPACITY\"\nplan = [2, 4, 2, 2]\ncredit = 0\nfree_after = [2, 5, 2, 3]\nfund_after = 30\nused_after = [70]\npaid_credit = 0"),
    ("זיכוי חסר", "fund = 23", "result = \"CREDIT\"\nplan = [3, 4, 2, 2]\ncredit = 24\nfree_after = [3, 5, 4, 3]\nfund_after = 23\nused_after = [70]\npaid_credit = 0"),
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
exec("free = free_after\nfund = fund_after\nused = used_after\nbatch_id = 72", ns)
exec(code, ns)
expected = {}
exec("result = \"CAPACITY\"\nplan = [0, 1, 2, 1]\ncredit = 0\nfree_after = [0, 1, 2, 1]\nfund_after = 6\nused_after = [70, 71]\npaid_credit = 0", expected)
for key, value in expected.items():
    if key != "__builtins__":
        assert ns[key] == value, ("second request", key, ns[key], value)
print("PASS: second request on committed state")

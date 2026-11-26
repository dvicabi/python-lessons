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
    ("אישור מלא", "", "flight_ok = True\npassenger_ready = True\nbag_ready = True\ngate_index = 1\nready_at = 29\nslot_ok = True\nresult = \"OK\"\ngate_busy_after = [False, True, True]\ndeparted_id = 41"),
    ("נוסע חסר", "checked = 4", "flight_ok = True\npassenger_ready = False\nbag_ready = False\ngate_index = -1\nready_at = -1\nslot_ok = False\nresult = \"PASSENGERS\"\ngate_busy_after = [False, False, True]\ndeparted_id = -1"),
    ("מטען שגוי", "bag_weights = [10, 21]", "flight_ok = True\npassenger_ready = True\nbag_ready = False\ngate_index = -1\nready_at = -1\nslot_ok = False\nresult = \"BAGS\"\ngate_busy_after = [False, False, True]\ndeparted_id = -1"),
    ("אין שער", "gate_busy = [True, True, True]", "flight_ok = True\npassenger_ready = True\nbag_ready = True\ngate_index = -1\nready_at = -1\nslot_ok = False\nresult = \"GATE\"\ngate_busy_after = [True, True, True]\ndeparted_id = -1"),
    ("איחור", "now = 24", "flight_ok = True\npassenger_ready = True\nbag_ready = True\ngate_index = 1\nready_at = 33\nslot_ok = False\nresult = \"TIME\"\ngate_busy_after = [False, False, True]\ndeparted_id = -1"),
    ("טיסה לא קיימת", "requested = 999", "flight_ok = False\npassenger_ready = False\nbag_ready = False\ngate_index = -1\nready_at = -1\nslot_ok = False\nresult = \"FLIGHT\"\ngate_busy_after = [False, False, True]\ndeparted_id = -1"),
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

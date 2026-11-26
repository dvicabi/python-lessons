"""Run student trace examples and teacher acceptance tests; Python 3.8+."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import re

BASE = Path(__file__).resolve().parent.parent

def first_python(path):
    text = path.read_text(encoding="utf-8")
    return re.search(r"```python\n(.*?)\n```", text, re.S).group(1)

def check_trace(filename, alternate, expected, alternate_expected):
    code = first_python(BASE / filename)
    stream = StringIO()
    namespace = {}
    with redirect_stdout(stream):
        exec(compile(code, filename, "exec"), namespace)
    assert stream.getvalue().splitlines() == expected, filename + " original"
    stream = StringIO()
    with redirect_stdout(stream):
        namespace["trace"](alternate)
    assert stream.getvalue().splitlines() == alternate_expected, filename + " alternate"

def check_teacher(filename):
    text = (BASE / "teacher" / filename).read_text(encoding="utf-8")
    blocks = re.findall(r"```python\n(.*?)\n```", text, re.S)
    assert len(blocks) == 2, filename
    namespace = {}
    exec(compile(blocks[0], filename, "exec"), namespace)
    exec(compile(blocks[1], filename, "exec"), namespace)

if __name__ == "__main__":
    check_trace("01_washing_machine.md", [6, 0, 0, 2, 4], ["1 FILL 3 0","2 WASH 6 0","3 WASH 6 1","4 DRAIN 6 2","5 DRAIN 2 2","6 DONE 0 2","7 DONE 0 2","8 DONE 0 2"], ["1 WASH 6 0","2 WASH 6 1","3 DRAIN 6 2","4 DRAIN 4 2","5 DONE 0 2"])
    check_teacher("01_washing_machine_solution.md")
    check_trace("02_robot_vacuum.md", ["L", "D", "U", "R", "L"], ["1 MOVED (0, 1) 8 2","2 BLOCKED (0, 1) 6 2","3 MOVED (1, 1) 4 3","4 MOVED (1, 0) 2 4","5 MOVED (2, 0) 0 5","6 STOP (2, 0) 0 5"], ["1 BLOCKED (0, 0) 8 1","2 MOVED (1, 0) 6 2","3 MOVED (0, 0) 4 2","4 MOVED (0, 1) 2 3","5 MOVED (0, 0) 0 3"])
    check_teacher("02_robot_vacuum_solution.md")
    check_trace("03_3d_printer.md", [3, 6, 1], ["1 PRINTED 4 9 1","2 PRINTED 6 3 2","3 PAUSED 5 3 2","FINAL 3 2"], ["1 PRINTED 4 9 1","2 PRINTED 7 2 2","3 PAUSED 2 2 2","FINAL 2 2"])
    check_teacher("03_3d_printer_solution.md")
    check_trace("04_wireless_earbuds.md", [("L",8), ("R",6), ("C",6), ("B",4), ("C",3)], ["1 B OK 5 7 8","2 L OK 1 7 8","3 B DENIED 1 7 8","4 C OK 6 10 0","5 R OK 6 3 0","6 B OK 4 1 0"], ["1 L OK 0 10 8","2 R OK 0 4 8","3 C OK 6 6 0","4 B OK 2 2 0","5 C OK 2 2 0"])
    check_teacher("04_wireless_earbuds_solution.md")
    check_trace("05_coffee_machine.md", ["G", "G", "E", "L"], ["1 L SERVED 5 6 3 1","2 E SERVED 4 4 3 2","3 L SERVED 2 1 1 3","4 G REJECTED 2 1 1 3","5 E REJECTED 2 1 1 3"], ["1 G SERVED 4 5 2 1","2 G REJECTED 4 5 2 1","3 E SERVED 3 3 2 2","4 L SERVED 1 0 0 3"])
    check_teacher("05_coffee_machine_solution.md")
    check_trace("06_solar_panels.md", [(8,2), (2,2), (0,3), (0,5)], ["1 -4 0 2 0","2 8 6 2 2","3 -4 2 2 2","4 6 6 2 4","5 -8 0 4 4"], ["1 6 6 0 2","2 0 6 0 2","3 -3 3 0 2","4 -5 0 2 2"])
    check_teacher("06_solar_panels_solution.md")
    check_trace("07_water_heater.md", [47,45,46,49,50,46,45], ["1 42 True False 1","2 45 True False 2","3 49 True False 3","4 50 False False 3","5 48 False False 3","6 44 True False 4","7 43 True False 5","8 99 False True 5","9 42 False True 5"], ["1 47 False False 0","2 45 True False 1","3 46 True False 2","4 49 True False 3","5 50 False False 3","6 46 False False 3","7 45 True False 4"])
    check_teacher("07_water_heater_solution.md")
    check_trace("08_factory_machine.md", [75,74,75,74,75,75,74,75], ["1 48 0 NORMAL","2 75 1 WARNING","3 78 2 WARNING","4 65 0 NORMAL","5 82 1 WARNING","6 83 2 WARNING","7 84 3 STOPPED","8 60 3 STOPPED"], ["1 75 1 WARNING","2 74 0 NORMAL","3 75 1 WARNING","4 74 0 NORMAL","5 75 1 WARNING","6 75 2 WARNING","7 74 0 NORMAL","8 75 1 WARNING"])
    check_teacher("08_factory_machine_solution.md")
    print("PASS: 16 trace scenarios + 48 acceptance tests (8 systems)")

# -*- coding: utf-8 -*-
# תרגיל 28 | **kwargs ומילון מפתחות
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def info(**data):
    for key in sorted(data):
        print(key, data[key])
    return len(data)

count = info(name="Noa", age=17, city="Eilat")
print("Fields", count)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# age 17
# city Eilat
# name Noa
# Fields 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=3

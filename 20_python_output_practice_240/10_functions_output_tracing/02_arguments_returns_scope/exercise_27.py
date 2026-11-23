# -*- coding: utf-8 -*-
# תרגיל 27 | **kwargs ומילון מפתחות
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def info(**data):
    for key in sorted(data):
        print(key, data[key])
    return len(data)

count = info(name="Dan", age=16, city="Haifa")
print("Fields", count)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# age 16
# city Haifa
# name Dan
# Fields 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=3

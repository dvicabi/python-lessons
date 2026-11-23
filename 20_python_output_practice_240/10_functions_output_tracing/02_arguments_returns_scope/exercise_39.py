# -*- coding: utf-8 -*-
# תרגיל 39 | פונקציה כארגומנט ושינוי התנהגות
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def apply(fn, values):
    result = []
    for x in values:
        result.append(fn(x))
    return result

def shift(x):
    return x + 2

values = [2, 5, 4]
print(apply(shift, values))
print(apply(lambda n: n * n, values))
print(values)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [4, 7, 6]
# [4, 25, 16]
# [2, 5, 4]
# <<< END EXPECTED OUTPUT

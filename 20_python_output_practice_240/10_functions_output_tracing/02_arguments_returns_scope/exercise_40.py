# -*- coding: utf-8 -*-
# תרגיל 40 | פונקציה כארגומנט ושינוי התנהגות
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def apply(fn, values):
    result = []
    for x in values:
        result.append(fn(x))
    return result

def shift(x):
    return x + 3

values = [3, 6, 5]
print(apply(shift, values))
print(apply(lambda n: n * n, values))
print(values)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [6, 9, 8]
# [9, 36, 25]
# [3, 6, 5]
# <<< END EXPECTED OUTPUT

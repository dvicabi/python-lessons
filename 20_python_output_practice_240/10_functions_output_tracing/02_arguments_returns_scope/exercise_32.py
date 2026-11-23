# -*- coding: utf-8 -*-
# תרגיל 32 | lambda ושילוב פונקציות
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def adjust(x, fn):
    return fn(x) + 1

f = lambda n: n * 2 + 3
print(f(6))
print(adjust(6, f))
print(adjust(3, lambda n: n * n))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 15
# 16
# 10
# <<< END EXPECTED OUTPUT

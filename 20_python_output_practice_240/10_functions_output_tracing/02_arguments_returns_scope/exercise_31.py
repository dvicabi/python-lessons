# -*- coding: utf-8 -*-
# תרגיל 31 | lambda ושילוב פונקציות
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def adjust(x, fn):
    return fn(x) + 1

f = lambda n: n * 2 + 2
print(f(5))
print(adjust(5, f))
print(adjust(3, lambda n: n * n))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 12
# 13
# 10
# <<< END EXPECTED OUTPUT

# -*- coding: utf-8 -*-
# תרגיל 23 | העברת פרמטרים לפי שמות ובסדר שונה
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def calculate(a, b, c=2):
    return a * c - b

print(calculate(4, 9))
print(calculate(b=9, a=4, c=2))
print(calculate(9, 4, 3))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# -1
# -1
# 23
# <<< END EXPECTED OUTPUT

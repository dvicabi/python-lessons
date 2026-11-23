# -*- coding: utf-8 -*-
# תרגיל 24 | העברת פרמטרים לפי שמות ובסדר שונה
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def calculate(a, b, c=2):
    return a * c - b

print(calculate(5, 10))
print(calculate(b=10, a=5, c=3))
print(calculate(10, 5, 3))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0
# 5
# 25
# <<< END EXPECTED OUTPUT

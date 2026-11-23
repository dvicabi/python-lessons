# -*- coding: utf-8 -*-
# תרגיל 36 | פונקציה שמחזירה פונקציה אחרת (Closure)
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def make_adder(step):
    def add(n):
        return n + step
    return add

f = make_adder(4)
print(f(3))
print(make_adder(2)(5))
print(f(5))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 7
# 7
# 9
# <<< END EXPECTED OUTPUT

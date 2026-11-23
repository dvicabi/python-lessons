# -*- coding: utf-8 -*-
# תרגיל 35 | פונקציה שמחזירה פונקציה אחרת (Closure)
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def make_adder(step):
    def add(n):
        return n + step
    return add

f = make_adder(3)
print(f(2))
print(make_adder(2)(4))
print(f(4))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 5
# 6
# 7
# <<< END EXPECTED OUTPUT

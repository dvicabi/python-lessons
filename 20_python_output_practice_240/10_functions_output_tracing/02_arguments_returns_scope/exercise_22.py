# -*- coding: utf-8 -*-
# תרגיל 22 | פרמטר עם ערך ברירת מחדל
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(4, 3))
print(power(5, 1))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 25
# 64
# 5
# <<< END EXPECTED OUTPUT

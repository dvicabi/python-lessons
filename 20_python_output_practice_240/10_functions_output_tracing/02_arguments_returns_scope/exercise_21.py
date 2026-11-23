# -*- coding: utf-8 -*-
# תרגיל 21 | פרמטר עם ערך ברירת מחדל
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def power(base, exponent=2):
    return base ** exponent

print(power(4))
print(power(3, 3))
print(power(4, 1))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 16
# 27
# 4
# <<< END EXPECTED OUTPUT

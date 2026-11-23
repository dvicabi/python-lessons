# -*- coding: utf-8 -*-
# תרגיל 38 | סדר חישוב הארגומנטים עם הדפסה
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def trace(tag, n):
    print(tag, n)
    return n + 1

def combine(a, b):
    print("Combine", a, b)
    return a * b

x = combine(trace("A", 3), trace("B", 4))
print("Result", x)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# A 3
# B 4
# Combine 4 5
# Result 20
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=20

# -*- coding: utf-8 -*-
# תרגיל 37 | סדר חישוב הארגומנטים עם הדפסה
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def trace(tag, n):
    print(tag, n)
    return n + 1

def combine(a, b):
    print("Combine", a, b)
    return a * b

x = combine(trace("A", 2), trace("B", 3))
print("Result", x)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# A 2
# B 3
# Combine 3 4
# Result 12
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=12

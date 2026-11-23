# -*- coding: utf-8 -*-
# תרגיל 54 | פונקציה שמחזירה ערך מינימום ומקסימום
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def extremes(numbers):
    low = numbers[0]
    high = numbers[0]
    for x in numbers:
        if x < low:
            low = x
        if x > high:
            high = x
    return low, high

numbers = [9, 5, 10, 3, 7]
lo, hi = extremes(numbers)
print(lo, hi)
print(hi - lo)
print(extremes(numbers[1:]))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 3 10
# 7
# (3, 10)
# <<< END EXPECTED OUTPUT
# ערכים סופיים: lo=3, hi=10

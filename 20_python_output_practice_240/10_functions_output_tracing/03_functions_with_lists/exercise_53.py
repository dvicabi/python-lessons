# -*- coding: utf-8 -*-
# תרגיל 53 | פונקציה שמחזירה ערך מינימום ומקסימום
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

numbers = [8, 4, 9, 2, 6]
lo, hi = extremes(numbers)
print(lo, hi)
print(hi - lo)
print(extremes(numbers[1:]))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 2 9
# 7
# (2, 9)
# <<< END EXPECTED OUTPUT
# ערכים סופיים: lo=2, hi=9

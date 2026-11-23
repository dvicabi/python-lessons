# -*- coding: utf-8 -*-
# תרגיל 41 | פונקציה שסוכמת ערכים לפי תנאי
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def total_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += x
    return result

numbers = [2, 5, 3, 8, 4]
print(total_even(numbers))
print(total_even(numbers[:4]))
print(numbers)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 14
# 10
# [2, 5, 3, 8, 4]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[2, 5, 3, 8, 4]

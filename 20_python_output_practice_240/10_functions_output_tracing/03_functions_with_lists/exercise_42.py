# -*- coding: utf-8 -*-
# תרגיל 42 | פונקציה שסוכמת ערכים לפי תנאי
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def total_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += x
    return result

numbers = [3, 6, 4, 9, 5]
print(total_even(numbers))
print(total_even(numbers[:5]))
print(numbers)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 10
# 10
# [3, 6, 4, 9, 5]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[3, 6, 4, 9, 5]

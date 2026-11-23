# -*- coding: utf-8 -*-
# תרגיל 49 | לשנות עותק ולא את הרשימה המקורית
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def change_copy(values):
    temp = values[:]
    for i in range(len(temp)):
        temp[i] -= i
    return temp

numbers = [7, 2, 6, 1]
new_numbers = change_copy(numbers)
print(new_numbers)
print(numbers)
print(sum(new_numbers))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [7, 1, 4, -2]
# [7, 2, 6, 1]
# 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[7, 2, 6, 1], new_numbers=[7, 1, 4, -2]

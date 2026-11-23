# -*- coding: utf-8 -*-
# תרגיל 50 | לשנות עותק ולא את הרשימה המקורית
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def change_copy(values):
    temp = values[:]
    for i in range(len(temp)):
        temp[i] -= i
    return temp

numbers = [8, 3, 7, 2]
new_numbers = change_copy(numbers)
print(new_numbers)
print(numbers)
print(sum(new_numbers))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [8, 2, 5, -1]
# [8, 3, 7, 2]
# 14
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[8, 3, 7, 2], new_numbers=[8, 2, 5, -1]

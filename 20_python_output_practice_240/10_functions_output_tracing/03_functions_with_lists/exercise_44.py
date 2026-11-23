# -*- coding: utf-8 -*-
# תרגיל 44 | שינוי רשימה בתוך פונקציה וערך None
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def add_to_all(values, amount):
    for i in range(len(values)):
        values[i] += amount

numbers = [3, 6, 4, 9]
result = add_to_all(numbers, 4)
print(numbers)
print(result)
add_to_all(numbers, 1)
print(numbers)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [7, 10, 8, 13]
# None
# [8, 11, 9, 14]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[8, 11, 9, 14], result=None

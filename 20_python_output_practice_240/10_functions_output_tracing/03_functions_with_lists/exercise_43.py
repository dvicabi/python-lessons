# -*- coding: utf-8 -*-
# תרגיל 43 | שינוי רשימה בתוך פונקציה וערך None
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def add_to_all(values, amount):
    for i in range(len(values)):
        values[i] += amount

numbers = [2, 5, 3, 8]
result = add_to_all(numbers, 3)
print(numbers)
print(result)
add_to_all(numbers, 1)
print(numbers)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [5, 8, 6, 11]
# None
# [6, 9, 7, 12]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[6, 9, 7, 12], result=None

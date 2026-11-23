# -*- coding: utf-8 -*-
# תרגיל 80 | רקורסיה שמנתחת שורות במטריצה
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def matrix_total(matrix, index=0):
    if index == len(matrix):
        return 0
    row_total = 0
    for value in matrix[index]:
        row_total += value
    later = matrix_total(matrix, index + 1)
    print("Row", index, row_total, later)
    return row_total + later

matrix = [[3, 5], [8, 2], [4, 7]]
print("TOTAL", matrix_total(matrix))
print("ROWS", len(matrix))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Row 2 11 0
# Row 1 10 11
# Row 0 8 21
# TOTAL 29
# ROWS 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[3, 5], [8, 2], [4, 7]]

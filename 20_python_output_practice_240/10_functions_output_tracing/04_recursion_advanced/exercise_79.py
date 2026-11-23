# -*- coding: utf-8 -*-
# תרגיל 79 | רקורסיה שמנתחת שורות במטריצה
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

matrix = [[2, 4], [7, 1], [3, 6]]
print("TOTAL", matrix_total(matrix))
print("ROWS", len(matrix))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Row 2 9 0
# Row 1 8 9
# Row 0 6 17
# TOTAL 23
# ROWS 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[2, 4], [7, 1], [3, 6]]

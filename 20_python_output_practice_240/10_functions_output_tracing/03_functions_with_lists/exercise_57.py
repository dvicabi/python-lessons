# -*- coding: utf-8 -*-
# תרגיל 57 | פונקציה שמשנה תאים במטריצה
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def adjust_matrix(matrix, step):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += step + i - j
            total += matrix[i][j]
    return total

matrix = [[2, 5], [7, 3]]
print(adjust_matrix(matrix, 2))
print(matrix)
print(adjust_matrix(matrix, 1))
print(matrix)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 25
# [[4, 6], [10, 5]]
# 29
# [[5, 6], [12, 6]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[5, 6], [12, 6]]

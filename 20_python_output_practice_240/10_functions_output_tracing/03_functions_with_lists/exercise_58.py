# -*- coding: utf-8 -*-
# תרגיל 58 | פונקציה שמשנה תאים במטריצה
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def adjust_matrix(matrix, step):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += step + i - j
            total += matrix[i][j]
    return total

matrix = [[3, 6], [8, 4]]
print(adjust_matrix(matrix, 3))
print(matrix)
print(adjust_matrix(matrix, 1))
print(matrix)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 33
# [[6, 8], [12, 7]]
# 37
# [[7, 8], [14, 8]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[7, 8], [14, 8]]

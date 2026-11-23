# -*- coding: utf-8 -*-
# תרגיל 44 | שינוי תאי מטריצה במקום
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[5, 9, 2], [1, 6, 4], [8, 3, 7]]
total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i + j) % 2 == 0:
            matrix[i][j] += 2 + i
        else:
            matrix[i][j] -= j
        total += matrix[i][j]
    print(i, matrix[i], total)

print("FINAL", matrix)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [7, 8, 4] 19
# 1 [1, 9, 2] 31
# 2 [12, 2, 11] 56
# FINAL [[7, 8, 4], [1, 9, 2], [12, 2, 11]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[7, 8, 4], [1, 9, 2], [12, 2, 11]], total=56

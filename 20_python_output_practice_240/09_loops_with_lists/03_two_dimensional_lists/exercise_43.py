# -*- coding: utf-8 -*-
# תרגיל 43 | שינוי תאי מטריצה במקום
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[8, 2, 5], [6, 3, 1], [4, 9, 7]]
total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i + j) % 2 == 0:
            matrix[i][j] += 1 + i
        else:
            matrix[i][j] -= j
        total += matrix[i][j]
    print(i, matrix[i], total)

print("FINAL", matrix)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [9, 1, 6] 16
# 1 [6, 5, -1] 26
# 2 [7, 8, 10] 51
# FINAL [[9, 1, 6], [6, 5, -1], [7, 8, 10]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[9, 1, 6], [6, 5, -1], [7, 8, 10]], total=51

# -*- coding: utf-8 -*-
# תרגיל 50 | סכום אלכסונים באמצעות שני אינדקסים
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[7, 6, 3], [1, 4, 9], [8, 2, 5]]
diag = 0
anti = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            diag += matrix[i][j]
        if i + j == len(matrix) - 1:
            anti += matrix[i][j]
    print(i, diag, anti)

print("FINAL", diag - anti)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 7 3
# 1 11 7
# 2 16 15
# FINAL 1
# <<< END EXPECTED OUTPUT
# ערכים סופיים: diag=16, anti=15

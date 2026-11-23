# -*- coding: utf-8 -*-
# תרגיל 49 | סכום אלכסונים באמצעות שני אינדקסים
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[5, 2, 7], [8, 3, 6], [1, 9, 4]]
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
# 0 5 7
# 1 8 10
# 2 12 11
# FINAL 1
# <<< END EXPECTED OUTPUT
# ערכים סופיים: diag=12, anti=11

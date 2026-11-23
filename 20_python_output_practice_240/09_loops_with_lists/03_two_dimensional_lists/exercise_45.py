# -*- coding: utf-8 -*-
# תרגיל 45 | סכומי עמודות ולא שורות
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[7, 4, 2], [3, 8, 5], [1, 6, 9]]
cols = []

for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][j] * 1
    cols.append(total)
    print(j, total)

print(cols)
print("FINAL", sum(cols))

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 11
# 1 18
# 2 16
# [11, 18, 16]
# FINAL 45
# <<< END EXPECTED OUTPUT
# ערכים סופיים: cols=[11, 18, 16]

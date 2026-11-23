# -*- coding: utf-8 -*-
# תרגיל 46 | סכומי עמודות ולא שורות
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[3, 5, 9], [7, 2, 4], [8, 1, 6]]
cols = []

for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][j] * 2
    cols.append(total)
    print(j, total)

print(cols)
print("FINAL", sum(cols))

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 36
# 1 16
# 2 38
# [36, 16, 38]
# FINAL 90
# <<< END EXPECTED OUTPUT
# ערכים סופיים: cols=[36, 16, 38]

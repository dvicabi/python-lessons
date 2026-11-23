# -*- coding: utf-8 -*-
# תרגיל 47 | בניית מטריצה הפוכה לפי שורות ועמודות
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[1, 8, 4], [5, 6, 2], [9, 3, 7]]
transpose = []

for j in range(len(matrix[0])):
    new_row = []
    for i in range(len(matrix)):
        new_row.append(matrix[i][j] + 0)
    transpose.append(new_row)
    print(j, new_row)

print("FINAL", transpose)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [1, 5, 9]
# 1 [8, 6, 3]
# 2 [4, 2, 7]
# FINAL [[1, 5, 9], [8, 6, 3], [4, 2, 7]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: transpose=[[1, 5, 9], [8, 6, 3], [4, 2, 7]]

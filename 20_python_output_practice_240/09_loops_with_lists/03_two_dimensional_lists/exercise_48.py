# -*- coding: utf-8 -*-
# תרגיל 48 | בניית מטריצה הפוכה לפי שורות ועמודות
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[2, 9, 5], [6, 1, 8], [4, 7, 3]]
transpose = []

for j in range(len(matrix[0])):
    new_row = []
    for i in range(len(matrix)):
        new_row.append(matrix[i][j] + 1)
    transpose.append(new_row)
    print(j, new_row)

print("FINAL", transpose)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [3, 7, 5]
# 1 [10, 2, 8]
# 2 [6, 9, 4]
# FINAL [[3, 7, 5], [10, 2, 8], [6, 9, 4]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: transpose=[[3, 7, 5], [10, 2, 8], [6, 9, 4]]

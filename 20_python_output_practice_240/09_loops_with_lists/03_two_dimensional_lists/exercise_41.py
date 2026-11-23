# -*- coding: utf-8 -*-
# תרגיל 41 | סכום כל שורה עם ספירת תנאים
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[2, 7, 4], [5, 1, 8], [6, 3, 9]]
grand = 0
hits = 0

for row in matrix:
    row_total = 0
    for value in row:
        row_total += value
        if value % 2 == 0:
            hits += 1
    grand += row_total
    print(row_total, grand, hits)

print("FINAL", grand - hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 13 13 2
# 14 27 3
# 18 45 4
# FINAL 41
# <<< END EXPECTED OUTPUT
# ערכים סופיים: grand=45, hits=4

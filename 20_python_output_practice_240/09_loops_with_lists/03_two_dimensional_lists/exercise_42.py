# -*- coding: utf-8 -*-
# תרגיל 42 | סכום כל שורה עם ספירת תנאים
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[4, 1, 6], [3, 8, 2], [9, 5, 7]]
grand = 0
hits = 0

for row in matrix:
    row_total = 0
    for value in row:
        row_total += value
        if value % 3 == 0:
            hits += 1
    grand += row_total
    print(row_total, grand, hits)

print("FINAL", grand - hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 11 11 1
# 13 24 2
# 21 45 3
# FINAL 42
# <<< END EXPECTED OUTPUT
# ערכים סופיים: grand=45, hits=3

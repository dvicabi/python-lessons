# -*- coding: utf-8 -*-
# תרגיל 56 | היפוך כל שורה תוך כדי תיעוד
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[2, 6, 7], [9, 1, 5], [4, 8, 3]]
count = 0

for row in matrix:
    left = 0
    right = len(row) - 1
    while left < right:
        row[left], row[right] = row[right], row[left]
        left += 1
        right -= 1
        count += 1
    print(row, count)

print("FINAL", matrix)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [7, 6, 2] 1
# [5, 1, 9] 2
# [3, 8, 4] 3
# FINAL [[7, 6, 2], [5, 1, 9], [3, 8, 4]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[7, 6, 2], [5, 1, 9], [3, 8, 4]], count=3

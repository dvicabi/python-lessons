# -*- coding: utf-8 -*-
# תרגיל 55 | היפוך כל שורה תוך כדי תיעוד
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[8, 5, 2], [3, 9, 6], [7, 1, 4]]
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
# [2, 5, 8] 1
# [6, 9, 3] 2
# [4, 1, 7] 3
# FINAL [[2, 5, 8], [6, 9, 3], [4, 1, 7]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[2, 5, 8], [6, 9, 3], [4, 1, 7]], count=3

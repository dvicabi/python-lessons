# -*- coding: utf-8 -*-
# תרגיל 52 | לולאת while שסורקת כל שורה הפוך
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[4, 8, 6], [2, 9, 1], [3, 5, 7]]
total = 0

for row in matrix:
    j = len(row) - 1
    while j >= 0:
        if row[j] > 5:
            total += row[j] - j
        else:
            total -= row[j] % 3
        j -= 1
    print(total)

print("FINAL", total)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 10
# 15
# 18
# FINAL 18
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=18

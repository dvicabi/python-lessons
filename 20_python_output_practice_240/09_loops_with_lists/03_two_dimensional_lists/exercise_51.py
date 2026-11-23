# -*- coding: utf-8 -*-
# תרגיל 51 | לולאת while שסורקת כל שורה הפוך
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[9, 3, 1], [6, 5, 8], [2, 7, 4]]
total = 0

for row in matrix:
    j = len(row) - 1
    while j >= 0:
        if row[j] > 4:
            total += row[j] - j
        else:
            total -= row[j] % 3
        j -= 1
    print(total)

print("FINAL", total)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 8
# 24
# 27
# FINAL 27
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=27

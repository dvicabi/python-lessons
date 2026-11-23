# -*- coding: utf-8 -*-
# תרגיל 54 | השטחת המטריצה לרשימה מסוננת
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[6, 2, 8], [9, 3, 5], [1, 7, 4]]
flat = []
skipped = 0

for i in range(len(matrix)):
    for value in matrix[i]:
        if (value + i) % 4 == 0:
            flat.append(value * 3)
        else:
            skipped += 1
    print(i, flat, skipped)

print("FINAL", len(flat), sum(flat))

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [24] 2
# 1 [24, 9] 4
# 2 [24, 9] 7
# FINAL 2 33
# <<< END EXPECTED OUTPUT
# ערכים סופיים: flat=[24, 9], skipped=7

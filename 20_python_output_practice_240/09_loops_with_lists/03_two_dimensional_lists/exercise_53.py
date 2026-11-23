# -*- coding: utf-8 -*-
# תרגיל 53 | השטחת המטריצה לרשימה מסוננת
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[5, 1, 9], [4, 7, 2], [8, 6, 3]]
flat = []
skipped = 0

for i in range(len(matrix)):
    for value in matrix[i]:
        if (value + i) % 3 == 0:
            flat.append(value * 2)
        else:
            skipped += 1
    print(i, flat, skipped)

print("FINAL", len(flat), sum(flat))

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [18] 2
# 1 [18, 4] 4
# 2 [18, 4] 7
# FINAL 2 22
# <<< END EXPECTED OUTPUT
# ערכים סופיים: flat=[18, 4], skipped=7

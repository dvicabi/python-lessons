# -*- coding: utf-8 -*-
# תרגיל 60 | בניית מטריצה חדשה לפי תנאי על התא
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[9, 2, 6], [4, 7, 3], [8, 5, 1]]
changed = []

for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
        x = matrix[i][j]
        if (x + i + j) % 3 == 0:
            new_row.append(x + i)
        else:
            new_row.append(x - j - 1)
    changed.append(new_row)
    print(i, new_row)

print("FINAL", changed)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [9, 2, 3]
# 1 [3, 8, 4]
# 2 [7, 3, -2]
# FINAL [[9, 2, 3], [3, 8, 4], [7, 3, -2]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: changed=[[9, 2, 3], [3, 8, 4], [7, 3, -2]]

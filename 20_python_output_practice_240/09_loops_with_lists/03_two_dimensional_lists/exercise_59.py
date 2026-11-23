# -*- coding: utf-8 -*-
# תרגיל 59 | בניית מטריצה חדשה לפי תנאי על התא
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[5, 8, 3], [6, 2, 9], [1, 4, 7]]
changed = []

for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
        x = matrix[i][j]
        if (x + i + j) % 3 == 0:
            new_row.append(x + i)
        else:
            new_row.append(x - j - 0)
    changed.append(new_row)
    print(i, new_row)

print("FINAL", changed)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [5, 8, 1]
# 1 [6, 1, 10]
# 2 [3, 3, 5]
# FINAL [[5, 8, 1], [6, 1, 10], [3, 3, 5]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: changed=[[5, 8, 1], [6, 1, 10], [3, 3, 5]]

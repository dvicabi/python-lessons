# -*- coding: utf-8 -*-
# תרגיל 57 | השוואה בין שורות שכנות
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[3, 7, 9], [8, 4, 1], [5, 2, 6]]
score = 1
differences = []

for i in range(1, len(matrix)):
    for j in range(len(matrix[i])):
        delta = matrix[i][j] - matrix[i - 1][j]
        differences.append(delta)
        if delta > 0:
            score += delta
        else:
            score -= 1
    print(i, score)

print(differences)
print("FINAL", score)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 4
# 2 7
# [5, -3, -8, -3, -2, 5]
# FINAL 7
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=7, differences=[5, -3, -8, -3, -2, 5]

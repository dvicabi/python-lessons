# -*- coding: utf-8 -*-
# תרגיל 58 | השוואה בין שורות שכנות
# נושא: רשימה של רשימות (מטריצה)
#
# משימה: בנו טבלת מעקב של שורה, עמודה, ערך ומשתני חישוב.

matrix = [[7, 1, 6], [2, 5, 9], [3, 8, 4]]
score = 2
differences = []

for i in range(1, len(matrix)):
    for j in range(len(matrix[i])):
        delta = matrix[i][j] - matrix[i - 1][j]
        differences.append(delta)
        if delta > 0:
            score += delta
        else:
            score -= 2
    print(i, score)

print(differences)
print("FINAL", score)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 7
# 2 9
# [-5, 4, 3, 1, 3, -5]
# FINAL 9
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=9, differences=[-5, 4, 3, 1, 3, -5]

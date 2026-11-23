# -*- coding: utf-8 -*-
# תרגיל 61 | השוואת כל תא לכל שורה אחרת
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[2, 7, 3], [5, 1, 6], [4, 8, 2]]
hits = 0
score = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(len(matrix)):
            if matrix[i][j] > matrix[k][j]:
                hits += 1
                score += i + k + 0
            else:
                score -= j % 2
    print(i, hits, score)

print("FINAL", score - hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 2 1
# 1 6 6
# 2 9 12
# FINAL 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: hits=9, score=12

# -*- coding: utf-8 -*-
# תרגיל 62 | השוואת כל תא לכל שורה אחרת
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[4, 2, 8], [6, 3, 1], [7, 5, 9]]
hits = 0
score = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(len(matrix)):
            if matrix[i][j] > matrix[k][j]:
                hits += 1
                score += i + k + 1
            else:
                score -= j % 2
    print(i, hits, score)

print("FINAL", score - hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 1 -1
# 1 3 1
# 2 9 21
# FINAL 12
# <<< END EXPECTED OUTPUT
# ערכים סופיים: hits=9, score=21

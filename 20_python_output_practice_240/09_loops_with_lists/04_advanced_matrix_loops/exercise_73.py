# -*- coding: utf-8 -*-
# תרגיל 73 | בדיקת שכנים שונים בכל עמודה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[6, 3, 7], [1, 8, 4], [5, 2, 9]]
matches = 0
score = 0

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            if i != k and matrix[i][j] < matrix[k][j]:
                score += matrix[k][j] - matrix[i][j]
                matches += 1
            elif i == k:
                score -= 1
    print(j, matches, score)

print("RESULT", matches + score)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 3 7
# 1 6 16
# 2 9 23
# RESULT 32
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matches=9, score=23

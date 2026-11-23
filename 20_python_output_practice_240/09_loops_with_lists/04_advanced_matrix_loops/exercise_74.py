# -*- coding: utf-8 -*-
# תרגיל 74 | בדיקת שכנים שונים בכל עמודה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[8, 4, 1], [7, 2, 6], [9, 3, 5]]
matches = 0
score = 0

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            if i != k and matrix[i][j] < matrix[k][j]:
                score += matrix[k][j] - matrix[i][j]
                matches += 1
            elif i == k:
                score -= 2
    print(j, matches, score)

print("RESULT", matches + score)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 3 -2
# 1 6 -4
# 2 9 0
# RESULT 9
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matches=9, score=0

# -*- coding: utf-8 -*-
# תרגיל 79 | שלוש לולאות עם חלון ושינויים ברשימה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[1, 7, 5], [8, 2, 9], [6, 4, 3]]
result = []
total = 0

for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
        value = matrix[i][j]
        for k in range(1, i + 2):
            if (value + k) % 2 == 0:
                value += k + j
            else:
                value -= 1
        new_row.append(value)
        total += value
    result.append(new_row)
    print(i, new_row, total)

print("FINAL", result)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [2, 9, 8] 19
# 1 [6, 0, 16] 41
# 2 [3, 1, 9] 54
# FINAL [[2, 9, 8], [6, 0, 16], [3, 1, 9]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: result=[[2, 9, 8], [6, 0, 16], [3, 1, 9]], total=54

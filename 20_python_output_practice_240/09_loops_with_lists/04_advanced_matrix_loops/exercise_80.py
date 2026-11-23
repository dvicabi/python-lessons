# -*- coding: utf-8 -*-
# תרגיל 80 | שלוש לולאות עם חלון ושינויים ברשימה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[7, 3, 8], [5, 9, 2], [4, 1, 6]]
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
                value -= 2
        new_row.append(value)
        total += value
    result.append(new_row)
    print(i, new_row, total)

print("FINAL", result)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [8, 5, 6] 19
# 1 [8, 9, 4] 40
# 2 [2, 5, 6] 53
# FINAL [[8, 5, 6], [8, 9, 4], [2, 5, 6]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: result=[[8, 5, 6], [8, 9, 4], [2, 5, 6]], total=53

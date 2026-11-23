# -*- coding: utf-8 -*-
# תרגיל 63 | יצירת רשימות על ידי שלוש לולאות
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[3, 8, 1], [5, 7, 2], [6, 4, 9]]
constructed = []
total = 0

for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
        value = 0
        for k in range(j + 1):
            value += (matrix[i][k] + i) % 4
        new_row.append(value)
        total += value
    constructed.append(new_row)
    print(i, new_row, total)

print("FINAL", constructed)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [3, 3, 4] 10
# 1 [2, 2, 5] 19
# 2 [0, 2, 5] 26
# FINAL [[3, 3, 4], [2, 2, 5], [0, 2, 5]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: constructed=[[3, 3, 4], [2, 2, 5], [0, 2, 5]], total=26

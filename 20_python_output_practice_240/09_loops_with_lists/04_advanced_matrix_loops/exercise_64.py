# -*- coding: utf-8 -*-
# תרגיל 64 | יצירת רשימות על ידי שלוש לולאות
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[8, 1, 6], [2, 9, 4], [7, 3, 5]]
constructed = []
total = 0

for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[i])):
        value = 0
        for k in range(j + 1):
            value += (matrix[i][k] + i) % 5
        new_row.append(value)
        total += value
    constructed.append(new_row)
    print(i, new_row, total)

print("FINAL", constructed)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [3, 4, 5] 12
# 1 [3, 3, 3] 21
# 2 [4, 4, 6] 35
# FINAL [[3, 4, 5], [3, 3, 3], [4, 4, 6]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: constructed=[[3, 4, 5], [3, 3, 3], [4, 4, 6]], total=35

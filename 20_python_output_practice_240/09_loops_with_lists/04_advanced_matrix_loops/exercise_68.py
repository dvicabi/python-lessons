# -*- coding: utf-8 -*-
# תרגיל 68 | לולאת while חיצונית ו־while פנימית
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[5, 9, 3], [7, 4, 1], [2, 8, 6]]
i = 0
total = 3
count = 0

while i < len(matrix):
    for j in range(len(matrix[i])):
        k = 0
        while k <= j:
            if (matrix[i][k] + total) % 2 == 0:
                total += matrix[i][k]
                count += 1
            else:
                total -= i + k
            k += 1
    print(i, total, count)
    i += 1

print("CHECK", total + count)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 14 3
# 1 22 6
# 2 50 12
# CHECK 62
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=3, total=50, count=12

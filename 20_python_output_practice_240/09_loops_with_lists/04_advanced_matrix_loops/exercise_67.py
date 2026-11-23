# -*- coding: utf-8 -*-
# תרגיל 67 | לולאת while חיצונית ו־while פנימית
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[6, 2, 5], [8, 3, 7], [1, 9, 4]]
i = 0
total = 2
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
# 0 22 5
# 1 39 8
# 2 29 10
# CHECK 39
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=3, total=29, count=10

# -*- coding: utf-8 -*-
# תרגיל 78 | תלות בין שורות ומצב התוצאה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[9, 6, 2], [4, 7, 1], [3, 5, 8]]
acc = 6
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(i + 1):
            if (matrix[k][j] + acc) % 4 == 0:
                acc += matrix[i][j] - k
                count += 1
            else:
                acc -= (matrix[k][j] + j) % 3
    print(i, acc, count)

print("CHECK", acc * 2 + count)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 11 1
# 1 26 4
# 2 34 7
# CHECK 75
# <<< END EXPECTED OUTPUT
# ערכים סופיים: acc=34, count=7

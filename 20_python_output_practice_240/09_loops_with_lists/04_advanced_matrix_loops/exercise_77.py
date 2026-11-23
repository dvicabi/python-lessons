# -*- coding: utf-8 -*-
# תרגיל 77 | תלות בין שורות ומצב התוצאה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[5, 1, 9], [2, 8, 6], [7, 3, 4]]
acc = 5
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
# 0 2 1
# 1 7 3
# 2 17 6
# CHECK 40
# <<< END EXPECTED OUTPUT
# ערכים סופיים: acc=17, count=6

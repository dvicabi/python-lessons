# -*- coding: utf-8 -*-
# תרגיל 65 | שינוי תא לפי חישובים על תאים קודמים
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[7, 3, 5], [4, 8, 1], [6, 2, 9]]
shifts = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(j):
            if (matrix[i][j] + matrix[i][k]) % 3 == 0:
                matrix[i][j] += 1
                shifts += 1
            else:
                matrix[i][j] -= 1
    print(i, matrix[i], shifts)

print("FINAL", matrix)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [7, 2, 5] 1
# 1 [4, 9, 1] 3
# 2 [6, 1, 9] 4
# FINAL [[7, 2, 5], [4, 9, 1], [6, 1, 9]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[7, 2, 5], [4, 9, 1], [6, 1, 9]], shifts=4

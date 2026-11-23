# -*- coding: utf-8 -*-
# תרגיל 66 | שינוי תא לפי חישובים על תאים קודמים
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[2, 6, 9], [3, 1, 7], [5, 8, 4]]
shifts = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(j):
            if (matrix[i][j] + matrix[i][k]) % 3 == 0:
                matrix[i][j] += 2
                shifts += 1
            else:
                matrix[i][j] -= 1
    print(i, matrix[i], shifts)

print("FINAL", matrix)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [2, 5, 7] 0
# 1 [3, 0, 8] 1
# 2 [5, 7, 5] 2
# FINAL [[2, 5, 7], [3, 0, 8], [5, 7, 5]]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[2, 5, 7], [3, 0, 8], [5, 7, 5]], shifts=2

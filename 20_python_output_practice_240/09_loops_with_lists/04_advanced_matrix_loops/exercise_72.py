# -*- coding: utf-8 -*-
# תרגיל 72 | מטריצה שעוברת סיבובי עדכון
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[2, 8, 5], [9, 6, 3], [4, 7, 1]]
passes = 3
total = 0

for p in range(passes):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i + j + p) % 2 == 0:
                matrix[i][j] += p + 1
            else:
                matrix[i][j] -= i + 1
            total += matrix[i][j]
    print(p, matrix, total)

print("FINAL", matrix[1][1])

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 [[3, 7, 6], [7, 7, 1], [5, 4, 2]] 42
# 1 [[2, 9, 5], [9, 5, 3], [2, 6, -1]] 82
# 2 [[5, 8, 8], [7, 8, 1], [5, 3, 2]] 129
# FINAL 8
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[5, 8, 8], [7, 8, 1], [5, 3, 2]], total=129

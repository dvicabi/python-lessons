# -*- coding: utf-8 -*-
# תרגיל 71 | מטריצה שעוברת סיבובי עדכון
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[7, 2, 6], [8, 4, 9], [3, 1, 5]]
passes = 2
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
# 0 [[8, 1, 7], [6, 5, 7], [4, -2, 6]] 42
# 1 [[7, 3, 6], [8, 3, 9], [1, 0, 3]] 82
# FINAL 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: matrix=[[7, 3, 6], [8, 3, 9], [1, 0, 3]], total=82

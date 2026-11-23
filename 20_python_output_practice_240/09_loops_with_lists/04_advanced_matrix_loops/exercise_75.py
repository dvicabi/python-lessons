# -*- coding: utf-8 -*-
# תרגיל 75 | לולאה משולשת שבונה מחרוזת לכל שורה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[3, 9, 6], [5, 1, 8], [2, 4, 7]]
mask = 2
hits = 0

for i in range(len(matrix)):
    line = ""
    for j in range(len(matrix[i])):
        for k in range(1, 3):
            if (matrix[i][j] + mask + k) % 3 == 0:
                line += "#"
                hits += 1
            else:
                line += "."
                mask += k
        line += "|"
    print(i, line, mask, hits)

print("FINAL", hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 #.|..|..| 10 1
# 1 .#|.#|#.| 14 4
# 2 ..|.#|..| 21 5
# FINAL 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: mask=21, hits=5

# -*- coding: utf-8 -*-
# תרגיל 76 | לולאה משולשת שבונה מחרוזת לכל שורה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[4, 7, 2], [6, 5, 9], [1, 8, 3]]
mask = 3
hits = 0

for i in range(len(matrix)):
    line = ""
    for j in range(len(matrix[i])):
        for k in range(1, 3):
            if (matrix[i][j] + mask + k) % 4 == 0:
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
# 0 #.|..|..| 11 1
# 1 .#|.#|..| 16 3
# 2 .#|.#|.#| 19 6
# FINAL 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: mask=19, hits=6

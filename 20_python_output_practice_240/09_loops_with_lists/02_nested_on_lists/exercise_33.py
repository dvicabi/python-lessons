# -*- coding: utf-8 -*-
# תרגיל 33 | לצייר דפוס לפי זוגות איברים
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [6, 3, 1, 5]
marks = 0
for i in range(len(numbers)):
    row = ""
    for j in range(len(numbers)):
        if (numbers[i] + j) % 3 == 0:
            row += "#"
            marks += 1
        else:
            row += "."
    print(i, row)
print("MARKS", marks)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 #..#
# 1 #..#
# 2 ..#.
# 3 .#..
# MARKS 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: marks=6

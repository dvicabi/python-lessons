# -*- coding: utf-8 -*-
# תרגיל 70 | ספירת שלשות תאים באותה שורה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[9, 5, 2], [4, 1, 8], [3, 7, 6]]
count = 0
acc = 0

for row in matrix:
    for a in range(len(row)):
        for b in range(a + 1, len(row)):
            if (row[a] + row[b]) % 4 == 0:
                count += 1
                acc += row[a] * row[b]
            else:
                acc -= 1
    print(count, acc)

print("FINAL", acc)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 0 -3
# 1 27
# 1 24
# FINAL 24
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=1, acc=24

# -*- coding: utf-8 -*-
# תרגיל 69 | ספירת שלשות תאים באותה שורה
# נושא: רשימות דו-ממדיות עם שלוש לולאות מקוננות או יותר.
# משימה: חשבו את הפלט, כולל כל שורות הביניים, ועקבו אחרי המשתנים.

matrix = [[3, 7, 4], [2, 9, 5], [8, 6, 1]]
count = 0
acc = 0

for row in matrix:
    for a in range(len(row)):
        for b in range(a + 1, len(row)):
            if (row[a] + row[b]) % 3 == 0:
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
# 0 -6
# 1 0
# FINAL 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=1, acc=0

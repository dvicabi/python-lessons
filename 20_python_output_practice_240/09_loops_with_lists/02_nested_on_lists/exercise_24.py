# -*- coding: utf-8 -*-
# תרגיל 24 | השוואת שתי רשימות בזוגות
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

a = [6, 2, 4]
b = [2, 4, 1]
total = 0
hits = 0
for x in a:
    for y in b:
        if (x + y) % 4 == 0:
            hits += 1
            total += x + y
        else:
            total -= 1
    print(x, hits, total)
print("FINAL", total)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 6 1 6
# 2 2 8
# 4 3 14
# FINAL 14
# <<< END EXPECTED OUTPUT
# ערכים סופיים: hits=3, total=14

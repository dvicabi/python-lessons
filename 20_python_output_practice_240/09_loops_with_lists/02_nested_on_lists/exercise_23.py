# -*- coding: utf-8 -*-
# תרגיל 23 | השוואת שתי רשימות בזוגות
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

a = [3, 8, 2]
b = [8, 2, 5]
total = 0
hits = 0
for x in a:
    for y in b:
        if (x + y) % 3 == 0:
            hits += 1
            total += x + y
        else:
            total -= 1
    print(x, hits, total)
print("FINAL", total)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 3 0 -3
# 8 0 -6
# 2 0 -9
# FINAL -9
# <<< END EXPECTED OUTPUT
# ערכים סופיים: hits=0, total=-9

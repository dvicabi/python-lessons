# -*- coding: utf-8 -*-
# תרגיל 29 | זוגות מסודרים מרשימה
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [6, 1, 8, 4]
pairs = []
total = 0
for a in numbers:
    for b in numbers:
        if a != b and (a * b) % 3 != 0:
            pairs.append(a + b)
            total += 1
    print(a, total)
print(pairs)
print("FINAL", sum(pairs))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 6 0
# 1 2
# 8 4
# 4 6
# [9, 5, 9, 12, 5, 12]
# FINAL 52
# <<< END EXPECTED OUTPUT
# ערכים סופיים: pairs=[9, 5, 9, 12, 5, 12], total=6

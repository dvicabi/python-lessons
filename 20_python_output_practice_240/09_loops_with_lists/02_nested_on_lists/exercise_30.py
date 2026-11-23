# -*- coding: utf-8 -*-
# תרגיל 30 | זוגות מסודרים מרשימה
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [2, 9, 3, 6]
pairs = []
total = 0
for a in numbers:
    for b in numbers:
        if a != b and (a * b) % 4 != 0:
            pairs.append(a + b)
            total += 1
    print(a, total)
print(pairs)
print("FINAL", sum(pairs))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 2 2
# 9 5
# 3 8
# 6 10
# [11, 5, 11, 12, 15, 5, 12, 9, 15, 9]
# FINAL 104
# <<< END EXPECTED OUTPUT
# ערכים סופיים: pairs=[11, 5, 11, 12, 15, 5, 12, 9, 15, 9], total=10

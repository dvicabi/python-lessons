# -*- coding: utf-8 -*-
# תרגיל 27 | רשימת הפרשי כל הזוגות
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [4, 7, 2, 5]
results = []
positive = 0
for i in range(len(numbers)):
    for j in range(i):
        diff = numbers[i] - numbers[j]
        if diff > 0:
            results.append(diff)
            positive += 1
    print(i, len(results))
print(results)
print("FINAL", positive)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 0
# 1 1
# 2 1
# 3 3
# [3, 1, 3]
# FINAL 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: results=[3, 1, 3], positive=3

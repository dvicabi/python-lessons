# -*- coding: utf-8 -*-
# תרגיל 28 | רשימת הפרשי כל הזוגות
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [3, 5, 9, 2]
results = []
positive = 0
for i in range(len(numbers)):
    for j in range(i):
        diff = numbers[i] - numbers[j]
        if diff > 1:
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
# 2 3
# 3 3
# [2, 6, 4]
# FINAL 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: results=[2, 6, 4], positive=3

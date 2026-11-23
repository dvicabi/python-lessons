# -*- coding: utf-8 -*-
# תרגיל 35 | הוספת איברים תוך כדי השוואה
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [4, 9, 3, 2]
size = len(numbers)
for i in range(size):
    extra = 0
    for j in range(size):
        if numbers[j] > numbers[i]:
            extra += 1
    numbers.append(extra + 0)
    print(i, extra, numbers[-1])
print("FINAL", numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 1 1
# 1 0 0
# 2 2 2
# 3 3 3
# FINAL [4, 9, 3, 2, 1, 0, 2, 3]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[4, 9, 3, 2, 1, 0, 2, 3], size=4

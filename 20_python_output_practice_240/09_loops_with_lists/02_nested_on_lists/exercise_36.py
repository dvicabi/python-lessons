# -*- coding: utf-8 -*-
# תרגיל 36 | הוספת איברים תוך כדי השוואה
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [7, 1, 6, 3]
size = len(numbers)
for i in range(size):
    extra = 0
    for j in range(size):
        if numbers[j] > numbers[i]:
            extra += 1
    numbers.append(extra + 1)
    print(i, extra, numbers[-1])
print("FINAL", numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 0 1
# 1 3 4
# 2 1 2
# 3 2 3
# FINAL [7, 1, 6, 3, 1, 4, 2, 3]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[7, 1, 6, 3, 1, 4, 2, 3], size=4

# -*- coding: utf-8 -*-
# תרגיל 25 | לשנות רשימה לפי שני אינדקסים
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [5, 3, 7, 2]
i = 0
while i < len(numbers):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) % 2 == 0:
            numbers[i] += 1
        else:
            numbers[j] -= 1
    print(i, numbers)
    i += 1
print("FINAL", sum(numbers))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 [7, 3, 6, 2]
# 1 [7, 3, 5, 1]
# 2 [7, 3, 6, 1]
# 3 [7, 3, 6, 1]
# FINAL 17
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[7, 3, 6, 1], i=4

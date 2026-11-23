# -*- coding: utf-8 -*-
# תרגיל 26 | לשנות רשימה לפי שני אינדקסים
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [1, 6, 4, 8]
i = 0
while i < len(numbers):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) % 2 == 0:
            numbers[i] += 2
        else:
            numbers[j] -= 1
    print(i, numbers)
    i += 1
print("FINAL", sum(numbers))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 [1, 5, 3, 7]
# 1 [1, 9, 3, 7]
# 2 [1, 9, 5, 7]
# 3 [1, 9, 5, 7]
# FINAL 22
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[1, 9, 5, 7], i=4

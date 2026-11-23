# -*- coding: utf-8 -*-
# תרגיל 31 | לולאת while כפולה עם חלון משתנה
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [7, 2, 5, 1]
score = 1
i = 0
while i < len(numbers):
    j = len(numbers) - 1
    while j > i:
        if (numbers[j] + score) % 3 == 0:
            score += numbers[i]
        else:
            score -= numbers[j] % 3
        j -= 1
    numbers[i] += score % 4
    print(i, numbers[i], score)
    i += 1
print("FINAL", numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 8 5
# 1 3 9
# 2 5 8
# 3 1 8
# FINAL [8, 3, 5, 1]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[8, 3, 5, 1], score=8

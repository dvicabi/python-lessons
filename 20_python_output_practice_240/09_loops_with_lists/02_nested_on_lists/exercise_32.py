# -*- coding: utf-8 -*-
# תרגיל 32 | לולאת while כפולה עם חלון משתנה
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [8, 4, 2, 7]
score = 2
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
# 0 9 17
# 1 7 19
# 2 4 18
# 3 9 18
# FINAL [9, 7, 4, 9]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[9, 7, 4, 9], score=18

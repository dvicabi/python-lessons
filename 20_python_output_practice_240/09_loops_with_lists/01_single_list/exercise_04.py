# -*- coding: utf-8 -*-
# תרגיל 04 | עדכון איברי רשימה באמצעות while
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [8, 1, 7, 3, 6]
i = 0
while i < len(numbers):
    if i % 2 == 0:
        numbers[i] += i + 2
    else:
        numbers[i] -= i
    i += 1
print(numbers)
print(sum(numbers), i)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [10, 0, 11, 0, 12]
# 33 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[10, 0, 11, 0, 12], i=5

# -*- coding: utf-8 -*-
# תרגיל 03 | עדכון איברי רשימה באמצעות while
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [6, 2, 9, 4, 5]
i = 0
while i < len(numbers):
    if i % 2 == 0:
        numbers[i] += i + 1
    else:
        numbers[i] -= i
    i += 1
print(numbers)
print(sum(numbers), i)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [7, 1, 12, 1, 10]
# 31 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[7, 1, 12, 1, 10], i=5

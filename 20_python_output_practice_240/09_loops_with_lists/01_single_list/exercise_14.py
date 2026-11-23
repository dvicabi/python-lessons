# -*- coding: utf-8 -*-
# תרגיל 14 | החלפת איברים בקצוות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [8, 2, 5, 1, 7]
left = 0
right = len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    print(left, right, numbers)
    left += 1
    right -= 1
print(numbers[1])

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 4 [7, 2, 5, 1, 8]
# 1 3 [7, 1, 5, 2, 8]
# 1
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[7, 1, 5, 2, 8], left=2, right=2

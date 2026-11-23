# -*- coding: utf-8 -*-
# תרגיל 13 | החלפת איברים בקצוות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [3, 9, 2, 6, 5]
left = 0
right = len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    print(left, right, numbers)
    left += 1
    right -= 1
print(numbers[0])

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 4 [5, 9, 2, 6, 3]
# 1 3 [5, 6, 2, 9, 3]
# 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[5, 6, 2, 9, 3], left=2, right=2

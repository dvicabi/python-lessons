# -*- coding: utf-8 -*-
# תרגיל 09 | הזזה מחזורית של איברי הרשימה
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [2, 6, 3, 8, 1]
removed = []
for i in range(3):
    first = numbers.pop(0)
    removed.append(first)
    numbers.append(first + i)
    print(i, numbers)
print(removed)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 [6, 3, 8, 1, 2]
# 1 [3, 8, 1, 2, 7]
# 2 [8, 1, 2, 7, 5]
# [2, 6, 3]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[8, 1, 2, 7, 5], removed=[2, 6, 3]

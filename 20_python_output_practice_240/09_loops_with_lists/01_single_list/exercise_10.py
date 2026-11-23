# -*- coding: utf-8 -*-
# תרגיל 10 | הזזה מחזורית של איברי הרשימה
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [7, 3, 9, 2, 5]
removed = []
for i in range(4):
    first = numbers.pop(0)
    removed.append(first)
    numbers.append(first + i)
    print(i, numbers)
print(removed)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 [3, 9, 2, 5, 7]
# 1 [9, 2, 5, 7, 4]
# 2 [2, 5, 7, 4, 11]
# 3 [5, 7, 4, 11, 5]
# [7, 3, 9, 2]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[5, 7, 4, 11, 5], removed=[7, 3, 9, 2]

# -*- coding: utf-8 -*-
# תרגיל 06 | מיון ערכים לשתי רשימות חדשות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [3, 7, 2, 9, 4]
evens = []
odds = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x * 3)
    else:
        odds.append(x + 2)
print(evens)
print(odds)
print(len(evens), len(odds))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [6, 12]
# [5, 9, 11]
# 2 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: evens=[6, 12], odds=[5, 9, 11]

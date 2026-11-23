# -*- coding: utf-8 -*-
# תרגיל 05 | מיון ערכים לשתי רשימות חדשות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [2, 5, 8, 1, 4]
evens = []
odds = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x * 2)
    else:
        odds.append(x + 1)
print(evens)
print(odds)
print(len(evens), len(odds))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [4, 16, 8]
# [6, 2]
# 3 2
# <<< END EXPECTED OUTPUT
# ערכים סופיים: evens=[4, 16, 8], odds=[6, 2]

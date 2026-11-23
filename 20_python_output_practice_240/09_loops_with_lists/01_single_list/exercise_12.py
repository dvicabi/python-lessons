# -*- coding: utf-8 -*-
# תרגיל 12 | סכום רץ ושינוי ערך לפי אינדקס
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [6, 1, 7, 4, 3]
acc = 2
for i in range(len(numbers)):
    acc += numbers[i]
    if i % 2 == 0:
        numbers[i] = acc % 7
    else:
        numbers[i] += acc // 4
    print(i, numbers[i], acc)
print(numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 1 8
# 1 3 9
# 2 2 16
# 3 9 20
# 4 2 23
# [1, 3, 2, 9, 2]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: acc=23, numbers=[1, 3, 2, 9, 2]

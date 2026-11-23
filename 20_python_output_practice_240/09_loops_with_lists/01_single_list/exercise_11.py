# -*- coding: utf-8 -*-
# תרגיל 11 | סכום רץ ושינוי ערך לפי אינדקס
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [4, 8, 2, 5, 9]
acc = 1
for i in range(len(numbers)):
    acc += numbers[i]
    if i % 2 == 0:
        numbers[i] = acc % 6
    else:
        numbers[i] += acc // 3
    print(i, numbers[i], acc)
print(numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 5 5
# 1 12 13
# 2 3 15
# 3 11 20
# 4 5 29
# [5, 12, 3, 11, 5]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: acc=29, numbers=[5, 12, 3, 11, 5]

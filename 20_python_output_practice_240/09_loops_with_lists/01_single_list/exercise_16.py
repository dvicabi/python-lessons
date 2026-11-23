# -*- coding: utf-8 -*-
# תרגיל 16 | עיבוד תנאי ובניית רשימת תוצאות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [5, 9, 4, 1, 6]
result = []
for x in numbers:
    if x > 5:
        result.append(x - 3)
    elif x % 2 == 0:
        result.append(x * 2)
    else:
        result.append(x + 4)
print(result)
print(sum(result))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [9, 6, 8, 5, 3]
# 31
# <<< END EXPECTED OUTPUT
# ערכים סופיים: result=[9, 6, 8, 5, 3]

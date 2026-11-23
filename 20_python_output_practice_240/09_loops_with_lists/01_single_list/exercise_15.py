# -*- coding: utf-8 -*-
# תרגיל 15 | עיבוד תנאי ובניית רשימת תוצאות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [4, 7, 3, 8, 2]
result = []
for x in numbers:
    if x > 4:
        result.append(x - 2)
    elif x % 2 == 0:
        result.append(x * 2)
    else:
        result.append(x + 3)
print(result)
print(sum(result))

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [8, 5, 6, 6, 4]
# 29
# <<< END EXPECTED OUTPUT
# ערכים סופיים: result=[8, 5, 6, 6, 4]

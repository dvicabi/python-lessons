# -*- coding: utf-8 -*-
# תרגיל 01 | סכום לסירוגין לפי זוגיות איבר
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [3, 8, 5, 2, 7]
score = 0
for value in numbers:
    if value % 2 == 0:
        score += value
    else:
        score -= value
    print(value, score)
print("FINAL", score)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 3 -3
# 8 5
# 5 0
# 2 2
# 7 -5
# FINAL -5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=-5, numbers=[3, 8, 5, 2, 7]

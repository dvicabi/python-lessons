# -*- coding: utf-8 -*-
# תרגיל 02 | סכום לסירוגין לפי זוגיות איבר
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [4, 9, 1, 6, 3]
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
# 4 4
# 9 -5
# 1 -6
# 6 0
# 3 -3
# FINAL -3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=-3, numbers=[4, 9, 1, 6, 3]

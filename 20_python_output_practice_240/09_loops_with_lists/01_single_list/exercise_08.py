# -*- coding: utf-8 -*-
# תרגיל 08 | הפרשים בין זוגות שכנים
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [9, 4, 1, 7, 2]
diffs = []
score = 0
for i in range(1, len(numbers)):
    d = numbers[i] - numbers[i - 1]
    diffs.append(d)
    if d > 0:
        score += d
    else:
        score -= 2
print(diffs)
print(score)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [-5, -3, 6, -5]
# 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: diffs=[-5, -3, 6, -5], score=0

# -*- coding: utf-8 -*-
# תרגיל 07 | הפרשים בין זוגות שכנים
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: בינונית

numbers = [5, 2, 8, 3, 6]
diffs = []
score = 0
for i in range(1, len(numbers)):
    d = numbers[i] - numbers[i - 1]
    diffs.append(d)
    if d > 0:
        score += d
    else:
        score -= 1
print(diffs)
print(score)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# [-3, 6, -5, 3]
# 7
# <<< END EXPECTED OUTPUT
# ערכים סופיים: diffs=[-3, 6, -5, 3], score=7

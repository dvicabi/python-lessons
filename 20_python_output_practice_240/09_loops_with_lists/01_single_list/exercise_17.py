# -*- coding: utf-8 -*-
# תרגיל 17 | בדיקת עליות וירידות
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [6, 3, 8, 2, 7]
ups = 0
downs = 0
i = 1
while i < len(numbers):
    if numbers[i] >= numbers[i - 1]:
        ups += 1
    else:
        downs += 1
    print(i, ups, downs)
    i += 1
print("RESULT", ups - downs)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 1 0 1
# 2 1 1
# 3 1 2
# 4 2 2
# RESULT 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: ups=2, downs=2, i=5

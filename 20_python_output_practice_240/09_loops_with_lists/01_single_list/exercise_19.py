# -*- coding: utf-8 -*-
# תרגיל 19 | תלות בין פריטי רשימה למשתנה זיכרון
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [5, 8, 1, 6, 3]
carry = 2
for i in range(len(numbers)):
    if (numbers[i] + carry) % 3 == 0:
        numbers[i] += carry
        carry += 1
    else:
        carry = (carry + numbers[i]) % 7
        numbers[i] -= carry
    print(i, numbers[i], carry)
print("FINAL", numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 5 0
# 1 7 1
# 2 -1 2
# 3 5 1
# 4 -1 4
# FINAL [5, 7, -1, 5, -1]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[5, 7, -1, 5, -1], carry=4

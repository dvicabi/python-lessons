# -*- coding: utf-8 -*-
# תרגיל 20 | תלות בין פריטי רשימה למשתנה זיכרון
# משימה: חשבו מה בדיוק יודפס ובנו טבלת מעקב למשתנים.
# נושא: לולאות עם רשימה אחת | דרגת קושי: מתקדמת

numbers = [7, 4, 9, 2, 5]
carry = 3
for i in range(len(numbers)):
    if (numbers[i] + carry) % 3 == 0:
        numbers[i] += carry
        carry += 2
    else:
        carry = (carry + numbers[i]) % 7
        numbers[i] -= carry
    print(i, numbers[i], carry)
print("FINAL", numbers)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 4 3
# 1 4 0
# 2 9 2
# 3 -2 4
# 4 9 6
# FINAL [4, 4, 9, -2, 9]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[4, 4, 9, -2, 9], carry=6

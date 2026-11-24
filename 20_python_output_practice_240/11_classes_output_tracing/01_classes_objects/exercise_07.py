# -*- coding: utf-8 -*-
# תרגיל 07 | שינוי הפניה למופע חדש
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Card:
    pass

a = Card()
a.value = 7
b = a
b = Card()
b.value = 12
print(a.value, b.value)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 7 12
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.value=7, b.value=12

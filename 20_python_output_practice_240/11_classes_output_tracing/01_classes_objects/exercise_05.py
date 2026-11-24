# -*- coding: utf-8 -*-
# תרגיל 05 | החלפת ערכים בין אובייקטים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Box:
    pass

a = Box()
b = Box()
a.value = 4
b.value = 9
a.value, b.value = b.value, a.value
print(a.value, b.value)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 9 4
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.value=9, b.value=4

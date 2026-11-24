# -*- coding: utf-8 -*-
# תרגיל 06 | שני שמות לאותו אובייקט
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Item:
    pass

first = Item()
first.qty = 3
second = first
second.qty += 2
print(first.qty, second.qty)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 5 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: first is second=True, qty=5

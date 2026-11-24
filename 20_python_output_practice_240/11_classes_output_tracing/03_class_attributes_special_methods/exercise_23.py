# -*- coding: utf-8 -*-
# תרגיל 23 | רשימה משותפת שמוגדרת במחלקה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Bag:
    items = []

a = Bag()
b = Bag()
a.items.append("A")
b.items.append("B")
print(a.items, b.items)
b.items = b.items + ["C"]
print(a.items, b.items)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# ['A', 'B'] ['A', 'B']
# ['A', 'B'] ['A', 'B', 'C']
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Bag.items=['A', 'B']; b.items is a separate list

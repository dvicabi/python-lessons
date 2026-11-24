# -*- coding: utf-8 -*-
# תרגיל 20 | שימוש ברשימה בתוך מחלקה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Register:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for name, price in self.items)

r = Register()
r.add("pen", 3)
r.add("book", 7)
r.add("pen", 3)
print(len(r.items), r.total())
print(r.items[1][0])

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 3 13
# book
# <<< END EXPECTED OUTPUT
# ערכים סופיים: r.total()=13

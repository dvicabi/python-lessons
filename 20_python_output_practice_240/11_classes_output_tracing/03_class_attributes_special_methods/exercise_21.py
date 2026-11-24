# -*- coding: utf-8 -*-
# תרגיל 21 | ספירת מופעים באמצעות מאפיין מחלקה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Visitor:
    total = 0

    def __init__(self, name):
        self.name = name
        Visitor.total += 1

a = Visitor("A")
b = Visitor("B")
print(Visitor.total, a.name, b.name)
c = Visitor("C")
print(Visitor.total)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 2 A B
# 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Visitor.total=3

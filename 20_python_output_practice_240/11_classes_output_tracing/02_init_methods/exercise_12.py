# -*- coding: utf-8 -*-
# תרגיל 12 | מתודה שמחזירה שטח
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
print(r.area())
r.width += 2
print(r.area())

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 12
# 20
# <<< END EXPECTED OUTPUT
# ערכים סופיים: r.width=5, r.height=4

# -*- coding: utf-8 -*-
# תרגיל 33 | ירושת מתודה בלי לדרוס אותה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Device:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Device:", self.name)

class Phone(Device):
    pass

p = Phone("Pixel")
p.show()
p.name = "Nokia"
p.show()

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# Device: Pixel
# Device: Nokia
# <<< END EXPECTED OUTPUT
# ערכים סופיים: p.name=Nokia

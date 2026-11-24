# -*- coding: utf-8 -*-
# תרגיל 15 | שרשור קריאות למתודה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Stepper:
    def __init__(self):
        self.x = 0

    def add(self, n):
        self.x += n
        return self

s = Stepper()
s.add(2).add(3)
print(s.x)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: s.x=5

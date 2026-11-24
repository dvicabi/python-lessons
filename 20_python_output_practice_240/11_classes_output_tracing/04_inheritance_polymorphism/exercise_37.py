# -*- coding: utf-8 -*-
# תרגיל 37 | דריסת מתודה שמשנה מצב אובייקט
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def boost(self):
        self.speed += 2

class Car(Vehicle):
    def boost(self):
        super().boost()
        self.speed *= 2

c = Car(3)
c.boost()
print(c.speed)
c.boost()
print(c.speed)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 10
# 24
# <<< END EXPECTED OUTPUT
# ערכים סופיים: c.speed=24

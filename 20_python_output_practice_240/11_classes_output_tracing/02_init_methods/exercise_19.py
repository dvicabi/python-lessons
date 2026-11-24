# -*- coding: utf-8 -*-
# תרגיל 19 | מתודה שפועלת על אובייקט אחר
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Team:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def transfer(self, other, amount):
        self.points -= amount
        other.points += amount

a = Team("A", 10)
b = Team("B", 3)
a.transfer(b, 4)
print(a.points, b.points)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 6 7
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.points=6, b.points=7

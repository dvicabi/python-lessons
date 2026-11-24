# -*- coding: utf-8 -*-
# תרגיל 17 | מתודה אחת קוראת למתודה אחרת
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Score:
    def __init__(self, points):
        self.points = points

    def bonus(self, n):
        return self.points + n

    def add_bonus(self, n):
        self.points = self.bonus(n)

s = Score(6)
print(s.bonus(4), s.points)
s.add_bonus(3)
print(s.points)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 10 6
# 9
# <<< END EXPECTED OUTPUT
# ערכים סופיים: s.points=9

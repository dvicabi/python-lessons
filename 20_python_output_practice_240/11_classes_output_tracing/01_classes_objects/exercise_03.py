# -*- coding: utf-8 -*-
# תרגיל 03 | מאפיין מחלקה לעומת מופע
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Player:
    points = 10

p = Player()
print(p.points)
p.points += 5
print(p.points, Player.points)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 10
# 15 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: p.points=15, Player.points=10

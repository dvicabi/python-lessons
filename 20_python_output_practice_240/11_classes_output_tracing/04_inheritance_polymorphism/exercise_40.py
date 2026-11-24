# -*- coding: utf-8 -*-
# תרגיל 40 | אתגר מסכם: ירושה, ספירת מופעים ולולאה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Player:
    count = 0

    def __init__(self, points):
        self.points = points
        Player.count += 1

    def add(self, n):
        self.points += n

    def score(self):
        return self.points

class BonusPlayer(Player):
    def add(self, n):
        super().add(n * 2)

a = Player(5)
b = BonusPlayer(3)
for i in range(1, 4):
    if i % 2 == 0:
        a.add(i)
    else:
        b.add(i)
    print(i, a.score(), b.score())
print("Players", Player.count)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 1 5 5
# 2 7 5
# 3 7 11
# Players 2
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.points=7, b.points=11, Player.count=2

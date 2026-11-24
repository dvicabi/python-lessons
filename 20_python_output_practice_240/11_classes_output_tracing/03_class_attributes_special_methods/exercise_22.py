# -*- coding: utf-8 -*-
# תרגיל 22 | עדכון מאפיין מחלקה והסתרה במופע
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Game:
    level = 1

g1 = Game()
g2 = Game()
g1.level = 5
Game.level = 3
print(g1.level, g2.level, Game.level)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 5 3 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: g1.level=5, g2.level=3, Game.level=3

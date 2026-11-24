# -*- coding: utf-8 -*-
# תרגיל 08 | הסתרת מאפיין מחלקה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Robot:
    version = 1

r1 = Robot()
r2 = Robot()
r1.version = 3
print(Robot.version, r1.version, r2.version)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 1 3 1
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Robot.version=1, r1.version=3, r2.version=1

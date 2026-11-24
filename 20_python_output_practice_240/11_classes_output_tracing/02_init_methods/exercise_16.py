# -*- coding: utf-8 -*-
# תרגיל 16 | ערכי ברירת מחדל בבנאי ובמתודה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Timer:
    def __init__(self, minutes=5):
        self.minutes = minutes

    def tick(self, amount=1):
        self.minutes -= amount
        return self.minutes

t1 = Timer()
t2 = Timer(3)
print(t1.tick(), t2.tick(2))
print(t1.minutes, t2.minutes)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 4 1
# 4 1
# <<< END EXPECTED OUTPUT
# ערכים סופיים: t1.minutes=4, t2.minutes=1

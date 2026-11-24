# -*- coding: utf-8 -*-
# תרגיל 26 | מאפיין property עם setter
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Thermometer:
    def __init__(self, temp):
        self._temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = max(0, value)

t = Thermometer(5)
t.temp = -3
print(t.temp)
t.temp = 8
print(t.temp)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 0
# 8
# <<< END EXPECTED OUTPUT
# ערכים סופיים: t._temp=8

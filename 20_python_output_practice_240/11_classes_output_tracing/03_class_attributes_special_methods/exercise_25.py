# -*- coding: utf-8 -*-
# תרגיל 25 | מתודה סטטית מול מתודת מופע
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Converter:
    @staticmethod
    def triple(n):
        return n * 3

    def calc(self, n):
        return self.triple(n) + 1

c = Converter()
print(Converter.triple(4))
print(c.calc(4))
print(c.triple(2))

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 12
# 13
# 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: calls returned 12, 13, 6

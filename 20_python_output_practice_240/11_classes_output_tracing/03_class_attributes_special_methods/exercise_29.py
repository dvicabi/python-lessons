# -*- coding: utf-8 -*-
# תרגיל 29 | מתודת מחלקה ושינוי ברמת המופע
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Counter:
    count = 0

    @classmethod
    def inc(cls):
        cls.count += 2

a = Counter()
b = Counter()
a.inc()
b.inc()
print(Counter.count, a.count)
a.count = 10
print(a.count, b.count)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 4 4
# 10 4
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Counter.count=4, a.count=10, b.count=4

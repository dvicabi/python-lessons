# -*- coding: utf-8 -*-
# תרגיל 18 | מעקב אחר מצבים נפרדים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Counter:
    def __init__(self, start):
        self.count = start

    def increase(self):
        self.count += 1
        print(self.count)

a = Counter(2)
b = Counter(8)
a.increase()
b.increase()
a.increase()
print(a.count + b.count)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 3
# 9
# 4
# 13
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.count=4, b.count=9

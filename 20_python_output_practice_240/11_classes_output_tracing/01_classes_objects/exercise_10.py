# -*- coding: utf-8 -*-
# תרגיל 10 | מעקב אחר שני אובייקטים בלולאה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Counter:
    pass

a = Counter()
b = Counter()
a.count = 1
b.count = 2

for i in range(1, 4):
    if i % 2 == 0:
        a.count += i
    else:
        b.count += i
    print(i, a.count, b.count)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 1 1 3
# 2 3 3
# 3 3 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.count=3, b.count=6

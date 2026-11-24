# -*- coding: utf-8 -*-
# תרגיל 09 | אובייקטים בתוך רשימה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Ticket:
    pass

tickets = []
for price in [5, 7, 10]:
    t = Ticket()
    t.price = price
    tickets.append(t)

tickets[0].price += 2
print([t.price for t in tickets])

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# [7, 7, 10]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: ticket prices=[7, 7, 10]

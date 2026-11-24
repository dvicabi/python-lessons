# -*- coding: utf-8 -*-
# תרגיל 13 | מתודות שמשנות יתרה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def pay(self, amount):
        self.balance -= amount

w = Wallet(20)
w.deposit(7)
w.pay(9)
print(w.balance)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 18
# <<< END EXPECTED OUTPUT
# ערכים סופיים: w.balance=18

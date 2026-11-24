# -*- coding: utf-8 -*-
# תרגיל 24 | מתודת מחלקה ליצירת מופעים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Member:
    count = 0

    def __init__(self, name):
        self.name = name
        Member.count += 1

    @classmethod
    def make(cls, name):
        return cls(name.upper())

a = Member.make("dan")
b = Member("Noa")
print(a.name, b.name, Member.count)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# DAN Noa 2
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Member.count=2

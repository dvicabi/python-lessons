# -*- coding: utf-8 -*-
# תרגיל 11 | בנאי __init__ ושינוי מצב
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Dana", 92)
print(s.name, s.grade)
s.grade += 5
print(s.grade)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# Dana 92
# 97
# <<< END EXPECTED OUTPUT
# ערכים סופיים: s.grade=97

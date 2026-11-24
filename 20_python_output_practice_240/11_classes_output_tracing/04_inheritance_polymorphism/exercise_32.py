# -*- coding: utf-8 -*-
# תרגיל 32 | קריאה לבנאי ההורה באמצעות super
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Noa", 90)
print(s.name, s.grade)
s.grade += 5
print(s.grade)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# Noa 90
# 95
# <<< END EXPECTED OUTPUT
# ערכים סופיים: s.name=Noa, s.grade=95

# -*- coding: utf-8 -*-
# תרגיל 30 | שינוי כלל משותף לכל האובייקטים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Course:
    threshold = 60

    def __init__(self, points):
        self.points = points

    def passed(self):
        return self.points >= Course.threshold

a = Course(65)
b = Course(58)
print(a.passed(), b.passed())
Course.threshold = 70
b.points += 15
print(a.passed(), b.passed())

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# True False
# False True
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Course.threshold=70; a.points=65; b.points=73

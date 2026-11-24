# -*- coding: utf-8 -*-
# תרגיל 27 | המתודה המיוחדת __str__
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages})"

b = Book("Python", 50)
print(b)
b.pages += 10
print(str(b))

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# Python (50)
# Python (60)
# <<< END EXPECTED OUTPUT
# ערכים סופיים: b.pages=60

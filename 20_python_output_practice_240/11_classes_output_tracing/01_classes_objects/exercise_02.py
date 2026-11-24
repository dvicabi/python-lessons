# -*- coding: utf-8 -*-
# תרגיל 02 | שני אובייקטים נפרדים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Dog:
    pass

a = Dog()
b = Dog()
a.name = "Rocky"
b.name = "Milo"
print(a.name, b.name)
print(a is b)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# Rocky Milo
# False
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a.name=Rocky, b.name=Milo

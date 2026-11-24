# -*- coding: utf-8 -*-
# תרגיל 38 | בדיקת סוג האובייקט והירושה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Shape:
    pass

class Circle(Shape):
    pass

x = Circle()
print(isinstance(x, Shape), isinstance(x, Circle))
print(type(x) == Shape)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# True True
# False
# <<< END EXPECTED OUTPUT
# ערכים סופיים: type(x)=Circle

# -*- coding: utf-8 -*-
# תרגיל 34 | פולימורפיזם ברשימת אובייקטים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Bird:
    def sound(self):
        return "tweet"

class Cow:
    def sound(self):
        return "moo"

animals = [Bird(), Cow(), Bird()]
for animal in animals:
    print(animal.sound(), end="|")
print("End")

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# tweet|moo|tweet|End
# <<< END EXPECTED OUTPUT
# ערכים סופיים: animals contains 3 objects

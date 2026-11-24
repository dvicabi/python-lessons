# -*- coding: utf-8 -*-
# תרגיל 31 | ירושה ודריסת מתודה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

a = Animal()
d = Dog()
print(a.speak(), d.speak())

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# ... Woof
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a is Animal; d is Dog

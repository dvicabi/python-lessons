# -*- coding: utf-8 -*-
# תרגיל 36 | קריאה דינמית למתודה שנדרסה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Parent:
    def message(self):
        return "parent"

    def show(self):
        print(self.message())

class Child(Parent):
    def message(self):
        return "child"

Parent().show()
Child().show()

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# parent
# child
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Parent().message()=parent; Child().message()=child

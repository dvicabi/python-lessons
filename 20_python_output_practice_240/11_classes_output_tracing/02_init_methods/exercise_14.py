# -*- coding: utf-8 -*-
# תרגיל 14 | הבדל בין print ל-return במתודה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Greeter:
    def say(self, name):
        print("Hi", name)
        return len(name)

g = Greeter()
result = g.say("Noa")
print("Length", result)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# Hi Noa
# Length 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: result=3

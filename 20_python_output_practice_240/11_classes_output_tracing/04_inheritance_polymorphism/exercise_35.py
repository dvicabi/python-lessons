# -*- coding: utf-8 -*-
# תרגיל 35 | שימוש ב-super למימוש חלקי של מתודה
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Base:
    def label(self):
        return "A"

class Child(Base):
    def label(self):
        return super().label() + "B"

print(Child().label())

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# AB
# <<< END EXPECTED OUTPUT
# ערכים סופיים: Child().label()=AB

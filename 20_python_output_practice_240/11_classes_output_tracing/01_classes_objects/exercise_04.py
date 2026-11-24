# -*- coding: utf-8 -*-
# תרגיל 04 | שינוי מאפיין בוליאני
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Lamp:
    pass

lamp = Lamp()
lamp.on = False
lamp.on = not lamp.on
print(lamp.on)
lamp.on = not lamp.on
print(lamp.on)

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# True
# False
# <<< END EXPECTED OUTPUT
# ערכים סופיים: lamp.on=False

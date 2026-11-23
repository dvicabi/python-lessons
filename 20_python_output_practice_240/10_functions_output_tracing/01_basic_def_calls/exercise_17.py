# -*- coding: utf-8 -*-
# תרגיל 17 | משתנה מקומי מול משתנה מחוץ לפונקציה
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

number = 5

def change(number):
    number += 4
    print("Inside", number)

change(number)
print("Outside", number)

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# Inside 9
# Outside 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: number outside=5

# -*- coding: utf-8 -*-
# תרגיל 01 | הגדרה וקריאות חוזרות
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def greet(name):
    print("Hello", name)

for i in range(2):
    greet("Dana")
print("Done")

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# Hello Dana
# Hello Dana
# Done
# <<< END EXPECTED OUTPUT
# ערכים סופיים: name in last call=Dana

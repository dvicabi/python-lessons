# -*- coding: utf-8 -*-
# תרגיל 19 | סדר הקריאה וההדפסה
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def start(n):
    print("Start", n)
    return n + 2

def finish(n):
    print("Finish", n)
    return n * 3

x = finish(start(3))
print("Result", x)

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# Start 3
# Finish 5
# Result 15
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=15

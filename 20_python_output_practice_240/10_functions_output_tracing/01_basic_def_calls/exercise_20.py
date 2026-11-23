# -*- coding: utf-8 -*-
# תרגיל 20 | סדר הקריאה וההדפסה
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def start(n):
    print("Start", n)
    return n + 2

def finish(n):
    print("Finish", n)
    return n * 3

x = finish(start(4))
print("Result", x)

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# Start 4
# Finish 6
# Result 18
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=18

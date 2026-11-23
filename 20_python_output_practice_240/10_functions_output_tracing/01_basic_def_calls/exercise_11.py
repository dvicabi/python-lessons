# -*- coding: utf-8 -*-
# תרגיל 11 | שתי פונקציות עם return
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def double(x):
    return x * 2

def plus_three(x):
    return x + 3

print(double(4))
print(plus_three(3))
print(double(plus_three(3)))

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# 8
# 6
# 12
# <<< END EXPECTED OUTPUT

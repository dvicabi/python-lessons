# -*- coding: utf-8 -*-
# תרגיל 12 | שתי פונקציות עם return
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def double(x):
    return x * 2

def plus_three(x):
    return x + 3

print(double(6))
print(plus_three(4))
print(double(plus_three(4)))

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# 12
# 7
# 14
# <<< END EXPECTED OUTPUT

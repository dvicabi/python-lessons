# -*- coding: utf-8 -*-
# תרגיל 16 | פונקציה שסוכמת בעזרת for
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def total_up_to(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(total_up_to(5))
print(total_up_to(7))

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# 15
# 28
# <<< END EXPECTED OUTPUT

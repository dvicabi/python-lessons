# -*- coding: utf-8 -*-
# תרגיל 15 | פונקציה שסוכמת בעזרת for
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def total_up_to(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(total_up_to(4))
print(total_up_to(6))

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# 10
# 21
# <<< END EXPECTED OUTPUT

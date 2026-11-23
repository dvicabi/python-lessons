# -*- coding: utf-8 -*-
# תרגיל 14 | תנאים בתוך פונקציה
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def label(number):
    if number % 2 == 0:
        return "EVEN"
    return "ODD"

print(label(6))
print(label(9))
print(label(4))

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# EVEN
# ODD
# EVEN
# <<< END EXPECTED OUTPUT

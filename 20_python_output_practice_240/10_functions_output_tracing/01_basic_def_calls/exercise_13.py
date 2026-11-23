# -*- coding: utf-8 -*-
# תרגיל 13 | תנאים בתוך פונקציה
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def label(number):
    if number % 2 == 0:
        return "EVEN"
    return "ODD"

print(label(5))
print(label(8))
print(label(3))

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# ODD
# EVEN
# ODD
# <<< END EXPECTED OUTPUT

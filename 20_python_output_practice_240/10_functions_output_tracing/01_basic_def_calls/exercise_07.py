# -*- coding: utf-8 -*-
# תרגיל 07 | ההבדל בין print לבין return
# חלק 1: הגדרת פונקציות וקריאה לפונקציות
# משימה: חשבו את הפלט המדויק לפני ההרצה. מתי יש print ומתי return?

def show_twice(x):
    print(x)
    print(x * 2)

result = show_twice(6)
print(result)
print("End")

# ------------------------------------------------------------
# פתרון סופי (תגובות בלבד):
# >>> EXPECTED OUTPUT
# 6
# 12
# None
# End
# <<< END EXPECTED OUTPUT
# ערכים סופיים: result=None

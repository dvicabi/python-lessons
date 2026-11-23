# -*- coding: utf-8 -*-
# תרגיל 45 | פונקציה שמחזירה רשימה חדשה בלי לשנות את המקור
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def transform(values, limit):
    output = []
    for x in values:
        if x > limit:
            output.append(x - 1)
        else:
            output.append(x * 2)
    return output

original = [2, 5, 3, 8, 4]
copy = transform(original, 4)
print(copy)
print(original)
print(transform(copy, 4))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [4, 4, 6, 7, 8]
# [2, 5, 3, 8, 4]
# [8, 8, 5, 6, 7]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: original=[2, 5, 3, 8, 4], copy=[4, 4, 6, 7, 8]

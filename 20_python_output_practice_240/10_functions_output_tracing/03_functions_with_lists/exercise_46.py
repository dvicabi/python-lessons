# -*- coding: utf-8 -*-
# תרגיל 46 | פונקציה שמחזירה רשימה חדשה בלי לשנות את המקור
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

original = [3, 6, 4, 9, 5]
copy = transform(original, 5)
print(copy)
print(original)
print(transform(copy, 5))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [6, 5, 8, 8, 10]
# [3, 6, 4, 9, 5]
# [5, 10, 7, 7, 9]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: original=[3, 6, 4, 9, 5], copy=[6, 5, 8, 8, 10]

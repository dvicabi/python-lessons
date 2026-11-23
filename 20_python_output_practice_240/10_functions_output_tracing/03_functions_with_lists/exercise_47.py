# -*- coding: utf-8 -*-
# תרגיל 47 | לשנות רשימה ולשמור הפניה (Alias)
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def modify(values):
    values.append(values[0] + values[-1])
    values[1] += 2
    return len(values)

items = [4, 1, 7]
alias = items
print(modify(alias))
print(items)
items.append(3)
print(alias)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 4
# [4, 3, 7, 11]
# [4, 3, 7, 11, 3]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: items=[4, 3, 7, 11, 3], alias refers to items

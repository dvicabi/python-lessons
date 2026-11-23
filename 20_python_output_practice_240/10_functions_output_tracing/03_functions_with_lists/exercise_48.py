# -*- coding: utf-8 -*-
# תרגיל 48 | לשנות רשימה ולשמור הפניה (Alias)
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def modify(values):
    values.append(values[0] + values[-1])
    values[1] += 2
    return len(values)

items = [5, 2, 8]
alias = items
print(modify(alias))
print(items)
items.append(4)
print(alias)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 4
# [5, 4, 8, 13]
# [5, 4, 8, 13, 4]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: items=[5, 4, 8, 13, 4], alias refers to items

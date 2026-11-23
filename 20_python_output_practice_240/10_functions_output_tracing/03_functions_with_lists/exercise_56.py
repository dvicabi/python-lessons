# -*- coding: utf-8 -*-
# תרגיל 56 | פונקציה שבונה מטריצה מרשימה
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def build_rows(values, offset):
    result = []
    for x in values:
        result.append([x, x + offset])
    return result

values = [3, 5, 7]
rows = build_rows(values, 4)
print(rows)
print(rows[1][1])
print(values)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [[3, 7], [5, 9], [7, 11]]
# 9
# [3, 5, 7]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: rows=[[3, 7], [5, 9], [7, 11]], values=[3, 5, 7]

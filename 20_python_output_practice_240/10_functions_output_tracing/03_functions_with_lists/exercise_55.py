# -*- coding: utf-8 -*-
# תרגיל 55 | פונקציה שבונה מטריצה מרשימה
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def build_rows(values, offset):
    result = []
    for x in values:
        result.append([x, x + offset])
    return result

values = [2, 4, 6]
rows = build_rows(values, 3)
print(rows)
print(rows[1][1])
print(values)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [[2, 5], [4, 7], [6, 9]]
# 7
# [2, 4, 6]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: rows=[[2, 5], [4, 7], [6, 9]], values=[2, 4, 6]

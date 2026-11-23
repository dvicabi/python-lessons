# -*- coding: utf-8 -*-
# תרגיל 51 | פונקציה שסופרת התאמות בין שתי רשימות
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def count_pairs(a, b, divisor):
    count = 0
    for x in a:
        for y in b:
            if (x + y) % divisor == 0:
                count += 1
    return count

a = [2, 5, 8]
b = [3, 4, 6]
print(count_pairs(a, b, 3))
print(count_pairs(b, a, 2))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 3
# 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a=[2, 5, 8], b=[3, 4, 6]

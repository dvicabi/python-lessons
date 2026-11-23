# -*- coding: utf-8 -*-
# תרגיל 59 | שתי פונקציות שקוראות אחת לשנייה ועובדות על רשימה
# חלק 3: פונקציות עם רשימות ולולאות
# משימה: האם הפונקציה מחזירה רשימה חדשה או משנה את הרשימה הקיימת? חשבו את הפלט.

def choose(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result

def score(numbers):
    selected = choose(numbers)
    total = 0
    for x in selected:
        total += x * 2
    return total

numbers = [2, 5, 8, 3]
print(choose(numbers))
print(score(numbers))
print(score(numbers[1:]))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [2, 8]
# 20
# 16
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[2, 5, 8, 3]

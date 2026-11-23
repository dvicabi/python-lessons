# -*- coding: utf-8 -*-
# תרגיל 60 | שתי פונקציות שקוראות אחת לשנייה ועובדות על רשימה
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

numbers = [3, 6, 9, 4]
print(choose(numbers))
print(score(numbers))
print(score(numbers[1:]))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# [6, 4]
# 20
# 20
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[3, 6, 9, 4]

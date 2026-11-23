# -*- coding: utf-8 -*-
# תרגיל 25 | *args מקבל מספר משתנה של ארגומנטים
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def summarize(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(len(numbers), total)
    return total

x = summarize(3, 5, 2)
print(x * 2)
summarize(3, 5)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 3 10
# 20
# 2 8
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=10

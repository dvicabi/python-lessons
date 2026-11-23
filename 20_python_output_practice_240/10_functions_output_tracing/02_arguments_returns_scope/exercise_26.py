# -*- coding: utf-8 -*-
# תרגיל 26 | *args מקבל מספר משתנה של ארגומנטים
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

def summarize(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(len(numbers), total)
    return total

x = summarize(4, 6, 3)
print(x * 2)
summarize(4, 6)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 3 13
# 26
# 2 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=13

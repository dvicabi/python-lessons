# -*- coding: utf-8 -*-
# תרגיל 64 | רקורסיה עם return אחרי חזרת הקריאה
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def factorial(n):
    if n == 1:
        print("Base", n)
        return 1
    result = n * factorial(n - 1)
    print("Return", n, result)
    return result

print("FINAL", factorial(5))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Base 1
# Return 2 2
# Return 3 6
# Return 4 24
# Return 5 120
# FINAL 120
# <<< END EXPECTED OUTPUT
# ערכים סופיים: factorial=120

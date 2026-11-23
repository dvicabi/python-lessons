# -*- coding: utf-8 -*-
# תרגיל 66 | עץ קריאות של פיבונאצ'י
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def fib(n):
    print("Call", n)
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("FINAL", fib(5))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Call 5
# Call 4
# Call 3
# Call 2
# Call 1
# Call 0
# Call 1
# Call 2
# Call 1
# Call 0
# Call 3
# Call 2
# Call 1
# Call 0
# Call 1
# FINAL 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: fib=5

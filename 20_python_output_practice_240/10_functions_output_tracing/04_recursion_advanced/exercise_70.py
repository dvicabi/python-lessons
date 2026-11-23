# -*- coding: utf-8 -*-
# תרגיל 70 | רקורסיה על ספרות של מספר
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def digit_sum(n):
    if n < 10:
        print("Last", n)
        return n
    rest = digit_sum(n // 10)
    digit = n % 10
    print("Digit", digit, "Sum", rest + digit)
    return rest + digit

print("FINAL", digit_sum(345))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Last 3
# Digit 4 Sum 7
# Digit 5 Sum 12
# FINAL 12
# <<< END EXPECTED OUTPUT
# ערכים סופיים: sum=12

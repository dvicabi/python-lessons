# -*- coding: utf-8 -*-
# תרגיל 74 | שתי פונקציות רקורסיביות שקוראות זו לזו
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def is_even(n):
    print("Even?", n)
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    print("Odd?", n)
    if n == 0:
        return False
    return is_even(n - 1)

print("FINAL", is_even(5))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Even? 5
# Odd? 4
# Even? 3
# Odd? 2
# Even? 1
# Odd? 0
# FINAL False
# <<< END EXPECTED OUTPUT

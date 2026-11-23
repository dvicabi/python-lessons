# -*- coding: utf-8 -*-
# תרגיל 73 | שתי פונקציות רקורסיביות שקוראות זו לזו
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

print("FINAL", is_even(4))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Even? 4
# Odd? 3
# Even? 2
# Odd? 1
# Even? 0
# FINAL True
# <<< END EXPECTED OUTPUT

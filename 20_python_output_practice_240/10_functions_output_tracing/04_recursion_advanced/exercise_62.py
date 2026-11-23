# -*- coding: utf-8 -*-
# תרגיל 62 | רקורסיה: הדפסה בירידה ובעלייה
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def countdown(n):
    if n == 0:
        print("ZERO")
        return
    print("Down", n)
    countdown(n - 1)
    print("Up", n)

countdown(4)
print("DONE")

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Down 4
# Down 3
# Down 2
# Down 1
# ZERO
# Up 1
# Up 2
# Up 3
# Up 4
# DONE
# <<< END EXPECTED OUTPUT

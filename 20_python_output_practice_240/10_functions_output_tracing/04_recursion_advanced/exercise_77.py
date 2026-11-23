# -*- coding: utf-8 -*-
# תרגיל 77 | פונקציה פנימית עם nonlocal ומונה קריאות
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def make_tracer():
    calls = 0
    def trace(n):
        nonlocal calls
        calls += 1
        print("Enter", n, calls)
        if n == 0:
            return calls
        answer = trace(n - 1)
        print("Exit", n, answer)
        return answer
    return trace

f = make_tracer()
print("First", f(3))
print("Second", f(1))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Enter 3 1
# Enter 2 2
# Enter 1 3
# Enter 0 4
# Exit 1 4
# Exit 2 4
# Exit 3 4
# First 4
# Enter 1 5
# Enter 0 6
# Exit 1 6
# Second 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: number of calls=6

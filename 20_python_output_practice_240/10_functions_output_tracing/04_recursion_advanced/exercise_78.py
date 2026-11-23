# -*- coding: utf-8 -*-
# תרגיל 78 | פונקציה פנימית עם nonlocal ומונה קריאות
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
print("First", f(4))
print("Second", f(2))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Enter 4 1
# Enter 3 2
# Enter 2 3
# Enter 1 4
# Enter 0 5
# Exit 1 5
# Exit 2 5
# Exit 3 5
# Exit 4 5
# First 5
# Enter 2 6
# Enter 1 7
# Enter 0 8
# Exit 1 8
# Exit 2 8
# Second 8
# <<< END EXPECTED OUTPUT
# ערכים סופיים: number of calls=8

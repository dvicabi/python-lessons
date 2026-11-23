# -*- coding: utf-8 -*-
# תרגיל 75 | פונקציה רקורסיבית עם לולאה בתוך כל קריאה
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def calculate(n):
    if n == 0:
        return 0
    previous = calculate(n - 1)
    local_sum = 0
    for i in range(1, n + 1):
        local_sum += i
    answer = previous + local_sum
    print(n, local_sum, answer)
    return answer

print("FINAL", calculate(3))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 1 1
# 2 3 4
# 3 6 10
# FINAL 10
# <<< END EXPECTED OUTPUT

# -*- coding: utf-8 -*-
# תרגיל 68 | סכום רשימה ברקורסיה ושורות החזרה
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def recursive_sum(values, i=0):
    if i == len(values):
        return 0
    tail = recursive_sum(values, i + 1)
    result = values[i] + tail
    print(i, result)
    return result

numbers = [4, 6, 3, 8]
print("FINAL", recursive_sum(numbers))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 3 8
# 2 11
# 1 17
# 0 21
# FINAL 21
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[4, 6, 3, 8]

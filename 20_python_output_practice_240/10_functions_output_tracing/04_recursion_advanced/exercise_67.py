# -*- coding: utf-8 -*-
# תרגיל 67 | סכום רשימה ברקורסיה ושורות החזרה
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def recursive_sum(values, i=0):
    if i == len(values):
        return 0
    tail = recursive_sum(values, i + 1)
    result = values[i] + tail
    print(i, result)
    return result

numbers = [3, 5, 2, 7]
print("FINAL", recursive_sum(numbers))

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 3 7
# 2 9
# 1 14
# 0 17
# FINAL 17
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[3, 5, 2, 7]

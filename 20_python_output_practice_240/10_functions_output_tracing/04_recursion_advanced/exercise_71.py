# -*- coding: utf-8 -*-
# תרגיל 71 | רקורסיה שבונה רשימה הפוכה בלי לשנות מקור
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def reverse_list(items):
    if len(items) == 0:
        return []
    result = reverse_list(items[1:]) + [items[0]]
    print("Step", result)
    return result

numbers = [2, 5, 8, 4]
print("Reverse", reverse_list(numbers))
print("Original", numbers)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Step [4]
# Step [4, 8]
# Step [4, 8, 5]
# Step [4, 8, 5, 2]
# Reverse [4, 8, 5, 2]
# Original [2, 5, 8, 4]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[2, 5, 8, 4]

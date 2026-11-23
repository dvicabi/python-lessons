# -*- coding: utf-8 -*-
# תרגיל 72 | רקורסיה שבונה רשימה הפוכה בלי לשנות מקור
# חלק 4: רקורסיה ופונקציות מתקדמות
# משימה: ציירו עץ קריאות ועקבו אחר סדר ההדפסות. כל קריאה מחזיקה ערכים מקומיים משלה.

def reverse_list(items):
    if len(items) == 0:
        return []
    result = reverse_list(items[1:]) + [items[0]]
    print("Step", result)
    return result

numbers = [3, 6, 9, 5]
print("Reverse", reverse_list(numbers))
print("Original", numbers)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Step [5]
# Step [5, 9]
# Step [5, 9, 6]
# Step [5, 9, 6, 3]
# Reverse [5, 9, 6, 3]
# Original [3, 6, 9, 5]
# <<< END EXPECTED OUTPUT
# ערכים סופיים: numbers=[3, 6, 9, 5]

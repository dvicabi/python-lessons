# -*- coding: utf-8 -*-
# תרגיל 33 | global לעומת משתנה מקומי
# חלק 2: פרמטרים, ברירות מחדל, החזרת ערכים ו-scope
# משימה: חשבו מה קורה בכל קריאה לפונקציה והציגו את הפלט המדויק.

value = 5

def local_change(value):
    value += 3
    print("Local", value)

def global_change():
    global value
    value += 2
    print("Global", value)

local_change(value)
print("Before", value)
global_change()
print("After", value)

# ------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# Local 8
# Before 5
# Global 7
# After 7
# <<< END EXPECTED OUTPUT
# ערכים סופיים: global value=7

# -*- coding: utf-8 -*-
# אתגר 36 | while ושתי for עם חישוב תלוי תוצאה קודמת
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

i = 1
result = 4
odd = 0
steps = 0

while i <= 5:
    for j in range(1, i + 3):
        for k in range(j + 1, 0, -1):
            if (result + j * k) % 2 == 1:
                result += i + k
                odd += 1
            else:
                result -= j

            if result > 30:
                result //= 2

            steps += 1

        if j % 2 == 0:
            result += odd % 3

    print(i, result, odd, steps)
    i += 1

print("FINAL", result + odd + steps)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 -16 0 9
# 2 -56 0 23
# 3 -126 0 43
# 4 -238 0 70
# 5 -406 0 105
# FINAL -301
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=6, result=-406, odd=0, steps=105

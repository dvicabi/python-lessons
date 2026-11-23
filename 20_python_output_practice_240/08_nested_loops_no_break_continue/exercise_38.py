# -*- coding: utf-8 -*-
# אתגר 38 | for-while-while עם שתי בדיקות מסונכרנות
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

total = 10
shifts = 0
pulses = 0

for i in range(5, 1, -1):
    j = i

    while j >= 1:
        k = 2

        while k <= j + 2:
            if (total + i + k) % 5 <= 1:
                total += j - k
                shifts += 1
            else:
                total += i - j
                pulses += 1

            if total % 3 == 0:
                total //= 3
                total += k

            k += 2

        j -= 1

    print(i, total, shifts, pulses)

print("FINAL", total + shifts * 2 - pulses)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 5 7 4 7
# 4 10 6 13
# 3 10 8 16
# 2 5 9 18
# FINAL 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=5, shifts=9, pulses=18

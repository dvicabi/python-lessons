# -*- coding: utf-8 -*-
# אתגר 37 | for-while-while עם שתי בדיקות מסונכרנות
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

total = 9
shifts = 0
pulses = 0

for i in range(4, 1, -1):
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
# 4 14 4 4
# 3 10 6 7
# 2 5 7 9
# FINAL 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=5, shifts=7, pulses=9

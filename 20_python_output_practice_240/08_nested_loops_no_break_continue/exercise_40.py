# -*- coding: utf-8 -*-
# אתגר 40 | שלוש לולאות עם if/elif/else ותוצאת checksum
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

x = 15
y = 5
z = 0
steps = 0

for i in range(1, 5):
    for j in range(i, i + 3):
        for k in range(2, j + 3, 2):
            if (x + y + i * k) % 4 == 0:
                x += j + k
                y -= i
            elif x % 3 == 1:
                y += k * i
                z += j
            else:
                x -= i + k
                z += y % 3

            if x < 0:
                x += y + 7

            if y > 25:
                y //= 2

            steps += 1

        if (x + z) % 2 == 0:
            z -= i
        else:
            z += j

    print(i, x, y, z, steps)

print("CHECKSUM", x * 2 + y * 3 + z - steps)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 4 11 16 5
# 2 14 14 28 12
# 3 14 11 33 20
# 4 2 11 58 30
# CHECKSUM 65
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=2, y=11, z=58, steps=30

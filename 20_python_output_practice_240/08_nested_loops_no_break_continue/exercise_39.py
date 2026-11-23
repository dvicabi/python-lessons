# -*- coding: utf-8 -*-
# אתגר 39 | שלוש לולאות עם if/elif/else ותוצאת checksum
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

x = 13
y = 4
z = 0
steps = 0

for i in range(1, 4):
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
# 1 13 18 15 5
# 2 14 13 23 12
# 3 21 13 38 20
# CHECKSUM 99
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=21, y=13, z=38, steps=20

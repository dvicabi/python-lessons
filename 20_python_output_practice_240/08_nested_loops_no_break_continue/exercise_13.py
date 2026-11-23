# -*- coding: utf-8 -*-
# אתגר 13 | for עם while ו-for נסתרת בתוכה
# רמה: קשה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וערכו טבלת מעקב לכל המשתנים.
# הקפידו על סדר ביצוע התנאים, וסיימו רק כשתנאי הלולאה מפסיק להתקיים.

x = 4
y = 1
count = 0

for i in range(1, 3+1):
    j = 1
    while j <= i + 2:
        for k in range(1, j + 1):
            if (i + j + k) % 2 == 0:
                x += k
            else:
                x -= i

            if x % 4 == 0:
                y += j
            count += 1

        if j % 2 == 0:
            y -= i
        j += 1

    print(i, x, y, count)

print("CHECK", x + y + count)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 3 5 6
# 2 8 16 16
# 3 -6 26 31
# CHECK 51
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=-6, y=26, count=31

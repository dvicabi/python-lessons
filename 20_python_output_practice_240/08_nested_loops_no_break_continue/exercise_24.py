# -*- coding: utf-8 -*-
# אתגר 24 | שלוש לולאות וקיזוז לפי שאריות
# רמה: קשה מאוד | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וסכמו את השינויים בטבלת מעקב.
# שימו לב: תנאים בתוך הלולאות עשויים להשפיע על כל סיבוב עתידי.

x = 11
y = 4
visits = 0

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, i + j):
            if (i * j + k) % 3 == 0:
                x += j * k
                y -= i
            elif (x + y) % 2 == 0:
                x -= i + k
                y += j
            else:
                x += i
                y += k

            visits += 1

    print(i, x, y, visits)

print("CHECK", x * 2 + y - visits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 22 8 6
# 2 27 14 15
# 3 26 23 27
# CHECK 48
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=26, y=23, visits=27

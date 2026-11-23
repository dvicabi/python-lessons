# -*- coding: utf-8 -*-
# אתגר 23 | שלוש לולאות וקיזוז לפי שאריות
# רמה: קשה מאוד | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וסכמו את השינויים בטבלת מעקב.
# שימו לב: תנאים בתוך הלולאות עשויים להשפיע על כל סיבוב עתידי.

x = 10
y = 3
visits = 0

for i in range(1, 3):
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
# 1 21 7 6
# 2 26 13 15
# CHECK 50
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=26, y=13, visits=15

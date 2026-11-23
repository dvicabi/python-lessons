# -*- coding: utf-8 -*-
# אתגר 26 | for-while-for ומשתנה שנשלט מכל הרמות
# רמה: קשה מאוד | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וסכמו את השינויים בטבלת מעקב.
# שימו לב: תנאים בתוך הלולאות עשויים להשפיע על כל סיבוב עתידי.

z = 7
total = 0
tick = 0

for i in range(1, 5):
    j = i + 2
    while j >= i:
        for k in range(j, 0, -2):
            if (z + i * k) % 5 < 2:
                z += j - k
                total += i
            else:
                z -= i
                total += k

            tick += 1

        j -= 1

    print(i, z, total, tick)

print("FINAL", z + total - tick)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 5 5 4
# 2 1 18 9
# 3 3 38 16
# 4 -11 68 24
# FINAL 33
# <<< END EXPECTED OUTPUT
# ערכים סופיים: z=-11, total=68, tick=24

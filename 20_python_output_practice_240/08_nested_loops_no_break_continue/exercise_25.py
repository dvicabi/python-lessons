# -*- coding: utf-8 -*-
# אתגר 25 | for-while-for ומשתנה שנשלט מכל הרמות
# רמה: קשה מאוד | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וסכמו את השינויים בטבלת מעקב.
# שימו לב: תנאים בתוך הלולאות עשויים להשפיע על כל סיבוב עתידי.

z = 5
total = 0
tick = 0

for i in range(1, 4):
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
# 1 5 7 4
# 2 1 20 9
# 3 3 40 16
# FINAL 27
# <<< END EXPECTED OUTPUT
# ערכים סופיים: z=3, total=40, tick=16

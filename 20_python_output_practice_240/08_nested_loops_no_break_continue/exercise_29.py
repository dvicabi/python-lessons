# -*- coding: utf-8 -*-
# אתגר 29 | שלוש לולאות שיוצרות מפת תווים משתנה
# רמה: קשה מאוד | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וסכמו את השינויים בטבלת מעקב.
# שימו לב: תנאים בתוך הלולאות עשויים להשפיע על כל סיבוב עתידי.

mask = 2
power = 0

for i in range(1, 4):
    row = ""

    for j in range(1, i + 3):
        for k in range(1, 4):
            if (i + j + k + mask) % 3 == 0:
                row += "@"
                power += k
            else:
                row += "-"
                mask += j % 2

        if power % 2 == 0:
            row += "|"
        else:
            row += ":"

    print(i, row, mask, power)

print("FINAL", mask + power)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 --@:-@-:@-@: 5 9
# 2 @-@:-@-:@-@:-@-: 7 21
# 3 @-@:-@-:@-@:-@-:@-@: 10 37
# FINAL 47
# <<< END EXPECTED OUTPUT
# ערכים סופיים: mask=10, power=37

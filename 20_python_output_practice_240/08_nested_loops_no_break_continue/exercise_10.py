# -*- coding: utf-8 -*-
# אתגר 10 | שלוש לולאות for ומשוואת הניקוד
# רמה: מתקדם | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק ובנו טבלת מעקב של המשתנים.
# הפתרון נמצא בתחתית הקובץ. קודם נסו לפתור בלי להריץ.

total = 5
count = 0

for i in range(1, 4):
    for j in range(1, i + 2):
        for k in range(1, j + 2):
            if (i + j + k) % 3 == 0:
                total += i * k
            else:
                total -= j
            count += 1

    print(i, total, count)

print("CHECK", total + count)

# ---------------------------------------------------------------
# פתרון סופי (הערות בלבד, לא מודפסות על ידי התוכנית):
# >>> EXPECTED OUTPUT
# 1 4 5
# 2 6 14
# 3 19 28
# CHECK 47
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=19, count=28

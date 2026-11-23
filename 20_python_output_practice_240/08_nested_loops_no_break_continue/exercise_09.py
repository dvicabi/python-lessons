# -*- coding: utf-8 -*-
# אתגר 09 | שלוש לולאות for ומשוואת הניקוד
# רמה: מתקדם | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק ובנו טבלת מעקב של המשתנים.
# הפתרון נמצא בתחתית הקובץ. קודם נסו לפתור בלי להריץ.

total = 4
count = 0

for i in range(1, 3):
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
# 1 3 5
# 2 5 14
# CHECK 19
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=5, count=14

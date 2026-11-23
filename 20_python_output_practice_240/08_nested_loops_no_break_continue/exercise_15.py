# -*- coding: utf-8 -*-
# אתגר 15 | while-for-while ושאריות מתחלפות
# רמה: קשה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וערכו טבלת מעקב לכל המשתנים.
# הקפידו על סדר ביצוע התנאים, וסיימו רק כשתנאי הלולאה מפסיק להתקיים.

i = 1
value = 6
hits = 0

while i <= 3:
    for j in range(i, i + 3):
        k = 1
        while k <= j:
            if (value + k) % 3 == 0:
                value = (value + i * j) % 41
                hits += 1
            else:
                value = (value * 2 + k) % 41

            k += 1

    print(i, value, hits)
    i += 1

print("TOTAL", value + hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 30 1
# 2 16 2
# 3 27 4
# TOTAL 31
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=4, value=27, hits=4

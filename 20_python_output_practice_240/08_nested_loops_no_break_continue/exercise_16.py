# -*- coding: utf-8 -*-
# אתגר 16 | while-for-while ושאריות מתחלפות
# רמה: קשה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וערכו טבלת מעקב לכל המשתנים.
# הקפידו על סדר ביצוע התנאים, וסיימו רק כשתנאי הלולאה מפסיק להתקיים.

i = 1
value = 7
hits = 0

while i <= 4:
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
# 1 29 1
# 2 28 3
# 3 39 7
# 4 15 11
# TOTAL 26
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=5, value=15, hits=11

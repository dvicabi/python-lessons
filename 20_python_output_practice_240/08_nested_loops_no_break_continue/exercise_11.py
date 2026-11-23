# -*- coding: utf-8 -*-
# אתגר 11 | שלוש לולאות עם בונוסים ותוצאה שלילית
# רמה: קשה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וערכו טבלת מעקב לכל המשתנים.
# הקפידו על סדר ביצוע התנאים, וסיימו רק כשתנאי הלולאה מפסיק להתקיים.

score = 9
bonus = 0

for i in range(4, 1, -1):
    for j in range(1, i + 1):
        for k in range(j, 0, -1):
            if (i * k + j) % 3 == 0:
                score += i + k
            else:
                score -= j

            if score % 7 == 0:
                bonus += k
                score += bonus % 3

    print(i, score, bonus)

print("FINAL", score - bonus)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 4 6 0
# 3 16 3
# 2 22 4
# FINAL 18
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=22, bonus=4

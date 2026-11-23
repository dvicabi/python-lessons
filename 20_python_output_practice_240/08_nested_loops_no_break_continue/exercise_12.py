# -*- coding: utf-8 -*-
# אתגר 12 | שלוש לולאות עם בונוסים ותוצאה שלילית
# רמה: קשה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק וערכו טבלת מעקב לכל המשתנים.
# הקפידו על סדר ביצוע התנאים, וסיימו רק כשתנאי הלולאה מפסיק להתקיים.

score = 10
bonus = 0

for i in range(5, 1, -1):
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
# 5 33 1
# 4 32 2
# 3 42 3
# 2 49 6
# FINAL 43
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=49, bonus=6

# -*- coding: utf-8 -*-
# אתגר 31 | שלוש לולאות while ומעקב אחרי שינויי מצב
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

i = 1
score = 8
hits = 0

while i <= 3:
    j = i + 1

    while j > 0:
        k = 1

        while k <= j:
            if (score + i * j + k) % 4 == 0:
                score += j * k
                hits += 1
            elif score % 2 == 0:
                score //= 2
                score += i
            else:
                score += i - k

            k += 1

        j -= 1

    print(i, score, hits)
    i += 1

print("FINAL", score + hits)

# ---------------------------------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 3 0
# 2 10 3
# 3 12 5
# FINAL 17
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=4, score=12, hits=5

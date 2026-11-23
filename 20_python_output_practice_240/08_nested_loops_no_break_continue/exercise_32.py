# -*- coding: utf-8 -*-
# אתגר 32 | שלוש לולאות while ומעקב אחרי שינויי מצב
# רמה: אתגר קצה | לולאות מקוננות: 3
# משימה: חשבו את הפלט המדויק. רשמו את סדר הפעולות ואת מצב המשתנים בכל סיבוב.
# רמז: טבלת מעקב מלאה עדיפה מניסיון לנחש את התוצאה.

i = 1
score = 9
hits = 0

while i <= 4:
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
# 1 11 2
# 2 14 5
# 3 16 8
# 4 12 10
# FINAL 22
# <<< END EXPECTED OUTPUT
# ערכים סופיים: i=5, score=12, hits=10

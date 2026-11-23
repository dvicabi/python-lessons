# -*- coding: utf-8 -*-
# אתגר בונוס 02: שלוש לולאות for מקוננות
# משימה: חשבו את כל הפלט ומלאו טבלת מעקב: i, j, k, score, subtotal, count, skipped.
# שימו לב: break ו-continue משפיעים רק על הלולאה הפנימית ביותר.

score = 3
count = 0
skipped = 0

for i in range(3, 0, -1):
    for j in range(i, 5):
        subtotal = 0

        for k in range(1, j + 1):
            if (i + j + k) % 4 == 0:
                skipped += 1
                continue

            if (i * k) % 2 == 0:
                score += j - k
            else:
                score -= i + k

            subtotal += score % 5
            count += 1

            if subtotal > 7:
                break

        if (score + subtotal) % 2 == 0:
            score += i
        else:
            score -= j

        print(i, j, score, subtotal, count, skipped)

    print("END", i, score)

print("FINAL", score, count, skipped)

# -----------------------------------------------------
# פתרון סופי: הפלט המדויק של התוכנית
# >>> EXPECTED OUTPUT
# 3 3 -4 7 2 1
# 3 4 -12 7 5 2
# END 3 -12
# 2 2 -13 8 7 2
# 2 3 -8 4 9 3
# 2 4 -2 2 12 4
# END 2 -2
# 1 1 -5 1 13 4
# 1 2 -7 0 14 5
# 1 3 -11 6 17 5
# 1 4 -15 10 20 6
# END 1 -15
# FINAL -15 20 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=-15, count=20, skipped=6, i=1, j=4, k=4

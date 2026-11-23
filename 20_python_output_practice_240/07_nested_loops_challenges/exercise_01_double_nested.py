# -*- coding: utf-8 -*-
# אתגר בונוס 01: שתי לולאות מקוננות (for + while)
# משימה: חשבו את כל שורות הפלט ובנו טבלת מעקב: i, j, x, y, skips.
# שימו לב: continue ו-break פועלים רק על לולאת while הפנימית.

x = 7
y = 3
skips = 0

for i in range(5, 0, -1):
    j = 1

    while j <= i + 1:
        if (i + j + y) % 4 == 0:
            skips += 1
            y += j % 3
            j += 1
            continue

        if (i * j + x) % 2 == 0:
            x += i * j - y
        else:
            x -= i + j

        if x < 0:
            x += y * 2

        if x > 20:
            x //= 2
            y += 1

        if j % 3 == 0 and x % 2 == 0:
            break

        j += 1

    if i % 2 == 0:
        y += i // 2

    print(i, j, x, y, skips)

print("FINAL", x + y + skips)

# -----------------------------------------------------
# פתרון סופי: הפלט המדויק של התוכנית
# >>> EXPECTED OUTPUT
# 5 3 0 3 0
# 4 3 12 6 1
# 3 5 14 6 2
# 2 3 8 7 2
# 1 3 1 7 2
# FINAL 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=1, y=7, skips=2, i=1, j=3

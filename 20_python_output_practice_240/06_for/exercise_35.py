# תרגיל 35 | לולאות for | אתגר
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

x = 6
y = 19
count = 0
for i in range(1, 9):
    if (x + i) % 3 == 0:
        x += i
        count += 1
    elif y % 2 == 0:
        y //= 2
        x -= 1
    else:
        y -= i
        x *= 2
    if x > 20:
        x //= 2
    print(i, x, y, count)
print("End", x, y, count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 12 18 0
# 2 11 9 0
# 3 11 6 0
# 4 15 6 1
# 5 14 3 1
# 6 14 -3 1
# 7 10 -3 2
# 8 18 -3 3
# End 18 -3 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=18, y=-3, count=3

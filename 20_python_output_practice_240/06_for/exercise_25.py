# תרגיל 25 | לולאות for | מתקדם
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

x = 5
y = 17
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
# 1 6 17 1
# 2 12 15 1
# 3 15 15 2
# 4 15 11 2
# 5 15 6 2
# 6 10 6 3
# 7 9 3 3
# 8 18 -5 3
# End 18 -5 3
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=18, y=-5, count=3

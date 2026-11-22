# תרגיל 05 | לולאות for | קל
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

x = 3
y = 13
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
# 1 6 12 0
# 2 5 6 0
# 3 4 3 0
# 4 8 -1 0
# 5 16 -6 0
# 6 15 -3 0
# 7 15 -10 0
# 8 14 -5 0
# End 14 -5 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=14, y=-5, count=0

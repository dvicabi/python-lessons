# תרגיל 15 | לולאות for | בינוני
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

x = 4
y = 15
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
# 1 8 14 0
# 2 7 7 0
# 3 14 4 0
# 4 18 4 1
# 5 17 2 1
# 6 16 1 1
# 7 16 -6 1
# 8 12 -6 2
# End 12 -6 2
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=12, y=-6, count=2

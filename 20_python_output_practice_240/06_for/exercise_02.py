# תרגיל 02 | לולאות for | קל
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

x = 18
for i in range(1, 6):
    if i % 2 == 0:
        x -= i
    else:
        x += i
    print(i, x)
print("Final", x)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 19
# 2 17
# 3 20
# 4 16
# 5 21
# Final 21
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=21

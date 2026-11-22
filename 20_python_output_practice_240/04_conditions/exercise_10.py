# תרגיל 10 | תנאים ופעולות לוגיות | קל
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

x = 12
y = 5
z = 3
if x > y:
    x -= z
    if x > y:
        y += z
    else:
        y -= z
else:
    x += y
if x > y:
    z = x - y
else:
    z = y - x
print(x, y, z)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 9 8 1
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=9, y=8, z=1

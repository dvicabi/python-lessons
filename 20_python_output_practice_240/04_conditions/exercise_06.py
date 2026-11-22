# תרגיל 06 | תנאים ופעולות לוגיות | קל
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

a = 4
b = 9
c = 13
if a + b == c and b - a > 5:
    print("A")
elif a * 3 > b and c % 2 == 1:
    print("B")
elif a + c > b or b % 3 == 0:
    print("C")
else:
    print("D")
if a * b < c * 3:
    print("E")

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# B
# E
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a=4, b=9, c=13

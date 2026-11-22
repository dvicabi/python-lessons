# תרגיל 08 | תנאים ופעולות לוגיות | קל
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

a = 7
b = 12
c = 5
if a + c > b and b - a > c:
    print("A")
elif a * 2 > b or c * 3 < b:
    print("B")
elif a + b > 20:
    print("C")
else:
    print("D")

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# B
# <<< END EXPECTED OUTPUT
# ערכים סופיים: a=7, b=12, c=5

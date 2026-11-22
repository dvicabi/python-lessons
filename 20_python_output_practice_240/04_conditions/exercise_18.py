# תרגיל 18 | תנאים ופעולות לוגיות | בינוני
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

a = 8
b = 11
c = 6
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
# ערכים סופיים: a=8, b=11, c=6

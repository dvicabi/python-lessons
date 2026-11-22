# תרגיל 38 | תנאים ופעולות לוגיות | אתגר
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

a = 10
b = 9
c = 8
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
# ערכים סופיים: a=10, b=9, c=8

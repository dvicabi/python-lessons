# תרגיל 35 | תנאים ופעולות לוגיות | אתגר
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

x = 26
y = 9
z = 5
if x % z == 0 and y * z > x:
    print("A")
elif x // y == 3 or x % y == 2:
    print("B")
    if x - y > 15 and z * 2 < y:
        print("C")
    elif x % y == 3 or z + y > 10:
        print("D")
    else:
        print("E")
else:
    print("F")
print(x + y + z)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# F
# 40
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=26, y=9, z=5

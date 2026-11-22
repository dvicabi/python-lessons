# תרגיל 15 | תנאים ופעולות לוגיות | בינוני
# איזה ענף תנאי מתבצע ומה הפלט המדויק? הכינו טבלת מעקב.

x = 22
y = 7
z = 3
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
# B
# E
# 32
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=22, y=7, z=3

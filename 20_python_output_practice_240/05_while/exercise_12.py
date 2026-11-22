# תרגיל 12 | לולאות while | בינוני
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

x = 2
total = 0
while x <= 7:
    total += x
    print(x, total)
    x += 1
print(total)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 2 2
# 3 5
# 4 9
# 5 14
# 6 20
# 7 27
# 27
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=8, total=27

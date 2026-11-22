# תרגיל 02 | לולאות while | קל
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

x = 1
total = 0
while x <= 5:
    total += x
    print(x, total)
    x += 1
print(total)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 1
# 2 3
# 3 6
# 4 10
# 5 15
# 15
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=6, total=15

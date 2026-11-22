# תרגיל 07 | לולאות while | קל
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

x = 26
count = 0
while x > 1:
    x //= 2
    count += 1
    print(x, count)
print("Done", count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 13 1
# 6 2
# 3 3
# 1 4
# Done 4
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=1, count=4

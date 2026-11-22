# תרגיל 17 | לולאות while | בינוני
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

x = 36
count = 0
while x > 1:
    x //= 2
    count += 1
    print(x, count)
print("Done", count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 18 1
# 9 2
# 4 3
# 2 4
# 1 5
# Done 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=1, count=5

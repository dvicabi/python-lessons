# תרגיל 37 | לולאות while | אתגר
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

x = 56
count = 0
while x > 1:
    x //= 2
    count += 1
    print(x, count)
print("Done", count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 28 1
# 14 2
# 7 3
# 3 4
# 1 5
# Done 5
# <<< END EXPECTED OUTPUT
# ערכים סופיים: x=1, count=5

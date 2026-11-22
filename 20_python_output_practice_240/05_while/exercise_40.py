# תרגיל 40 | לולאות while | אתגר
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

i = 0
total = 0
while i < 22:
    i += 1
    if i % 4 == 0:
        continue
    if total > 28:
        break
    total += i
    print(i, total)
print("Final", total, i)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1 1
# 2 3
# 3 6
# 5 11
# 6 17
# 7 24
# 9 33
# Final 33 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=33, i=10

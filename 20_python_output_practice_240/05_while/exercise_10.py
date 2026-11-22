# תרגיל 10 | לולאות while | קל
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

i = 0
total = 0
while i < 16:
    i += 1
    if i % 4 == 0:
        continue
    if total > 16:
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
# Final 17 7
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=17, i=7

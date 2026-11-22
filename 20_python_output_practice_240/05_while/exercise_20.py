# תרגיל 20 | לולאות while | בינוני
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

i = 0
total = 0
while i < 18:
    i += 1
    if i % 4 == 0:
        continue
    if total > 20:
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
# Final 24 9
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=24, i=9

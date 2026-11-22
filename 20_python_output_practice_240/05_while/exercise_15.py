# תרגיל 15 | לולאות while | בינוני
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

num = 93524
total = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        total += digit
    else:
        total -= digit
    num //= 10
print(total, num)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# -11 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: num=0, total=-11

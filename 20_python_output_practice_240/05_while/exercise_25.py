# תרגיל 25 | לולאות while | מתקדם
# מה הפלט המדויק? מלאו טבלת מעקב והסבירו מתי הלולאה נעצרת.

num = 61873
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
# 3 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: num=0, total=3

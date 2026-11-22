# תרגיל 14 | לולאות for | בינוני
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

num = 49582
total = 0
for i in range(5):
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
# 0 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=0, num=0

# תרגיל 34 | לולאות for | אתגר
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

num = 96248
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
# 11 0
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=11, num=0

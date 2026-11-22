# תרגיל 18 | לולאות for | בינוני
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

total = 0
for i in range(1, 15):
    if i % 4 == 0:
        continue
    if total > 25:
        break
    total += i
print(total, i)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 33 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=33, i=10

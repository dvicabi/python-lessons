# תרגיל 08 | לולאות for | קל
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

total = 0
for i in range(1, 15):
    if i % 4 == 0:
        continue
    if total > 20:
        break
    total += i
print(total, i)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 24 9
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=24, i=9

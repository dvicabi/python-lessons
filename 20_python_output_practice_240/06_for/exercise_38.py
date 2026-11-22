# תרגיל 38 | לולאות for | אתגר
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

total = 0
for i in range(1, 15):
    if i % 4 == 0:
        continue
    if total > 35:
        break
    total += i
print(total, i)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 43 11
# <<< END EXPECTED OUTPUT
# ערכים סופיים: total=43, i=11

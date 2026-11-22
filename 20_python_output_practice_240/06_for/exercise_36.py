# תרגיל 36 | לולאות for | אתגר
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

count = 0
for i in range(1, 24):
    if i % 3 == 0 or i % 4 == 0:
        count += 1
print(count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 11
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=11

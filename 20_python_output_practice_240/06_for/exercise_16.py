# תרגיל 16 | לולאות for | בינוני
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

count = 0
for i in range(1, 18):
    if i % 3 == 0 or i % 4 == 0:
        count += 1
print(count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 8
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=8

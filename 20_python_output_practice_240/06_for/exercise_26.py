# תרגיל 26 | לולאות for | מתקדם
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

count = 0
for i in range(1, 21):
    if i % 3 == 0 or i % 4 == 0:
        count += 1
print(count)

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 10
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=10

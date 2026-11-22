# תרגיל 07 | לולאות for | קל
# מה הפלט המדויק? הכינו טבלת מעקב לכל איטרציה.

for i in range(1, 4):
    for j in range(1, i + 1):
        print(i * j, end="|")
    print()

# --------------------------------------
# פתרון סופי:
# >>> EXPECTED OUTPUT
# 1|
# 2|4|
# 3|6|9|
# <<< END EXPECTED OUTPUT

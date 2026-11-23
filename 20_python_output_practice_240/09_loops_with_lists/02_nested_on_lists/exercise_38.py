# -*- coding: utf-8 -*-
# תרגיל 38 | תחרות בין איברי רשימה בסדר הפוך
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

a = [5, 8, 1, 4]
b = a[::-1]
wins = 0
score = 0
for x in a:
    for y in b:
        if x > y:
            wins += 1
            score += x - y
        elif x == y:
            score += 2
    print(x, wins, score)
print("FINAL", score)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 5 2 7
# 8 5 23
# 1 5 25
# 4 6 30
# FINAL 30
# <<< END EXPECTED OUTPUT
# ערכים סופיים: wins=6, score=30

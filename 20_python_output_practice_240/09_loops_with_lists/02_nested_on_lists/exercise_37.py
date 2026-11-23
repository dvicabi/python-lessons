# -*- coding: utf-8 -*-
# תרגיל 37 | תחרות בין איברי רשימה בסדר הפוך
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

a = [3, 6, 2, 8]
b = a[::-1]
wins = 0
score = 0
for x in a:
    for y in b:
        if x > y:
            wins += 1
            score += x - y
        elif x == y:
            score += 1
    print(x, wins, score)
print("FINAL", score)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 3 1 2
# 6 3 10
# 2 3 11
# 8 6 25
# FINAL 25
# <<< END EXPECTED OUTPUT
# ערכים סופיים: wins=6, score=25

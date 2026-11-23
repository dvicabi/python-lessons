# -*- coding: utf-8 -*-
# תרגיל 22 | ספירת זוגות שאפשר לחבר
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [4, 1, 6, 2]
count = 0
score = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) % 4 == 0:
            count += 1
            score += numbers[i] * numbers[j]
    print(i, count, score)
print("FINAL", score - count)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 0 0
# 1 0 0
# 2 1 12
# 3 1 12
# FINAL 11
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=1, score=12

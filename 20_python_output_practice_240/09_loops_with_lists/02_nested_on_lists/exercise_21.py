# -*- coding: utf-8 -*-
# תרגיל 21 | ספירת זוגות שאפשר לחבר
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 2
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [2, 5, 3, 7]
count = 0
score = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) % 3 == 0:
            count += 1
            score += numbers[i] * numbers[j]
    print(i, count, score)
print("FINAL", score - count)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 1 14
# 1 2 49
# 2 2 49
# 3 2 49
# FINAL 47
# <<< END EXPECTED OUTPUT
# ערכים סופיים: count=2, score=49

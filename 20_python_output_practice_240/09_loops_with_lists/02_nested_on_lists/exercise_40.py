# -*- coding: utf-8 -*-
# תרגיל 40 | שלוש לולאות על רשימה אחת
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 3
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [9, 3, 5]
score = 3
count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1):
            if (numbers[i] + numbers[j] + k + score) % 2 == 0:
                score += i + j + k
                count += 1
            else:
                score -= numbers[k] % 4
    print(i, score, count)
print("FINAL", score + count)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 -6 0
# 1 0 2
# 2 0 2
# FINAL 2
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=0, count=2

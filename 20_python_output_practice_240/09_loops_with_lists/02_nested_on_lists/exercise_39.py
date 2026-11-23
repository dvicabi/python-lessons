# -*- coding: utf-8 -*-
# תרגיל 39 | שלוש לולאות על רשימה אחת
# נושא: לולאות מקוננות על רשימה אחת או מספר רשימות.
# עומק לולאות: 3
# משימה: חשבו את הפלט ובנו טבלת מעקב לכל שינוי באיברים.

numbers = [2, 7, 4]
score = 2
count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1):
            if (numbers[i] + numbers[j] + k + score) % 2 == 0:
                score += i + j + k
                count += 1
            else:
                score -= numbers[k] % 3
    print(i, score, count)
print("FINAL", score + count)

# --------------------------------------------------------
# הפלט הסופי המדויק:
# >>> EXPECTED OUTPUT
# 0 2 2
# 1 3 3
# 2 3 3
# FINAL 6
# <<< END EXPECTED OUTPUT
# ערכים סופיים: score=3, count=3

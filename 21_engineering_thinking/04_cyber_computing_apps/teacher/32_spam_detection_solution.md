# פתרונות למורה: מערכת לזיהוי ספאם: מתי התראה שגויה מזיקה יותר מהחמצה?

[חזרה למשימת התלמיד](../32_spam_detection.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
MESSAGE 12 | DEMO
Flags: 2 / 3
Links: 1 / 3
Score: 8 points
Decision: REVIEW | CHECK
```

### ב. פלט התרחיש השני

```text
MESSAGE  | 12 | DEMO
Flags: 2 / 3
Links: 1 / 3
Score: 8 points
Decision: REVIEW | CHECK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("MESSAGE ", end="")
print("13", end="")
print(" | DEMO")
print("Flags: ", end="")
print("1", end="")
print(" / 3")
print("Links: ", end="")
print("0", end="")
print(" / 3")
print("Score: ", end="")
print("3", end="")
print(" points")
print("Decision: ", end="")
print("NORMAL", end="")
print(" | READY")
```

פלט:

```text
MESSAGE 13 | DEMO
Flags: 1 / 3
Links: 0 / 3
Score: 3 points
Decision: NORMAL | READY
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
1 0 1 7
2 2 1 14
2 2 0 10
2 1 0 8
Parts: 6 2 0
Change: 1
Check: 8
```

### ב. פלט התרחיש השני

```text
1 0 1 7
2 3 1 16
2 3 0 12
2 2 0 10
Parts: 6 4 0
Change: 3
Check: 10
```

### ג. תשובות והערות לדיון

ערך נגזר חייב להתעדכן.

unknown מוסיף 4 ליחידה, flags 3 ו-links 2.

צבירה על ניקוד קודם סופרת מאפיינים פעמיים.

ניקוד הוא כלל דמה, לא הוכחה.

### ד. פתרון אפשרי

```python
flags = 0
links = 1
unknown = 0
first = flags * 3 + links * 2 + unknown * 4
flags += 2
print(flags * 3, links * 2, unknown * 4, flags * 3 + links * 2 + unknown * 4)
unknown = 1
print(flags * 3, links * 2, unknown * 4, flags * 3 + links * 2 + unknown * 4)
links += 1
print(flags * 3, links * 2, unknown * 4, flags * 3 + links * 2 + unknown * 4)
flags -= 1
score = flags * 3 + links * 2 + unknown * 4
print(flags * 3, links * 2, unknown * 4, score)
print(score - first)
```

פלט:

```text
6 2 0 8
6 2 4 12
6 4 4 14
3 4 4 11
9
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 8 0
B: 7 -1
Score gap: 1
Flag gap: 1
Link gap: 1
Unknown gap: -1
Total: 15
```

### ב. פלט התרחיש השני

```text
A: 14 4
B: 7 -3
Score gap: 7
Flag gap: 1
Link gap: 2
Unknown gap: 0
Total: 21
```

### ג. תשובות והערות לדיון

gap=0 הוא גבול הסף.

שלילי מציין מתחתיו.

סכומי משקלים יכולים להיות זהים עבור מאפיינים שונים.

נדרשת תווית אמת עצמאית.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
2
1
0
1
0
1
3
2
1
8
```

```python
flags_a = int(input())
links_a = int(input())
unknown_a = int(input())
flags_b = int(input())
links_b = int(input())
unknown_b = int(input())
flags_c = int(input())
links_c = int(input())
unknown_c = int(input())
threshold = int(input())
score_a = flags_a * 3 + links_a * 2 + unknown_a * 4
score_b = flags_b * 3 + links_b * 2 + unknown_b * 4
score_c = flags_c * 3 + links_c * 2 + unknown_c * 4
print(score_a, score_a - threshold)
print(score_b, score_b - threshold)
print(score_c, score_c - threshold)
total = score_a + score_b + score_c
print(total, total // 3)
```

פלט:

```text
8 0
7 -1
17 9
32 10
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
REVIEW
8 FP
Cost: 2
```

### ב. פלט התרחיש השני

```text
NORMAL
8 TN
Cost: 0
```

### ג. תשובות והערות לדיון

predicted הוא החלטה ו-truth תווית בדויה עצמאית.

פריט תקין שסומן הוא FP.

8 הוא ערך גבול חוקי.

FP הוא סימון יתר ו-FN החמצה.

נתון שגוי אינו בסיס להערכת איכות.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
1
0
1
1
8
```

```python
flags = int(input())
links = int(input())
unknown = int(input())
truth = int(input())
threshold = int(input())
score = -1
if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
    outcome = "INVALID"
else:
    score = flags * 3 + links * 2 + unknown * 4
    predicted = score >= threshold
    if predicted:
        print("REVIEW")
        if truth == 1:
            outcome = "TP"
        else:
            outcome = "FP"
    else:
        print("NORMAL")
        if truth == 1:
            outcome = "FN"
        else:
            outcome = "TN"
print(score, outcome)
cost = 0
if outcome == "FP":
    cost = 2
elif outcome == "FN":
    cost = 5
print("Cost:", cost)
if outcome != "INVALID":
    print(outcome == "TP" or outcome == "TN")
```

פלט:

```text
NORMAL
7 FN
Cost: 5
False
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 8 FP
2 7 FN
3 17 TP
4 2 TN
5 7 FN
6 10 FP
7 INVALID
8 0 TN
1 2 2 2
Valid: 7 Invalid: 1
Cost: 14
Correct percent: 42
```

### ב. פלט התרחיש השני

```text
1 8 TP
2 7 TN
3 17 TP
4 2 TN
5 7 FN
6 10 FP
7 INVALID
8 0 TN
2 1 1 3
Valid: 7 Invalid: 1
Cost: 7
Correct percent: 71
```

### ג. תשובות והערות לדיון

invalid אינו בסיס להערכת החלטה.

טעויות בעלות שונה ולכן אחוז הצלחה לבדו אינו מספיק.

valid+invalid שווה מספר פריטים.

יש להימנע מחלוקה באפס.

סף גבוה עשוי להפחית FP אך להגדיל FN.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
8
8
2
5
2
1
0
0
1
0
1
1
3
2
1
1
0
1
0
0
1
2
0
1
2
2
0
0
4
0
0
1
0
0
0
0
```

```python
count = int(input())
threshold = int(input())
fp_cost = int(input())
fn_cost = int(input())
tp = 0
fp = 0
fn = 0
tn = 0
invalid = 0
for i in range(count):
    flags = int(input())
    links = int(input())
    unknown = int(input())
    truth = int(input())
    if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
        invalid += 1
        print(i + 1, "INVALID")
    else:
        score = flags * 3 + links * 2 + unknown * 4
        if score >= threshold:
            if truth == 1:
                tp += 1
                outcome = "TP"
            else:
                fp += 1
                outcome = "FP"
        elif truth == 1:
            fn += 1
            outcome = "FN"
        else:
            tn += 1
            outcome = "TN"
        print(i + 1, score, outcome)
valid = tp + fp + fn + tn
cost = fp * fp_cost + fn * fn_cost
print(tp, fp, fn, tn)
print("Valid:", valid, "Invalid:", invalid)
print("Cost:", cost)
print("Marked:", tp + fp)
print("Actual spam:", tp + fn)
if valid > 0:
    correct = (tp + tn) * 100
    print("Correct percent:", correct // valid)
else:
    print("NO DATA")
```

פלט:

```text
1 8 FP
2 7 FN
3 17 TP
4 2 TN
5 7 FN
6 10 FP
7 INVALID
8 0 TN
1 2 2 2
Valid: 7 Invalid: 1
Cost: 14
Marked: 3
Actual spam: 3
Correct percent: 42
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
6 [3, 2, 0, 2] 1 4
8 [1, 2, 2, 2] 1 14
10 [1, 1, 2, 3] 1 12
Best: 6 4
[[6, [3, 2, 0, 2], 1, 4], [8, [1, 2, 2, 2], 1, 14], [10, [1, 1, 2, 3], 1, 12]]
```

### ב. פלט התרחיש השני

```text
6 [3, 2, 0, 2] 1 10
8 [1, 2, 2, 2] 1 14
10 [1, 1, 2, 3] 1 9
Best: 10 9
[[6, [3, 2, 0, 2], 1, 10], [8, [1, 2, 2, 2], 1, 14], [10, [1, 1, 2, 3], 1, 9]]
```

### ג. תשובות והערות לדיון

כל מדיניות נבדקת מאפס.

האינדקסים הם TP,FP,FN,TN לפי סדר.

שינוי מחיר נותן משקל אחר לטעויות.

best משווה את הספים.

שוויון משאיר ראשון.

אוסף נוסף בודק האם הבחירה מתאימה גם לנתונים אחרים.

### ד. פתרון אפשרי

```python
messages = [[2, 1, 0, 0], [1, 0, 1, 1], [3, 2, 1, 1], [0, 1, 0, 0], [1, 2, 0, 1], [2, 2, 0, 0], [4, 0, 0, 1], [0, 0, 0, 0]]
thresholds = [6, 8, 10]
reports = []
best = -1
best_cost = -1
fewest = -1
best_errors = -1
for threshold in thresholds:
    counts = [0, 0, 0, 0]
    invalid = 0
    for row in messages:
        flags = row[0]
        links = row[1]
        unknown = row[2]
        truth = row[3]
        if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
            invalid += 1
        else:
            score = flags * 3 + links * 2 + unknown * 4
            if score >= threshold:
                if truth == 1:
                    counts[0] += 1
                else:
                    counts[1] += 1
            elif truth == 1:
                counts[2] += 1
            else:
                counts[3] += 1
    cost = counts[1] * 2 + counts[2] * 5
    valid = counts[0] + counts[1] + counts[2] + counts[3]
    correct = (counts[0] + counts[3]) * 100
    accuracy = -1
    if valid > 0:
        accuracy = correct // valid
    errors = counts[1] + counts[2]
    if fewest == -1 or errors < best_errors:
        fewest = threshold
        best_errors = errors
    reports.append([threshold, counts, invalid, cost, accuracy, errors])
    if best == -1 or cost < best_cost:
        best = threshold
        best_cost = cost
    print(threshold, counts, invalid, cost)
print("Best:", best, best_cost)
print("Fewest errors:", fewest, best_errors)
print(reports)
```

פלט:

```text
6 [3, 2, 0, 2] 1 4
8 [1, 2, 2, 2] 1 14
10 [1, 1, 2, 3] 1 12
Best: 6 4
Fewest errors: 6 2
[[6, [3, 2, 0, 2], 1, 4, 71, 2], [8, [1, 2, 2, 2], 1, 14, 42, 4], [10, [1, 1, 2, 3], 1, 12, 57, 3]]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
1
[[6, [3, 2, 0, 1], 0, 4], [[6, [3, 2, 0, 1], 0, 4], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 12]]]
[[10, [1, 1, 2, 2], 0, 9], [[6, [3, 2, 0, 1], 0, 10], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 9]]]
[[], []]
```

### ב. פלט התרחיש השני

```text
3
[[6, [3, 2, 0, 1], 0, 4], [[6, [3, 2, 0, 1], 0, 4], [8, [1, 1, 2, 2], 0, 12], [10, [1, 0, 2, 3], 0, 10]]]
[[10, [1, 0, 2, 3], 0, 4], [[6, [3, 2, 0, 1], 0, 10], [8, [1, 1, 2, 2], 0, 9], [10, [1, 0, 2, 3], 0, 4]]]
[[], []]
```

### ג. תשובות והערות לדיון

אינדקס מקל על ספירת ארבע קטגוריות.

-1 בפייתון הוא האינדקס האחרון ולכן יש לסנן.

ניקוד 8 חייב להיספר REVIEW בסף 8.

evaluate בודקת מדיניות אחת, choose משווה.

הקלט רק נקרא.

ספים ריקים מחזירים שתי רשימות ריקות.

### ד. פתרון אפשרי

```python
def classify(row, threshold):
    flags = row[0]
    links = row[1]
    unknown = row[2]
    truth = row[3]
    if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
        return -1
    score = flags * 3 + links * 2 + unknown * 4
    if score >= threshold:
        if truth == 1:
            return 0
        return 1
    if truth == 1:
        return 2
    return 3

def evaluate(messages, threshold, fp_cost, fn_cost):
    counts = [0, 0, 0, 0]
    invalid = 0
    for row in messages:
        index = classify(row, threshold)
        if index == -1:
            invalid += 1
        else:
            counts[index] += 1
    cost = counts[1] * fp_cost + counts[2] * fn_cost
    valid = counts[0] + counts[1] + counts[2] + counts[3]
    percent = -1
    if valid > 0:
        correct = (counts[0] + counts[3]) * 100
        percent = correct // valid
    return [threshold, counts, invalid, cost, percent]

def choose(messages, thresholds, fp_cost, fn_cost):
    best = []
    reports = []
    for threshold in thresholds:
        result = evaluate(messages, threshold, fp_cost, fn_cost)
        reports.append(result)
        if len(best) == 0 or result[3] < best[3]:
            best = result
    return [best, reports]

def compare_on_new(new_messages, selection, fp_cost, fn_cost):
    best = selection[0]
    if len(best) == 0:
        return []
    return evaluate(new_messages, best[0], fp_cost, fn_cost)

messages = [[2, 1, 0, 0], [1, 0, 1, 1], [3, 2, 1, 1], [0, 1, 0, 0], [1, 2, 0, 1], [2, 2, 0, 0]]
print(classify([2, 1, 0, 0], 8))
print(choose(messages, [6, 8, 10], 2, 5))
print(choose(messages, [6, 8, 10], 5, 2))
print(choose(messages, [], 2, 5))
selection = choose(messages, [6, 8, 10], 2, 5)
print(compare_on_new([[0, 1, 1, 0], [2, 0, 0, 1], [3, 1, 0, 1]], selection, 2, 5))
```

פלט:

```text
1
[[6, [3, 2, 0, 1], 0, 4, 66], [[6, [3, 2, 0, 1], 0, 4, 66], [8, [1, 2, 2, 1], 0, 14, 33], [10, [1, 1, 2, 2], 0, 12, 50]]]
[[10, [1, 1, 2, 2], 0, 9, 50], [[6, [3, 2, 0, 1], 0, 10, 66], [8, [1, 2, 2, 1], 0, 14, 33], [10, [1, 1, 2, 2], 0, 9, 50]]]
[[], []]
[6, [2, 1, 0, 0], 0, 2, 66]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[0, [[6, [3, 2, 0, 1], 0, 4], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 12]]]
[2, [[6, [3, 2, 0, 1], 0, 10], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 9]]]
[6, [2, 1, 0, 0], 0, 2]
[10, [1, 0, 1, 1], 0, 2]
[]
1 1
```

### ב. פלט התרחיש השני

```text
[2, [[6, [3, 2, 0, 1], 0, 16], [8, [1, 2, 2, 1], 0, 18], [10, [1, 1, 2, 2], 0, 10]]]
[2, [[6, [3, 2, 0, 1], 0, 10], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 9]]]
[10, [1, 0, 1, 1], 0, 1]
[10, [1, 0, 1, 1], 0, 2]
[]
1 1
```

### ג. תשובות והערות לדיון

המדיניות משותפת לקריאה בלבד והיומנים עצמאיים.

מטרות עלות שונות יכולות לבחור ספים שונים.

בדיקה נפרדת חייבת לבדוק את הבחירה ולא להתאים אותה מחדש.

שימוש חוזר בנתוני בחירה עלול להטעות.

סכום מונים ו-invalid תואם מספר רשומות.

אין להסיק ביצועי מערכת אמיתית מסימולציה.

### ד. פתרון אפשרי

```python
class ReviewPolicy:
    def __init__(self, threshold):
        self.threshold = threshold

    def outcome(self, row):
        flags = row[0]
        links = row[1]
        unknown = row[2]
        truth = row[3]
        if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
            return -1
        score = flags * 3 + links * 2 + unknown * 4
        if score >= self.threshold:
            if truth == 1:
                return 0
            return 1
        if truth == 1:
            return 2
        return 3

class Experiment:
    def __init__(self, policies, fp_cost, fn_cost):
        self.policies = policies
        self.fp_cost = fp_cost
        self.fn_cost = fn_cost
        self.history = []

    def report(self, policy, messages):
        counts = [0, 0, 0, 0]
        invalid = 0
        for row in messages:
            result = policy.outcome(row)
            if result == -1:
                invalid += 1
            else:
                counts[result] += 1
        cost = counts[1] * self.fp_cost + counts[2] * self.fn_cost
        return [policy.threshold, counts, invalid, cost]

    def run(self, messages):
        reports = []
        best = -1
        for i in range(len(self.policies)):
            result = self.report(self.policies[i], messages)
            reports.append(result)
            if best == -1 or result[3] < reports[best][3]:
                best = i
        self.history.append(reports)
        return [best, reports]

    def audit(self, report, count):
        values = report[1]
        return values[0] + values[1] + values[2] + values[3] + report[2] == count

    def summary(self):
        total = 0
        for reports in self.history:
            total += len(reports)
        return [len(self.history), total]

    def review_selected(self, messages, index):
        if index < 0 or index >= len(self.policies):
            return []
        return self.report(self.policies[index], messages)

a = ReviewPolicy(6)
b = ReviewPolicy(8)
c = ReviewPolicy(10)
lab = Experiment([a, b, c], 2, 5)
other = Experiment([a, b, c], 5, 2)
messages = [[2, 1, 0, 0], [1, 0, 1, 1], [3, 2, 1, 1], [0, 1, 0, 0], [1, 2, 0, 1], [2, 2, 0, 0]]
test = [[0, 1, 1, 0], [2, 0, 0, 1], [3, 1, 0, 1]]
first = lab.run(messages)
second = other.run(messages)
print(first)
print(second)
print(lab.review_selected(test, first[0]))
print(other.review_selected(test, second[0]))
print(lab.review_selected(test, -1))
for report in first[1]:
    print(lab.audit(report, len(messages)))
for report in second[1]:
    print(other.audit(report, len(messages)))
print(lab.audit(lab.review_selected(test, first[0]), len(test)))
print(lab.summary(), other.summary())
```

פלט:

```text
[0, [[6, [3, 2, 0, 1], 0, 4], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 12]]]
[2, [[6, [3, 2, 0, 1], 0, 10], [8, [1, 2, 2, 1], 0, 14], [10, [1, 1, 2, 2], 0, 9]]]
[6, [2, 1, 0, 0], 0, 2]
[10, [1, 0, 1, 1], 0, 2]
[]
True
True
True
True
True
True
True
[1, 3] [1, 3]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

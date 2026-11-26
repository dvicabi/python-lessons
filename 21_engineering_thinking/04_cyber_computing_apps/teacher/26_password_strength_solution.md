# פתרונות למורה: בדיקת חוזק סיסמה: מה מדד פשוט יודע ומה הוא מפספס?

[חזרה למשימת התלמיד](../26_password_strength.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
CHECK 01 | DEMO
Length: 8 chars
Groups: 3 / 4
Score: 25 points
Result: PASS_DEMO | RULE
```

### ב. פלט התרחיש השני

```text
CHECK  | 01 | DEMO
Length: 8 chars
Groups: 3 / 4
Score: 25 points
Result: PASS_DEMO | RULE
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("CHECK ", end="")
print("02", end="")
print(" | DEMO")
print("Length: ", end="")
print("6", end="")
print(" chars")
print("Groups: ", end="")
print("2", end="")
print(" / 4")
print("Score: ", end="")
print("18", end="")
print(" points")
print("Result: ", end="")
print("REVIEW", end="")
print(" | RULE")
```

פלט:

```text
CHECK 02 | DEMO
Length: 6 chars
Groups: 2 / 4
Score: 18 points
Result: REVIEW | RULE
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
8 4 28
10 4 32
9 3 27
12 3 33
Length part: 24
Group part: 9
Check: 12
```

### ב. פלט התרחיש השני

```text
8 4 28
12 4 36
11 3 31
14 3 37
Length part: 28
Group part: 9
Check: 14
```

### ג. תשובות והערות לדיון

מספר קבוצות תלוי בקיום קבוצה ולא בכמותה.

הסרת תו אחרון בקבוצה מבטלת אותה.

ערך מחושב חייב להתעדכן.

הניקוד מלאכותי.

### ד. פתרון אפשרי

```python
lower = 4
upper = 1
digits = 2
symbols = 0
groups = 3
symbols += 2
groups += 1
length = lower + upper + digits + symbols
print(length, groups, length * 2 + groups * 3)
upper -= 1
groups -= 1
length = lower + upper + digits + symbols
print(length, groups, length * 2 + groups * 3)
digits += 1
length = lower + upper + digits + symbols
print(length, groups, length * 2 + groups * 3)
```

פלט:

```text
9 4 30
8 3 25
9 3 27
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Features: 3 2 2 1
Length: 8
Score: 28
Parts: 16 12
Gaps: 0 1
Check: 28
```

### ב. פלט התרחיש השני

```text
Features: 5 0 2 0
Length: 7
Score: 20
Parts: 14 6
Gaps: -1 -1
Check: 20
```

### ג. תשובות והערות לדיון

פער שלילי מציין חוסר.

groups צריך להתאים לקבוצות לא ריקות.

ניקוד אינו מחליף שני תנאי סף.

אפשר לחשב קבוצות מהספירות ברמה הבאה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
9
2
8
3
8
3
```

```python
length_a = int(input())
groups_a = int(input())
length_b = int(input())
groups_b = int(input())
min_length = int(input())
min_groups = int(input())
score_a = length_a * 2 + groups_a * 3
score_b = length_b * 2 + groups_b * 3
print("A:", score_a, length_a - min_length, groups_a - min_groups)
print("B:", score_b, length_b - min_length, groups_b - min_groups)
print("Gap:", score_a - score_b)
```

פלט:

```text
A: 24 1 -1
B: 25 0 0
Gap: -1
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
PASS_DEMO
8 3
Score: 25
```

### ב. פלט התרחיש השני

```text
FEW GROUPS
REVIEW
8 2
Score: 22
```

### ג. תשובות והערות לדיון

קבוצות מתקיימות במקביל.

שני ספים חובה.

ניקוד יכול לנבוע ממאפיינים שונים.

אורך 8 ושלוש קבוצות הוא הגבול.

שלילי אינו מאפיין חוקי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
1
1
0
12
3
```

```python
lower = int(input())
upper = int(input())
digits = int(input())
symbols = int(input())
min_length = int(input())
min_groups = int(input())
groups = 0
score = -1
if lower < 0 or upper < 0 or digits < 0 or symbols < 0:
    print("INVALID")
else:
    if lower > 0:
        groups += 1
    if upper > 0:
        groups += 1
    if digits > 0:
        groups += 1
    if symbols > 0:
        groups += 1
    length = lower + upper + digits + symbols
    score = length * 2 + groups * 3
    if length < min_length:
        print("SHORT")
    if groups < min_groups:
        print("FEW GROUPS")
    if length >= min_length and groups >= min_groups:
        print("PASS_DEMO")
    else:
        print("REVIEW")
    print(length, groups)
print("Score:", score)
```

פלט:

```text
SHORT
REVIEW
8 3
Score: 25
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 8 3 25 PASS_DEMO
2 10 1 23 REVIEW
3 INVALID
4 8 4 28 PASS_DEMO
5 4 4 20 REVIEW
2 2 1
Best score: 4 28
```

### ב. פלט התרחיש השני

```text
1 8 2 22 REVIEW
2 10 1 23 REVIEW
3 INVALID
4 8 4 28 PASS_DEMO
5 4 4 20 REVIEW
1 3 1
Best score: 4 28
```

### ג. תשובות והערות לדיון

כל דוגמה עצמאית.

השוויון נשאר עם הראשונה.

ניקוד גבוה אינו בהכרח עומד בספים.

אם best=-1, אין דוגמה חוקית.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
8
3
4
1
3
0
10
0
0
0
-1
2
3
1
3
2
2
1
1
1
1
1
```

```python
count = int(input())
min_length = int(input())
min_groups = int(input())
short = 0
few = 0
passed = 0
review = 0
invalid = 0
best = -1
best_index = 0
for i in range(count):
    lower = int(input())
    upper = int(input())
    digits = int(input())
    symbols = int(input())
    if lower < 0 or upper < 0 or digits < 0 or symbols < 0:
        invalid += 1
        print(i + 1, "INVALID")
    else:
        length = lower + upper + digits + symbols
        groups = 0
        if lower > 0:
            groups += 1
        if upper > 0:
            groups += 1
        if digits > 0:
            groups += 1
        if symbols > 0:
            groups += 1
        score = length * 2 + groups * 3
        if length < min_length:
            short += 1
        if groups < min_groups:
            few += 1
        if length >= min_length and groups >= min_groups:
            passed += 1
            status = "PASS_DEMO"
        else:
            review += 1
            status = "REVIEW"
        if status == "PASS_DEMO" and score > best:
            best = score
            best_index = i + 1
        print(i + 1, length, groups, score, status)
print(passed, review, invalid)
print(short, few)
print("Best score:", best_index, best)
```

פלט:

```text
1 8 3 25 PASS_DEMO
2 10 1 23 REVIEW
3 INVALID
4 8 4 28 PASS_DEMO
5 4 4 20 REVIEW
2 2 1
1 1
Best score: 4 28
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[[8, 4], [8, 1], [4, 3], [8, 2], [8, 4], [0, 0]]
[28, 19, 17, 22, 28, 0]
['PASS_DEMO', 'REVIEW', 'REVIEW', 'REVIEW', 'PASS_DEMO', 'REVIEW']
```

### ב. פלט התרחיש השני

```text
[[8, 4], [8, 1], [4, 3], [8, 3], [8, 4], [0, 0]]
[28, 19, 17, 25, 28, 0]
['PASS_DEMO', 'REVIEW', 'REVIEW', 'PASS_DEMO', 'PASS_DEMO', 'REVIEW']
```

### ג. תשובות והערות לדיון

ענפי elif מונעים ספירה כפולה.

שומרים רק מאפיינים.

Xy9!Xy9!

חוזרת על תבנית.

ריקה נותנת אפס ומדווחת REVIEW.

הכלל לא מתאים אוטומטית לכל Unicode.

### ד. פתרון אפשרי

```python
samples = ["aaBB11!!", "abcdefgh", "Ab12", "QQQQQQ99", "Xy9!Xy9!", ""]
scores = []
statuses = []
features = []
gaps = []
passed_indexes = []
index = 0
for sample in samples:
    lower = 0
    upper = 0
    digits = 0
    symbols = 0
    for ch in sample:
        if ch >= "a" and ch <= "z":
            lower += 1
        elif ch >= "A" and ch <= "Z":
            upper += 1
        elif ch >= "0" and ch <= "9":
            digits += 1
        else:
            symbols += 1
    groups = 0
    counts = [lower, upper, digits, symbols]
    for amount in counts:
        if amount > 0:
            groups += 1
    length = len(sample)
    score = length * 2 + groups * 3
    if length >= 8 and groups >= 3:
        status = "PASS_DEMO"
    else:
        status = "REVIEW"
    features.append([length, groups])
    scores.append(score)
    statuses.append(status)
    length_gap = 8 - length
    groups_gap = 3 - groups
    if length_gap < 0:
        length_gap = 0
    if groups_gap < 0:
        groups_gap = 0
    gaps.append([length_gap, groups_gap])
    if status == "PASS_DEMO":
        passed_indexes.append(index)
    index += 1
print(features)
print(scores)
print(statuses)
print(gaps)
print(passed_indexes)
```

פלט:

```text
[[8, 4], [8, 1], [4, 3], [8, 2], [8, 4], [0, 0]]
[28, 19, 17, 22, 28, 0]
['PASS_DEMO', 'REVIEW', 'REVIEW', 'REVIEW', 'PASS_DEMO', 'REVIEW']
[[0, 0], [0, 2], [4, 0], [0, 1], [0, 0], [8, 3]]
[0, 4]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[[[8, 3], [25, 'PASS_DEMO']], [[8, 1], [19, 'REVIEW']], [[8, 2], [22, 'REVIEW']], [[8, 4], [28, 'PASS_DEMO']]]
[[[8, 3], [25, 'REVIEW']], [[8, 1], [19, 'REVIEW']], [[8, 2], [22, 'REVIEW']], [[8, 4], [28, 'REVIEW']]]
[25, 'PASS_DEMO']
```

### ב. פלט התרחיש השני

```text
[[[8, 3], [25, 'REVIEW']], [[8, 1], [19, 'REVIEW']], [[8, 2], [22, 'REVIEW']], [[8, 4], [28, 'REVIEW']]]
[[[8, 3], [25, 'REVIEW']], [[8, 1], [19, 'REVIEW']], [[8, 2], [22, 'REVIEW']], [[8, 4], [28, 'REVIEW']]]
[25, 'REVIEW']
```

### ג. תשובות והערות לדיון

מאפיינים מספיקים למדד.

אורך 8 חוקי;

> שגוי.

כל דוח עצמאי.

משווים מאפיינים והחלטות.

### ד. פתרון אפשרי

```python
def features(sample):
    counts = [0, 0, 0, 0]
    for ch in sample:
        if ch >= "a" and ch <= "z":
            counts[0] += 1
        elif ch >= "A" and ch <= "Z":
            counts[1] += 1
        elif ch >= "0" and ch <= "9":
            counts[2] += 1
        else:
            counts[3] += 1
    groups = 0
    for value in counts:
        if value > 0:
            groups += 1
    return [len(sample), groups]

def evaluate(data, min_length, min_groups):
    length = data[0]
    groups = data[1]
    score = length * 2 + groups * 3
    missing_length = min_length - length
    missing_groups = min_groups - groups
    if missing_length < 0:
        missing_length = 0
    if missing_groups < 0:
        missing_groups = 0
    status = "REVIEW"
    if missing_length == 0 and missing_groups == 0:
        status = "PASS_DEMO"
    return [score, status, missing_length, missing_groups]

def compare(samples, min_length, min_groups):
    result = []
    passed = 0
    for sample in samples:
        data = features(sample)
        verdict = evaluate(data, min_length, min_groups)
        result.append([data, verdict])
        if verdict[1] == "PASS_DEMO":
            passed += 1
    return [result, passed]

samples = ["Abcdef12", "abcdefgh", "AAAA1111", "xyXY00!!"]
print(compare(samples, 8, 3))
print(compare(samples, 12, 2))
print(evaluate([8, 3], 8, 3))
```

פלט:

```text
[[[[8, 3], [25, 'PASS_DEMO', 0, 0]], [[8, 1], [19, 'REVIEW', 0, 2]], [[8, 2], [22, 'REVIEW', 0, 1]], [[8, 4], [28, 'PASS_DEMO', 0, 0]]], 2]
[[[[8, 3], [25, 'REVIEW', 4, 0]], [[8, 1], [19, 'REVIEW', 4, 1]], [[8, 2], [22, 'REVIEW', 4, 0]], [[8, 4], [28, 'REVIEW', 4, 0]]], 0]
[25, 'PASS_DEMO', 0, 0]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[8, 3, 25, 'PASS_DEMO'] [0, 0]
[8, 3, 25, 'REVIEW'] [4, 0]
[8, 1, 19, 'REVIEW'] [0, 2]
[8, 1, 19, 'REVIEW'] [4, 1]
[12, 2, 30, 'REVIEW'] [0, 1]
[12, 2, 30, 'PASS_DEMO'] [0, 0]
[8, 4, 28, 'PASS_DEMO'] [0, 0]
[8, 4, 28, 'REVIEW'] [4, 0]
[4, 2, 2] [4, 1, 3]
[[8, 3, 25, 'PASS_DEMO'], [8, 1, 19, 'REVIEW'], [12, 2, 30, 'REVIEW'], [8, 4, 28, 'PASS_DEMO']]
[[8, 3, 25, 'REVIEW'], [8, 1, 19, 'REVIEW'], [12, 2, 30, 'PASS_DEMO'], [8, 4, 28, 'REVIEW']]
```

### ב. פלט התרחיש השני

```text
[8, 3, 25, 'PASS_DEMO'] [0, 0]
[8, 3, 25, 'PASS_DEMO'] [0, 0]
[8, 1, 19, 'REVIEW'] [0, 2]
[8, 1, 19, 'REVIEW'] [0, 1]
[12, 2, 30, 'REVIEW'] [0, 1]
[12, 2, 30, 'PASS_DEMO'] [0, 0]
[8, 4, 28, 'PASS_DEMO'] [0, 0]
[8, 4, 28, 'PASS_DEMO'] [0, 0]
[4, 2, 2] [4, 3, 1]
[[8, 3, 25, 'PASS_DEMO'], [8, 1, 19, 'REVIEW'], [12, 2, 30, 'REVIEW'], [8, 4, 28, 'PASS_DEMO']]
[[8, 3, 25, 'PASS_DEMO'], [8, 1, 19, 'REVIEW'], [12, 2, 30, 'PASS_DEMO'], [8, 4, 28, 'PASS_DEMO']]
```

### ג. תשובות והערות לדיון

אין צורך במחרוזת בדוח.

Policy קובעת ספים, Inspector מפיק דוחות.

מדיניות משותפת משפיעה על שניהם.

דוחות ישנים מתארים את זמן ההערכה.

בדקו ששדות הדוח כוללים מאפיינים בלבד.

### ד. פתרון אפשרי

```python
class Policy:
    def __init__(self, min_length, min_groups):
        self.min_length = min_length
        self.min_groups = min_groups

    def assess(self, length, groups):
        score = length * 2 + groups * 3
        if length >= self.min_length and groups >= self.min_groups:
            return [score, "PASS_DEMO"]
        return [score, "REVIEW"]

class Inspector:
    def __init__(self, policy):
        self.policy = policy
        self.reports = []
        self.passed = 0
        self.reasons = []

    def inspect(self, sample):
        counts = [0, 0, 0, 0]
        for ch in sample:
            if ch >= "a" and ch <= "z":
                counts[0] += 1
            elif ch >= "A" and ch <= "Z":
                counts[1] += 1
            elif ch >= "0" and ch <= "9":
                counts[2] += 1
            else:
                counts[3] += 1
        groups = 0
        for value in counts:
            if value > 0:
                groups += 1
        length = len(sample)
        result = self.policy.assess(length, groups)
        report = [length, groups, result[0], result[1]]
        self.reports.append(report)
        reasons = []
        if length < self.policy.min_length:
            reasons.append("SHORT")
        if groups < self.policy.min_groups:
            reasons.append("FEW_GROUPS")
        self.reasons.append(reasons)
        if result[1] == "PASS_DEMO":
            self.passed += 1
        return report

    def report_policy(self):
        return [self.policy.min_length, self.policy.min_groups]

    def summary(self):
        return [len(self.reports), self.passed, len(self.reports) - self.passed]

    def gap(self, report):
        length_gap = self.policy.min_length - report[0]
        groups_gap = self.policy.min_groups - report[1]
        if length_gap < 0:
            length_gap = 0
        if groups_gap < 0:
            groups_gap = 0
        return [length_gap, groups_gap]

a = Inspector(Policy(8, 3))
b = Inspector(Policy(12, 2))
samples = ["Abcdef12", "abcdefgh", "ABCDEFGHIJ12", "xyXY00!!"]
for sample in samples:
    first = a.inspect(sample)
    second = b.inspect(sample)
    print(first, a.gap(first))
    print(second, b.gap(second))
print(a.summary(), b.summary())
print(a.reports)
print(b.reports)
print(a.reasons, a.report_policy())
print(b.reasons, b.report_policy())
```

פלט:

```text
[8, 3, 25, 'PASS_DEMO'] [0, 0]
[8, 3, 25, 'REVIEW'] [4, 0]
[8, 1, 19, 'REVIEW'] [0, 2]
[8, 1, 19, 'REVIEW'] [4, 1]
[12, 2, 30, 'REVIEW'] [0, 1]
[12, 2, 30, 'PASS_DEMO'] [0, 0]
[8, 4, 28, 'PASS_DEMO'] [0, 0]
[8, 4, 28, 'REVIEW'] [4, 0]
[4, 2, 2] [4, 1, 3]
[[8, 3, 25, 'PASS_DEMO'], [8, 1, 19, 'REVIEW'], [12, 2, 30, 'REVIEW'], [8, 4, 28, 'PASS_DEMO']]
[[8, 3, 25, 'REVIEW'], [8, 1, 19, 'REVIEW'], [12, 2, 30, 'PASS_DEMO'], [8, 4, 28, 'REVIEW']]
[[], ['FEW_GROUPS'], ['FEW_GROUPS'], []] [8, 3]
[['SHORT'], ['SHORT', 'FEW_GROUPS'], [], ['SHORT']] [12, 2]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

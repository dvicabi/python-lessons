# פתרונות למורה: מערכת ניטור מנועים: איך מזהים חריגות ובוחרים מה לבדוק קודם?

[חזרה למשימת התלמיד](../24_engine_monitor.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
ENGINE E1 | SIM
Reference A: 40 | Value: 45
Reference B: 30 | Value: 34
Score: 13 | WATCH
```

### ב. פלט התרחיש השני

```text
ENGINE  | E1 | SIM
Reference A: 40 | Value: 45
Reference B: 30 | Value: 34
Score: 13 | WATCH
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("ENGINE ", end="")
print("E2", end="")
print(" | SIM")
print("Reference A: ", end="")
print("50", end="")
print(" | Value: 65")
print("Reference B: ", end="")
print("40", end="")
print(" | Value: 45")
print("Score: ", end="")
print("25", end="")
print(" | CHECK")
```

פלט:

```text
ENGINE E2 | SIM
Reference A: 50 | Value: 65
Reference B: 40 | Value: 45
Score: 25 | CHECK
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
43 32 3 2 7
49 36 9 6 21
54 34 14 4 22
Average: 16
```

### ב. פלט התרחיש השני

```text
43 32 3 2 7
49 36 9 6 21
54 39 14 9 32
Average: 20
```

### ג. תשובות והערות לדיון

זהו כלל משקל מלאכותי במודל.

חישוב מוקדם משתמש בסטייה ישנה.

נקודת ייחוס קבועה מאפשרת השוואה.

ממוצע מתאר את כל המדידות, לא רק אחרונה.

### ד. פתרון אפשרי

```python
ref_a = 50
ref_b = 40
a = 53
b = 45
da = a - ref_a
db = b - ref_b
score1 = da + db * 2
print(da, db, score1)
a = 60
b = 43
da = a - ref_a
db = b - ref_b
score2 = da + db * 2
print(da, db, score2)
a = 65
b = 50
da = a - ref_a
db = b - ref_b
score3 = da + db * 2
print(da, db, score3)
total = score1 + score2 + score3
print(score2 - score1, score3 - score2)
print(total, total // 3)
```

פלט:

```text
3 5 13
10 3 16
15 10 35
3 19
64 21
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
7 21 22
Changes: 14 1
Average: 16
```

### ב. פלט התרחיש השני

```text
3 17 18
Changes: 14 1
Average: 12
```

### ג. תשובות והערות לדיון

בשלב זה הפרשים חתומים עלולים להקטין ניקוד אף שסטייה קיימת.

בהמשך מחשבים גודל סטייה.

ייחוס משפיע על כל זוג.

נתון לא חוקי אינו בסיס לדירוג.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
40
30
49
36
54
34
3
```

```python
ref_a = int(input())
ref_b = int(input())
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
weight = int(input())
da1 = a1 - ref_a
db1 = b1 - ref_b
da2 = a2 - ref_a
db2 = b2 - ref_b
score1 = da1 + weight * db1
score2 = da2 + weight * db2
total = score1 + score2
print(score1, score2)
print(total // 2, score2 - score1)
```

פלט:

```text
27 26
26 -1
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
CHECK 24
Margin to check: 0
```

### ב. פלט התרחיש השני

```text
WATCH 22
Margin to check: 2
```

### ג. תשובות והערות לדיון

גודל סטייה אינו תלוי בכיוון.

חוקיות קודמת לחישוב כדי למנוע דירוג נתונים שגויים.

24 מסווג CHECK.

-1 הוא סימון שאין ניקוד חוקי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
40
30
32
38
```

```python
ref_a = int(input())
ref_b = int(input())
a = int(input())
b = int(input())
if a < 0 or a > 100 or b < 0 or b > 100:
    print("INVALID", -1)
else:
    da = a - ref_a
    db = b - ref_b
    if da < 0:
        da = -da
    if db < 0:
        db = -db
    score = da + db * 2
    if score >= 24:
        status = "CHECK"
    elif score >= 12:
        status = "WATCH"
    else:
        status = "NORMAL"
    print(status, score)
    print(da, db)
```

פלט:

```text
CHECK 24
8 8
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 NORMAL 0 0
2 CHECK 24 24
3 CHECK 30 30
4 INVALID -1 30
5 CHECK 24 30
6 NORMAL 7 30
7 CHECK 28 30
6 1 4 3
```

### ב. פלט התרחיש השני

```text
1 NORMAL 0 0
2 WATCH 22 22
3 CHECK 30 30
4 INVALID -1 30
5 CHECK 24 30
6 NORMAL 7 30
7 CHECK 28 30
6 1 3 3
```

### ג. תשובות והערות לדיון

checks סופר כל מדידה במצב CHECK;

transitions סופר כניסה חדשה למצב זה.

INVALID קוטע רצף לפי הקוד.

ניקוד לא חוקי אינו נתון אמיתי.

ענפי הסיווג מכסים כל קלט.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
40
30
40
30
32
38
-1
30
45
34
50
39
```

```python
count = int(input())
ref_a = int(input())
ref_b = int(input())
normal = 0
watch = 0
checks = 0
invalid = 0
total = 0
peak = -1
peak_index = 0
for i in range(count):
    a = int(input())
    b = int(input())
    if a < 0 or a > 100 or b < 0 or b > 100:
        invalid += 1
    else:
        da = a - ref_a
        db = b - ref_b
        if da < 0:
            da = -da
        if db < 0:
            db = -db
        score = da + db * 2
        total += score
        if score >= 24:
            checks += 1
        elif score >= 12:
            watch += 1
        else:
            normal += 1
        if score > peak:
            peak = score
            peak_index = i + 1
valid = normal + watch + checks
print(normal, watch, checks, invalid)
if valid > 0:
    print(total // valid)
else:
    print("NO DATA")
print(peak_index, peak)
```

פלט:

```text
1 1 2 1
16
5 28
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
Rank 1 1 25
Rank 2 5 25
[24, 25, 15, -1, 5, 25]
[1, 5]
```

### ב. פלט התרחיש השני

```text
Rank 1 0 26
Rank 2 1 25
[26, 25, 15, -1, 5, 25]
[0, 1]
```

### ג. תשובות והערות לדיון

הניקוד תלוי בסטייה מנקודת ייחוס.

מניעת בחירה כפולה.

אינדקס -1 חוקי בפייתון אך לא מייצג מועמד;

התנאי הקצר מונע קריאה מיותרת.

השוואת > בלבד משאירה את הראשון בשוויון.

### ד. פתרון אפשרי

```python
ref_a = [40, 50, 30, 70, 20, 45]
ref_b = [30, 40, 20, 50, 10, 30]
values_a = [48, 65, 35, 110, 25, 60]
values_b = [38, 45, 25, 52, 10, 35]
scores = []
checks = []
for i in range(len(ref_a)):
    a = values_a[i]
    b = values_b[i]
    score = -1
    if a >= 0 and a <= 100 and b >= 0 and b <= 100:
        da = a - ref_a[i]
        db = b - ref_b[i]
        if da < 0:
            da = -da
        if db < 0:
            db = -db
        score = da + db * 2
    scores.append(score)
    if score >= 24:
        checks.append(i)
ranking = []
for turn in range(len(checks)):
    best = -1
    for i in checks:
        if i not in ranking:
            if best == -1 or scores[i] > scores[best]:
                best = i
    if best != -1:
        ranking.append(best)
print(scores)
print(checks)
print(ranking)
```

פלט:

```text
[24, 25, 15, -1, 5, 25]
[0, 1, 5]
[1, 5, 0]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
['CHECK', 24]
['WATCH', 22]
['INVALID', -1]
[1, 3, 0]
[]
```

### ב. פלט התרחיש השני

```text
['WATCH', 24]
['WATCH', 22]
['INVALID', -1]
[3, 1, 0]
[]
```

### ג. תשובות והערות לדיון

evaluate מסווגת זוג יחיד ואינה מכירה רשימה.

24 יסווג WATCH בטעות.

בשוויון >= מעדכן למועמד מאוחר.

מוחזרות כל החוקיות בלבד, ללא כפילויות.

### ד. פתרון אפשרי

```python
def evaluate(ref_a, ref_b, a, b):
    if a < 0 or a > 100 or b < 0 or b > 100:
        return ["INVALID", -1]
    da = a - ref_a
    db = b - ref_b
    if da < 0:
        da = -da
    if db < 0:
        db = -db
    score = da + db * 2
    if score >= 24:
        return ["CHECK", score]
    if score >= 12:
        return ["WATCH", score]
    return ["NORMAL", score]

def top(scores, count):
    selected = []
    for turn in range(count):
        best = -1
        for i in range(len(scores)):
            if scores[i] >= 0 and i not in selected:
                if best == -1 or scores[i] > scores[best]:
                    best = i
        if best != -1:
            selected.append(best)
    return selected

def rank(refs_a, refs_b, values_a, values_b, count):
    if len(refs_a) != len(refs_b) or len(refs_a) != len(values_a) or len(refs_a) != len(values_b) or count < 0:
        return ["ERROR", [], []]
    scores = []
    for i in range(len(refs_a)):
        result = evaluate(refs_a[i], refs_b[i], values_a[i], values_b[i])
        scores.append(result[1])
    return ["OK", scores, top(scores, count)]

print(rank([40, 40, 40], [30, 30, 30], [32, 48, 101], [38, 38, 30], 3))
print(rank([40], [], [32], [38], 1))
```

פלט:

```text
['OK', [24, 24, -1], [0, 1]]
['ERROR', [], []]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
CHECK CHECK
NORMAL NORMAL
INVALID NORMAL
[24, 0, -1] [25, 3, 0]
24 25
1
```

### ב. פלט התרחיש השני

```text
CHECK CHECK
NORMAL NORMAL
INVALID NORMAL
[24, 0, -1] [24, 3, 0]
24 24
0
```

### ג. תשובות והערות לדיון

peak שומר את המרב בכל ההיסטוריה;

ניקוד מנרמל ביחס לייחוס המדומה.

הפעולה קוראת בלבד.

בשוויון נבחר האינדקס הראשון.

### ד. פתרון אפשרי

```python
class Engine:
    def __init__(self, name, ref_a, ref_b):
        self.name = name
        self.ref_a = ref_a
        self.ref_b = ref_b
        self.scores = []
        self.statuses = []

    def measure(self, a, b):
        score = -1
        status = "INVALID"
        if a >= 0 and a <= 100 and b >= 0 and b <= 100:
            da = a - self.ref_a
            db = b - self.ref_b
            if da < 0:
                da = -da
            if db < 0:
                db = -db
            score = da + db * 2
            if score >= 24:
                status = "CHECK"
            elif score >= 12:
                status = "WATCH"
            else:
                status = "NORMAL"
        self.scores.append(score)
        self.statuses.append(status)
        return status

    def peak(self):
        highest = -1
        for score in self.scores:
            if score > highest:
                highest = score
        return highest

    def last_valid(self):
        last = -1
        for score in self.scores:
            if score >= 0:
                last = score
        return last

class Fleet:
    def __init__(self, engines):
        self.engines = engines

    def first_for_review(self):
        best = -1
        highest = -1
        for i in range(len(self.engines)):
            peak = self.engines[i].peak()
            if peak >= 24 and peak > highest:
                best = i
                highest = peak
        return best

    def first_by_last(self):
        best = -1
        highest = -1
        for i in range(len(self.engines)):
            score = self.engines[i].last_valid()
            if score >= 24 and score > highest:
                best = i
                highest = score
        return best

a = Engine("A", 40, 30)
b = Engine("B", 50, 40)
print(a.measure(32, 38), b.measure(65, 45))
print(a.measure(40, 30), b.measure(51, 41))
print(a.measure(101, 30), b.measure(50, 40))
fleet = Fleet([a, b])
print(a.scores, b.scores)
print(a.peak(), b.peak())
print(fleet.first_for_review())
print(a.last_valid(), b.last_valid())
print(fleet.first_by_last())
```

פלט:

```text
CHECK CHECK
NORMAL NORMAL
INVALID NORMAL
[24, 0, -1] [25, 3, 0]
24 25
1
0 0
-1
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

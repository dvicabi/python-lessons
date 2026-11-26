# פתרונות למורה: מערכת גיבוי: האם הקובץ המעודכן באמת נמצא גם בגיבוי?

[חזרה למשימת התלמיד](../31_backup_system.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
BACKUP 01 | SIM
Source: 5 version
Copy: 3 version
Budget: 12 units
State: STALE | WAIT
```

### ב. פלט התרחיש השני

```text
BACKUP  | 01 | SIM
Source: 5 version
Copy: 3 version
Budget: 12 units
State: STALE | WAIT
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("BACKUP ", end="")
print("02", end="")
print(" | SIM")
print("Source: ", end="")
print("7", end="")
print(" version")
print("Copy: ", end="")
print("7", end="")
print(" version")
print("Budget: ", end="")
print("4", end="")
print(" units")
print("State: ", end="")
print("CURRENT", end="")
print(" | OK")
```

פלט:

```text
BACKUP 02 | SIM
Source: 7 version
Copy: 7 version
Budget: 4 units
State: CURRENT | OK
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
2 1 40 1
3 1 40 2
3 3 34 0
5 3 34 2
5 5 24 0
Updates: 2
Transferred: 16
Check: 40
```

### ב. פלט התרחיש השני

```text
2 1 40 1
3 1 40 2
3 3 34 0
5 3 34 2
5 5 20 0
Updates: 2
Transferred: 20
Check: 40
```

### ג. תשובות והערות לדיון

המקור יכול להשתנות בנפרד.

גיבוי מעתיק את הגרסה העדכנית גם אם קפצנו גרסאות.

budget+transferred=40.

updates מונה פריטים ולא נפח.

### ד. פתרון אפשרי

```python
source = 3
copy = 0
budget = 50
size = 7
transferred = 0
copy = source
budget -= size
transferred += size
print(source, copy, source - copy, budget)
source += 3
size += 2
print(source, copy, source - copy, budget)
copy = source
budget -= size
transferred += size
print(source, copy, source - copy, budget)
source += 1
print(source, copy, source - copy, budget)
print(budget + transferred)
```

פלט:

```text
3 3 0 43
6 3 3 43
6 6 0 34
7 6 1 34
50
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 2 6
B: 0 4
C: 3 8
All sizes: 18
Remaining: -3
Version gaps: 5
```

### ב. פלט התרחיש השני

```text
A: 2 6
B: -2 4
C: 3 8
All sizes: 18
Remaining: -8
Version gaps: 3
```

### ג. תשובות והערות לדיון

0 הוא עדכני.

שלילי מציין גיבוי מתקדם מהמקור.

רק מי שאינו עדכני וניתן להעברה צורך תקציב.

פערים חיוביים ושליליים יכולים להתקזז.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
1
6
3
0
8
12
```

```python
source_a = int(input())
copy_a = int(input())
size_a = int(input())
source_b = int(input())
copy_b = int(input())
size_b = int(input())
budget = int(input())
print(source_a - copy_a, source_b - copy_b)
budget -= size_a
print("After A:", budget)
budget -= size_b
print("After B:", budget)
print("Planned transfer:", size_a + size_b)
```

פלט:

```text
4 3
After A: 6
After B: -2
Planned transfer: 14
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
COPIED
5 5 0
0 8
Check: True
UP TO DATE
```

### ב. פלט התרחיש השני

```text
WAIT
5 2 3
7 0
Check: True
NOT CURRENT
```

### ג. תשובות והערות לדיון

בדיקת סכסוך קודמת לביצוע.

שוויון לתקציב חוקי.

גיבוי קיים לא נמחק.

חוקיות קודמת לעדכניות.

מספר גרסאות אינו גודל קובץ.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
2
9
4
```

```python
source = int(input())
copy = int(input())
size = int(input())
budget = int(input())
missing = 0
initial = budget
transferred = 0
if source <= 0 or copy < 0 or size <= 0 or budget < 0:
    status = "INVALID"
elif copy > source:
    status = "CONFLICT"
elif copy == source:
    status = "CURRENT"
elif size > budget:
    status = "WAIT"
    missing = size - budget
else:
    budget -= size
    transferred = size
    copy = source
    status = "COPIED"
print(status, missing)
print(source, copy, source - copy)
print(budget, transferred)
print("Check:", initial == budget + transferred)
if source == copy:
    print("UP TO DATE")
else:
    print("NOT CURRENT")
```

פלט:

```text
WAIT 5
5 2 3
4 0
Check: True
NOT CURRENT
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 COPIED 5 5 12
2 CURRENT 3 3 12
3 CONFLICT 4 5 12
4 WAIT 4 0 12
5 COPIED 2 2 8
6 COPIED 3 3 1
7 INVALID 0 0 1
3 1 1 1 1
Check: 7
19 1 True
```

### ב. פלט התרחיש השני

```text
1 COPIED 5 5 13
2 CURRENT 3 3 13
3 CONFLICT 4 5 13
4 WAIT 4 0 13
5 COPIED 2 2 9
6 COPIED 3 3 2
7 INVALID 0 0 2
3 1 1 1 1
Check: 7
18 2 True
```

### ג. תשובות והערות לדיון

אין שינוי לגרסה עדכנית.

פריט קטן יותר עשוי להתאים אחרי פריט גדול.

סכום חמישה מונים שווה למספר פריטים.

copied לא מתאר סיבות דחייה או גדלים.

CURRENT עדיין מסווג תקין.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
20
7
5
2
8
3
3
4
4
5
2
4
0
14
2
1
4
3
0
7
0
0
2
```

```python
budget = int(input())
count = int(input())
wait_size = 0
first_wait = 0
initial = budget
copied = 0
current = 0
waiting = 0
conflicts = 0
invalid = 0
transferred = 0
for i in range(count):
    source = int(input())
    copy = int(input())
    size = int(input())
    if source <= 0 or copy < 0 or size <= 0:
        status = "INVALID"
        invalid += 1
    elif copy > source:
        status = "CONFLICT"
        conflicts += 1
    elif copy == source:
        status = "CURRENT"
        current += 1
    elif size > budget:
        status = "WAIT"
        waiting += 1
        wait_size += size
        if first_wait == 0:
            first_wait = i + 1
    else:
        copy = source
        budget -= size
        transferred += size
        copied += 1
        status = "COPIED"
    print(i + 1, status, source, copy, budget)
print(copied, current, waiting, conflicts, invalid)
print("Check:", copied + current + waiting + conflicts + invalid)
print(transferred, budget, initial == transferred + budget)
print(wait_size, first_wait)
```

פלט:

```text
1 COPIED 5 5 12
2 CURRENT 3 3 12
3 CONFLICT 4 5 12
4 WAIT 4 0 12
5 COPIED 2 2 8
6 COPIED 3 3 1
7 INVALID 0 0 1
3 1 1 1 1
Check: 7
19 1 True
14 4
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
['COPIED', 'CURRENT', 'CONFLICT', 'WAIT', 'COPIED', 'WAIT']
[101, 105] 0
[5, 3, 5, 0, 2, 0]
['CURRENT', 'CURRENT', 'CONFLICT', 'COPIED', 'CURRENT', 'WAIT']
[104] 2
[5, 3, 5, 4, 2, 0]
[[['COPIED', 'CURRENT', 'CONFLICT', 'WAIT', 'COPIED', 'WAIT'], [101, 105], 0], [['CURRENT', 'CURRENT', 'CONFLICT', 'COPIED', 'CURRENT', 'WAIT'], [104], 2]]
Pending: [106]
```

### ב. פלט התרחיש השני

```text
['COPIED', 'CURRENT', 'CONFLICT', 'WAIT', 'COPIED', 'WAIT']
[101, 105] 0
[5, 3, 5, 0, 2, 0]
['CURRENT', 'CURRENT', 'CONFLICT', 'COPIED', 'CURRENT', 'COPIED']
[104, 106] 0
[5, 3, 5, 4, 2, 3]
[[['COPIED', 'CURRENT', 'CONFLICT', 'WAIT', 'COPIED', 'WAIT'], [101, 105], 0], [['CURRENT', 'CURRENT', 'CONFLICT', 'COPIED', 'CURRENT', 'COPIED'], [104, 106], 0]]
Pending: []
```

### ג. תשובות והערות לדיון

גרסת הגיבוי כבר עדכנית.

CONFLICT הוא עודף גרסה, Pending הוא גיבוי ישן יותר.

כל סבב צריך דוח עצמאי.

בודקים מזהי moved בסבבים שאין שינוי מקור.

המתנה אינה מחיקה.

### ד. פתרון אפשרי

```python
ids = [101, 102, 103, 104, 105, 106]
sources = [5, 3, 4, 4, 2, 3]
copies = [2, 3, 5, 0, 1, 0]
sizes = [8, 4, 2, 14, 4, 7]
budgets = [12, 16]
history = []
for budget in budgets:
    statuses = []
    moved = []
    for i in range(len(ids)):
        if sources[i] <= 0 or copies[i] < 0 or sizes[i] <= 0:
            status = "INVALID"
        elif copies[i] > sources[i]:
            status = "CONFLICT"
        elif copies[i] == sources[i]:
            status = "CURRENT"
        elif sizes[i] > budget:
            status = "WAIT"
        else:
            copies[i] = sources[i]
            budget -= sizes[i]
            moved.append(ids[i])
            status = "COPIED"
        statuses.append(status)
    history.append([statuses, moved, budget])
    print(statuses)
    print(moved, budget)
    print(copies)
pending = []
current_ids = []
conflict_ids = []
need = 0
for i in range(len(ids)):
    if copies[i] < sources[i]:
        pending.append(ids[i])
        need += sizes[i]
    elif copies[i] == sources[i]:
        current_ids.append(ids[i])
    else:
        conflict_ids.append(ids[i])
print(history)
print("Pending:", pending)
print(current_ids, conflict_ids)
print("Needed:", need)
```

פלט:

```text
['COPIED', 'CURRENT', 'CONFLICT', 'WAIT', 'COPIED', 'WAIT']
[101, 105] 0
[5, 3, 5, 0, 2, 0]
['CURRENT', 'CURRENT', 'CONFLICT', 'COPIED', 'CURRENT', 'WAIT']
[104] 2
[5, 3, 5, 4, 2, 0]
[[['COPIED', 'CURRENT', 'CONFLICT', 'WAIT', 'COPIED', 'WAIT'], [101, 105], 0], [['CURRENT', 'CURRENT', 'CONFLICT', 'COPIED', 'CURRENT', 'WAIT'], [104], 2]]
Pending: [106]
[101, 102, 104, 105] [103]
Needed: 7
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[[5, 3, 0, 4], ['COPIED', 'CURRENT', 'WAIT', 'CONFLICT'], 0, 8]
[[5, 3, 4, 4], ['CURRENT', 'CURRENT', 'COPIED', 'CONFLICT'], 0, 12]
[2, 3, 0, 4]
[]
```

### ב. פלט התרחיש השני

```text
[[2, 3, 0, 4], ['WAIT', 'CURRENT', 'WAIT', 'CONFLICT'], 8, 0]
[[5, 3, 0, 4], ['COPIED', 'CURRENT', 'WAIT', 'CONFLICT'], 4, 8]
[2, 3, 0, 4]
[]
```

### ג. תשובות והערות לדיון

שוויון size=budget חוקי.

רשימה חדשה מאפשרת לבחון תוכנית בלי לשנות מקור.

הסבב השני מקבל תוצאת גרסאות ראשונה.

אי-התאמה מחזירה [].

בכשל אין העברה ולכן אין להפחית תקציב.

### ד. פתרון אפשרי

```python
def sync(source, copy, size, budget):
    if source <= 0 or copy < 0 or size <= 0 or budget < 0:
        return [copy, budget, "INVALID"]
    if copy > source:
        return [copy, budget, "CONFLICT"]
    if copy == source:
        return [copy, budget, "CURRENT"]
    if size > budget:
        return [copy, budget, "WAIT"]
    return [source, budget - size, "COPIED"]

def batch(sources, copies, sizes, budget):
    if len(sources) != len(copies) or len(sources) != len(sizes) or budget < 0:
        return []
    statuses = []
    new_copies = []
    copied_indexes = []
    waiting_indexes = []
    initial = budget
    for i in range(len(sources)):
        result = sync(sources[i], copies[i], sizes[i], budget)
        new_copies.append(result[0])
        budget = result[1]
        statuses.append(result[2])
        if result[2] == "COPIED":
            copied_indexes.append(i)
        elif result[2] == "WAIT":
            waiting_indexes.append(i)
    return [new_copies, statuses, budget, initial - budget, copied_indexes, waiting_indexes]

sources = [5, 3, 4, 2]
copies = [2, 3, 0, 4]
sizes = [8, 4, 12, 1]
first = batch(sources, copies, sizes, 8)
second = batch(sources, first[0], sizes, 12)
print(first)
print(second)
print(copies)
print(batch(sources, [], sizes, 10))
print(batch([], [], [], 10))
```

פלט:

```text
[[5, 3, 0, 4], ['COPIED', 'CURRENT', 'WAIT', 'CONFLICT'], 0, 8, [0], [2]]
[[5, 3, 4, 4], ['CURRENT', 'CURRENT', 'COPIED', 'CONFLICT'], 0, 12, [2], []]
[2, 3, 0, 4]
[]
[[], [], 10, 0, [], []]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'WAIT'], ['D', 'CONFLICT']], 8, 0]
[[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'COPIED'], ['D', 'CONFLICT']], 12, 0]
True
[[['A', 'WAIT'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 0, 6]
[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 7, 0]
[['A', 6, 6, 'CURRENT'], ['B', 3, 3, 'CURRENT'], ['C', 4, 4, 'CURRENT'], ['D', 2, 4, 'CONFLICT']]
27
[[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'WAIT'], ['D', 'CONFLICT']], 8, 0], [[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'COPIED'], ['D', 'CONFLICT']], 12, 0], [[['A', 'WAIT'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 0, 6], [[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 7, 0]]
```

### ב. פלט התרחיש השני

```text
[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'WAIT'], ['D', 'CONFLICT']], 8, 0]
[[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'COPIED'], ['D', 'CONFLICT']], 12, 0]
True
[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 7, 0]
[[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 0, 7]
[['A', 6, 6, 'CURRENT'], ['B', 3, 3, 'CURRENT'], ['C', 4, 4, 'CURRENT'], ['D', 2, 4, 'CONFLICT']]
27
[[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'WAIT'], ['D', 'CONFLICT']], 8, 0], [[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'COPIED'], ['D', 'CONFLICT']], 12, 0], [[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 7, 0], [[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 0, 7]]
```

### ג. תשובות והערות לדיון

status אינה משנה מידע.

גרסה חדשה חייבת לעלות לפי המודל.

כל סבב מתועד בנפרד.

CURRENT אינו מפחית תקציב.

BackupJob מנהלת משאבים מצטברים.

סכסוך אינו נפתר אוטומטית.

### ד. פתרון אפשרי

```python
class FileRecord:
    def __init__(self, name, source, copy, size):
        self.name = name
        self.source = source
        self.copy = copy
        self.size = size

    def status(self):
        if self.source <= 0 or self.copy < 0 or self.size <= 0:
            return "INVALID"
        if self.copy > self.source:
            return "CONFLICT"
        if self.copy == self.source:
            return "CURRENT"
        return "STALE"

    def edit(self, version, size):
        if version <= self.source or size <= 0:
            return False
        self.source = version
        self.size = size
        return True

    def synchronize(self, budget):
        status = self.status()
        if status != "STALE":
            return [budget, status]
        if self.size > budget:
            return [budget, "WAIT"]
        self.copy = self.source
        return [budget - self.size, "COPIED"]

    def report(self):
        return [self.name, self.source, self.copy, self.status()]

class BackupJob:
    def __init__(self, files):
        self.files = files
        self.history = []
        self.transferred = 0

    def run(self, budget):
        if budget < 0:
            return []
        initial = budget
        events = []
        for file in self.files:
            result = file.synchronize(budget)
            budget = result[0]
            events.append([file.name, result[1]])
        amount = initial - budget
        self.transferred += amount
        report = [events, amount, budget]
        self.history.append(report)
        return report

    def pending_size(self):
        total = 0
        for file in self.files:
            if file.status() == "STALE":
                total += file.size
        return total

    def current_count(self):
        count = 0
        for file in self.files:
            if file.status() == "CURRENT":
                count += 1
        return count

    def reports(self):
        result = []
        for file in self.files:
            result.append(file.report())
        return result

a = FileRecord("A", 5, 2, 8)
b = FileRecord("B", 3, 3, 4)
c = FileRecord("C", 4, 0, 12)
d = FileRecord("D", 2, 4, 1)
job = BackupJob([a, b, c, d])
print(job.pending_size(), job.current_count())
print(job.run(8))
print(job.run(12))
print(job.pending_size(), job.current_count())
print(a.edit(6, 7))
print(job.run(6))
print(job.run(7))
print(job.reports())
print(job.transferred)
print(job.pending_size(), job.current_count())
print(job.history)
```

פלט:

```text
20 1
[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'WAIT'], ['D', 'CONFLICT']], 8, 0]
[[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'COPIED'], ['D', 'CONFLICT']], 12, 0]
0 3
True
[[['A', 'WAIT'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 0, 6]
[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 7, 0]
[['A', 6, 6, 'CURRENT'], ['B', 3, 3, 'CURRENT'], ['C', 4, 4, 'CURRENT'], ['D', 2, 4, 'CONFLICT']]
27
0 3
[[[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'WAIT'], ['D', 'CONFLICT']], 8, 0], [[['A', 'CURRENT'], ['B', 'CURRENT'], ['C', 'COPIED'], ['D', 'CONFLICT']], 12, 0], [[['A', 'WAIT'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 0, 6], [[['A', 'COPIED'], ['B', 'CURRENT'], ['C', 'CURRENT'], ['D', 'CONFLICT']], 7, 0]]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

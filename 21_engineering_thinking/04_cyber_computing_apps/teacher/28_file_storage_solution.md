# פתרונות למורה: מערכת אחסון קבצים: איך שומרים על מכסת מקום ומידע עקבי?

[חזרה למשימת התלמיד](../28_file_storage.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
STORAGE A | SIM
Capacity: 40 units
Used: 27 units
Free: 13 units
State: READY | OK
```

### ב. פלט התרחיש השני

```text
STORAGE  | A | SIM
Capacity: 40 units
Used: 27 units
Free: 13 units
State: READY | OK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("STORAGE ", end="")
print("B", end="")
print(" | SIM")
print("Capacity: ", end="")
print("30", end="")
print(" units")
print("Used: ", end="")
print("30", end="")
print(" units")
print("Free: ", end="")
print("0", end="")
print(" units")
print("State: ", end="")
print("FULL", end="")
print(" | WAIT")
```

פלט:

```text
STORAGE B | SIM
Capacity: 30 units
Used: 30 units
Free: 0 units
State: FULL | WAIT
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
18 22 3
23 17 4
19 21 3
26 14 4
Totals: 20 4
Check: 26
Capacity: 40
```

### ב. פלט התרחיש השני

```text
18 22 3
23 17 4
19 21 3
31 9 4
Totals: 25 4
Check: 31
Capacity: 40
```

### ג. תשובות והערות לדיון

added הוא נפח מצטבר שנוסף;

used מצב רגעי.

10+added-removed=used.

files מונה פריטים.

שינוי מונה שגוי מפר את משמעות המאזן.

הביטוי `used + capacity - used` שווה תמיד ל-capacity ולכן אינו בדיקת תקינות עצמאית. יש להשוות את used לסכום גדלים פעילים או לחשב אותו ממאזן הוספות ומחיקות שנשמר בנפרד.

### ד. פתרון אפשרי

```python
capacity = 50
used = 20
files = 3
added = 0
removed = 0
used += 9
added += 9
files += 1
print(used, capacity - used, files)
used -= 6
removed += 6
files -= 1
print(used, capacity - used, files)
used += 4
added += 4
files += 1
print(used, capacity - used, files)
used -= 8
removed += 8
files -= 1
print(used, capacity - used, files)
print(added, removed, 20 + added - removed)
```

פלט:

```text
29 21 4
23 27 3
27 23 4
19 31 3
13 14 19
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Add 1: 28 12
Delete: 24 16
Add 2: 31 9
Delta: 21
Check: 31
Total writes: 25
Free: 9
```

### ב. פלט התרחיש השני

```text
Add 1: 33 -8
Delete: 21 4
Add 2: 22 3
Delta: 7
Check: 22
Total writes: 19
Free: 3
```

### ג. תשובות והערות לדיון

מקום שלילי הוא חריגה.

חריגה זמנית יכולה להיעלם במחיקה.

גודל אינו מזהה.

נבדוק כל פעולה לפני עדכון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
50
20
9
6
4
8
```

```python
capacity = int(input())
used = int(input())
initial = used
a1 = int(input())
d1 = int(input())
a2 = int(input())
d2 = int(input())
used += a1
print(used, capacity - used)
used -= d1
print(used, capacity - used)
used += a2
print(used, capacity - used)
used -= d2
print(used, capacity - used)
print(initial + a1 + a2 - d1 - d2, used)
```

פלט:

```text
29 21
23 27
27 23
19 31
19 19
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
ADDED
30 0
1 0
FULL
```

### ב. פלט התרחיש השני

```text
NO SPACE
24 6
0 1
PARTIAL
```

### ג. תשובות והערות לדיון

גודל שווה למקום פנוי חוקי.

סוג שגוי אינו פעולה.

מחיקה גדולה מדי נדחית.

בקבצים נדרשת גם בדיקת מזהה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
30
24
2
8
```

```python
capacity = int(input())
used = int(input())
kind = int(input())
size = int(input())
initial = used
accepted = 0
rejected = 0
if size <= 0 or (kind != 1 and kind != 2):
    print("INVALID")
elif kind == 1:
    if size <= capacity - used:
        used += size
        accepted += 1
        print("ADDED")
    else:
        rejected += 1
        print("NO SPACE")
else:
    if size <= used:
        used -= size
        accepted += 1
        print("REMOVED")
    else:
        rejected += 1
        print("NOT ENOUGH")
print(used, capacity - used)
print(accepted, rejected)
print("Delta:", used - initial)
if used == capacity:
    print("FULL")
elif used == 0:
    print("EMPTY")
else:
    print("PARTIAL")
```

פלט:

```text
REMOVED
16 14
1 0
Delta: -8
PARTIAL
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 ADDED 22 8
2 NO SPACE 22 8
3 REMOVED 16 14
4 ADDED 30 0
5 NOT ENOUGH 30 0
6 INVALID 30 0
7 INVALID 30 0
8 REMOVED 26 4
4 2 2
26 10 30
Check: 26 26
```

### ב. פלט התרחיש השני

```text
1 ADDED 22 8
2 ADDED 30 0
3 REMOVED 24 6
4 ADDED 30 0
5 NOT ENOUGH 30 0
6 INVALID 30 0
7 INVALID 30 0
8 REMOVED 26 4
5 1 2
26 10 30
Check: 26 26
```

### ג. תשובות והערות לדיון

peak שיא היסטורי.

שינוי בדחייה יפר את מאזן הגדלים.

ok מונה פעולות מוצלחות, לא קבצים.

ok+rejected+invalid שווה למספר האירועים.

מצב נשאר ראשוני.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
30
10
8
1
12
1
9
2
6
1
14
2
50
0
5
1
-1
2
4
```

```python
capacity = int(input())
used = int(input())
count = int(input())
full_count = 0
initial = used
added = 0
removed = 0
ok = 0
rejected = 0
invalid = 0
peak = used
for i in range(count):
    kind = int(input())
    size = int(input())
    if size <= 0 or (kind != 1 and kind != 2):
        invalid += 1
        status = "INVALID"
    elif kind == 1:
        if size <= capacity - used:
            used += size
            added += size
            ok += 1
            status = "ADDED"
        else:
            rejected += 1
            status = "NO SPACE"
    elif size <= used:
        used -= size
        removed += size
        ok += 1
        status = "REMOVED"
    else:
        rejected += 1
        status = "NOT ENOUGH"
    if (status == "ADDED" or status == "REMOVED") and used == capacity:
        full_count += 1
    if used > peak:
        peak = used
    print(i + 1, status, used, capacity - used)
print(ok, rejected, invalid)
print(added, removed, peak, full_count)
print("Check:", initial + added - removed, used)
```

פלט:

```text
1 ADDED 22 8
2 NO SPACE 22 8
3 REMOVED 16 14
4 ADDED 30 0
5 NOT ENOUGH 30 0
6 INVALID 30 0
7 INVALID 30 0
8 REMOVED 26 4
4 2 2
26 10 30 1
Check: 26 26
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
30 ADDED 24 [True, True, True, False]
40 NO SPACE 24 [True, True, True, False]
20 REMOVED 16 [True, False, True, False]
40 ADDED 28 [True, False, True, True]
30 DUPLICATE 28 [True, False, True, True]
99 INVALID 28 [True, False, True, True]
10 REMOVED 22 [False, False, True, True]
['ADDED', 'NO SPACE', 'REMOVED', 'ADDED', 'DUPLICATE', 'INVALID', 'REMOVED']
Check: 22 22
```

### ב. פלט התרחיש השני

```text
30 ADDED 24 [True, True, True, False]
40 NO SPACE 24 [True, True, True, False]
20 REMOVED 16 [True, False, True, False]
40 NO SPACE 16 [True, False, True, False]
30 DUPLICATE 16 [True, False, True, False]
99 INVALID 16 [True, False, True, False]
10 REMOVED 10 [False, False, True, False]
['ADDED', 'NO SPACE', 'REMOVED', 'NO SPACE', 'DUPLICATE', 'INVALID', 'REMOVED']
Check: 10 10
```

### ג. תשובות והערות לדיון

found=-1 הוא סימון ולא אינדקס חוקי.

MISSING מוכר אך לא פעיל;

INVALID לא מוכר.

כפילות סופרת נפח פעמיים.

סריקה מסכמת רק פעילים.

מזהים כפולים יוצרים מיפוי לא חד משמעי.

### ד. פתרון אפשרי

```python
ids = [10, 20, 30, 40]
sizes = [6, 8, 10, 12]
active = [True, True, False, False]
events = [[1, 30], [1, 40], [2, 20], [1, 40], [1, 30], [2, 99], [2, 10]]
capacity = 30
used = 14
history = []
for event in events:
    kind = event[0]
    target = event[1]
    found = -1
    for i in range(len(ids)):
        if ids[i] == target:
            found = i
    if found == -1 or (kind != 1 and kind != 2):
        status = "INVALID"
    elif kind == 1:
        if active[found]:
            status = "DUPLICATE"
        elif sizes[found] > capacity - used:
            status = "NO SPACE"
        else:
            active[found] = True
            used += sizes[found]
            status = "ADDED"
    elif not active[found]:
        status = "MISSING"
    else:
        active[found] = False
        used -= sizes[found]
        status = "REMOVED"
    history.append(status)
    print(target, status, used, active)
check = 0
largest = 0
active_ids = []
for i in range(len(ids)):
    if active[i]:
        check += sizes[i]
        active_ids.append(ids[i])
        if sizes[i] > largest:
            largest = sizes[i]
print(history)
print(active_ids, largest)
print("Check:", used, check)
```

פלט:

```text
30 ADDED 24 [True, True, True, False]
40 NO SPACE 24 [True, True, True, False]
20 REMOVED 16 [True, False, True, False]
40 ADDED 28 [True, False, True, True]
30 DUPLICATE 28 [True, False, True, True]
99 INVALID 28 [True, False, True, True]
10 REMOVED 22 [False, False, True, True]
['ADDED', 'NO SPACE', 'REMOVED', 'ADDED', 'DUPLICATE', 'INVALID', 'REMOVED']
[30, 40] 12
Check: 22 22
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[14, 'ADDED'] [True, True, False]
[14, 'NO SPACE'] [True, True, False]
[8, 'REMOVED'] [False, True, False]
[18, 'ADDED'] [False, True, True]
18 18
```

### ב. פלט התרחיש השני

```text
[14, 'ADDED'] [True, True, False]
[24, 'ADDED'] [True, True, True]
[18, 'REMOVED'] [False, True, True]
[18, 'DUPLICATE'] [False, True, True]
18 18
```

### ג. תשובות והערות לדיון

used מספר ולכן מחזירים ערך.

active מצב הקיום, ids זהות קבועה.

total מחשבת מאזן מחדש.

דחייה משאירה מצב.

find ו-total ניתנות לבדיקה בנפרד.

### ד. פתרון אפשרי

```python
def find(ids, target):
    index = -1
    for i in range(len(ids)):
        if ids[i] == target:
            index = i
    return index

def change(ids, sizes, active, capacity, used, kind, target):
    index = find(ids, target)
    if index == -1 or (kind != 1 and kind != 2):
        return [used, "INVALID"]
    if kind == 1:
        if active[index]:
            return [used, "DUPLICATE"]
        if sizes[index] > capacity - used:
            return [used, "NO SPACE"]
        active[index] = True
        return [used + sizes[index], "ADDED"]
    if not active[index]:
        return [used, "MISSING"]
    active[index] = False
    return [used - sizes[index], "REMOVED"]

def total(sizes, active):
    used = 0
    for i in range(len(sizes)):
        if active[i]:
            used += sizes[i]
    return used

def audit(sizes, active, used, capacity):
    return total(sizes, active) == used and used >= 0 and used <= capacity

ids = [10, 20, 30]
sizes = [6, 8, 10]
active = [True, False, False]
used = total(sizes, active)
for event in [[1, 20], [1, 30], [2, 10], [1, 30]]:
    result = change(ids, sizes, active, 20, used, event[0], event[1])
    used = result[0]
    print(result, active, audit(sizes, active, used, 20))
print(used, total(sizes, active))
print(audit(sizes, active, used + 1, 20))
```

פלט:

```text
[14, 'ADDED'] [True, True, False] True
[14, 'NO SPACE'] [True, True, False] True
[8, 'REMOVED'] [False, True, False] True
[18, 'ADDED'] [False, True, True] True
18 18
False
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
True True True
DENIED
DENIED
True
MOVED
DENIED
[9, 21, [20]] [8, 4, [10]]
[[10, 'DENIED'], [20, 'DENIED'], [10, 'MOVED'], [20, 'DENIED']]
Combined: 17
```

### ב. פלט התרחיש השני

```text
True True True
MOVED
DENIED
True
DENIED
DENIED
[9, 21, [20]] [8, 8, [10]]
[[10, 'MOVED'], [20, 'DENIED'], [10, 'DENIED'], [20, 'DENIED']]
Combined: 17
```

### ג. תשובות והערות לדיון

can_add היא שאילתה.

העברה לאותה מכסה אינה הגיונית במודל.

דחייה שומרת את המקור.

נפח שנגרע ממקור שווה לנפח שנוסף ליעד.

מחיקה מורידה נפח כולל, העברה לא.

מחיקה מוקדמת עלולה לאבד קובץ.

### ד. פתרון אפשרי

```python
class Drive:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ids = []
        self.sizes = []
        self.active = []
        self.used = 0

    def find(self, target):
        index = -1
        for i in range(len(self.ids)):
            if self.ids[i] == target and self.active[i]:
                index = i
        return index

    def can_add(self, target, size):
        return size > 0 and self.find(target) == -1 and size <= self.capacity - self.used

    def add(self, target, size):
        if not self.can_add(target, size):
            return False
        self.ids.append(target)
        self.sizes.append(size)
        self.active.append(True)
        self.used += size
        return True

    def remove(self, target):
        index = self.find(target)
        if index == -1:
            return False
        self.active[index] = False
        self.used -= self.sizes[index]
        return True

    def audit(self):
        total = 0
        for i in range(len(self.sizes)):
            if self.active[i]:
                total += self.sizes[i]
        return total == self.used and self.used >= 0 and self.used <= self.capacity

    def report(self):
        items = []
        for i in range(len(self.ids)):
            if self.active[i]:
                items.append(self.ids[i])
        return [self.used, self.capacity - self.used, items]

class StorageLab:
    def __init__(self):
        self.history = []

    def move(self, source, target, item):
        index = source.find(item)
        status = "DENIED"
        if index != -1 and source != target:
            size = source.sizes[index]
            if target.can_add(item, size):
                target.add(item, size)
                source.remove(item)
                status = "MOVED"
        self.history.append([item, status])
        return status

    def count_moved(self):
        count = 0
        for event in self.history:
            if event[1] == "MOVED":
                count += 1
        return count

a = Drive(30)
b = Drive(12)
lab = StorageLab()
print(a.add(10, 8), a.add(20, 9), b.add(30, 5))
print(lab.move(a, b, 10))
print(lab.move(a, b, 20))
print(b.remove(30))
print(lab.move(a, b, 10))
print(lab.move(a, b, 20))
print(a.report(), b.report())
print(lab.history)
print("Combined:", a.used + b.used)
print(a.audit(), b.audit(), lab.count_moved())
print(lab.move(b, a, 10))
print(a.audit(), b.audit(), lab.count_moved())
```

פלט:

```text
True True True
DENIED
DENIED
True
MOVED
DENIED
[9, 21, [20]] [8, 4, [10]]
[[10, 'DENIED'], [20, 'DENIED'], [10, 'MOVED'], [20, 'DENIED']]
Combined: 17
True True 1
MOVED
True True 2
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

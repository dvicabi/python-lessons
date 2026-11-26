# פתרונות למורה: קופסה שחורה: איך שומרים את האירועים האחרונים בזיכרון מוגבל?

[חזרה למשימת התלמיד](../22_black_box_logger.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
LOGGER A | SIM
Stored: 3 / 4
Latest: 4 | REVIEW
Sequence: 12 | READY
```

### ב. פלט התרחיש השני

```text
LOGGER  | A | SIM
Stored: 3 / 4
Latest: 4 | REVIEW
Sequence: 12 | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("LOGGER ", end="")
print("B", end="")
print(" | SIM")
print("Stored: ", end="")
print("4", end="")
print(" / 4")
print("Latest: ", end="")
print("2", end="")
print(" | NORMAL")
print("Sequence: ", end="")
print("18", end="")
print(" | FULL")
```

פלט:

```text
LOGGER B | SIM
Stored: 4 / 4
Latest: 2 | NORMAL
Sequence: 18 | FULL
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
1 1 0 1
2 2 0 2
3 3 0 4
4 4 0 3
4 5 1 4
Check: 5
Free: 0
```

### ב. פלט התרחיש השני

```text
1 1 0 1
2 2 0 2
3 3 0 4
4 4 0 1
4 5 1 4
Check: 5
Free: 0
```

### ג. תשובות והערות לדיון

הקיבולת כבר מלאה.

accepted=stored+overwritten כאשר מתחילים ריק.

latest הוא קוד האירוע האחרון, לא מונה.

הגדלת stored תחרוג מהקיבולת.

### ד. פתרון אפשרי

```python
capacity = 3
stored = 0
accepted = 0
overwritten = 0
latest = 2
stored += 1
accepted += 1
print(stored, accepted, overwritten, latest)
latest = 4
stored += 1
accepted += 1
print(stored, accepted, overwritten, latest)
latest = 1
stored += 1
accepted += 1
print(stored, accepted, overwritten, latest)
latest = 3
accepted += 1
overwritten += 1
print(stored, accepted, overwritten, latest)
latest = 4
accepted += 1
overwritten += 1
print(stored, accepted, overwritten, latest)
print(accepted, stored + overwritten)
```

פלט:

```text
1 1 0 2
2 2 0 4
3 3 0 1
3 4 1 3
3 5 2 4
5 5
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
3 0 1
2 3
Next: 0
Sequence: 8
Rounds: 2
```

### ב. פלט התרחיש השני

```text
0 1 2
0 1
Next: 2
Sequence: 8
Rounds: 2
```

### ג. תשובות והערות לדיון

שארית חלוקה במספר חיובי נמצאת בין 0 לקיבולת פחות 1.

כל capacity כתיבות האינדקס חוזר.

sequence שומר סדר כולל.

חלוקה באפס אינה חוקית.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
8
```

```python
capacity = int(input())
sequence = int(input())
print(sequence % capacity)
sequence += 1
print(sequence % capacity)
sequence += 1
print(sequence % capacity)
sequence += 1
print(sequence % capacity)
sequence += 1
print(sequence % capacity)
sequence += 1
print(sequence % capacity)
sequence += 1
print("Next:", sequence % capacity)
print("Sequence:", sequence)
```

פלט:

```text
3
4
0
1
2
3
Next: 4
Sequence: 14
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
ADDED
INVALID
3 3 0 4
```

### ב. פלט התרחיש השני

```text
ADDED
REPLACED
3 4 1 3
```

### ג. תשובות והערות לדיון

latest מציין אירוע חוקי אחרון.

ADDED מגדיל מספר שמור, REPLACED שומר קיבולת ומגדיל מונה החלפות.

accepted מונה לאורך זמן, לכן יכול לגדול.

שוויון מציין זיכרון מלא.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
3
3
4
```

```python
capacity = int(input())
stored = int(input())
code = int(input())
if code < 1 or code > 4:
    print("INVALID")
else:
    if stored < capacity:
        stored += 1
        print("ADDED")
    else:
        print("REPLACED")
    if code == 4:
        print("REVIEW")
print(stored)
```

פלט:

```text
REPLACED
REVIEW
3
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 0 1 1
2 1 4 2
3 2 2 3
4 INVALID
5 0 3 3
6 1 4 3
7 INVALID
8 2 2 3
6 2 3 2
Next: 0
Check: 6
```

### ב. פלט התרחיש השני

```text
1 0 1 1
2 1 4 2
3 2 2 3
4 0 3 3
5 1 3 3
6 2 4 3
7 INVALID
8 0 2 3
7 1 4 2
Next: 1
Check: 7
```

### ג. תשובות והערות לדיון

אירוע לא חוקי אינו כתיבה.

בהתחלה ריק, next_slot=accepted%capacity.

review כולל היסטוריה שנדרסה.

מונים מאבדים סדר וזהות ולכן נדרשת רשימה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
3
7
2
4
0
3
1
4
2
```

```python
capacity = int(input())
count = int(input())
stored = 0
accepted = 0
overwritten = 0
invalid = 0
rounds = 0
next_slot = 0
for step in range(count):
    code = int(input())
    if code < 1 or code > 4:
        invalid += 1
    else:
        accepted += 1
        next_slot = (next_slot + 1) % capacity
        if next_slot == 0:
            rounds += 1
        if stored < capacity:
            stored += 1
        else:
            overwritten += 1
        print(step + 1, accepted, next_slot)
print(accepted, invalid, overwritten, rounds)
print(stored, next_slot)
```

פלט:

```text
1 1 1
2 2 2
4 3 0
5 4 1
6 5 2
7 6 0
6 1 3 2
3 0
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
2 [2, 0, 0, 0] 1 1
4 [2, 4, 0, 0] 2 2
1 [2, 4, 1, 0] 3 3
3 [2, 4, 1, 3] 0 4
4 [4, 4, 1, 3] 1 4
0 [4, 4, 1, 3] 1 4
2 [4, 2, 1, 3] 2 4
1 [4, 2, 1, 3] 3 4
Physical: [4, 2, 1, 3]
Ordered: [3, 4, 2, 1]
Replaced: 3
```

### ב. פלט התרחיש השני

```text
2 [2, 0, 0, 0] 1 1
4 [2, 4, 0, 0] 2 2
1 [2, 4, 1, 0] 3 3
3 [2, 4, 1, 3] 0 4
4 [4, 4, 1, 3] 1 4
2 [4, 2, 1, 3] 2 4
2 [4, 2, 2, 3] 3 4
1 [4, 2, 2, 1] 0 4
Physical: [4, 2, 2, 1]
Ordered: [4, 2, 2, 1]
Replaced: 4
```

### ג. תשובות והערות לדיון

הכתיבה מתגלגלת, ולכן האינדקס הראשון לא בהכרח הישן ביותר.

לפני מילוי מלא הרשומות מתחילות ב-0.

accepted כולל רשומות שהוחלפו ויגרום לקריאה חוזרת.

מודולו מחזיר אינדקס בטווח.

### ד. פתרון אפשרי

```python
events = [2, 4, 1, 3, 4, 0, 2, 1]
capacity = 4
memory = [0, 0, 0, 0]
sequence = [0, 0, 0, 0]
next_slot = 0
stored = 0
accepted = 0
for code in events:
    if code >= 1 and code <= 4:
        accepted += 1
        memory[next_slot] = code
        sequence[next_slot] = accepted
        next_slot = (next_slot + 1) % capacity
        if stored < capacity:
            stored += 1
oldest = 0
if stored == capacity:
    oldest = next_slot
ordered = []
numbers = []
for i in range(stored):
    slot = (oldest + i) % capacity
    ordered.append(memory[slot])
    numbers.append(sequence[slot])
print(ordered)
print(numbers)
print(accepted - stored)
```

פלט:

```text
[3, 4, 2, 1]
[4, 5, 6, 7]
3
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[1, 1, True] [1]
[2, 2, True] [1, 4]
[0, 3, True] [1, 4, 2]
[0, 3, False] [1, 4, 2]
[1, 3, True] [4, 2, 3]
[2, 3, True] [2, 3, 4]
[3, 4, 2]
```

### ב. פלט התרחיש השני

```text
[1, 1, True] [1]
[2, 2, True] [1, 4]
[0, 3, True] [1, 4, 2]
[0, 3, False] [1, 4, 2]
[1, 3, True] [3, 4, 2]
[2, 3, True] [3, 4, 2]
[3, 4, 2]
```

### ג. תשובות והערות לדיון

רשימה ניתנת לשינוי באמצעות אינדקס;

מספרים אינם משתנים מחוץ לפעולה.

ordered יוצרת רשימה חדשה.

התקלה מופיעה אחרי שמילוי מלא ואינדקס הכתיבה עבר מ-0.

בדקו קוד לא חוקי ושימור מצב, ואז החלפה.

### ד. פתרון אפשרי

```python
def write_event(memory, next_slot, stored, code):
    if code < 1 or code > 4:
        return [next_slot, stored, False]
    capacity = len(memory)
    memory[next_slot] = code
    next_slot = (next_slot + 1) % capacity
    if stored < capacity:
        stored += 1
    return [next_slot, stored, True]

def ordered(memory, next_slot, stored):
    capacity = len(memory)
    oldest = 0
    if stored == capacity:
        oldest = next_slot
    result = []
    for i in range(stored):
        slot = (oldest + i) % capacity
        result.append(memory[slot])
    return result

def summarize(events, capacity):
    if capacity <= 0:
        return []
    memory = []
    for i in range(capacity):
        memory.append(0)
    next_slot = 0
    stored = 0
    accepted = 0
    invalid = 0
    for code in events:
        result = write_event(memory, next_slot, stored, code)
        next_slot = result[0]
        stored = result[1]
        if result[2]:
            accepted += 1
        else:
            invalid += 1
    return [accepted, invalid, accepted - stored, ordered(memory, next_slot, stored)]

print(summarize([1, 4, 2, 0, 3, 4], 2))
print(summarize([1, 4, 2, 0, 3, 4], 4))
print(summarize([1, 4], 0))
```

פלט:

```text
[5, 1, 3, [3, 4]]
[5, 1, 1, [4, 2, 3, 4]]
[]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[[3, 4, 5], [2, 3, 4]]
[[1, 2, 3, 4, 5], [1, 4, 2, 3, 4]]
2 0
```

### ב. פלט התרחיש השני

```text
[[4, 5], [3, 4]]
[[1, 2, 3, 4, 5], [1, 4, 2, 3, 4]]
3 0
```

### ג. תשובות והערות לדיון

אותו אינדקס מייצג רשומה אחת.

קיבולת שונה שומרת חלון היסטורי שונה.

report היא שאילתה בלבד.

צריך להגדיר דרישה לקיבולת חיובית או ליצור מנגנון סירוב מפורש.

### ד. פתרון אפשרי

```python
class Recorder:
    def __init__(self, capacity):
        self.memory = []
        self.sequence = []
        for i in range(capacity):
            self.memory.append(0)
            self.sequence.append(0)
        self.next_slot = 0
        self.stored = 0
        self.accepted = 0
        self.invalid = 0

    def record(self, code):
        if code < 1 or code > 4:
            self.invalid += 1
            return False
        capacity = len(self.memory)
        self.accepted += 1
        self.memory[self.next_slot] = code
        self.sequence[self.next_slot] = self.accepted
        self.next_slot = (self.next_slot + 1) % capacity
        if self.stored < capacity:
            self.stored += 1
        return True

    def report(self):
        capacity = len(self.memory)
        oldest = 0
        if self.stored == capacity:
            oldest = self.next_slot
        codes = []
        numbers = []
        for i in range(self.stored):
            slot = (oldest + i) % capacity
            codes.append(self.memory[slot])
            numbers.append(self.sequence[slot])
        return [numbers, codes]

    def count_review(self):
        result = self.report()
        count = 0
        for code in result[1]:
            if code == 4:
                count += 1
        return count

    def stats(self):
        return [self.accepted, self.invalid, self.accepted - self.stored]

a = Recorder(3)
b = Recorder(5)
for code in [1, 4, 2, 0, 3, 4]:
    a.record(code)
    b.record(code)
print(a.report())
print(b.report())
print(a.accepted - a.stored, b.accepted - b.stored)
print(a.count_review(), a.stats())
print(b.count_review(), b.stats())
```

פלט:

```text
[[3, 4, 5], [2, 3, 4]]
[[1, 2, 3, 4, 5], [1, 4, 2, 3, 4]]
2 0
1 [5, 1, 2]
2 [5, 1, 0]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

# פתרונות למורה: אוטובוס: איך מונעים חריגה ממספר הנוסעים?

[חזרה למשימת התלמיד](../12_bus_capacity.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
LINE 18 | STOP 3
Passengers: 9/12
Free: 3 | Waiting: 2
BOARD
```

### ב. פלט התרחיש השני

```text
LINE 18 | STOP 3
Passengers: 9/12 | Free: 3
Waiting: 2
BOARD
```

### ג. תשובות והערות לדיון

end="/" יוצר חיבור מדויק.

השורה השנייה תפוסה וקיבולת, השלישית מקומות וממתינים.

שינוי התצוגה עלול להקשות על זיהוי כמה מקומות נשארו.

### ד. פתרון אפשרי

```python
print("LINE ", end="")
print("25", end=" | ")
print("STOP 4")
print("Passengers: ", end="")
print("12", end="/")
print("12")
print("Free: ", end="")
print("0", end=" | ")
print("Waiting: 5")
print("FULL")
```

פלט:

```text
LINE 25 | STOP 4
Passengers: 12/12
Free: 0 | Waiting: 5
FULL
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
9 3
8 4
Total: 9 6
Check: 8
```

### ב. פלט התרחיש השני

```text
9 3
11 1
Total: 12 6
Check: 11
```

### ג. תשובות והערות לדיון

boarded סופר את כל מי שעלה מאז ההתחלה.

passengers=initial+boarded-left.

השמה במקום צבירה מוחקת את הירידה הראשונה, והבדיקה לא תתאים.

### ד. פתרון אפשרי

```python
capacity = 15
passengers = 4
boarded = 0
left = 0
passengers -= 1
left += 1
passengers += 6
boarded += 6
print(passengers, capacity - passengers)
passengers -= 3
left += 3
passengers += 5
boarded += 5
print(passengers, capacity - passengers)
passengers -= 4
left += 4
passengers += 2
boarded += 2
print(passengers, capacity - passengers)
print(boarded, left)
```

פלט:

```text
9 6
11 4
9 6
13 8
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Stop 1: 9 3
Stop 2: 8 4
Boarded: 9
Left: 6
```

### ב. פלט התרחיש השני

```text
Stop 1: 13 -1
Stop 2: 14 -2
Boarded: 15
Left: 6
```

### ג. תשובות והערות לדיון

ערך שלילי מייצג חריגה מקיבולת.

עליות וירידות יכולות להתקזז.

בשלב זה משתנים נפרדים מאפשרים לחשב דוח מצטבר.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
15
4
1
6
3
5
4
2
```

```python
capacity = int(input())
passengers = int(input())
off1 = int(input())
on1 = int(input())
off2 = int(input())
on2 = int(input())
off3 = int(input())
on3 = int(input())
passengers -= off1
print("Off 1:", passengers)
passengers += on1
print("On 1:", passengers)
passengers -= off2
print("Off 2:", passengers)
passengers += on2
print("On 2:", passengers)
passengers -= off3
print("Off 3:", passengers)
passengers += on3
print("On 3:", passengers)
print("Free:", capacity - passengers)
```

פלט:

```text
Off 1: 3
On 1: 9
Off 2: 6
On 2: 11
Off 3: 7
On 3: 9
Free: 6
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
Boarded: 6
Denied: 2
FULL
Passengers: 12
```

### ב. פלט התרחיש השני

```text
ERROR
Passengers: 9
```

### ג. תשובות והערות לדיון

ירידה גדולה מהתפוסה יוצרת מצב בלתי חוקי.

ירידה משחררת מקומות.

בדוגמה 6 ממתינים ממלאים את כל המקומות.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
11
1
5
```

```python
passengers = int(input())
off = int(input())
waiting = int(input())
if off < 0 or off > passengers or waiting < 0:
    print("ERROR")
else:
    passengers -= off
    free = 12 - passengers
    boarded = waiting
    if boarded > free:
        boarded = free
    passengers += boarded
    print("Boarded:", boarded)
    print("Denied:", waiting - boarded)
    print("Free:", 12 - passengers)
print("Passengers:", passengers)
```

פלט:

```text
Boarded: 2
Denied: 3
Free: 0
Passengers: 12
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 9 0
2 12 1
ERROR 3
4 12 1
5 11 0
Boarded: 15
Denied: 2
```

### ב. פלט התרחיש השני

```text
1 12 11
2 12 0
3 1 0
4 12 4
5 9 0
Boarded: 23
Denied: 15
```

### ג. תשובות והערות לדיון

denied_total הוא סכום כל האירועים החוקיים.

התנאי נבדק לפני השמות.

סך היורדים = התחלה + סך עליות - סוף.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
10
4
3
1
9
20
1
5
3
2
10
```

```python
capacity = int(input())
count = int(input())
passengers = int(input())
initial = passengers
boarded_total = 0
off_total = 0
denied_total = 0
full_count = 0
for i in range(count):
    off = int(input())
    waiting = int(input())
    if off < 0 or off > passengers or waiting < 0:
        print("ERROR")
        continue
    passengers -= off
    off_total += off
    boarded = waiting
    if boarded > capacity - passengers:
        boarded = capacity - passengers
    passengers += boarded
    boarded_total += boarded
    denied_total += waiting - boarded
    if passengers == capacity:
        full_count += 1
    print(i + 1, passengers)
print(boarded_total, off_total, denied_total, full_count)
print("Check:", initial + boarded_total - off_total)
```

פלט:

```text
1 10
ERROR
3 8
4 10
15 8 7 2
Check: 10
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[9, 12, 12, 8, 12]
[0, 1, 2, 0, 0]
[2, 3, 5]
```

### ב. פלט התרחיש השני

```text
[12, 12, 12, 8, 12]
[0, 4, 2, 0, 0]
[1, 2, 3, 5]
```

### ג. תשובות והערות לדיון

שני ערכים לכל תחנה.

מילוי מדויק לקיבולת יכול להסתיים באפס נדחים.

לפני הפחתת נוסעים נבדוק טווח off וממתינים.

### ד. פתרון אפשרי

```python
offs = [2, 4, 0, 5, 3]
waitings = [6, 8, 2, 1, 7]
passengers = 5
occupancy = []
denied = []
free_after = []
total = 0
peak = -1
peak_stop = 0
for i in range(len(offs)):
    passengers -= offs[i]
    boarded = waitings[i]
    if boarded > 12 - passengers:
        boarded = 12 - passengers
    passengers += boarded
    rejected = waitings[i] - boarded
    occupancy.append(passengers)
    denied.append(rejected)
    free_after.append(12 - passengers)
    total += rejected
    if rejected > peak:
        peak = rejected
        peak_stop = i + 1
print(occupancy)
print(denied)
print(free_after)
print(total, peak_stop, peak)
```

פלט:

```text
[9, 12, 12, 8, 12]
[0, 1, 2, 0, 0]
[3, 0, 0, 4, 0]
3 3 2
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[12, 6, 2, 'OK']
[4, 0, 0, 'ERROR']
[[9, 6, 0, 'OK'], [12, 7, 1, 'OK'], [12, 0, 2, 'OK']]
```

### ב. פלט התרחיש השני

```text
[12, 6, 2, 'OK']
[12, 12, 0, 'OK']
[[9, 6, 0, 'OK'], [12, 7, 1, 'OK'], [12, 0, 2, 'OK']]
```

### ג. תשובות והערות לדיון

המסלול ממשיך ומצב התפוסה צריך להישמר.

רשימה חדשה מאפשרת לתעד כל אירוע.

ב-route בודקים len לפני הלולאה.

### ד. פתרון אפשרי

```python
def stop(capacity, passengers, off, waiting):
    if off < 0 or off > passengers or waiting < 0:
        return [passengers, 0, 0, "ERROR"]
    passengers -= off
    boarded = waiting
    if boarded > capacity - passengers:
        boarded = capacity - passengers
    passengers += boarded
    return [passengers, boarded, waiting - boarded, "OK"]

def route(capacity, passengers, offs, waitings):
    if len(offs) != len(waitings):
        return []
    denied = 0
    errors = 0
    for i in range(len(offs)):
        result = stop(capacity, passengers, offs[i], waitings[i])
        passengers = result[0]
        denied += result[2]
        if result[3] == "ERROR":
            errors += 1
    return [passengers, denied, errors]

print(route(12, 5, [2, 4, 0], [6, 8, 2]))
print(route(12, 5, [2, 20, 0], [6, 8, 2]))
print(route(12, 5, [2], []))
```

פלט:

```text
[12, 3, 0]
[11, 0, 1]
[]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
9
6
ERROR
3
1
11 1 [12, 11]
6 4 [8, 6]
```

### ב. פלט התרחיש השני

```text
9
1
ERROR
3
1
11 1 [12, 11]
6 9 [8, 6]
```

### ג. תשובות והערות לדיון

קיבולת ותפוסה שונות.

היסטוריה זו מתעדת תחנות מוצלחות בלבד;

אפשר להוסיף רשימת אירועים לשגיאות.

פעולה free() יכולה להחזיר capacity-passengers בלי לשנות דבר.

### ד. פתרון אפשרי

```python
class Bus:
    def __init__(self, capacity, passengers):
        self.capacity = capacity
        self.passengers = passengers
        self.denied = 0
        self.errors = 0
        self.history = []

    def stop(self, off, waiting):
        if off < 0 or off > self.passengers or waiting < 0:
            self.errors += 1
            return "ERROR"
        self.passengers -= off
        boarded = waiting
        if boarded > self.capacity - self.passengers:
            boarded = self.capacity - self.passengers
        self.passengers += boarded
        self.denied += waiting - boarded
        self.history.append(self.passengers)
        return boarded

    def free(self):
        return self.capacity - self.passengers

a = Bus(12, 5)
b = Bus(8, 3)
print(a.stop(2, 10))
print(b.stop(1, 10))
print(a.stop(20, 2))
print(a.stop(4, 3))
print(b.stop(3, 1))
print(a.passengers, a.denied, a.history)
print(b.passengers, b.denied, b.history)
print(a.free(), a.errors)
print(b.free(), b.errors)
```

פלט:

```text
9
6
ERROR
3
1
11 1 [12, 11]
6 4 [8, 6]
1 1
2 0
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

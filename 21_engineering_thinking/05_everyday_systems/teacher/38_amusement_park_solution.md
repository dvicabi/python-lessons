# פתרונות למורה: לונה פארק: איך מנהלים תורים וקיבולת מתקנים?

[חזרה למשימת התלמיד](../38_amusement_park.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
RIDE 01 | SIM
Capacity: 8 seats
Waiting: 11 guests
Boarded: 8 guests
Remaining: 3 | WAIT
```

### ב. פלט התרחיש השני

```text
RIDE  | 01 | SIM
Capacity: 8 seats
Waiting: 11 guests
Boarded: 8 guests
Remaining: 3 | WAIT
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("RIDE ", end="")
print("02", end="")
print(" | SIM")
print("Capacity: ", end="")
print("6", end="")
print(" seats")
print("Waiting: ", end="")
print("4", end="")
print(" guests")
print("Boarded: ", end="")
print("4", end="")
print(" guests")
print("Remaining: ", end="")
print("0", end="")
print(" | READY")
```

פלט:

```text
RIDE 02 | SIM
Capacity: 6 seats
Waiting: 4 guests
Boarded: 4 guests
Remaining: 0 | READY
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
0 5 5 3
4 17 13 3
0 19 19 5
Check: 0
Seats: 24
```

### ב. פלט התרחיש השני

```text
0 5 5 3
4 17 13 3
0 21 21 3
Check: 0
Seats: 24
```

### ג. תשובות והערות לדיון

waiting מצב רגעי.

unused מצטבר על פני סבבים.

arrived=boarded+waiting.

boarded+unused שווה קיבולת כפול סבבים.

### ד. פתרון אפשרי

```python
capacity = 6
waiting = 0
arrived = 0
boarded = 0
unused = 0
incoming = 4
waiting += incoming
arrived += incoming
taken = 4
waiting -= taken
boarded += taken
unused += capacity - taken
print(waiting, arrived, boarded, unused)
incoming = 9
waiting += incoming
arrived += incoming
taken = 6
waiting -= taken
boarded += taken
unused += capacity - taken
print(waiting, arrived, boarded, unused)
incoming = 1
waiting += incoming
arrived += incoming
taken = 4
waiting -= taken
boarded += taken
unused += capacity - taken
print(waiting, arrived, boarded, unused)
incoming = 3
waiting += incoming
arrived += incoming
taken = 3
waiting -= taken
boarded += taken
unused += capacity - taken
print(waiting, arrived, boarded, unused)
print("Check:", arrived - boarded)
print("Seats:", boarded + unused)
```

פלט:

```text
0 4 4 2
3 13 10 2
0 14 14 4
0 17 17 7
Check: 0
Seats: 24
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
11 8 3 0
4 4 0 4
Check: 0
```

### ב. פלט התרחיש השני

```text
11 9 2 -1
3 4 -1 4
Check: -1
```

### ג. תשובות והערות לדיון

מקום שלילי מציין חריגה מקיבולת, תור שלילי העלאת אנשים שאינם קיימים.

שתי מגבלות עצמאיות.

גם ערכים שגויים יכולים לקיים משוואה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
4
4
9
6
1
4
```

```python
capacity = int(input())
a = int(input())
x = int(input())
b = int(input())
y = int(input())
c = int(input())
z = int(input())
left1 = a - x
before2 = left1 + b
left2 = before2 - y
before3 = left2 + c
left3 = before3 - z
print(a, left1, capacity - x)
print(before2, left2, capacity - y)
print(before3, left3, capacity - z)
print(a + b + c, x + y + z, left3)
```

פלט:

```text
4 0 2
9 3 0
4 0 2
14 14 0
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
FULL 8 2
Unused: 0
Check: True
```

### ב. פלט התרחיש השני

```text
PARTIAL 6 0
Unused: 2
Check: True
```

### ג. תשובות והערות לדיון

אי אפשר להעלות יותר מהממתינים.

שוויון ממלא את המתקן.

הגעה שלילית אינה חוקית.

בדיקת מאזן משווה התחלה והגעות מול עלו וממתינים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
8
0
8
```

```python
capacity = int(input())
waiting = int(input())
arrivals = int(input())
initial = waiting
taken = 0
if arrivals < 0:
    status = "INVALID"
else:
    waiting += arrivals
    taken = waiting
    if taken > capacity:
        taken = capacity
    waiting -= taken
    if taken == capacity:
        status = "FULL"
    elif taken == 0:
        status = "EMPTY"
    else:
        status = "PARTIAL"
print(status, taken, waiting)
print("Unused:", capacity - taken)
if status != "INVALID":
    print("Check:", initial + arrivals == taken + waiting)
    if waiting == 0:
        print("CLEAR")
    else:
        print("QUEUE")
else:
    print("No update")
```

פלט:

```text
FULL 8 0
Unused: 0
Check: True
CLEAR
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 5 0
2 8 4
3 4 0
4 4 0
5 INVALID
6 8 10
7 8 4
41 37 4
6 1 18 11
Guests check: True
Seats check: True
```

### ב. פלט התרחיש השני

```text
1 5 0
2 8 4
3 8 4
4 8 0
5 INVALID
6 8 10
7 8 4
49 45 4
6 1 18 3
Guests check: True
Seats check: True
```

### ג. תשובות והערות לדיון

מדידה לפני עלייה מתעדת שיא.

אירוע פסול אינו סבב.

taken==capacity.

סך קיבולת=boarded+unused.

קצב הגעה עשוי לעלות על קצב טיפול.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
8
7
5
12
0
4
-1
18
2
```

```python
capacity = int(input())
count = int(input())
full_rounds = 0
empty_rounds = 0
waiting = 0
arrived = 0
boarded = 0
unused = 0
peak = 0
valid = 0
invalid = 0
for i in range(count):
    incoming = int(input())
    if incoming < 0:
        invalid += 1
        print(i + 1, "INVALID")
    else:
        valid += 1
        waiting += incoming
        arrived += incoming
        if waiting > peak:
            peak = waiting
        taken = waiting
        if taken > capacity:
            taken = capacity
        waiting -= taken
        boarded += taken
        unused += capacity - taken
        if taken == capacity:
            full_rounds += 1
        if taken == 0:
            empty_rounds += 1
        print(i + 1, taken, waiting)
print(arrived, boarded, waiting)
print(valid, invalid, peak, unused)
print(full_rounds, empty_rounds)
print("Guests check:", arrived == boarded + waiting)
print("Seats check:", valid * capacity == boarded + unused)
```

פלט:

```text
1 5 0
2 8 4
3 4 0
4 4 0
5 INVALID
6 8 10
7 8 4
41 37 4
6 1 18 11
3 0
Guests check: True
Seats check: True
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 [0] 3
2 [1, 2] 0
3 [3, 4] 0
4 [5] 3
[[0], [1, 2], [3, 4], [5]]
[] 0
18 6
```

### ב. פלט התרחיש השני

```text
1 [0, 1] 0
2 [2, 3] 0
3 [4, 5] 3
4 [] 7
[[0, 1], [2, 3], [4, 5], []]
[] 0
18 10
```

### ג. תשובות והערות לדיון

אחרת קבוצה תיעלם.

running מסיים סבב בלי לשנות מיקום.

first סופר קבוצות ו-boarded אנשים.

קבוצה שלמה עשויה לא להתאים.

סורקים היסטוריה וממתינים לפי אינדקס.

### ד. פתרון אפשרי

```python
groups = [3, 4, 2, 5, 1, 3]
capacity = 6
rounds = 4
first = 0
boarded = 0
unused = 0
history = []
people_per_round = []
for r in range(rounds):
    free = capacity
    taken = []
    running = True
    while first < len(groups) and running:
        size = groups[first]
        if size <= free:
            taken.append(first)
            free -= size
            boarded += size
            first += 1
        else:
            running = False
    unused += free
    history.append(taken)
    people_per_round.append(capacity - free)
    print(r + 1, taken, free)
pending = []
waiting = 0
for i in range(len(groups)):
    if i >= first:
        pending.append(i)
        waiting += groups[i]
print(history)
print(pending, waiting)
total = 0
for size in groups:
    total += size
print(boarded, unused)
print(people_per_round)
print(total == boarded + waiting, rounds * capacity == boarded + unused)
```

פלט:

```text
1 [0] 3
2 [1, 2] 0
3 [3, 4] 0
4 [5] 3
[[0], [1, 2], [3, 4], [5]]
[] 0
18 6
[3, 6, 6, 3]
True True
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[1, [0], 3]
[[[[0], 3], [[1, 2], 0], [[3, 4], 0], [[5], 3]], 6]
[[[[0, 1], 0], [[2, 3], 0], [[4, 5], 3]], 6]
[3, 4, 2, 5, 1, 3]
```

### ב. פלט התרחיש השני

```text
[1, [0], 3]
[[[[0], 3], [[1], 2], [[2], 4], [[3], 1]], 4]
[[[[0], 4], [[1, 2], 1], [[3, 4], 1]], 5]
[3, 4, 2, 5, 1, 3]
```

### ג. תשובות והערות לדיון

התאמה מדויקת מותרת.

הפעולה רק קוראת נתונים.

קבוצה גדולה תחסום תור ולכן צריך לדחות בקליטה.

סבב ריק.

מספר סבבים מגביל ניסוי.

### ד. פתרון אפשרי

```python
def round_plan(groups, first, capacity):
    taken = []
    free = capacity
    index = first
    running = True
    while index < len(groups) and running:
        size = groups[index]
        if size > 0 and size <= free:
            taken.append(index)
            free -= size
            index += 1
        else:
            running = False
    return [index, taken, free]

def simulate(groups, capacity, rounds):
    if capacity <= 0:
        return []
    for size in groups:
        if size <= 0 or size > capacity:
            return []
    first = 0
    report = []
    for r in range(rounds):
        result = round_plan(groups, first, capacity)
        first = result[0]
        report.append([result[1], result[2]])
    return [report, first]

groups = [3, 4, 2, 5, 1, 3]
print(round_plan(groups, 0, 6))
print(simulate(groups, 6, 4))
print(simulate(groups, 7, 3))
print(groups)
print(simulate([7, 2], 6, 3))
print(simulate([], 6, 2))
```

פלט:

```text
[1, [0], 3]
[[[[0], 3], [[1, 2], 0], [[3, 4], 0], [[5], 3]], 6]
[[[[0, 1], 0], [[2, 3], 0], [[4, 5], 3]], 6]
[3, 4, 2, 5, 1, 3]
[]
[[[[], 6], [[], 6]], 0]
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
True
True
True
False
True
False
[[11], 3] [[14], 0]
[[9, 3, 6, True], [8, 8, 0, True]]
[[12, 13], 0]
[[9, 9, 0, True], [8, 8, 0, True]]
[11, 12, 13, 14] [11, 15]
```

### ב. פלט התרחיש השני

```text
True
True
True
False
True
True
[[11, 12], 0] [[14], 0]
[[16, 7, 9, True], [8, 8, 0, True]]
[[13], 5]
[[16, 9, 7, True], [8, 8, 0, True]]
[11, 12, 13, 14, 15] [11]
```

### ג. תשובות והערות לדיון

Group נתון בלבד.

מזהה ייחודי לאורך הניסוי.

first שומר תור.

queue כוללת היסטוריה;

waiting רק המשך.

גודל מלא נבדק.

Park שומרת accepted משותפת.

### ד. פתרון אפשרי

```python
class Group:
    def __init__(self, code, size):
        self.code = code
        self.size = size

class Ride:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.first = 0
        self.boarded = 0
        self.arrived = 0
        self.history = []

    def admit(self, group):
        if group.size <= 0 or group.size > self.capacity:
            return False
        self.queue.append(group)
        self.arrived += group.size
        return True

    def round(self):
        free = self.capacity
        taken = []
        running = True
        while self.first < len(self.queue) and running:
            group = self.queue[self.first]
            if group.size <= free:
                free -= group.size
                self.boarded += group.size
                taken.append(group.code)
                self.first += 1
            else:
                running = False
        self.history.append([taken, free])
        return [taken, free]

    def waiting(self):
        total = 0
        for i in range(len(self.queue)):
            if i >= self.first:
                total += self.queue[i].size
        return total

    def audit(self):
        return self.arrived == self.boarded + self.waiting()

class Park:
    def __init__(self, rides):
        self.rides = rides
        self.accepted = []
        self.rejected = []

    def add(self, index, group):
        if group.code <= 0 or group.code in self.accepted or index < 0 or index >= len(self.rides):
            self.rejected.append(group.code)
            return False
        if not self.rides[index].admit(group):
            self.rejected.append(group.code)
            return False
        self.accepted.append(group.code)
        return True

    def best_for(self, group):
        best = -1
        for i in range(len(self.rides)):
            ride = self.rides[i]
            if group.size > 0 and group.size <= ride.capacity:
                if best == -1 or ride.waiting() < self.rides[best].waiting():
                    best = i
        return best

    def assign(self, group):
        return self.add(self.best_for(group), group)

    def report(self):
        result = []
        for ride in self.rides:
            result.append([ride.arrived, ride.boarded, ride.waiting(), ride.audit()])
        return result

a = Ride(6)
b = Ride(8)
park = Park([a, b])
print(park.add(0, Group(11, 3)))
print(park.add(0, Group(12, 4)))
print(park.add(0, Group(13, 2)))
print(park.add(1, Group(11, 3)))
print(park.add(1, Group(14, 8)))
print(park.add(0, Group(15, 7)))
print(a.round(), b.round())
print(park.report())
print(a.round())
print(park.report())
print(park.accepted, park.rejected)
print(park.best_for(Group(16, 4)))
print(park.report())
print(park.assign(Group(16, 4)))
print(park.report())
```

פלט:

```text
True
True
True
False
True
False
[[11], 3] [[14], 0]
[[9, 3, 6, True], [8, 8, 0, True]]
[[12, 13], 0]
[[9, 9, 0, True], [8, 8, 0, True]]
[11, 12, 13, 14] [11, 15]
0
[[9, 9, 0, True], [8, 8, 0, True]]
True
[[13, 9, 4, True], [8, 8, 0, True]]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

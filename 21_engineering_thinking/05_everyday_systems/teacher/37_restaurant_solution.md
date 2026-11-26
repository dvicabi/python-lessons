# פתרונות למורה: מסעדה: כיצד משבצים קבוצות ומנהלים שולחנות בלי לאבד הזמנה?

[חזרה למשימת התלמיד](../37_restaurant.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
RESTAURANT 01 | DEMO
Group: 3 guests
Table: 2 | Capacity: 4
Free: 1 seat
State: SEATED | OK
```

### ב. פלט התרחיש השני

```text
RESTAURANT  | 01 | DEMO
Group: 3 guests
Table: 2 | Capacity: 4
Free: 1 seat
State: SEATED | OK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("RESTAURANT ", end="")
print("02", end="")
print(" | DEMO")
print("Group: ", end="")
print("5", end="")
print(" guests")
print("Table: ", end="")
print("NONE", end="")
print(" | Capacity: 0")
print("Free: ", end="")
print("0", end="")
print(" seats")
print("State: ", end="")
print("WAIT", end="")
print(" | NO TABLE")
```

פלט:

```text
RESTAURANT 02 | DEMO
Group: 5 guests
Table: NONE | Capacity: 0
Free: 0 seats
State: WAIT | NO TABLE
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 4 4 4 0
2 3 6 6 0
3 2 9 9 0
2 3 5 9 4
Guests check: 5
Tables check: 5
```

### ב. פלט התרחיש השני

```text
1 4 4 4 0
2 3 6 6 0
3 2 11 11 0
2 3 7 11 4
Guests check: 7
Tables check: 5
```

### ג. תשובות והערות לדיון

שולחן אחד מכיל כמה אנשים.

arrived-left=guests.

הסכום אינו זהות או גודל כל קבוצה.

קיבולת מגבילה התאמה.

### ד. פתרון אפשרי

```python
tables = 6
occupied = 0
guests = 0
arrived = 0
left = 0
group = 2
occupied += 1
guests += group
arrived += group
print(occupied, tables - occupied, guests, arrived, left)
group = 5
occupied += 1
guests += group
arrived += group
print(occupied, tables - occupied, guests, arrived, left)
group = 3
occupied += 1
guests += group
arrived += group
print(occupied, tables - occupied, guests, arrived, left)
group = 5
occupied -= 1
guests -= group
left += group
print(occupied, tables - occupied, guests, arrived, left)
group = 4
occupied += 1
guests += group
arrived += group
print(occupied, tables - occupied, guests, arrived, left)
print("Guests check:", arrived - left)
print("Tables check:", occupied + tables - occupied)
```

פלט:

```text
1 5 2 2 0
2 4 7 7 0
3 3 10 10 0
2 4 5 10 5
3 3 9 14 5
Guests check: 9
Tables check: 6
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
A: 2 2 0
B: 4 5 -1
C: 6 3 3
Total: 12 10 2
Check: 2
```

### ב. פלט התרחיש השני

```text
A: 2 2 0
B: 4 3 1
C: 6 5 1
Total: 12 10 2
Check: 2
```

### ג. תשובות והערות לדיון

שלילי מציין קבוצה גדולה מהשולחן.

מקומות כוללים אינם ניתנים לאיחוד במודל.

צריך לבדוק התאמה לכל שולחן.

שינוי שיבוץ משנה פערים פרטניים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
2
6
5
2
```

```python
cap_a = int(input())
cap_b = int(input())
group_a = int(input())
group_b = int(input())
total = cap_a + cap_b - group_a - group_b
print("Plan 1:", cap_a - group_a, cap_b - group_b)
print("Plan 2:", cap_a - group_b, cap_b - group_a)
print("Total:", total)
```

פלט:

```text
Plan 1: -3 4
Plan 2: 0 1
Total: 1
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
C 4
False False True
Unused: 1
```

### ב. פלט התרחיש השני

```text
B 6
False True True
Unused: 3
```

### ג. תשובות והערות לדיון

שומרים שולחן גדול לקבוצה גדולה.

סריקה לא מתחייבת עד בחירה.

< שומר ראשון.

קבוצה שווה לקיבולת מתאימה.

שולחן תפוס אינו פנוי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
4
2
6
4
0
0
0
```

```python
group = int(input())
cap_a = int(input())
cap_b = int(input())
cap_c = int(input())
busy_a = int(input()) == 1
busy_b = int(input()) == 1
busy_c = int(input()) == 1
best = "NONE"
best_cap = 0
if group > 0:
    if not busy_a and cap_a >= group:
        best = "A"
        best_cap = cap_a
    if not busy_b and cap_b >= group:
        if best == "NONE" or cap_b < best_cap:
            best = "B"
            best_cap = cap_b
    if not busy_c and cap_c >= group:
        if best == "NONE" or cap_c < best_cap:
            best = "C"
            best_cap = cap_c
if best == "A":
    busy_a = True
elif best == "B":
    busy_b = True
elif best == "C":
    busy_c = True
print(best, best_cap)
print(busy_a, busy_b, busy_c)
if best != "NONE":
    print("Unused:", best_cap - group)
else:
    print("WAIT")
```

פלט:

```text
C 4
False False True
Unused: 0
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 SEATED 3 1
2 WAIT 3 1
3 LEFT 0 4
4 WAIT 0 4
5 SEATED 4 0
6 LEFT 0 4
7 EMPTY 0 4
8 INVALID 0 4
7 7 2 2 1
Check: True
```

### ב. פלט התרחיש השני

```text
1 WAIT 0 4
2 SEATED 1 3
3 LEFT 0 4
4 WAIT 0 4
5 SEATED 4 0
6 LEFT 0 4
7 EMPTY 0 4
8 INVALID 0 4
5 5 2 2 1
Check: True
```

### ג. תשובות והערות לדיון

שחרור מסיים ביקור של הקבוצה כולה.

visits מונה קבוצות, seated אנשים.

WAIT לא שובץ.

שולחן אחד לקבוצה אחת.

seated-departed=guests.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
4
8
1
3
1
1
2
0
1
5
1
4
2
0
2
0
3
2
```

```python
capacity = int(input())
count = int(input())
peak = 0
success = 0
guests = 0
seated = 0
departed = 0
waiting = 0
invalid = 0
visits = 0
for i in range(count):
    kind = int(input())
    group = int(input())
    if kind == 1 and group > 0:
        if guests == 0 and group <= capacity:
            guests = group
            seated += group
            visits += 1
            status = "SEATED"
        else:
            waiting += 1
            status = "WAIT"
    elif kind == 2 and group == 0:
        if guests > 0:
            departed += guests
            guests = 0
            status = "LEFT"
        else:
            status = "EMPTY"
    else:
        invalid += 1
        status = "INVALID"
    if status == "SEATED" or status == "LEFT":
        success += 1
    if guests > peak:
        peak = guests
    print(i + 1, status, guests, capacity - guests)
print(seated, departed, waiting, visits, invalid)
print("Check:", seated - departed == guests)
print(peak, success, count - success)
```

פלט:

```text
1 SEATED 3 1
2 WAIT 3 1
3 LEFT 0 4
4 WAIT 0 4
5 SEATED 4 0
6 LEFT 0 4
7 EMPTY 0 4
8 INVALID 0 4
7 7 2 2 1
Check: True
4 4 4
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[0, 0, 3, 0]
[5, 0, 3, 0]
[5, 2, 3, 0]
[5, 2, 3, 4]
[5, 2, 3, 4]
[5, 2, 0, 4]
[5, 2, 3, 4]
[5, 2, 3, 4]
[['SEATED', 2], ['SEATED', 0], ['SEATED', 1], ['SEATED', 3], ['WAIT', -1], ['LEFT', 2], ['SEATED', 2], ['INVALID', -1]]
Check: True
```

### ב. פלט התרחיש השני

```text
[3, 0, 0, 0]
[3, 0, 0, 0]
[3, 0, 2, 0]
[3, 0, 2, 4]
[3, 1, 2, 4]
[3, 1, 0, 4]
[3, 1, 3, 4]
[3, 1, 3, 4]
[['SEATED', 0], ['WAIT', -1], ['SEATED', 2], ['SEATED', 3], ['SEATED', 1], ['LEFT', 2], ['SEATED', 2], ['INVALID', -1]]
Check: True
```

### ג. תשובות והערות לדיון

הבחירה תלויה במצב הנוכחי.

שולחן גדול עלול להיתפס מוקדם.

אינדקס פסול מסוכן.

total לא מראה שיבוץ או קיבולת.

history מתאר אירועים ולא מצב נוכחי.

### ד. פתרון אפשרי

```python
capacities = [6, 2, 4, 4]
guests = [0, 0, 0, 0]
events = [[1, 3], [1, 5], [1, 2], [1, 4], [1, 1], [2, 2], [1, 3], [2, 9]]
history = []
wait_count = 0
invalid_count = 0
seated = 0
departed = 0
for event in events:
    kind = event[0]
    value = event[1]
    if kind == 1 and value > 0:
        best = -1
        for i in range(len(capacities)):
            if guests[i] == 0 and capacities[i] >= value:
                if best == -1 or capacities[i] < capacities[best]:
                    best = i
        if best == -1:
            status = "WAIT"
            wait_count += 1
        else:
            guests[best] = value
            seated += value
            status = "SEATED"
        history.append([status, best])
    elif kind == 2 and value >= 0 and value < len(guests):
        if guests[value] > 0:
            departed += guests[value]
            guests[value] = 0
            status = "LEFT"
        else:
            status = "EMPTY"
        history.append([status, value])
    else:
        history.append(["INVALID", -1])
        invalid_count += 1
    print(guests)
total = 0
for group in guests:
    total += group
free_tables = 0
free_seats = 0
for i in range(len(guests)):
    if guests[i] == 0:
        free_tables += 1
        free_seats += capacities[i]
print(history)
print(wait_count, invalid_count, free_tables, free_seats)
print("Check:", seated - departed == total)
```

פלט:

```text
[0, 0, 3, 0]
[5, 0, 3, 0]
[5, 2, 3, 0]
[5, 2, 3, 4]
[5, 2, 3, 4]
[5, 2, 0, 4]
[5, 2, 3, 4]
[5, 2, 3, 4]
[['SEATED', 2], ['SEATED', 0], ['SEATED', 1], ['SEATED', 3], ['WAIT', -1], ['LEFT', 2], ['SEATED', 2], ['INVALID', -1]]
1 1 0 0
Check: True
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
2
[0, 0, 0, 0]
2
0
3
-1
3
2
[5, 0, 3, 4]
```

### ב. פלט התרחיש השני

```text
3
[0, 0, 0, 0]
3
0
2
-1
4
2
[5, 0, 3, 3]
```

### ג. תשובות והערות לדיון

choose שאילתה, seat מעדכנת.

<= מעדיף מאוחר.

משווים guests לפני ואחרי choose.

שחרור שני מחזיר 0.

האורכים צריכים להיות זהים.

### ד. פתרון אפשרי

```python
def choose(capacities, guests, size):
    if size <= 0:
        return -1
    best = -1
    for i in range(len(capacities)):
        if guests[i] == 0 and capacities[i] >= size:
            if best == -1 or capacities[i] < capacities[best]:
                best = i
    return best

def seat(capacities, guests, size):
    index = choose(capacities, guests, size)
    if index != -1:
        guests[index] = size
    return index

def leave(guests, index):
    if index < 0 or index >= len(guests) or guests[index] == 0:
        return 0
    size = guests[index]
    guests[index] = 0
    return size

def move(capacities, guests, source, target):
    if source < 0 or target < 0 or source >= len(guests) or target >= len(guests):
        return False
    if guests[source] == 0 or guests[target] != 0 or guests[source] > capacities[target]:
        return False
    guests[target] = guests[source]
    guests[source] = 0
    return True

capacities = [6, 2, 4, 4]
guests = [0, 0, 0, 0]
print(choose(capacities, guests, 3))
print(guests)
print(seat(capacities, guests, 3))
print(seat(capacities, guests, 5))
print(seat(capacities, guests, 4))
print(seat(capacities, guests, 3))
print(leave(guests, 2))
print(seat(capacities, guests, 3))
print(guests)
print(leave(guests, 0))
print(move(capacities, guests, 2, 1))
print(move(capacities, guests, 2, 0))
print(guests)
```

פלט:

```text
2
[0, 0, 0, 0]
2
0
3
-1
3
2
[5, 0, 3, 4]
5
False
True
[3, 0, 0, 4]
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
SEATED
SEATED
SEATED
SEATED
WAIT
DUPLICATE
[[6, 102, 5], [2, 103, 2], [4, 101, 3], [4, 104, 4]]
3
SEATED
[[6, 102, 5], [2, 103, 2], [4, 105, 1], [4, 104, 4]]
[[101, 'SEATED', 2], [102, 'SEATED', 0], [103, 'SEATED', 1], [104, 'SEATED', 3], [105, 'WAIT', -1], [101, 'DUPLICATE', -1], [105, 'SEATED', 2]] True
```

### ב. פלט התרחיש השני

```text
SEATED
SEATED
SEATED
SEATED
WAIT
DUPLICATE
[[6, 102, 5], [2, 103, 2], [3, 101, 3], [4, 104, 4]]
3
SEATED
[[6, 102, 5], [2, 103, 2], [3, 105, 1], [4, 104, 4]]
[[101, 'SEATED', 2], [102, 'SEATED', 0], [103, 'SEATED', 1], [104, 'SEATED', 3], [105, 'WAIT', -1], [101, 'DUPLICATE', -1], [105, 'SEATED', 2]] True
```

### ג. תשובות והערות לדיון

Table אחראית למצבה.

WAIT רשאית לנסות שוב.

מזהה ביקור חד-פעמי מונע כפילות.

סך guests שווה seated-departed.

choose היא שאילתה.

שחרור שני מחזיר 0.

### ד. פתרון אפשרי

```python
class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.group = 0
        self.guests = 0

    def fits(self, size):
        return size > 0 and self.group == 0 and size <= self.capacity

    def seat(self, group, size):
        if group <= 0 or not self.fits(size):
            return False
        self.group = group
        self.guests = size
        return True

    def leave(self):
        size = self.guests
        self.group = 0
        self.guests = 0
        return size

class Restaurant:
    def __init__(self, tables):
        self.tables = tables
        self.visits = []
        self.history = []
        self.seated = 0
        self.departed = 0

    def choose(self, size):
        best = -1
        for i in range(len(self.tables)):
            table = self.tables[i]
            if table.fits(size):
                if best == -1 or table.capacity < self.tables[best].capacity:
                    best = i
        return best

    def arrive(self, group, size):
        best = -1
        if group <= 0 or size <= 0:
            status = "INVALID"
        elif group in self.visits:
            status = "DUPLICATE"
        else:
            best = self.choose(size)
            if best == -1:
                status = "WAIT"
            else:
                self.tables[best].seat(group, size)
                self.visits.append(group)
                self.seated += size
                status = "SEATED"
        self.history.append([group, status, best])
        return status

    def leave(self, index):
        if index < 0 or index >= len(self.tables):
            return 0
        size = self.tables[index].leave()
        self.departed += size
        return size

    def find_group(self, group):
        index = -1
        if group > 0:
            for i in range(len(self.tables)):
                if self.tables[i].group == group:
                    index = i
        return index

    def leave_group(self, group):
        return self.leave(self.find_group(group))

    def report(self):
        result = []
        for table in self.tables:
            result.append([table.capacity, table.group, table.guests])
        return result

    def audit(self):
        total = 0
        for table in self.tables:
            total += table.guests
        return total == self.seated - self.departed

place = Restaurant([Table(6), Table(2), Table(4), Table(4)])
print(place.arrive(101, 3))
print(place.arrive(102, 5))
print(place.arrive(103, 2))
print(place.arrive(104, 4))
print(place.arrive(105, 1))
print(place.arrive(101, 1))
print(place.report())
print(place.leave(2))
print(place.arrive(105, 1))
print(place.report())
print(place.history, place.audit())
print(place.leave_group(102))
print(place.leave_group(102))
print(place.leave_group(999))
print(place.report(), place.audit())
```

פלט:

```text
SEATED
SEATED
SEATED
SEATED
WAIT
DUPLICATE
[[6, 102, 5], [2, 103, 2], [4, 101, 3], [4, 104, 4]]
3
SEATED
[[6, 102, 5], [2, 103, 2], [4, 105, 1], [4, 104, 4]]
[[101, 'SEATED', 2], [102, 'SEATED', 0], [103, 'SEATED', 1], [104, 'SEATED', 3], [105, 'WAIT', -1], [101, 'DUPLICATE', -1], [105, 'SEATED', 2]] True
5
0
0
[[6, 0, 0], [2, 103, 2], [4, 105, 1], [4, 104, 4]] True
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

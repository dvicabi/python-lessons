# פתרונות למורה: קורקינט חשמלי: איזו דרך באמת תחסוך סוללה?

[חזרה למשימת התלמיד](../13_electric_scooter.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
RIDE 02 | UPHILL
Battery: 18/30
Segment: 4 km | Cost: 8
```

### ב. פלט התרחיש השני

```text
RIDE 02 | UPHILL
Battery: 18
30
Segment: 4Cost: 8
```

### ג. תשובות והערות לדיון

18/30 מופיע באותה שורה.

ללא המפריד 4 נצמד ל-Cost.

יש להכיר רזרבה ועלות המקטע.

### ד. פתרון אפשרי

```python
print("RIDE ", end="")
print("03", end=" | ")
print("FLAT")
print("Battery: ", end="")
print("9", end="/")
print("30")
print("Segment: ", end="")
print("5", end=" km | ")
print("Cost: ", end="")
print("5")
```

פלט:

```text
RIDE 03 | FLAT
Battery: 9/30
Segment: 5 km | Cost: 5
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
19 5 0 5
11 13 0 9
14 13 3 12
Net used: 10
```

### ב. פלט התרחיש השני

```text
19 5 0 5
11 13 0 9
17 13 6 15
Net used: 7
```

### ג. תשובות והערות לדיון

used מתעד צריכה ברוטו;

recovered החזרה ברוטו.

battery=24-used+recovered.

עלייה, מישור וירידה משפיעים אחרת על הסוללה.

### ד. פתרון אפשרי

```python
battery = 25
distance = 0
used = 0
recovered = 0
battery -= 6
distance += 6
used += 6
print(battery, distance)
battery -= 4 * 2
distance += 4
used += 4 * 2
print(battery, distance)
battery += 5
distance += 5
recovered += 5
print(battery, distance)
battery -= 3
distance += 3
used += 3
print(battery, distance)
print(used, recovered, used - recovered)
```

פלט:

```text
19 6
11 10
16 15
13 18
17 5 12
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Flat: 19
Uphill: 9
Downhill: 13
Length: 15
Net: 12
Above reserve: 11
```

### ב. פלט התרחיש השני

```text
Flat: 6
Uphill: 0
Downhill: 5
Length: 12
Net: 5
Above reserve: 3
```

### ג. תשובות והערות לדיון

ייתכן שבאמצע הסוללה יורדת מתחת לרזרבה ואז הירידה המדומה משיבה אנרגיה.

בקלט השני אחרי עלייה היתרה 0.

החזרה חייבת להיות מוגבלת ל-30.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
28
4
3
5
2
```

```python
battery = int(input())
up1 = int(input())
down = int(input())
up2 = int(input())
flat = int(input())
battery -= up1 * 2
print(battery)
battery += down
print(battery)
battery -= up2 * 2
print(battery)
battery -= flat
print(battery)
print("Length:", up1 + down + up2 + flat)
```

פלט:

```text
20
23
13
11
Length: 14
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
RECOVERED
Battery: 30
Unused recovery: 3
```

### ב. פלט התרחיש השני

```text
DENIED
Battery: 13
Unused recovery: 0
```

### ג. תשובות והערות לדיון

27+6=33 ולכן 3 יחידות לא נאגרות.

יתרה בדיוק 2 חוקית;

פחות מזה לא.

battery < 2 נבדק לפני סוג המקטע.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
28
5
3
```

```python
battery = int(input())
length = int(input())
kind = int(input())
used = 0
gained = 0
if length <= 0 or kind < 1 or kind > 3:
    print("ERROR")
elif battery < 2:
    print("LOW")
elif kind == 3:
    gained = length
    if gained > 30 - battery:
        gained = 30 - battery
    battery += gained
    print("RECOVERED")
else:
    cost = length
    if kind == 2:
        cost *= 2
    if battery - cost >= 2:
        battery -= cost
        used = cost
        print("GO")
    else:
        print("DENIED")
print(used, gained, battery)
```

פלט:

```text
RECOVERED
0 2 30
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 16 4
2 6 9
3 12 15
STOP 4
14 6 12
```

### ב. פלט התרחיש השני

```text
1 30 15
2 16 22
3 8 30
4 17 39
5 7 44
32 19 7
```

### ג. תשובות והערות לדיון

אין לרשום מקטע שלא בוצע.

gained צריך להיות הכמות שנכנסה בפועל, אחרת מאזן יישבר.

סדר מסלול מחייב מעבר פיזי במקטעים הקודמים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
28
4
3
6
2
8
1
6
2
4
```

```python
battery = int(input())
count = int(input())
done = 0
overflow = 0
distance = 0
running = True
index = 0
while index < count and running:
    i = index
    index += 1
    kind = int(input())
    length = int(input())
    if length <= 0 or kind < 1 or kind > 3:
        print("ERROR")
        running = False
    else:
        if battery < 2:
            print("LOW")
            running = False
        else:
            if kind == 3:
                battery += length
                if battery > 30:
                    overflow += battery - 30
                    battery = 30
            else:
                cost = length
                if kind == 2:
                    cost *= 2
                if battery - cost < 2:
                    print("STOP")
                    running = False
                else:
                    battery -= cost
            if running:
                done += 1
                distance += length
                print(done, battery)
print(done, distance, overflow)
```

פלט:

```text
1 30
2 14
3 8
STOP
3 20 4
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[1, 2, 3]
[16, 6, 12]
Remaining: 2
```

### ב. פלט התרחיש השני

```text
[1, 2, 3, 4, 5]
[20, 10, 16, 4, 2]
Remaining: 0
```

### ג. תשובות והערות לדיון

המקטע הבא הוא len(completed)+1 אם נשארו מקטעים.

history מכילה מצבים, לא מרחקים.

עודף החזרה עלול להיזרק ולכן סדר המקטעים משנה.

### ד. פתרון אפשרי

```python
kinds = [3, 2, 1, 2]
lengths = [8, 6, 5, 5]
battery = 26
history = []
overflows = []
total = 0
running = True
index = 0
while index < len(kinds) and running:
    i = index
    index += 1
    length = lengths[i]
    overflow = 0
    if kinds[i] == 3:
        battery += length
        if battery > 30:
            overflow = battery - 30
            battery = 30
    else:
        cost = length
        if kinds[i] == 2:
            cost *= 2
        if battery - cost < 2:
            running = False
        else:
            battery -= cost
    if running:
        history.append(battery)
        overflows.append(overflow)
        total += overflow
print(history)
print(overflows)
print(total, len(history))
```

פלט:

```text
[30, 18, 13, 3]
[4, 0, 0, 0]
4 4
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[18, 8, 14, 2]
[30, 14, 8]
```

### ב. פלט התרחיש השני

```text
[18, 8, 14]
[30, 14, 8]
```

### ג. תשובות והערות לדיון

היתרה החוקית אינה שלילית.

צריך לשמור את המצב הקודם בעת דחייה.

כאשר battery=10,cost=8, יתרה 2 חוקית, אבל <= דוחה.

### ד. פתרון אפשרי

```python
def step(battery, kind, length, reserve, capacity):
    if length <= 0 or kind < 1 or kind > 3 or battery < reserve:
        return -1
    if kind == 3:
        battery += length
        if battery > capacity:
            battery = capacity
        return battery
    cost = length
    if kind == 2:
        cost *= 2
    if battery - cost < reserve:
        return -1
    return battery - cost
def route(battery, kinds, lengths, reserve, capacity):
    history = []
    if len(kinds) != len(lengths):
        return history
    running = True
    index = 0
    while index < len(kinds) and running:
        i = index
        index += 1
        next_battery = step(battery, kinds[i], lengths[i], reserve, capacity)
        if next_battery == -1:
            running = False
        else:
            battery = next_battery
            history.append(battery)
    return history
print(route(22, [1, 2, 3, 2], [4, 5, 6, 6], 2, 30))
print(route(22, [1, 2, 3, 2], [4, 5, 6, 6], 5, 30))
```

פלט:

```text
[18, 8, 14, 2]
[18, 8, 14]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
True
False
True
True
18 13 [10, 18]
15 12 [15]
```

### ב. פלט התרחיש השני

```text
True
True
True
True
18 13 [10, 18]
14 17 [2, 14]
```

### ג. תשובות והערות לדיון

כל המצב המקורי נשמר.

קיבולת משתנה בין דגמים.

משתנה מועמד מאפשר לבדוק את התוצאה לפני ביצוע.

### ד. פתרון אפשרי

```python
class Scooter:
    def __init__(self, battery, capacity):
        self.battery = battery
        self.capacity = capacity
        self.distance = 0
        self.history = []
        self.rejected = 0

    def ride(self, kind, length):
        if length <= 0 or kind < 1 or kind > 3 or self.battery < 2:
            self.rejected += 1
            return False
        next_battery = self.battery
        if kind == 3:
            next_battery += length
            if next_battery > self.capacity:
                next_battery = self.capacity
        else:
            cost = length
            if kind == 2:
                cost *= 2
            if next_battery - cost < 2:
                self.rejected += 1
                return False
            next_battery -= cost
        self.battery = next_battery
        self.distance += length
        self.history.append(self.battery)
        return True

    def charge(self, amount):
        if amount > 0:
            self.battery += amount
            if self.battery > self.capacity:
                self.battery = self.capacity

a = Scooter(20, 30)
b = Scooter(8, 15)
print(a.ride(2, 5))
print(b.ride(2, 5))
print(a.ride(3, 8))
print(b.ride(3, 12))
print(a.battery, a.distance, a.history)
print(b.battery, b.distance, b.history)
b.charge(50)
print(a.battery, a.rejected)
print(b.battery, b.rejected)
```

פלט:

```text
True
False
True
True
18 13 [10, 18]
15 12 [15]
18 0
15 1
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

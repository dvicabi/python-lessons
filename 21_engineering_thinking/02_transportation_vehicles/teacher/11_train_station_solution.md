# פתרונות למורה: תחנת רכבת: מדוע רכבת אחת מאחרת לכל הקו?

[חזרה למשימת התלמיד](../11_train_station.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
PLATFORM 2 | TRAIN 17
Planned: 120 | Actual: 127
Delay: 7 min | WAIT
```

### ב. פלט התרחיש השני

```text
PLATFORM 2 | TRAIN 17
Planned: 120 | Actual: 127 / Delay: 7
WAIT
```

### ג. תשובות והערות לדיון

שלוש שורות: רציף ורכבת;

זמן מתוכנן וזמן בפועל;

איחור וסטטוס.

שינוי end משפיע רק על תצוגה.

בתרחיש השני Delay מתחבר לשורת Actual ו-WAIT מופרד.

### ד. פתרון אפשרי

```python
print("PLATFORM ", end="")
print("4", end=" | ")
print("TRAIN 22")
print("Planned: ", end="")
print("150", end=" | ")
print("Actual: ", end="")
print("150")
print("Delay: ", end="")
print("0", end=" min | ")
print("READY")
```

פלט:

```text
PLATFORM 4 | TRAIN 22
Planned: 150 | Actual: 150
Delay: 0 min | READY
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
Arrival: 112
115 113 2
133 128 5
Total elapsed: 33
```

### ב. פלט התרחיש השני

```text
Arrival: 112
115 113 2
131 128 3
Total elapsed: 31
```

### ג. תשובות והערות לדיון

travel הוא זמן נסיעה ו-dwell זמן שהייה.

planned מייצג לוח קבוע שאינו משתנה בגלל איחור.

חישוב לפני העדכונים עלול לייצג נקודת זמן אחרת.

### ד. פתרון אפשרי

```python
actual = 80
planned = 80
actual += 9
planned += 8
actual += 4
planned += 2
print(actual, planned, actual - planned)
actual += 14
planned += 10
actual += 3
planned += 2
print(actual, planned, actual - planned)
print("Elapsed:", actual - 80)
```

פלט:

```text
93 90 3
110 102 8
Elapsed: 30
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Arrival: 112
Earliest: 115
Gap: 5
Time spent: 15
Planned gap: 10
```

### ב. פלט התרחיש השני

```text
Arrival: 105
Earliest: 107
Gap: -5
Time spent: 7
Planned gap: 12
```

### ג. תשובות והערות לדיון

Gap שלילי מציין שהרכבת יכולה לסיים שהייה מוקדם מהמתוכנן, אבל אסור לה לצאת לפני planned.

Earliest הוא זמן מוקדם אפשרי בלבד.

זמן השהייה כלול.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
100
12
3
110
8
2
130
```

```python
departure = int(input())
travel1 = int(input())
dwell1 = int(input())
planned1 = int(input())
travel2 = int(input())
dwell2 = int(input())
planned2 = int(input())
arrival1 = departure + travel1
earliest1 = arrival1 + dwell1
arrival2 = earliest1 + travel2
earliest2 = arrival2 + dwell2
print("Station 1:", arrival1, earliest1, earliest1 - planned1)
print("Station 2:", arrival2, earliest2, earliest2 - planned2)
```

פלט:

```text
Station 1: 112 115 5
Station 2: 123 125 -5
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
WAIT 3
112 0
DEPART
128 3
```

### ב. פלט התרחיש השני

```text
DEPART
114 2
DEPART
130 5
```

### ג. תשובות והערות לדיון

זמן יציאה בפועל קובע את ההגעה הבאה.

בגבול מתבצע DEPART ללא המתנה.

actual כבר שווה לזמן הכולל ולכן הוספה תכפיל את ההמתנה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
107
2
112
```

```python
arrival = int(input())
dwell = int(input())
planned = int(input())
if arrival < 0 or dwell < 0 or planned < 0:
    print("ERROR")
else:
    earliest = arrival + dwell
    wait = 0
    if earliest < planned:
        wait = planned - earliest
        actual = planned
    else:
        actual = earliest
    print("Actual:", actual)
    print("Wait:", wait)
    print("Delay:", actual - planned)
    if actual == planned:
        print("ON TIME")
    else:
        print("LATE")
```

פלט:

```text
Actual: 112
Wait: 3
Delay: 0
ON TIME
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 112 0
2 127 2
3 140 0
4 154 2
Late: 2
Worst: 2
```

### ב. פלט התרחיש השני

```text
1 117 5
2 125 0
3 140 0
4 152 0
Late: 1
Worst: 5
```

### ג. תשובות והערות לדיון

מונה סופר כמה תחנות מאחרות, worst מתאר חומרת האיחור הגדול ביותר.

מרווח מתוכנן מאפשר התאוששות.

worst מצטבר לאורך המסלול.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
3
100
7
2
112
13
3
125
6
2
140
```

```python
count = int(input())
actual = int(input())
total_wait = 0
on_time = 0
for i in range(count):
    travel = int(input())
    dwell = int(input())
    planned = int(input())
    earliest = actual + travel + dwell
    if earliest < planned:
        total_wait += planned - earliest
        actual = planned
    else:
        actual = earliest
    if actual == planned:
        on_time += 1
    print(i + 1, actual, actual - planned)
print("Wait:", total_wait)
print("On time:", on_time)
```

פלט:

```text
1 112 0
2 128 3
3 140 0
Wait: 7
On time: 2
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[112, 127, 140, 154, 162]
[0, 2, 0, 2, 0]
[2, 4]
```

### ב. פלט התרחיש השני

```text
[114, 129, 140, 154, 162]
[2, 4, 0, 2, 0]
[1, 2, 4]
```

### ג. תשובות והערות לדיון

כל אינדקס מייצג תחנה אחת.

late_stations[0] אם הרשימה אינה ריקה מציין איחור ראשון.

אורכים שונים דורשים בדיקה לפני הלולאה.

### ד. פתרון אפשרי

```python
travels = [7, 13, 8, 12, 5]
plans = [112, 125, 140, 152, 162]
actual = 100
departures = []
delays = []
waits = []
late_count = 0
wait_count = 0
for i in range(len(travels)):
    earliest = actual + travels[i] + 2
    wait = 0
    if earliest < plans[i]:
        wait = plans[i] - earliest
        actual = plans[i]
        wait_count += 1
    else:
        actual = earliest
    delay = actual - plans[i]
    if delay > 0:
        late_count += 1
    departures.append(actual)
    delays.append(delay)
    waits.append(wait)
print(departures)
print(delays)
print(waits)
print(late_count, wait_count)
```

פלט:

```text
[112, 127, 140, 154, 162]
[0, 2, 0, 2, 0]
[3, 0, 3, 0, 1]
2 3
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
112
127
[0, 2, 0, 2]
[2, 4, 0, 2]
```

### ב. פלט התרחיש השני

```text
112
127
[0, 4, 1, 5]
[4, 8, 5, 9]
```

### ג. תשובות והערות לדיון

departure מחזירה זמן יחיד, line רשימת איחורים.

אפשר לבדוק מקרים מוקדם, שווה ומאוחר בלי מסלול שלם.

מסלול עם מרווח מאוחר גדול מאפשר לאפס איחור.

### ד. פתרון אפשרי

```python
def departure(arrival, dwell, planned):
    earliest = arrival + dwell
    if earliest < planned:
        return planned
    return earliest

def line(travels, dwells, plans, start):
    delays = []
    if len(travels) != len(dwells) or len(dwells) != len(plans):
        return delays
    actual = start
    for i in range(len(travels)):
        actual = departure(actual + travels[i], dwells[i], plans[i])
        delays.append(actual - plans[i])
    return delays

print(line([7, 13, 8], [2, 2, 2], [112, 125, 140], 100))
print(line([7, 13, 8], [5, 4, 2], [112, 125, 140], 100))
print(line([7], [], [112], 100))
```

פלט:

```text
[0, 2, 0]
[0, 4, 0]
[]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
0
2
2
4
0
0
140 6 [0, 2, 0]
140 1 [2, 4, 0]
```

### ב. פלט התרחיש השני

```text
0
7
2
9
0
4
140 6 [0, 2, 0]
144 0 [7, 9, 4]
```

### ג. תשובות והערות לדיון

actual,delays,total_wait נשמרים לכל אובייקט.

רשימה משותפת תערבב היסטוריות.

אפשר להוסיף פעולה שמחשבת earliest וזמן מתוכנן בלי השמה ל-self.

### ד. פתרון אפשרי

```python
class Train:
    def __init__(self, start):
        self.actual = start
        self.delays = []
        self.total_wait = 0

    def station(self, travel, dwell, planned):
        earliest = self.actual + travel + dwell
        if earliest < planned:
            self.total_wait += planned - earliest
            self.actual = planned
        else:
            self.actual = earliest
        delay = self.actual - planned
        self.delays.append(delay)
        return delay

    def last_delay(self):
        if len(self.delays) == 0:
            return 0
        return self.delays[len(self.delays) - 1]

    def count_late(self):
        count = 0
        for d in self.delays:
            if d > 0:
                count += 1
        return count

a = Train(100)
b = Train(105)
print(a.last_delay(), b.count_late())
print(a.station(7, 2, 112))
print(b.station(7, 2, 112))
print(a.station(13, 2, 125))
print(b.station(13, 2, 125))
print(a.station(8, 2, 140))
print(b.station(8, 2, 140))
print(a.actual, a.total_wait, a.delays)
print(b.actual, b.total_wait, b.delays)
print(a.last_delay(), a.count_late())
print(b.last_delay(), b.count_late())
```

פלט:

```text
0 0
0
2
2
4
0
0
140 6 [0, 2, 0]
140 1 [2, 4, 0]
0 1
0 2
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

# פתרונות למורה: לוויין תקשורת: מה קורה כשהקשר נקטע?

[חזרה למשימת התלמיד](../20_satellite_communication.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
LINK A | SIM
Queue: 4 / 5
Rate: 2 msgs
Status: ONLINE | Window 3
```

### ב. פלט התרחיש השני

```text
LINK  | A | SIM
Queue: 4 / 5
Rate: 2 msgs
Status: ONLINE | Window 3
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("LINK ", end="")
print("B", end="")
print(" | SIM")
print("Queue: ", end="")
print("5", end="")
print(" / 5")
print("Rate: ", end="")
print("0", end="")
print(" msgs")
print("Status: ", end="")
print("OFFLINE", end="")
print(" | Window 8")
```

פלט:

```text
LINK B | SIM
Queue: 5 / 5
Rate: 0 msgs
Status: OFFLINE | Window 8
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
2 3 1
4 5 1
2 6 4
Check: 2
Total: 6
```

### ב. פלט התרחיש השני

```text
2 3 1
4 5 1
1 6 5
Check: 1
Total: 6
```

### ג. תשובות והערות לדיון

תחילה קליטה ואז שליחה.

received=waiting+sent כאשר אין דחיות.

בקשר מנותק אין שליחה.

קצב הוא גבול ולא מספר שנשלח בפועל.

### ד. פתרון אפשרי

```python
waiting = 0
received = 0
sent = 0
waiting += 2
received += 2
waiting -= 1
sent += 1
print(waiting, received, sent)
waiting += 3
received += 3
print(waiting, received, sent)
waiting += 1
received += 1
waiting -= 3
sent += 3
print(waiting, received, sent)
print(received, waiting + sent)
```

פלט:

```text
1 2 1
4 5 1
2 6 4
6 6
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Before send 1: 5 0
After send 1: 3
Before send 2: 6 -1
After send 2: 4
Totals: 6 4
Check: 4
```

### ב. פלט התרחיש השני

```text
Before send 1: 7 -2
After send 1: 3
Before send 2: 6 -1
After send 2: 4
Totals: 6 6
Check: 4
```

### ג. תשובות והערות לדיון

הסדר משפיע על עומס התור.

מקום פנוי שלילי מעיד על חריגה לפני השידור.

מצב סופי חוקי יכול להסתיר חריגה זמנית.

שליחה ללא תנאי עלולה להוביל לתור שלילי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
2
2
1
3
0
2
4
```

```python
capacity = int(input())
waiting = int(input())
a1 = int(input())
r1 = int(input())
a2 = int(input())
r2 = int(input())
a3 = int(input())
r3 = int(input())
waiting += a1
print(waiting, capacity - waiting)
waiting -= r1
print(waiting)
waiting += a2
print(waiting, capacity - waiting)
waiting -= r2
print(waiting)
waiting += a3
print(waiting, capacity - waiting)
waiting -= r3
print(waiting)
print(a1 + a2 + a3, r1 + r2 + r3)
```

פלט:

```text
4 1
3
6 -1
6
8 -3
4
7 5
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
Accepted: 1
Dropped: 2
Sent: 2
Waiting: 3
PENDING
```

### ב. פלט התרחיש השני

```text
Accepted: 1
Dropped: 2
Sent: 5
Waiting: 0
EMPTY
```

### ג. תשובות והערות לדיון

המודל מגדיר סדר אירועים.

sent מוגבל לפי התור.

dropped הן בקשות שהגיעו אך לא התקבלו.

שינוי הסדר עשוי לפנות מקום להודעות נוספות ולשנות מה נדחה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
4
3
2
```

```python
capacity = int(input())
waiting = int(input())
arrivals = int(input())
rate = int(input())
initial = waiting
if arrivals < 0 or rate < 0:
    print("INVALID")
else:
    accepted = arrivals
    if accepted > capacity - waiting:
        accepted = capacity - waiting
    dropped = arrivals - accepted
    waiting += accepted
    sent = rate
    if sent > waiting:
        sent = waiting
    waiting -= sent
    print(accepted, dropped, sent, waiting)
    print(initial + accepted, sent + waiting)
```

פלט:

```text
1 2 2 3
5 5
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 3 0 1 2
2 3 1 0 5
3 0 2 2 3
4 INVALID
5 2 1 1 4
6 0 0 4 0
8 4 8
1 1 0
Check: 0
```

### ב. פלט התרחיש השני

```text
1 3 0 1 2
2 3 1 3 2
3 2 0 2 2
4 INVALID
5 3 0 1 4
6 0 0 4 0
11 1 11
0 1 0
Check: 0
```

### ג. תשובות והערות לדיון

ניתוק הוא תכונת חלון;

דחייה נובעת מקיבולת.

accepted_total=sent_total+waiting כאשר התחלה 0.

קלט שגוי לא מעדכן את המצב.

צריך למדוד לפני הפחתת sent.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
5
2
3
1
4
0
2
2
-1
4
0
5
```

```python
count = int(input())
capacity = int(input())
waiting = int(input())
initial = waiting
accepted_total = 0
dropped_total = 0
sent_total = 0
peak = waiting
full = 0
for i in range(count):
    arrivals = int(input())
    rate = int(input())
    if arrivals >= 0 and rate >= 0:
        accepted = arrivals
        if accepted > capacity - waiting:
            accepted = capacity - waiting
        waiting += accepted
        accepted_total += accepted
        dropped_total += arrivals - accepted
        if waiting > peak:
            peak = waiting
        if waiting == capacity:
            full += 1
        sent = rate
        if sent > waiting:
            sent = waiting
        waiting -= sent
        sent_total += sent
        print(i + 1, waiting)
print(peak, full, dropped_total)
print(initial + accepted_total, sent_total + waiting)
```

פלט:

```text
1 4
2 5
3 3
5 0
5 3 5
6 6
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
1 1 0
2 2 0
3 3 0
4 4 0
5 5 0
6 3 2
7 3 1
8 0 4
[101, 102, 103, 104, 105, 107, 108]
[106]
[]
Check: 8
```

### ב. פלט התרחיש השני

```text
1 1 0
2 2 0
3 3 0
4 4 0
5 4 1
6 3 2
7 3 1
8 2 2
[101, 102, 103, 104, 105, 106]
[]
[107, 108]
Check: 8
```

### ג. תשובות והערות לדיון

first מציין גבול בין היסטוריה לתור.

מספר הממתינות הוא len(buffer)-first.

שליפה מהאינדקס הבא משמרת סדר.

רשימה יכולה לגדול למרות תור קצר, ולכן ביישום ארוך נדרש ניקוי מבוקר.

### ד. פתרון אפשרי

```python
arrivals = [101, 102, 103, 104, 105, 106, 107, 108]
rates = [0, 0, 0, 0, 0, 2, 1, 5]
buffer = []
sent = []
windows = []
dropped = []
first = 0
for i in range(len(arrivals)):
    if len(buffer) - first < 5:
        buffer.append(arrivals[i])
    else:
        dropped.append(arrivals[i])
    count = 0
    while count < rates[i] and first < len(buffer):
        sent.append(buffer[first])
        windows.append(i + 1)
        first += 1
        count += 1
pending = []
for i in range(len(buffer)):
    if i >= first:
        pending.append(buffer[i])
print(sent)
print(windows)
print(dropped)
print(pending)
print(len(sent) + len(dropped) + len(pending))
```

פלט:

```text
[101, 102, 103, 104, 105, 107, 108]
[6, 6, 7, 8, 8, 8, 8]
[106]
[]
8
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[[11, 12, 13, 15], [14], 0]
[[11, 12, 15], [13, 14], 0]
[[], [], 0]
```

### ב. פלט התרחיש השני

```text
[[11, 12, 13, 14, 15], [], 0]
[[11, 12, 13, 15], [14], 0]
[[], [], 0]
```

### ג. תשובות והערות לדיון

התנאי השגוי מאפשר להכניס הודעה מעל הקיבולת.

receive משנה buffer, transmit מוסיפה ל-sent;

first מספר ולכן צריך לעדכנו מהחזרה.

תוצאה ריקה עלולה להתפרש כסימולציה תקינה.

### ד. פתרון אפשרי

```python
def receive(buffer, first, message, capacity):
    if len(buffer) - first >= capacity:
        return False
    buffer.append(message)
    return True

def transmit(buffer, first, rate, sent):
    count = 0
    while count < rate and first < len(buffer):
        sent.append(buffer[first])
        first += 1
        count += 1
    return first

def simulate(arrivals, rates, capacity):
    if len(arrivals) != len(rates) or capacity <= 0:
        return ["ERROR", [], [], []]
    for rate in rates:
        if rate < 0:
            return ["ERROR", [], [], []]
    buffer = []
    sent = []
    dropped = []
    first = 0
    for i in range(len(arrivals)):
        if not receive(buffer, first, arrivals[i], capacity):
            dropped.append(arrivals[i])
        first = transmit(buffer, first, rates[i], sent)
    pending = []
    for i in range(len(buffer)):
        if i >= first:
            pending.append(buffer[i])
    return ["OK", sent, dropped, pending]

print(simulate([11, 12, 13, 14, 15], [0, 0, 0, 1, 4], 3))
print(simulate([11, 12], [1, -1], 3))
```

פלט:

```text
['OK', [11, 12, 13, 15], [14], []]
['ERROR', [], [], []]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
1 0 0
2 0 1
3 1 0
4 2 3
[101, 102, 104] [103] 0
[101, 102, 103, 104] [] 0
```

### ב. פלט התרחיש השני

```text
1 0 0
2 0 1
3 1 0
4 3 3
[101, 102, 103, 104] [] 0
[101, 102, 103, 104] [] 0
```

### ג. תשובות והערות לדיון

כל ערוץ עצמאי, עם קיבולת וקצב שונים.

Station מתאמת חלונות;

Channel מנהלת את התור.

כאן שתי שליחות מכוונות לשני ערוצים, לא כפילות בתוך ערוץ אחד.

משנים rate_left בלבד.

### ד. פתרון אפשרי

```python
class Channel:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.first = 0
        self.sent = []
        self.dropped = []

    def pending(self):
        return len(self.buffer) - self.first

    def snapshot(self):
        return [len(self.sent), len(self.dropped), self.pending()]

    def receive(self, message):
        if self.pending() >= self.capacity:
            self.dropped.append(message)
            return False
        self.buffer.append(message)
        return True

    def transmit(self, rate):
        count = 0
        while count < rate and self.first < len(self.buffer):
            self.sent.append(self.buffer[self.first])
            self.first += 1
            count += 1
        return count

class Station:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.windows = 0
        self.both = 0

    def tick(self, message, rate_left, rate_right):
        self.windows += 1
        accepted_left = self.left.receive(message)
        accepted_right = self.right.receive(message)
        if accepted_left and accepted_right:
            self.both += 1
        print(self.windows, self.left.transmit(rate_left), self.right.transmit(rate_right))

a = Channel(2)
b = Channel(4)
station = Station(a, b)
station.tick(101, 0, 0)
station.tick(102, 0, 1)
station.tick(103, 1, 0)
station.tick(104, 3, 3)
print(a.sent, a.dropped, a.pending())
print(b.sent, b.dropped, b.pending())
print(a.snapshot(), b.snapshot())
print(station.both, station.windows)
```

פלט:

```text
1 0 0
2 0 1
3 1 0
4 2 3
[101, 102, 104] [103] 0
[101, 102, 103, 104] [] 0
[3, 1, 0] [4, 0, 0]
3 4
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

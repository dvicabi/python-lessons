# פתרונות למורה: שרת אינטרנט: איך מנהלים תור תחת עומס?

[חזרה למשימת התלמיד](../27_web_server.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
SERVER S1 | SIM
Queue: 4 / 6
Rate: 2 jobs
Done: 15 total
State: BUSY | OK
```

### ב. פלט התרחיש השני

```text
SERVER  | S1 | SIM
Queue: 4 / 6
Rate: 2 jobs
Done: 15 total
State: BUSY | OK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("SERVER ", end="")
print("S2", end="")
print(" | SIM")
print("Queue: ", end="")
print("6", end="")
print(" / 6")
print("Rate: ", end="")
print("0", end="")
print(" jobs")
print("Done: ", end="")
print("20", end="")
print(" total")
print("State: ", end="")
print("FULL", end="")
print(" | WAIT")
```

פלט:

```text
SERVER S2 | SIM
Queue: 6 / 6
Rate: 0 jobs
Done: 20 total
State: FULL | WAIT
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
Before: 5
3 3 2
Before: 5
4 5 3
Before: 5
1 6 7
Check: 1
```

### ב. פלט התרחיש השני

```text
Before: 5
3 3 2
Before: 5
4 5 3
Before: 5
2 6 6
Check: 2
```

### ג. תשובות והערות לדיון

waiting הוא מצב רגעי, accepted מצטבר.

2+accepted=waiting+done.

לפני עיבוד אפשר לזהות עומס זמני.

השמה מוחקת עבודה קודמת.

### ד. פתרון אפשרי

```python
waiting = 1
accepted = 0
done = 0
waiting += 3
accepted += 3
print(waiting)
waiting -= 2
done += 2
print(waiting, accepted, done)
waiting += 2
accepted += 2
print(waiting)
waiting -= 1
done += 1
print(waiting, accepted, done)
waiting += 1
accepted += 1
print(waiting)
waiting -= 3
done += 3
print(waiting, accepted, done)
print(1 + accepted, waiting + done)
```

פלט:

```text
4
2 3 2
4
3 5 3
4
1 6 6
7 7
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Before 1: 5 1
After 1: 3
Before 2: 5 1
After 2: 4
Totals: 5 3
Check: 4
```

### ב. פלט התרחיש השני

```text
Before 1: 6 -2
After 1: 2
Before 2: 4 0
After 2: 3
Totals: 5 5
Check: 3
```

### ג. תשובות והערות לדיון

מקום שלילי הוא חריגה.

עיבוד מאוחר יכול להסתיר חריגה זמנית.

rate הוא גבול עליון.

ברמה הבאה מוסיפים תנאים לבדיקת חוקיות.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
1
3
2
2
1
1
3
```

```python
capacity = int(input())
waiting = int(input())
initial = waiting
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
print(initial + a1 + a2 + a3, waiting + r1 + r2 + r3)
```

פלט:

```text
4 2
2
4 2
3
4 2
1
7 7
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
Accepted: 1
Rejected: 3
Done: 3
Waiting: 3
BUSY
Peak: 6
Check: 6 6
```

### ב. פלט התרחיש השני

```text
Accepted: 1
Rejected: 3
Done: 6
Waiting: 0
EMPTY
Peak: 6
Check: 6 6
```

### ג. תשובות והערות לדיון

הסדר קובע כמה מקום פנוי לקליטה.

קבלה ללא הגבלה מפרה קיבולת.

אפשר לעבד רק ממתינים.

דחויים אינם בתור ולכן מאזן מתחיל בקליטות שאושרו.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
5
4
8
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
    rejected = arrivals - accepted
    waiting += accepted
    peak = waiting
    done = rate
    if done > waiting:
        done = waiting
    waiting -= done
    print("Accepted:", accepted)
    print("Rejected:", rejected)
    print("Done:", done)
    print("Waiting:", waiting)
    if rate == 0:
        print("OFFLINE")
    elif waiting == 0:
        print("EMPTY")
    else:
        print("BUSY")
    print("Peak:", peak)
    print("Free:", capacity - waiting)
    print("Arrival check:", accepted + rejected)
    print("Check:", initial + accepted, waiting + done)
```

פלט:

```text
Accepted: 1
Rejected: 3
Done: 6
Waiting: 0
EMPTY
Peak: 6
Free: 6
Arrival check: 4
Check: 6 6
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 4 0 1 3
2 3 2 0 6
3 0 2 2 4
4 INVALID
5 2 1 3 3
6 1 0 0 4
7 0 0 4 0
10 5 10
2 1 6 0
Check: 0
```

### ב. פלט התרחיש השני

```text
1 4 0 4 0
2 5 0 0 5
3 1 1 2 4
4 INVALID
5 2 1 3 3
6 1 0 0 4
7 0 0 4 0
13 2 13
2 1 6 0
Check: 0
```

### ג. תשובות והערות לדיון

שיא לפני עיבוד כולל את העומס המרבי.

ניתוק לא בהכרח ממלא את התור.

קלט שגוי אינו אירוע עסקי.

peak==capacity מציין מילוי.

איפוס מאבד היסטוריה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
7
4
1
5
0
2
2
-1
1
3
3
1
0
0
4
```

```python
capacity = int(input())
count = int(input())
full_windows = 0
empty_windows = 0
waiting = 0
accepted_total = 0
rejected_total = 0
done_total = 0
offline = 0
invalid = 0
peak = 0
for i in range(count):
    arrivals = int(input())
    rate = int(input())
    if arrivals < 0 or rate < 0:
        invalid += 1
        print(i + 1, "INVALID")
    else:
        accepted = arrivals
        if accepted > capacity - waiting:
            accepted = capacity - waiting
        waiting += accepted
        rejected = arrivals - accepted
        if waiting == capacity:
            full_windows += 1
        if waiting > peak:
            peak = waiting
        done = rate
        if done > waiting:
            done = waiting
        waiting -= done
        if waiting == 0:
            empty_windows += 1
        accepted_total += accepted
        rejected_total += rejected
        done_total += done
        if rate == 0:
            offline += 1
        print(i + 1, accepted, rejected, done, waiting)
print(accepted_total, rejected_total, done_total)
print(offline, invalid, peak, waiting)
print("Check:", accepted_total - done_total)
print(full_windows, empty_windows)
```

פלט:

```text
1 4 0 1 3
2 3 2 0 6
3 0 2 2 4
4 INVALID
5 2 1 3 3
6 1 0 0 4
7 0 0 4 0
10 5 10
2 1 6 0
Check: 0
3 1
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
1 1 0 1
2 2 0 2
3 3 0 3
4 4 0 4
5 4 2 2
6 3 1 2
7 3 0 3
8 4 2 2
9 3 3 0
[101, 102, 103, 104, 106, 107, 108, 109]
[105]
[]
[[1, 1], [2, 2], [3, 3], [4, 4], [4, 2], [3, 2], [3, 3], [4, 2], [3, 0]]
Check: 9
```

### ב. פלט התרחיש השני

```text
1 1 0 1
2 2 0 2
3 3 0 3
4 4 1 3
5 4 2 2
6 3 1 2
7 3 0 3
8 4 2 2
9 3 3 0
[101, 102, 103, 104, 105, 106, 107, 108, 109]
[]
[]
[[1, 1], [2, 2], [3, 3], [4, 3], [4, 2], [3, 2], [3, 3], [4, 2], [3, 0]]
Check: 9
```

### ג. תשובות והערות לדיון

first מפריד בין היסטוריה לתור.

עיבוד מגדיל אותו.

דחוי לא התקבל.

רשימה יכולה לגדול למרות תור קצר;

יש לתכנן ניקוי.

בודקים מאזן ואי-כפילות מזהים.

### ד. פתרון אפשרי

```python
arrivals = [101, 102, 103, 104, 105, 106, 107, 108, 109]
rates = [0, 0, 0, 0, 2, 1, 0, 2, 5]
capacity = 4
queue = []
first = 0
processed = []
windows = []
full = 0
rejected = []
waiting_log = []
for i in range(len(arrivals)):
    if len(queue) - first < capacity:
        queue.append(arrivals[i])
    else:
        rejected.append(arrivals[i])
    before = len(queue) - first
    if before == capacity:
        full += 1
    done = 0
    while done < rates[i] and first < len(queue):
        processed.append(queue[first])
        windows.append(i + 1)
        first += 1
        done += 1
    after = len(queue) - first
    waiting_log.append([before, after])
    print(i + 1, before, done, after)
pending = []
for j in range(len(queue)):
    if j >= first:
        pending.append(queue[j])
print(processed)
print(rejected)
print(pending)
print(waiting_log)
print(windows, full)
print("Check:", len(processed) + len(rejected) + len(pending))
```

פלט:

```text
1 1 0 1
2 2 0 2
3 3 0 3
4 4 0 4
5 4 2 2
6 3 1 2
7 3 0 3
8 4 2 2
9 3 3 0
[101, 102, 103, 104, 106, 107, 108, 109]
[105]
[]
[[1, 1], [2, 2], [3, 3], [4, 4], [4, 2], [3, 2], [3, 3], [4, 2], [3, 0]]
[5, 5, 6, 8, 8, 9, 9, 9] 3
Check: 9
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
['OK', [1, 2, 3, 5], [4], [6]]
['OK', [], [3], [1, 2]]
['ERROR', [], [], []]
```

### ב. פלט התרחיש השני

```text
['OK', [1, 2, 3, 4], [], [5, 6]]
['OK', [], [], [1, 2, 3]]
['ERROR', [], [], []]
```

### ג. תשובות והערות לדיון

שוויון לקיבולת חייב לדחות.

first מספר ולכן מחזירים חדש.

arrivals רק נקראת.

יש לאמת קצבים לפני עיבוד.

ERROR מציין קלט פסול.

### ד. פתרון אפשרי

```python
def receive(queue, first, message, capacity):
    if len(queue) - first >= capacity:
        return False
    queue.append(message)
    return True

def process(queue, first, rate, processed):
    count = 0
    while count < rate and first < len(queue):
        processed.append(queue[first])
        first += 1
        count += 1
    return first

def simulate(arrivals, rates, capacity):
    if len(arrivals) != len(rates) or capacity <= 0:
        return ["ERROR", [], [], []]
    for rate in rates:
        if rate < 0:
            return ["ERROR", [], [], []]
    queue = []
    rejected = []
    processed = []
    first = 0
    for i in range(len(arrivals)):
        if not receive(queue, first, arrivals[i], capacity):
            rejected.append(arrivals[i])
        first = process(queue, first, rates[i], processed)
    pending = []
    for i in range(len(queue)):
        if i >= first:
            pending.append(queue[i])
    return ["OK", processed, rejected, pending, len(arrivals), len(queue)]

print(simulate([1, 2, 3, 4, 5, 6], [0, 0, 0, 1, 2, 1], 3))
print(simulate([1, 2, 3], [0, 0, 0], 2))
print(simulate([1], [], 3))
print(simulate([1, 2], [1, -1], 3))
```

פלט:

```text
['OK', [1, 2, 3, 5], [4], [6], 6, 5]
['OK', [], [3], [1, 2], 3, 2]
['ERROR', [], [], []]
['ERROR', [], [], []]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
11 0
12 1
13 0
14 1
15 1
16 -1
[[2, 0, 2], [3, 0, 3]]
1 2
0
1
[[11, 0], [12, 1], [13, 0], [14, 1], [15, 1], [16, -1], [17, 0], [18, 1]]
[16]
[11] [12, 14]
[[2, 1, 2], [2, 2, 3]]
```

### ב. פלט התרחיש השני

```text
11 0
12 1
13 0
14 1
15 0
16 1
[[3, 0, 3], [3, 0, 3]]
1 2
1
0
[[11, 0], [12, 1], [13, 0], [14, 1], [15, 0], [16, 1], [17, 1], [18, 0]]
[]
[11] [12, 14]
[[3, 1, 3], [2, 2, 3]]
```

### ג. תשובות והערות לדיון

סריקה מחפשת מועמד בלבד;

רק אחרי הבחירה מתבצעת קליטה.

שוויון משאיר ראשון.

-1 הוא דחייה.

reports רק קוראת מצב.

בודקים מזהים ייחודיים והקצאה אחת לכל submit.

### ד. פתרון אפשרי

```python
class Server:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.first = 0
        self.done = []

    def pending(self):
        return len(self.queue) - self.first

    def available(self):
        return self.pending() < self.capacity

    def receive(self, message):
        if not self.available():
            return False
        self.queue.append(message)
        return True

    def process(self, rate):
        count = 0
        while count < rate and self.first < len(self.queue):
            self.done.append(self.queue[self.first])
            self.first += 1
            count += 1
        return count

    def report(self):
        return [self.pending(), len(self.done), self.capacity]

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.history = []
        self.rejected = []
        self.accepted = 0

    def submit(self, message):
        best = -1
        for i in range(len(self.servers)):
            server = self.servers[i]
            if server.available():
                if best == -1 or server.pending() < self.servers[best].pending():
                    best = i
        if best == -1:
            self.rejected.append(message)
        else:
            self.servers[best].receive(message)
            self.accepted += 1
        self.history.append([message, best])
        return best

    def balance(self):
        pending = 0
        done = 0
        for server in self.servers:
            pending += server.pending()
            done += len(server.done)
        return [self.accepted, len(self.rejected), pending, done]

    def reports(self):
        result = []
        for server in self.servers:
            result.append(server.report())
        return result

a = Server(2)
b = Server(3)
lab = LoadBalancer([a, b])
for message in [11, 12, 13, 14, 15, 16]:
    print(message, lab.submit(message))
print(lab.reports())
print(lab.balance())
print(a.process(1), b.process(2))
print(lab.balance())
print(lab.submit(17))
print(lab.submit(18))
print(lab.history)
print(lab.rejected)
print(a.done, b.done)
print(lab.balance())
print(lab.reports())
```

פלט:

```text
11 0
12 1
13 0
14 1
15 1
16 -1
[[2, 0, 2], [3, 0, 3]]
[5, 1, 5, 0]
1 2
[5, 1, 2, 3]
0
1
[[11, 0], [12, 1], [13, 0], [14, 1], [15, 1], [16, -1], [17, 0], [18, 1]]
[16]
[11] [12, 14]
[7, 1, 4, 3]
[[2, 1, 2], [2, 2, 3]]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

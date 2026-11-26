# פתרונות למורה: וואטסאפ מדומה: האם מספר ההתראות שווה למספר ההודעות שלא נקראו?

[חזרה למשימת התלמיד](../29_whatsapp_unread.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
CHAT A | SIM
Unread: 5 messages
Received: 12 total
Alerts: 7 total
State: MUTED | READY
```

### ב. פלט התרחיש השני

```text
CHAT  | A | SIM
Unread: 5 messages
Received: 12 total
Alerts: 7 total
State: MUTED | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("CHAT ", end="")
print("B", end="")
print(" | SIM")
print("Unread: ", end="")
print("0", end="")
print(" messages")
print("Received: ", end="")
print("9", end="")
print(" total")
print("Alerts: ", end="")
print("9", end="")
print(" total")
print("State: ", end="")
print("SOUND", end="")
print(" | READ")
```

פלט:

```text
CHAT B | SIM
Unread: 0 messages
Received: 9 total
Alerts: 9 total
State: SOUND | READ
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
4 4 0 4
2 4 2 4
5 7 2 4
1 7 6 4
3 9 6 6
Check: 3
Silent arrivals: 3
```

### ב. פלט התרחיש השני

```text
4 4 0 4
2 4 2 4
7 9 2 4
3 9 6 4
5 11 6 6
Check: 5
Silent arrivals: 5
```

### ג. תשובות והערות לדיון

חלק מהקבלות בשיחה מושתקת.

unread=received-read_total.

alerts מתארת התראות היסטוריות.

ההפרש הוא הודעות שנקלטו בזמן השתקה.

### ד. פתרון אפשרי

```python
unread = 0
received = 0
read_total = 0
alerts = 0
unread += 5
received += 5
alerts += 5
print(unread, received, read_total, alerts)
unread -= 2
read_total += 2
print(unread, received, read_total, alerts)
unread += 4
received += 4
print(unread, received, read_total, alerts)
unread -= 3
read_total += 3
print(unread, received, read_total, alerts)
unread += 1
received += 1
alerts += 1
print(unread, received, read_total, alerts)
print(received - read_total, unread)
```

פלט:

```text
5 5 0 5
3 5 2 5
7 9 2 5
4 9 5 5
5 10 5 6
5 5
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 5 5
B: 0 0
C: 4 6
Total: 9
Check: 9
Alerts: 16
```

### ב. פלט התרחיש השני

```text
A: 7 5
B: 0 0
C: 4 2
Total: 11
Check: 11
Alerts: 20
```

### ג. תשובות והערות לדיון

unread שלילי מפר מאזן.

התראות הן אירועים היסטוריים.

received-alerts מייצג הודעות שנקלטו בהשתקה.

מצב השתקה נוכחי דורש דגל נפרד.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
12
7
7
9
9
9
```

```python
a_received = int(input())
a_read = int(input())
a_alerts = int(input())
b_received = int(input())
b_read = int(input())
b_alerts = int(input())
a_unread = a_received - a_read
b_unread = b_received - b_read
print(a_unread, a_received - a_alerts)
print(b_unread, b_received - b_alerts)
print(a_received + b_received, a_read + b_read, a_alerts + b_alerts)
print(a_unread - b_unread)
```

פלט:

```text
5 5
0 0
21 16 16
5
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
READ 5
0 12 12 7
Check: 0
CLEAR
```

### ב. פלט התרחיש השני

```text
RECEIVED
13 20 7 7
Check: 13
PENDING
```

### ג. תשובות והערות לדיון

קריאה אינה יכולה לקרוא יותר מהממתינות.

השתקה היא מדיניות התראות.

פעולה 3 ללא כמות;

כמות חיובית נדרשת לקריאה וקבלה.

קבלה מושתקת לא מגדילה alerts.

כל המונים והדגל נשמרים באירוע שגוי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
2
10
```

```python
unread = 5
received = 12
read_total = 7
alerts = 7
muted = True
kind = int(input())
amount = int(input())
actual_read = 0
actual_alerts = 0
if kind == 1 and amount > 0:
    unread += amount
    received += amount
    if not muted:
        alerts += amount
        actual_alerts = amount
    print("RECEIVED")
elif kind == 2 and amount > 0:
    actual = amount
    if actual > unread:
        actual = unread
    unread -= actual
    read_total += actual
    actual_read = actual
    print("READ", actual)
elif kind == 3 and amount == 0:
    muted = not muted
    print("MUTE", muted)
else:
    print("INVALID")
print(unread, received, read_total, alerts)
print("Check:", received - read_total)
print(actual_read, actual_alerts)
if unread == 0:
    print("CLEAR")
else:
    print("PENDING")
```

פלט:

```text
READ 5
0 12 12 7
Check: 0
5 0
CLEAR
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 RECEIVED 4 4 False
2 MUTE 4 4 True
3 RECEIVED 7 4 True
4 READ 5 4 True
5 READ 0 4 True
6 READ 0 4 True
7 MUTE 0 4 False
8 RECEIVED 5 9 False
9 INVALID 5 9 False
12 7 5
7 2 1
Check: 5
```

### ב. פלט התרחיש השני

```text
1 RECEIVED 4 4 False
2 MUTE 4 4 True
3 RECEIVED 7 4 True
4 READ 5 4 True
5 READ 0 4 True
6 READ 0 4 True
7 INVALID 0 4 True
8 RECEIVED 5 4 True
9 INVALID 5 4 True
12 7 5
7 1 2
Check: 5
```

### ג. תשובות והערות לדיון

peak שיא היסטורי.

החלפת בוליאן פעמיים מחזירה מצב.

ההגבלה על actual מונעת שלילי.

אירוע יכול לקרוא כמה הודעות.

alerts הוא מונה היסטורי ולא תג נוכחי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
9
1
4
3
0
1
3
2
2
2
9
2
1
3
0
1
5
9
0
```

```python
count = int(input())
unread = 0
received_while_muted = 0
empty_reads = 0
received = 0
read_total = 0
alerts = 0
muted = False
invalid = 0
peak = 0
mute_changes = 0
for i in range(count):
    kind = int(input())
    amount = int(input())
    if kind == 1 and amount > 0:
        unread += amount
        received += amount
        if not muted:
            alerts += amount
        else:
            received_while_muted += amount
        status = "RECEIVED"
    elif kind == 2 and amount > 0:
        actual = amount
        if actual > unread:
            actual = unread
        if actual == 0:
            empty_reads += 1
        unread -= actual
        read_total += actual
        status = "READ"
    elif kind == 3 and amount == 0:
        muted = not muted
        mute_changes += 1
        status = "MUTE"
    else:
        invalid += 1
        status = "INVALID"
    if unread > peak:
        peak = unread
    print(i + 1, status, unread, alerts, muted)
print(received, read_total, unread)
print(peak, mute_changes, invalid)
print("Check:", received - read_total)
print(received_while_muted, empty_reads)
print(received, alerts + received_while_muted)
```

פלט:

```text
1 RECEIVED 4 4 False
2 MUTE 4 4 True
3 RECEIVED 7 4 True
4 READ 5 4 True
5 READ 0 4 True
6 READ 0 4 True
7 MUTE 0 4 False
8 RECEIVED 5 9 False
9 INVALID 5 9 False
12 7 5
7 2 1
Check: 5
3 1
12 12
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
0 RECEIVED [5, 0] [False, False]
1 RECEIVED [5, 3] [False, False]
0 MUTE [5, 3] [True, False]
0 RECEIVED [9, 3] [True, False]
1 READ [9, 1] [True, False]
2 UNKNOWN [9, 1] [True, False]
0 READ [0, 1] [True, False]
1 MUTE [0, 1] [True, True]
1 RECEIVED [0, 3] [True, True]
[5, 3] [9, 5] [9, 2]
[[0, 'RECEIVED'], [1, 'RECEIVED'], [0, 'MUTE'], [0, 'RECEIVED'], [1, 'READ'], [2, 'UNKNOWN'], [0, 'READ'], [1, 'MUTE'], [1, 'RECEIVED']]
[True, True]
```

### ב. פלט התרחיש השני

```text
0 RECEIVED [5, 0] [False, False]
1 RECEIVED [5, 3] [False, False]
1 MUTE [5, 3] [False, True]
0 RECEIVED [9, 3] [False, True]
1 READ [9, 1] [False, True]
2 UNKNOWN [9, 1] [False, True]
0 READ [0, 1] [False, True]
1 MUTE [0, 1] [False, False]
1 RECEIVED [0, 3] [False, False]
[9, 5] [9, 5] [9, 2]
[[0, 'RECEIVED'], [1, 'RECEIVED'], [1, 'MUTE'], [0, 'RECEIVED'], [1, 'READ'], [2, 'UNKNOWN'], [0, 'READ'], [1, 'MUTE'], [1, 'RECEIVED']]
[True, True]
```

### ג. תשובות והערות לדיון

אינדקס שלילי יכול לפנות לשיחה שגויה.

כל שדה מייצג תכונה שונה.

אירועים מעדכנים את מצב אותה שיחה ברצף.

received-read_total=unread.

מסננים לפי unread>0.

### ד. פתרון אפשרי

```python
events = [[0, 1, 5], [1, 1, 3], [0, 3, 0], [0, 1, 4], [1, 2, 2], [2, 1, 8], [0, 2, 12], [1, 3, 0], [1, 1, 2]]
unread = [0, 0]
received = [0, 0]
read_total = [0, 0]
alerts = [0, 0]
muted = [False, False]
history = []
for event in events:
    chat = event[0]
    kind = event[1]
    amount = event[2]
    if chat < 0 or chat >= len(unread):
        status = "UNKNOWN"
    elif kind == 1 and amount > 0:
        unread[chat] += amount
        received[chat] += amount
        if not muted[chat]:
            alerts[chat] += amount
        status = "RECEIVED"
    elif kind == 2 and amount > 0:
        actual = amount
        if actual > unread[chat]:
            actual = unread[chat]
        unread[chat] -= actual
        read_total[chat] += actual
        status = "READ"
    elif kind == 3 and amount == 0:
        muted[chat] = not muted[chat]
        status = "MUTE"
    else:
        status = "INVALID"
    history.append([chat, status])
    print(chat, status, unread, muted)
checks = []
with_unread = []
muted_chats = []
total_unread = 0
total_alerts = 0
for i in range(len(unread)):
    checks.append(received[i] - read_total[i] == unread[i])
    if unread[i] > 0:
        with_unread.append(i)
    if muted[i]:
        muted_chats.append(i)
    total_unread += unread[i]
    total_alerts += alerts[i]
print(alerts, received, read_total)
print(history)
print(checks)
print(with_unread, muted_chats)
print(total_unread, total_alerts)
```

פלט:

```text
0 RECEIVED [5, 0] [False, False]
1 RECEIVED [5, 3] [False, False]
0 MUTE [5, 3] [True, False]
0 RECEIVED [9, 3] [True, False]
1 READ [9, 1] [True, False]
2 UNKNOWN [9, 1] [True, False]
0 READ [0, 1] [True, False]
1 MUTE [0, 1] [True, True]
1 RECEIVED [0, 3] [True, True]
[5, 3] [9, 5] [9, 2]
[[0, 'RECEIVED'], [1, 'RECEIVED'], [0, 'MUTE'], [0, 'RECEIVED'], [1, 'READ'], [2, 'UNKNOWN'], [0, 'READ'], [1, 'MUTE'], [1, 'RECEIVED']]
[True, True]
[1] [0, 1]
3 8
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[[0, False, 4, 4, 4], 'READ']
[[4, True, 8, 4, 5], ['RECEIVED', 'MUTE', 'RECEIVED', 'READ']]
[[0, True, 8, 8, 5], ['RECEIVED', 'MUTE', 'RECEIVED', 'READ']]
```

### ב. פלט התרחיש השני

```text
[[0, False, 4, 4, 4], 'READ']
[[4, True, 8, 4, 3], ['RECEIVED', 'MUTE', 'RECEIVED', 'READ']]
[[0, True, 8, 8, 3], ['RECEIVED', 'MUTE', 'RECEIVED', 'READ']]
```

### ג. תשובות והערות לדיון

צילום מצב חדש מאפשר לבדוק שינויים בלי לגעת בקלט.

השינוי מייצר התראות דווקא בהשתקה.

מדפיסים state לפני ואחרי.

update מרכזת כללים.

הבקשה 12 כשיש רק 8 מדגימה הגבלה.

### ד. פתרון אפשרי

```python
def update(state, kind, amount):
    unread = state[0]
    muted = state[1]
    received = state[2]
    read_total = state[3]
    alerts = state[4]
    if kind == 1 and amount > 0:
        unread += amount
        received += amount
        if not muted:
            alerts += amount
        status = "RECEIVED"
    elif kind == 2 and amount > 0:
        actual = amount
        if actual > unread:
            actual = unread
        unread -= actual
        read_total += actual
        status = "READ"
    elif kind == 3 and amount == 0:
        muted = not muted
        status = "MUTE"
    else:
        status = "INVALID"
    return [[unread, muted, received, read_total, alerts], status]

def audit(state):
    return state[0] >= 0 and state[2] - state[3] == state[0] and state[4] >= 0 and state[4] <= state[2]

def simulate(events):
    state = [0, False, 0, 0, 0]
    history = []
    checks = []
    for event in events:
        result = update(state, event[0], event[1])
        state = result[0]
        history.append(result[1])
        checks.append(audit(state))
    return [state, history, checks]

print(update([4, False, 4, 0, 4], 2, 9))
print(audit([5, False, 4, 0, 4]))
print(simulate([[1, 5], [3, 0], [1, 3], [2, 4]]))
print(simulate([[1, 5], [3, 0], [1, 3], [2, 12]]))
```

פלט:

```text
[[0, False, 4, 4, 4], 'READ']
False
[[4, True, 8, 4, 5], ['RECEIVED', 'MUTE', 'RECEIVED', 'READ'], [True, True, True, True]]
[[0, True, 8, 8, 5], ['RECEIVED', 'MUTE', 'RECEIVED', 'READ'], [True, True, True, True]]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
RECEIVED
RECEIVED
3
UNKNOWN
RECEIVED
7
[['A', 4, 7, False], ['B', 0, 0, True]]
4 [[0, 'RECEIVED'], [1, 'RECEIVED'], [2, 'UNKNOWN'], [0, 'RECEIVED']]
```

### ב. פלט התרחיש השני

```text
RECEIVED
RECEIVED
3
UNKNOWN
RECEIVED
7
[['A', 4, 5, True], ['B', 0, 7, False]]
4 [[0, 'RECEIVED'], [1, 'RECEIVED'], [2, 'UNKNOWN'], [0, 'RECEIVED']]
```

### ג. תשובות והערות לדיון

Chat אחראית למצבה;

Inbox לצבירה וניתוב.

badge כולל הכול.

אינדקס פסול נדחה.

alerts היסטורי.

כל מופע נפרד.

### ד. פתרון אפשרי

```python
class Chat:
    def __init__(self, name):
        self.name = name
        self.unread = 0
        self.received = 0
        self.read_total = 0
        self.alerts = 0
        self.muted = False

    def receive(self, amount):
        if amount <= 0:
            return False
        self.unread += amount
        self.received += amount
        if not self.muted:
            self.alerts += amount
        return True

    def read(self, amount):
        if amount <= 0:
            return 0
        actual = amount
        if actual > self.unread:
            actual = self.unread
        self.unread -= actual
        self.read_total += actual
        return actual

    def toggle(self):
        self.muted = not self.muted

    def report(self):
        return [self.name, self.unread, self.alerts, self.muted]

class Inbox:
    def __init__(self, chats):
        self.chats = chats
        self.history = []

    def deliver(self, index, amount):
        status = "UNKNOWN"
        if index >= 0 and index < len(self.chats):
            if self.chats[index].receive(amount):
                status = "RECEIVED"
            else:
                status = "INVALID"
        self.history.append([index, status])
        return status

    def badge(self):
        total = 0
        for chat in self.chats:
            total += chat.unread
        return total

    def visible(self):
        result = []
        for chat in self.chats:
            if chat.unread > 0:
                result.append(chat.report())
        return result

    def muted_count(self):
        count = 0
        for chat in self.chats:
            if chat.muted:
                count += 1
        return count

    def reports(self):
        result = []
        for chat in self.chats:
            result.append(chat.report())
        return result

a = Chat("A")
b = Chat("B")
inbox = Inbox([a, b])
print(inbox.deliver(0, 5))
b.toggle()
print(inbox.deliver(1, 7))
print(a.read(3))
print(inbox.deliver(2, 1))
print(inbox.deliver(0, 2))
print(b.read(10))
print(inbox.reports())
print(inbox.badge(), inbox.history)
print(inbox.visible(), inbox.muted_count())
print(inbox.deliver(1, 4))
print(inbox.visible(), inbox.muted_count())
print(inbox.badge())
```

פלט:

```text
RECEIVED
RECEIVED
3
UNKNOWN
RECEIVED
7
[['A', 4, 7, False], ['B', 0, 0, True]]
4 [[0, 'RECEIVED'], [1, 'RECEIVED'], [2, 'UNKNOWN'], [0, 'RECEIVED']]
[['A', 4, 7, False]] 1
RECEIVED
[['A', 4, 7, False], ['B', 4, 0, True]] 1
8
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

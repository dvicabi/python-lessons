# פתרונות למורה: מערכת התחברות: האם כל ניסיון משנה את מצב החשבון?

[חזרה למשימת התלמיד](../25_login_system.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
LOGIN A01 | SIM
Attempts: 2 / 3
Account: OPEN | READY
Result: FAIL | RETRY
Event: 07 | LOG
```

### ב. פלט התרחיש השני

```text
LOGIN  | A01 | SIM
Attempts: 2 / 3
Account: OPEN | READY
Result: FAIL | RETRY
Event: 07 | LOG
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("LOGIN ", end="")
print("B02", end="")
print(" | SIM")
print("Attempts: ", end="")
print("3", end="")
print(" / 3")
print("Account: ", end="")
print("LOCKED", end="")
print(" | REVIEW")
print("Result: ", end="")
print("DENIED", end="")
print(" | WAIT")
print("Event: ", end="")
print("08", end="")
print(" | LOG")
```

פלט:

```text
LOGIN B02 | SIM
Attempts: 3 / 3
Account: LOCKED | REVIEW
Result: DENIED | WAIT
Event: 08 | LOG
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
1 1 0 1
2 2 0 2
3 2 1 0
4 3 1 1
5 4 1 2
Remaining: 1
Check: 5
Difference: 2
```

### ב. פלט התרחיש השני

```text
1 1 0 1
2 2 0 2
3 2 1 1
4 3 1 2
5 4 1 3
Remaining: 0
Check: 5
Difference: 1
```

### ג. תשובות והערות לדיון

failures מצטבר, streak הוא רצף.

attempts=failures+successes.

השינוי אינו מאפס רצף ולכן מדווח יותר מדי כישלונות רצופים.

דיווח אינו משנה מצב.

### ד. פתרון אפשרי

```python
attempts = 0
failures = 0
successes = 0
streak = 0
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
attempts += 1
successes += 1
streak = 0
print(attempts, failures, successes, streak)
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
attempts += 1
successes += 1
streak = 0
print(attempts, failures, successes, streak)
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
remaining = 3 - streak
print("Remaining:", remaining)
print("Check:", failures + successes)
print("Difference:", failures - streak)
```

פלט:

```text
1 1 0 1
2 1 1 0
3 2 1 1
4 3 1 2
5 3 2 0
6 4 2 1
Remaining: 2
Check: 6
Difference: 3
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 8 2 1
B: 9 1 2
Totals: 17 7 10
Account gap: -1
Check: 17
Streak gap: 1
```

### ב. פלט התרחיש השני

```text
A: 8 2 1
B: 7 3 0
Totals: 15 11 4
Account gap: 1
Check: 15
Streak gap: -1
```

### ג. תשובות והערות לדיון

נעילה תלויה ברצף.

מרווח 0 מציין הגעה לסף.

רצף אינו גדול מסך הכישלונות.

סכום משותף לא מזהה חשבון מסוים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
3
2
2
7
1
4
2
3
3
```

```python
a_fail = int(input())
a_ok = int(input())
a_streak = int(input())
b_fail = int(input())
b_ok = int(input())
b_streak = int(input())
c_fail = int(input())
c_ok = int(input())
c_streak = int(input())
limit = int(input())
print(a_fail + a_ok, limit - a_streak)
print(b_fail + b_ok, limit - b_streak)
print(c_fail + c_ok, limit - c_streak)
total_fail = a_fail + b_fail + c_fail
total_ok = a_ok + b_ok + c_ok
print(total_fail, total_ok, total_fail + total_ok)
```

פלט:

```text
8 1
9 2
6 0
11 12 23
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
FAIL True
LOCKED
3 True 0 1
```

### ב. פלט התרחיש השני

```text
FAIL False
SUCCESS
0 False 1 1
```

### ג. תשובות והערות לדיון

הצלחה אינה משנה חשבון נעול.

INVALID אינו תוצאת אימות חוקית.

אירוע חסום או שגוי אינו נכלל בשני המונים.

רצף 2 וכישלון מגיעים לסף 3.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
2
0
1
```

```python
streak = int(input())
locked = False
successes = 0
failures = 0
blocked = 0
invalid = 0
event = int(input())
if event != 0 and event != 1:
    invalid += 1
    print("INVALID")
elif locked:
    blocked += 1
    print("LOCKED")
elif event == 1:
    successes += 1
    streak = 0
    print("SUCCESS")
else:
    failures += 1
    streak += 1
    if streak >= 3:
        locked = True
    print("FAIL")
event = int(input())
if event != 0 and event != 1:
    invalid += 1
    print("INVALID")
elif locked:
    blocked += 1
    print("LOCKED")
elif event == 1:
    successes += 1
    streak = 0
    print("SUCCESS")
else:
    failures += 1
    streak += 1
    if streak >= 3:
        locked = True
    print("FAIL")
print(streak, locked)
print(successes, failures, blocked, invalid)
```

פלט:

```text
FAIL
LOCKED
3 True
0 1 1 0
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 FAIL 1 False
2 FAIL 2 False
3 SUCCESS 0 False
4 FAIL 1 False
5 INVALID 1 False
6 FAIL 2 False
7 FAIL 3 True
8 LOCKED 3 True
9 LOCKED 3 True
10 INVALID 3 True
Counters: 1 5 2 2
Check: 10
Lock index: 7
```

### ב. פלט התרחיש השני

```text
1 FAIL 1 False
2 FAIL 2 False
3 FAIL 3 True
4 LOCKED 3 True
5 INVALID 3 True
6 LOCKED 3 True
7 LOCKED 3 True
8 LOCKED 3 True
9 LOCKED 3 True
10 INVALID 3 True
Counters: 0 3 5 2
Check: 10
Lock index: 3
```

### ג. תשובות והערות לדיון

lock_index מתעד מעבר למצב נעול.

סכום ארבעת המונים שווה למספר האירועים.

INVALID אינו ראיה לתוצאה חוקית.

0,0,1,0,0,1,0,0 הוא רצף מתאים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
10
4
0
0
1
0
0
2
0
0
1
0
```

```python
count = int(input())
limit = int(input())
streak = 0
longest = 0
locked = False
successes = 0
failures = 0
blocked = 0
invalid = 0
lock_index = 0
for i in range(count):
    event = int(input())
    if event != 0 and event != 1:
        invalid += 1
        status = "INVALID"
    elif locked:
        blocked += 1
        status = "LOCKED"
    elif event == 1:
        successes += 1
        streak = 0
        status = "SUCCESS"
    else:
        failures += 1
        streak += 1
        status = "FAIL"
        if streak > longest:
            longest = streak
        if streak >= limit:
            locked = True
            lock_index = i + 1
    print(i + 1, status, streak, locked)
print("Counters:", successes, failures, blocked, invalid)
print("Check:", successes + failures + blocked + invalid)
print("Lock index:", lock_index)
print("Longest:", longest)
```

פלט:

```text
1 FAIL 1 False
2 FAIL 2 False
3 SUCCESS 0 False
4 FAIL 1 False
5 FAIL 2 False
6 INVALID 2 False
7 FAIL 3 False
8 FAIL 4 True
9 LOCKED 4 True
10 LOCKED 4 True
Counters: 1 6 2 1
Check: 10
Lock index: 8
Longest: 4
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
0 0 FAIL [1, 0] [False, False]
1 1 FAIL [1, 1] [False, False]
2 0 FAIL [2, 1] [False, False]
3 1 SUCCESS [2, 0] [False, False]
4 0 FAIL [3, 0] [True, False]
5 0 LOCKED [3, 0] [True, False]
6 1 FAIL [3, 1] [True, False]
7 1 FAIL [3, 2] [True, False]
8 2 UNKNOWN [3, 2] [True, False]
9 0 INVALID [3, 2] [True, False]
History: ['FAIL', 'FAIL', 'FAIL', 'SUCCESS', 'FAIL', 'LOCKED', 'FAIL', 'FAIL', 'UNKNOWN', 'INVALID']
Failures: [3, 3]
Successes: [0, 1]
```

### ב. פלט התרחיש השני

```text
0 0 FAIL [1, 0] [False, False]
1 1 FAIL [1, 1] [False, False]
2 0 FAIL [2, 1] [False, False]
3 1 FAIL [2, 2] [False, False]
4 0 SUCCESS [0, 2] [False, False]
5 0 SUCCESS [0, 2] [False, False]
6 1 FAIL [0, 3] [False, True]
7 1 LOCKED [0, 3] [False, True]
8 2 UNKNOWN [0, 3] [False, True]
9 0 INVALID [0, 3] [False, True]
History: ['FAIL', 'FAIL', 'FAIL', 'FAIL', 'SUCCESS', 'SUCCESS', 'FAIL', 'LOCKED', 'UNKNOWN', 'INVALID']
Failures: [2, 3]
Successes: [2, 0]
```

### ג. תשובות והערות לדיון

אינדקס שלילי יכול להפנות לחשבון אחר.

כל רשימה מתארת שדה של אותו חשבון.

ההפרדה מונעת תלות.

משתנה משותף מערבב רצפים.

יש להאריך את כל רשימות המצב.

### ד. פתרון אפשרי

```python
accounts = [0, 1, 0, 1, 0, 0, 1, 1, 2, 0]
events = [0, 0, 0, 1, 0, 1, 0, 0, 1, 2]
streaks = [0, 0]
locked = [False, False]
failures = [0, 0]
successes = [0, 0]
history = []
blocked = [0, 0]
unknown = 0
lock_indexes = []
for i in range(len(accounts)):
    account = accounts[i]
    event = events[i]
    if account < 0 or account >= len(streaks):
        status = "UNKNOWN"
        unknown += 1
    elif event != 0 and event != 1:
        status = "INVALID"
    elif locked[account]:
        status = "LOCKED"
        blocked[account] += 1
    elif event == 1:
        streaks[account] = 0
        successes[account] += 1
        status = "SUCCESS"
    else:
        failures[account] += 1
        streaks[account] += 1
        status = "FAIL"
        if streaks[account] >= 3:
            locked[account] = True
            lock_indexes.append(i)
    history.append(status)
    print(i, account, status, streaks, locked)
print("History:", history)
print("Failures:", failures)
print("Successes:", successes)
print(blocked, unknown, lock_indexes)
```

פלט:

```text
0 0 FAIL [1, 0] [False, False]
1 1 FAIL [1, 1] [False, False]
2 0 FAIL [2, 1] [False, False]
3 1 SUCCESS [2, 0] [False, False]
4 0 FAIL [3, 0] [True, False]
5 0 LOCKED [3, 0] [True, False]
6 1 FAIL [3, 1] [True, False]
7 1 FAIL [3, 2] [True, False]
8 2 UNKNOWN [3, 2] [True, False]
9 0 INVALID [3, 2] [True, False]
History: ['FAIL', 'FAIL', 'FAIL', 'SUCCESS', 'FAIL', 'LOCKED', 'FAIL', 'FAIL', 'UNKNOWN', 'INVALID']
Failures: [3, 3]
Successes: [0, 1]
[1, 0] 1 [4]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[3, True, 'FAIL']
[3, True, 'LOCKED']
0 [1, False, 'FAIL']
1 [2, False, 'FAIL']
2 [0, False, 'SUCCESS']
3 [1, False, 'FAIL']
4 [2, False, 'FAIL']
5 [3, True, 'FAIL']
6 [3, True, 'LOCKED']
7 [3, True, 'INVALID']
[['FAIL', 'FAIL', 'SUCCESS', 'FAIL', 'FAIL', 'FAIL', 'LOCKED', 'INVALID'], 3, True, 5]
['ERROR', []]
```

### ב. פלט התרחיש השני

```text
[3, False, 'FAIL']
[3, True, 'LOCKED']
0 [1, False, 'FAIL']
1 [2, False, 'FAIL']
2 [0, False, 'SUCCESS']
3 [1, False, 'FAIL']
4 [2, False, 'FAIL']
5 [3, False, 'FAIL']
6 [0, False, 'SUCCESS']
7 [0, False, 'INVALID']
[['FAIL', 'FAIL', 'SUCCESS', 'FAIL', 'FAIL', 'FAIL', 'SUCCESS', 'INVALID'], 0, False, -1]
['ERROR', []]
```

### ג. תשובות והערות לדיון

הפעולה מחזירה ערכים חדשים.

streak=limit חייב לנעול.

first_lock הוא אינדקס מעבר.

רשימה ריקה תחזיר היסטוריה ריקה ומצב פתוח.

old_locked מבדיל מעבר ממצב קבוע.

### ד. פתרון אפשרי

```python
def evaluate(streak, locked, event, limit):
    if event != 0 and event != 1:
        return [streak, locked, "INVALID"]
    if locked:
        return [streak, locked, "LOCKED"]
    if event == 1:
        return [0, False, "SUCCESS"]
    streak += 1
    return [streak, streak >= limit, "FAIL"]

def report(events, limit):
    if limit <= 0:
        return ["ERROR", []]
    streak = 0
    locked = False
    history = []
    first_lock = -1
    counters = [0, 0, 0, 0]
    for i in range(len(events)):
        old_locked = locked
        result = evaluate(streak, locked, events[i], limit)
        streak = result[0]
        locked = result[1]
        history.append(result[2])
        if result[2] == "SUCCESS":
            counters[0] += 1
        elif result[2] == "FAIL":
            counters[1] += 1
        elif result[2] == "LOCKED":
            counters[2] += 1
        else:
            counters[3] += 1
        if locked and not old_locked:
            first_lock = i
        print(i, result)
    return [history, streak, locked, first_lock, counters, len(history)]

print(evaluate(2, False, 0, 3))
print(evaluate(3, True, 1, 3))
print(report([0, 0, 1, 0, 0, 0, 1, 2], 3))
print(report([0], 0))
print(report([], 3))
```

פלט:

```text
[3, True, 'FAIL']
[3, True, 'LOCKED']
0 [1, False, 'FAIL']
1 [2, False, 'FAIL']
2 [0, False, 'SUCCESS']
3 [1, False, 'FAIL']
4 [2, False, 'FAIL']
5 [3, True, 'FAIL']
6 [3, True, 'LOCKED']
7 [3, True, 'INVALID']
[['FAIL', 'FAIL', 'SUCCESS', 'FAIL', 'FAIL', 'FAIL', 'LOCKED', 'INVALID'], 3, True, 5, [1, 5, 1, 1], 8]
['ERROR', []]
[[], 0, False, -1, [0, 0, 0, 0], 0]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
FAIL
FAIL
FAIL
FAIL
SUCCESS
LOCKED
UNKNOWN
INVALID
LOCKED
['A', 0, False, 1, 2] ['B', 2, True, 0, 2]
['FAIL', 'FAIL', 'SUCCESS', 'INVALID']
['FAIL', 'FAIL', 'LOCKED', 'LOCKED']
[[0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 1, 'SUCCESS'], [1, 1, 'LOCKED'], [2, 1, 'UNKNOWN'], [0, 2, 'INVALID'], [1, 0, 'LOCKED']]
Locked: 1
```

### ב. פלט התרחיש השני

```text
FAIL
FAIL
FAIL
FAIL
SUCCESS
SUCCESS
UNKNOWN
INVALID
FAIL
['A', 0, False, 1, 2] ['B', 1, False, 1, 3]
['FAIL', 'FAIL', 'SUCCESS', 'INVALID']
['FAIL', 'FAIL', 'SUCCESS', 'FAIL']
[[0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 1, 'SUCCESS'], [1, 1, 'SUCCESS'], [2, 1, 'UNKNOWN'], [0, 2, 'INVALID'], [1, 0, 'FAIL']]
Locked: 0
```

### ג. תשובות והערות לדיון

Account אחראית למצבה.

היומן מתעד גם מזהים לא מוכרים.

snapshot היא שאילתה.

השוואת שני התרחישים מדגימה עצמאות.

אותו מופע פעמיים יוצר מצב משותף.

### ד. פתרון אפשרי

```python
class Account:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.streak = 0
        self.locked = False
        self.history = []
        self.failures = 0
        self.successes = 0

    def event(self, code):
        if code != 0 and code != 1:
            status = "INVALID"
        elif self.locked:
            status = "LOCKED"
        elif code == 1:
            self.streak = 0
            self.successes += 1
            status = "SUCCESS"
        else:
            self.streak += 1
            self.failures += 1
            status = "FAIL"
            if self.streak >= self.limit:
                self.locked = True
        self.history.append(status)
        return status

    def reset_for_demo(self):
        self.streak = 0
        self.locked = False
        self.history.append("RESET")

    def snapshot(self):
        return [self.name, self.streak, self.locked, self.successes, self.failures]

class LoginLab:
    def __init__(self, accounts):
        self.accounts = accounts
        self.audit = []

    def process(self, index, code):
        if index < 0 or index >= len(self.accounts):
            status = "UNKNOWN"
        else:
            status = self.accounts[index].event(code)
        self.audit.append([index, code, status])
        return status

    def reset_for_demo(self, index):
        if index >= 0 and index < len(self.accounts):
            self.accounts[index].reset_for_demo()
            self.audit.append([index, 2, "RESET"])
            return True
        return False

    def locked_count(self):
        count = 0
        for account in self.accounts:
            if account.locked:
                count += 1
        return count

a = Account("A", 3)
b = Account("B", 2)
lab = LoginLab([a, b])
print(lab.process(0, 0))
print(lab.process(1, 0))
print(lab.process(0, 0))
print(lab.process(1, 0))
print(lab.process(0, 1))
print(lab.process(1, 1))
print(lab.process(2, 1))
print(lab.process(0, 2))
print(lab.process(1, 0))
print(a.snapshot(), b.snapshot())
print(a.history)
print(b.history)
print(lab.audit)
print("Locked:", lab.locked_count())
print(lab.reset_for_demo(1))
print(a.snapshot(), b.snapshot())
print(lab.audit)
```

פלט:

```text
FAIL
FAIL
FAIL
FAIL
SUCCESS
LOCKED
UNKNOWN
INVALID
LOCKED
['A', 0, False, 1, 2] ['B', 2, True, 0, 2]
['FAIL', 'FAIL', 'SUCCESS', 'INVALID']
['FAIL', 'FAIL', 'LOCKED', 'LOCKED']
[[0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 1, 'SUCCESS'], [1, 1, 'LOCKED'], [2, 1, 'UNKNOWN'], [0, 2, 'INVALID'], [1, 0, 'LOCKED']]
Locked: 1
True
['A', 0, False, 1, 2] ['B', 0, False, 0, 2]
[[0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 0, 'FAIL'], [1, 0, 'FAIL'], [0, 1, 'SUCCESS'], [1, 1, 'LOCKED'], [2, 1, 'UNKNOWN'], [0, 2, 'INVALID'], [1, 0, 'LOCKED'], [1, 2, 'RESET']]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

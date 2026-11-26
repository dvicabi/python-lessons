# פתרונות למורה: מכונה במפעל: מתי חריגה הופכת לתקלה?

[חזרה למשימת התלמיד](../08_factory_machine.md)

כל פתרון הוא דרך אפשרית.

יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט.

מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה.

הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Load: 78 | Streak: 2
Status: WARNING
```

מדידה בודדת אינה מספר החריגות הרצופות;

שתי התוויות מסבירות את ההחלטה.

### ב. שינוי ודיון

Status:  | STOPPED;

יש רווח מיותר לפני המפריד כי התווית כבר כוללת רווח.

### ג. פתרון אפשרי

```python
print("Load: 84", end=" | ")
print("Streak: 3")
print("Status: ", end="")
print("STOPPED")
```

פלט:

```text
Load: 84 | Streak: 3
Status: STOPPED
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
3 1
```

total מודד חריגות מהתחלת הניסוי;

streak מודד את הרצף האחרון.

### ב. שינוי ודיון

1 3;

שני המונים מתארים כעת מידע שגוי.

### ג. פתרון אפשרי

```python
total = 0
streak = 0
total += 1
streak += 1
print(total, streak)
streak = 0
print(total, streak)
total += 1
streak += 1
print(total, streak)
total += 1
streak += 1
print(total, streak)
streak = 0
print(total, streak)
total += 1
streak += 1
print(total, streak)
```

פלט:

```text
1 1
1 0
2 1
3 2
3 0
4 1
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Load: 79
Change: 7
```

לא.

יש צורך גם במדידה עצמה ובכלל סיווג, למשל סף 75.

### ב. שינוי ודיון

Load: 72, Change: -7.

המדידה ירדה ב-7.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
70
78
75
```

```python
a = int(input())
b = int(input())
c = int(input())
print("First change:", b - a)
print("Second change:", c - b)
print("Total change:", c - a)
```

פלט:

```text
First change: 8
Second change: -3
Total change: 5
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
STOPPED
3
```

75 מוגדרת חריגה;

שינוי האופרטור מפספס את ערך הגבול.

### ב. שינוי ודיון

NORMAL, 0.

ללא איפוס היינו מדווחים WARNING, 2.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
1
90
```

```python
streak = int(input())
reading = int(input())
if reading < 0 or reading > 100:
    print("INVALID")
elif reading >= 90:
    print("CRITICAL")
else:
    if reading >= 75:
        streak += 1
    else:
        streak = 0
    if streak >= 3:
        print("STOPPED")
    elif streak > 0:
        print("WARNING")
    else:
        print("NORMAL")
print(streak)
```

פלט:

```text
CRITICAL
1
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
1
2
0
1
2
3
STOPPED
```

כאן שתי חריגות ראשונות נקטעות במדידה תקינה;

עצירה מתרחשת רק במדידה 6.

### ב. שינוי ודיון

שלוש.

יודפסו 1,2,3,STOPPED והשאר לא ייקראו.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
75
70
77
95
```

```python
streak = 0
count = 0
reason = ""
running = True
while (streak < 3) and running:
    reading = int(input())
    count += 1
    if reading >= 90:
        reason = "CRITICAL"
        running = False
    else:
        if reading >= 75:
            streak += 1
        else:
            streak = 0
if reason == "":
    reason = "STREAK"
print(reason, count)
```

פלט:

```text
CRITICAL 4
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[1, 0, 1, 2, 3]
Read: 5
```

המכונה עצרה לפני המדידה השישית.

רשימת הקלט אינה הוכחה שהנתונים עובדו.

### ב. שינוי ודיון

[1,0,1,0,1,2,0,1], Read: 8.

יש 5 חריגות מצטברות אבל אין שלוש רצופות.

### ג. פתרון אפשרי

```python
readings = [70, 75, 80, 73, 78, 91, 60]
history = []
streak = 0
running = True
index = 0
while index < len(readings) and running:
    value = readings[index]
    index += 1
    if value >= 90:
        history.append("CRITICAL")
        running = False
    else:
        if value >= 75:
            streak += 1
        else:
            streak = 0
        if streak >= 3:
            history.append("STOPPED")
            running = False
        elif streak > 0:
            history.append("WARNING")
        else:
            history.append("NORMAL")
print(history)
print(len(history))
```

פלט:

```text
['NORMAL', 'WARNING', 'WARNING', 'NORMAL', 'WARNING', 'CRITICAL']
6
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
NORMAL
WARNING
CRITICAL
INVALID
```

101 עונה גם על >=90 וגם על >=75, אבל נתון לא חוקי קודם.

90 חמור ולא אזהרה רגילה.

### ב. שינוי ודיון

NORMAL, WARNING, WARNING, INVALID;

חריגה חמורה סווגה לא נכון.

### ג. פתרון אפשרי

```python
def classify(value):
    if value < 0 or value > 100:
        return "INVALID"
    if value >= 90:
        return "CRITICAL"
    if value >= 75:
        return "WARNING"
    return "NORMAL"
def monitor(readings):
    history = []
    streak = 0
    running = True
    index = 0
    while index < len(readings) and running:
        value = readings[index]
        index += 1
        status = classify(value)
        if status == "INVALID" or status == "CRITICAL":
            history.append(status)
            running = False
        else:
            if status == "WARNING":
                streak += 1
                if streak >= 3:
                    history.append("STOPPED")
                    running = False
            else:
                streak = 0
            if running:
                history.append(status)
    return history
print(monitor([75, 80, 60, 75, 76, 77, 90]))
```

פלט:

```text
['WARNING', 'WARNING', 'NORMAL', 'WARNING', 'WARNING', 'STOPPED']
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
3 True
1 False
```

העצירה נעולה;

הפעולה חוזרת לפני עיבוד המדידה.

### ב. שינוי ודיון

a לא נעצר: streak=0, stopped=False;

b נשאר 1 False.

### ג. פתרון אפשרי

```python
class Monitor:
    def __init__(self):
        self.reset()

    def reset(self):
        self.streak = 0
        self.stopped = False
        self.reason = "NONE"

    def measure(self, value):
        if self.stopped:
            return
        if value < 0 or value > 100:
            self.stopped = True
            self.reason = "INVALID"
        elif value >= 90:
            self.stopped = True
            self.reason = "CRITICAL"
        elif value >= 75:
            self.streak += 1
            if self.streak >= 3:
                self.stopped = True
                self.reason = "STREAK"
        else:
            self.streak = 0

a = Monitor()
b = Monitor()
a.measure(75)
a.measure(101)
a.measure(70)
b.measure(75)
b.measure(75)
print(a.streak, a.stopped, a.reason)
print(b.streak, b.stopped, b.reason)
a.reset()
print(a.streak, a.stopped, a.reason)
```

פלט:

```text
1 True INVALID
2 False NONE
0 False NONE
```

---

## אתגר מסכם

אין פתרון יחיד.

בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית.

אין לדרוש נושא תכנות שלא נלמד.

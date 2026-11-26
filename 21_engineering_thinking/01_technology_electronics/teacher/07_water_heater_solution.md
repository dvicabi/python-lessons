# פתרונות למורה: דוד חשמל מדומה: מתי להפעיל ומתי לכבות?

[חזרה למשימת התלמיד](../07_water_heater.md)

כל פתרון הוא דרך אפשרית. יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט. מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה. הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Reading: 44
Heater: ON | Status: OK
```

הראשון מחבר תווית לערך והשני מוסיף מפריד.

### ב. שינוי ודיון

Heater: ONStatus: OK; שני שדות נראים כמילה אחת.

### ג. פתרון אפשרי

```python
print("Reading: ", end="")
print("52")
print("Heater: OFF", end=" | ")
print("Status: OK")
```

פלט:

```text
Reading: 52
Heater: OFF | Status: OK
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
Reading: 46
Ticks: 2
```

active מונה פרקי זמן פעילים; הטמפרטורה משתנה במספר יחידות אחר.

### ב. שינוי ודיון

Reading: 46, Ticks: 1; הדוח מפספס פרק חימום.

### ג. פתרון אפשרי

```python
reading = 38
active = 0
reading += 4
active += 1
print(reading)
reading += 4
active += 1
print(reading)
reading -= 1
print(reading)
print("Ticks:", active)
```

פלט:

```text
42
46
45
Ticks: 2
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Difference: 6
```

המדידה מעל היעד; זהו הפרש חוקי, לא החלטה להפעיל.

### ב. שינוי ודיון

Difference: -3; חישוב לבדו לא מדליק ולא מכבה.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
48
50
45
```

```python
current = int(input())
previous = int(input())
first = int(input())
print("Last change:", current - previous)
print("Total change:", current - first)
```

פלט:

```text
Last change: -2
Total change: 3
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
True
```

כי בטווח 46–49 צריך לשמור מצב קודם. else היה הופך את הסף היחיד ל-45.

### ב. שינוי ודיון

48: False; 45: True; 50: False. אותו טווח ביניים יכול לייצג שני מצבים שונים.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
1
47
```

```python
heater = int(input())
reading = int(input())
if reading < 0 or reading > 80:
    heater = 0
    print("FAULT")
else:
    if reading <= 45:
        heater = 1
    elif reading >= 50:
        heater = 0
    if heater == 1:
        print("ON")
    else:
        print("OFF")
print(heater)
```

פלט:

```text
ON
1
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
True 1
True 2
False 2
False 2
True 3
```

בטווח הביניים נשמר המצב הקודם, ולכן היסטוריית המדידות משנה את התוצאה.

### ב. שינוי ודיון

True 1; False 1; False 1; False 1; True 2. איבדנו את זיכרון המצב באזור הביניים.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
4
44
90
40
50
```

```python
count = int(input())
heater = False
fault = False
for step in range(count):
    reading = int(input())
    if reading < 0 or reading > 80:
        fault = True
    if fault:
        heater = False
    elif reading <= 45:
        heater = True
    elif reading >= 50:
        heater = False
    print(heater, fault)
```

פלט:

```text
True False
False True
False True
False True
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[True, True, False, False, True]
```

שני מופעים של 48 מובילים לערכים שונים, לפי ההיסטוריה.

### ב. שינוי ודיון

שני ספים: [False,False,False,False]. סף יחיד: [True,False,True,False].

### ג. פתרון אפשרי

```python
readings = [44, 48, 49, 50, 46, 45, 90, 42]
history = []
heater = False
fault = False
active = 0
for reading in readings:
    if reading < 0 or reading > 80:
        fault = True
    if fault:
        heater = False
        history.append("FAULT")
    else:
        if reading <= 45:
            heater = True
        elif reading >= 50:
            heater = False
        if heater:
            active += 1
            history.append("ON")
        else:
            history.append("OFF")
print(history)
print(active)
```

פלט:

```text
['ON', 'ON', 'ON', 'OFF', 'OFF', 'ON', 'FAULT', 'FAULT']
4
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
True
True
False
False
```

בלי החזרה מפורשת, מצב ביניים היה הופך ל-None ולא לבוליאני הקודם.

### ב. שינוי ודיון

True, False, False, False. טווח ביניים כבר לא שומר את המצב האמיתי.

### ג. פתרון אפשרי

```python
def decide(previous, reading):
    if reading <= 45:
        return True
    if reading >= 50:
        return False
    return previous

def run(readings):
    heater = False
    fault = False
    history = []
    for reading in readings:
        if reading < 0 or reading > 80:
            fault = True
        if fault:
            heater = False
            history.append("FAULT")
        else:
            heater = decide(heater, reading)
            if heater:
                history.append("ON")
            else:
                history.append("OFF")
    return history

print(run([48, 45, 48, 81, 42]))
```

פלט:

```text
['OFF', 'ON', 'ON', 'FAULT', 'FAULT']
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
False True
True False
```

תקלה נעולה; נדרש איפוס מתוכנן ולא רק שינוי חיישן.

### ב. שינוי ודיון

80 מדידה חוקית מכבה, ואז 42 מפעילה: a=True False, b=True False.

### ג. פתרון אפשרי

```python
class Heater:
    def __init__(self):
        self.active = 0
        self.reset()

    def reset(self):
        self.on = False
        self.fault = False

    def measure(self, value):
        if value < 0 or value > 80:
            self.fault = True
        if self.fault:
            self.on = False
        elif value <= 45:
            self.on = True
        elif value >= 50:
            self.on = False
        if self.on:
            self.active += 1

a = Heater()
b = Heater()
a.measure(44)
a.measure(90)
a.measure(42)
a.reset()
a.measure(43)
b.measure(48)
print(a.on, a.fault, a.active)
print(b.on, b.fault, b.active)
```

פלט:

```text
True False 2
False False 0
```

---

## אתגר מסכם

אין פתרון יחיד. בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית. אין לדרוש נושא תכנות שלא נלמד.

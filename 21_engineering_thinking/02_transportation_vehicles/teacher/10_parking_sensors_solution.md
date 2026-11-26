# פתרונות למורה: חיישני רוורס: איך מתרגמים מרחק להתראה?

[חזרה למשימת התלמיד](../10_parking_sensors.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
REAR | Sensor 1
Distance: 18 cm | Level: STOP
[!!!]
```

### ב. פלט התרחיש השני

```text
REAR | Sensor 1
Distance: 18
 | Level: STOP
[!!! ]
```

### ג. תשובות והערות לדיון

end שומר את התוויות יחד ומאפשר לצייר סוגריים ללא רווח.

שינוי תצוגה לא משנה את נתון החיישן.

סטטוס הוא מידע שנגזר מהמרחק.

### ד. פתרון אפשרי

```python
print("REAR", end=" | ")
print("Sensor 2")
print("Distance: ", end="")
print("42", end=" cm")
print(" | Level: ", end="")
print("NEAR")
print("[", end="")
print("!!", end="")
print("]")
```

פלט:

```text
REAR | Sensor 2
Distance: 42 cm | Level: NEAR
[!!]
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
85 25 25
55 30 55
65 -10 45
Check: 45
```

### ב. פלט התרחיש השני

```text
85 25 25
55 30 55
45 10 65
Check: 65
```

### ג. תשובות והערות לדיון

previous מתעד את המדידה הקודמת.

change שלילי מציין התרחקות.

סכום השינויים שווה להפרש בין התחלה לסוף.

### ד. פתרון אפשרי

```python
distance = 100
start = distance
distance -= 20
print(distance, start - distance)
distance += 5
print(distance, start - distance)
distance -= 40
print(distance, start - distance)
distance -= 15
print(distance, start - distance)
print("Total:", start - distance)
```

פלט:

```text
80 20
85 15
45 55
30 70
Total: 70
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Changes: 20 30 15
Total: 65
Average: 21
Last: 35
Check: 65
```

### ב. פלט התרחיש השני

```text
Changes: 60 -50 -10
Total: 0
Average: 0
Last: 100
Check: 0
```

### ג. תשובות והערות לדיון

ממוצע מסתיר סדר ואירועים בודדים.

// מחזיר מנה שלמה מעוגלת מטה.

רצף יכול לחזור לערך התחלתי לאחר ירידה ועלייה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
80
65
70
20
```

```python
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("Step:", a - b, b - c, c - d)
print("From start:", a - b, a - c, a - d)
print("Total:", a - d)
```

פלט:

```text
Step: 15 -5 50
From start: 15 10 60
Total: 60
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
CLEAR
STOP
Alerts: 1
```

### ב. פלט התרחיש השני

```text
NEAR
ERROR
Alerts: 1
```

### ג. תשובות והערות לדיון

ערך שלילי היה נכנס ל-STOP אילו לא נבדק ראשון.

תנאי רחב לפני צר מסתיר STOP.

כרגע ERROR אינו נספר;

אפשר להוסיף מונה errors נפרד.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
20
201
```

```python
a = int(input())
b = int(input())
stops = 0
errors = 0
if a < 0 or a > 200:
    errors += 1
    print("ERROR")
elif a <= 20:
    stops += 1
    print("STOP")
elif a <= 50:
    print("NEAR")
else:
    print("CLEAR")
if b < 0 or b > 200:
    errors += 1
    print("ERROR")
elif b <= 20:
    stops += 1
    print("STOP")
elif b <= 50:
    print("NEAR")
else:
    print("CLEAR")
print(stops, errors)
```

פלט:

```text
STOP
ERROR
1 1
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 True 0
2 True 1
3 True 0
4 True 1
5 False 2
ERROR False
7 True 0
Final: True
```

### ב. פלט התרחיש השני

```text
1 True 0
2 True 1
3 False 2
4 False 0
5 True 0
6 True 1
7 False 2
Final: False
```

### ג. תשובות והערות לדיון

רק שתי CLEAR רצופות מצדיקות שחרור;

NEAR ו-ERROR קוטעים את הרצף.

תקלה אינה הוכחה שהסביבה פנויה.

איפוס בראש הלולאה ימחק זיכרון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
7
15
60
-1
70
80
30
10
```

```python
count = int(input())
locked = False
clear_count = 0
stops = 0
errors = 0
for step in range(count):
    d = int(input())
    if d < 0 or d > 200:
        errors += 1
        clear_count = 0
        print("ERROR")
    else:
        if d <= 20:
            locked = True
            clear_count = 0
        elif d > 50:
            clear_count += 1
            if clear_count >= 2:
                locked = False
        else:
            clear_count = 0
        if locked:
            stops += 1
        print(locked, clear_count)
print(stops, errors)
```

פלט:

```text
True 0
True 1
ERROR
True 1
False 2
False 0
True 0
4 1
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
['CLEAR', 'NEAR', 'STOP', 'ERROR', 'NEAR', 'STOP', 'CLEAR']
Closest: 10
Errors: 1
Count: 7
```

### ב. פלט התרחיש השני

```text
['ERROR', 'ERROR', 'CLEAR', 'NEAR', 'STOP', 'STOP', 'CLEAR']
Closest: 0
Errors: 2
Count: 7
```

### ג. תשובות והערות לדיון

201 גדול מכל מרחק חוקי ולכן כל מדידה חוקית יכולה להחליפו.

אם נשאר 201 צריך לדווח שאין מדידה חוקית.

שמירת ERROR שומרת התאמה לאינדקס המקורי.

### ד. פתרון אפשרי

```python
readings = [201, -1, 50, 20, 0, 75]
valid = []
stop_indexes = []
closest = 201
for i in range(len(readings)):
    d = readings[i]
    if not (d < 0 or d > 200):
        valid.append(d)
        if d < closest:
            closest = d
        if d <= 20:
            stop_indexes.append(i)
print(valid)
print(stop_indexes)
if len(valid) == 0:
    print("NO DATA")
else:
    print("Closest:", closest)
```

פלט:

```text
[50, 20, 0, 75]
[3, 4]
Closest: 0
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
Stops: 2
Stops: 0
['NEAR', 'STOP', 'ERROR', 'CLEAR', 'STOP']
['CLEAR', 'CLEAR', 'CLEAR']
```

### ב. פלט התרחיש השני

```text
Stops: 1
Stops: 0
['NEAR', 'NEAR', 'ERROR', 'CLEAR', 'STOP']
['CLEAR', 'CLEAR', 'CLEAR']
```

### ג. תשובות והערות לדיון

20 חייב להיות STOP.

פעולה יחידה מרכזת כללי סף.

report קוראת ערכים ויוצרת רשימה חדשה;

הדפיסו את הקלט לפני ואחרי.

### ד. פתרון אפשרי

```python
def classify(distance):
    if distance < 0 or distance > 200:
        return "ERROR"
    if distance <= 20:
        return "STOP"
    if distance <= 50:
        return "NEAR"
    return "CLEAR"

def combine(left, right):
    a = classify(left)
    b = classify(right)
    if a == "ERROR" or b == "ERROR":
        return "ERROR"
    if a == "STOP" or b == "STOP":
        return "STOP"
    if a == "NEAR" or b == "NEAR":
        return "NEAR"
    return "CLEAR"

print(combine(10, 100))
print(combine(50, 80))
print(combine(51, 200))
print(combine(-1, 80))
print(combine(80, 20))
```

פלט:

```text
STOP
NEAR
CLEAR
ERROR
STOP
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
STOP
CLEAR
STOP
CLEAR
ERROR
['STOP', 'STOP', 'CLEAR']
['CLEAR', 'ERROR']
```

### ב. פלט התרחיש השני

```text
STOP
CLEAR
STOP
STOP
ERROR
['STOP', 'STOP', 'STOP']
['CLEAR', 'ERROR']
```

### ג. תשובות והערות לדיון

המצב פרטי לאובייקט.

ERROR מאפס רצף ולא משנה נעילה.

אפשר להגדיר את מספר המדידות כפרמטר בבנאי במקום מספר קבוע.

### ד. פתרון אפשרי

```python
class Sensor:
    def __init__(self, required):
        self.required = required
        self.locked = False
        self.clear_count = 0
        self.history = []

    def read(self, distance):
        if distance < 0 or distance > 200:
            self.clear_count = 0
            self.history.append("ERROR")
            return "ERROR"
        if distance <= 20:
            self.locked = True
            self.clear_count = 0
        elif distance > 50:
            self.clear_count += 1
            if self.clear_count >= self.required:
                self.locked = False
        else:
            self.clear_count = 0
        if self.locked:
            self.history.append("STOP")
            return "STOP"
        if distance <= 50:
            self.history.append("NEAR")
            return "NEAR"
        self.history.append("CLEAR")
        return "CLEAR"

a = Sensor(2)
b = Sensor(3)
for d in [15, 60, 70, 80]:
    a.read(d)
    b.read(d)
print(a.history)
print(b.history)
```

פלט:

```text
['STOP', 'STOP', 'CLEAR', 'CLEAR']
['STOP', 'STOP', 'STOP', 'CLEAR']
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

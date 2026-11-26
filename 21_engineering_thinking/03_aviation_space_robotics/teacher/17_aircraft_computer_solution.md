# פתרונות למורה: מחשב בקרה במטוס: האם אפשר לסמוך על המדידה?

[חזרה למשימת התלמיד](../17_aircraft_computer.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
SIM 17 | A
Sensor A: 62 points
Sensor B: 65 points
Gap: 3 | NORMAL
```

### ב. פלט התרחיש השני

```text
SIM  | 17 | A
Sensor A: 62 points
Sensor B: 65 points
Gap: 3 | NORMAL
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("SIM ", end="")
print("18", end="")
print(" | B")
print("Sensor A: ", end="")
print("79", end="")
print(" points")
print("Sensor B: ", end="")
print("95", end="")
print(" points")
print("Gap: ", end="")
print("16", end="")
print(" | MISMATCH")
```

פלט:

```text
SIM 18 | B
Sensor A: 79 points
Sensor B: 95 points
Gap: 16 | MISMATCH
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
50 54 4
62 69 7
72 72 0
Totals: 184 195 11
Check: 11
```

### ב. פלט התרחיש השני

```text
50 54 4
62 74 12
72 77 5
Totals: 184 205 21
Check: 21
```

### ג. תשובות והערות לדיון

הפער תלוי בזוג העדכני.

כאשר B אינו קטן מ-A, סכום הפערים שווה להפרש הסכומים.

השמה מוחקת פערים קודמים.

פער מצטבר יכול להצטבר מהרבה פערים קטנים.

### ד. פתרון אפשרי

```python
a = 40
b = 45
total_a = a
total_b = b
gap_total = b - a
print(a, b, b - a)
a += 8
b += 12
total_a += a
total_b += b
gap_total += b - a
print(a, b, b - a)
a += 15
b += 5
total_a += a
total_b += b
gap_total += b - a
print(a, b, b - a)
a -= 4
b += 3
total_a += a
total_b += b
gap_total += b - a
print(a, b, b - a)
print(gap_total, total_b - total_a)
```

פלט:

```text
40 45 5
48 57 9
63 62 -1
59 65 6
19 19
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 50 72 55
B: 54 75 95
Pairs: 52 73 75
Signed gaps: 4 3 40
Overall: 66
Trend: 23
```

### ב. פלט התרחיש השני

```text
A: 40 75 70
B: 100 65 70
Pairs: 70 70 70
Signed gaps: 60 -10 0
Overall: 70
Trend: 0
```

### ג. תשובות והערות לדיון

חילוק שלם מעגל כלפי מטה.

זוג 40,100 ומדידה 70,70 עשויים להיות בעלי אותו ממוצע אך אמינות שונה.

סימן שלילי מציין B קטן מ-A.

נדרשת בדיקת פער בנפרד.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
62
65
80
81
59
75
70
```

```python
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
threshold = int(input())
sum1 = a1 + b1
sum2 = a2 + b2
sum3 = a3 + b3
avg1 = sum1 // 2
avg2 = sum2 // 2
avg3 = sum3 // 2
print(avg1, b1 - a1, avg1 - threshold)
print(avg2, b2 - a2, avg2 - threshold)
print(avg3, b3 - a3, avg3 - threshold)
```

פלט:

```text
63 3 -7
80 1 10
67 16 -3
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
REVIEW 8
MISMATCH 20
```

### ב. פלט התרחיש השני

```text
MISMATCH 9
INVALID
```

### ג. תשובות והערות לדיון

ערך מחוץ לטווח אינו נתון אמין גם אם הפער קטן.

הכלל מגדיר מעל 8 בלבד.

ממוצע עלול להסוות מחלוקת.

לזוג 75,65 פער 10 ולכן MISMATCH.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
69
71
```

```python
a = int(input())
b = int(input())
gap = b - a
if gap < 0:
    gap = -gap
if a < 0 or a > 100 or b < 0 or b > 100:
    print("INVALID")
elif gap > 8:
    print("MISMATCH", gap)
else:
    total = a + b
    average = total // 2
    if average >= 70:
        print("REVIEW", average)
    else:
        print("NORMAL", average)
```

פלט:

```text
REVIEW 70
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 REVIEW 1 False
2 REVIEW 2 False
3 REVIEW 3 True
4 MISMATCH 0 True
5 NORMAL 0 True
6 REVIEW 1 True
1 4 True
```

### ב. פלט התרחיש השני

```text
1 REVIEW 1 False
2 REVIEW 2 False
3 MISMATCH 0 False
4 REVIEW 1 False
5 REVIEW 2 False
6 REVIEW 3 True
1 5 True
```

### ג. תשובות והערות לדיון

streak סופר רצף נוכחי;

flag מתעד אירוע שכבר התרחש.

reviews סופר כל אירוע REVIEW.

מדידה לא אמינה אינה ראיה ל-REVIEW ולכן קוטעת רצף.

למשל REVIEW,NORMAL,REVIEW,NORMAL,REVIEW אינו רצף.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
2
70
72
73
74
65
85
75
77
60
62
70
70
```

```python
count = int(input())
required = int(input())
streak = 0
faults = 0
reviews = 0
normal = 0
flags = 0
flag = False
for step in range(count):
    a = int(input())
    b = int(input())
    gap = b - a
    if gap < 0:
        gap = -gap
    if a < 0 or a > 100 or b < 0 or b > 100 or gap > 8:
        faults += 1
        streak = 0
    else:
        total = a + b
        average = total // 2
        if average >= 70:
            reviews += 1
            streak += 1
        else:
            normal += 1
            streak = 0
    if streak >= required and not flag:
        flags += 1
        flag = True
    print(step + 1, streak, flag)
print(normal, reviews, faults, flags)
```

פלט:

```text
1 1 False
2 2 True
3 0 True
4 1 True
5 0 True
6 1 True
1 4 1 1
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
0 NORMAL 0
1 REVIEW 1
2 MISMATCH 0
3 REVIEW 1
4 INVALID 0
5 REVIEW 1
6 REVIEW 2
7 REVIEW 3
[4, 4, 15, 2, 40, 2, 2, 2]
[1, 3, 5, 6, 7]
True
```

### ב. פלט התרחיש השני

```text
0 NORMAL 0
1 REVIEW 1
2 REVIEW 2
3 REVIEW 3
4 INVALID 0
5 REVIEW 1
6 REVIEW 2
7 REVIEW 3
[4, 4, 3, 2, 40, 2, 2, 2]
[1, 2, 3, 5, 6, 7]
True
```

### ג. תשובות והערות לדיון

אינדקסים צריכים להישאר מותאמים למדידה המקורית.

review_indexes לא מתעד NORMAL או כשלים.

יש לבדוק שוויון אורכים לפני גישה.

אפשר לשמור מונה פער מקסימלי רק אחרי בדיקת טווח.

### ד. פתרון אפשרי

```python
readings_a = [70, 72, 74, 60, 80, 81, 82, 100]
readings_b = [72, 74, 76, 61, 82, 83, 84, 120]
bad = []
averages = []
marks = []
streak = 0
for i in range(len(readings_a)):
    a = readings_a[i]
    b = readings_b[i]
    gap = b - a
    if gap < 0:
        gap = -gap
    if a < 0 or a > 100 or b < 0 or b > 100 or gap > 8:
        bad.append(i)
        streak = 0
    else:
        total = a + b
        average = total // 2
        averages.append(average)
        if average >= 70:
            streak += 1
        else:
            streak = 0
        if streak == 3:
            marks.append(i)
print(bad)
print(averages)
print(marks)
```

פלט:

```text
[7]
[71, 73, 75, 60, 81, 82, 83]
[2, 6]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
REVIEW
MISMATCH
[['REVIEW', 'REVIEW', 'REVIEW', 'NORMAL'], [2]]
[[], []]
```

### ב. פלט התרחיש השני

```text
MISMATCH
MISMATCH
[['REVIEW', 'REVIEW', 'REVIEW', 'NORMAL'], [2]]
[[], []]
```

### ג. תשובות והערות לדיון

classify תלויה רק בזוג וספים.

תוצאה ריקה כפולה עלולה להסתיר שגיאת קלט;

אפשר להחזיר סטטוס מפורש ברשימה.

בגבול פער 8 עדיין תקין.

בדקו ערך לא חוקי, פער חריג, ממוצע מתחת ובגבול הסף.

### ד. פתרון אפשרי

```python
def classify(a, b, gap_limit, threshold):
    if a < 0 or a > 100 or b < 0 or b > 100:
        return "INVALID"
    gap = b - a
    if gap < 0:
        gap = -gap
    if gap > gap_limit:
        return "MISMATCH"
    total = a + b
    average = total // 2
    if average >= threshold:
        return "REVIEW"
    return "NORMAL"

def analyze(left, right, gap_limit, threshold, required):
    statuses = []
    marks = []
    streak = 0
    if len(left) != len(right) or required <= 0:
        return ["ERROR", statuses, marks]
    for i in range(len(left)):
        status = classify(left[i], right[i], gap_limit, threshold)
        statuses.append(status)
        if status == "REVIEW":
            streak += 1
        else:
            streak = 0
        if streak == required:
            marks.append(i)
    return ["OK", statuses, marks]

print(analyze([70, 72, 74, 60], [76, 74, 76, 62], 8, 70, 2))
print(analyze([70, 72, 74, 60], [76, 74, 76, 62], 4, 70, 2))
print(analyze([70], [], 8, 70, 2))
```

פלט:

```text
['OK', ['REVIEW', 'REVIEW', 'REVIEW', 'NORMAL'], [1]]
['OK', ['MISMATCH', 'REVIEW', 'REVIEW', 'NORMAL'], [2]]
['ERROR', [], []]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
REVIEW
MISMATCH
REVIEW
REVIEW
True 2 ['REVIEW', 'REVIEW']
False 1 ['MISMATCH', 'REVIEW']
```

### ב. פלט התרחיש השני

```text
REVIEW
REVIEW
REVIEW
REVIEW
True 2 ['REVIEW', 'REVIEW']
True 2 ['REVIEW', 'REVIEW']
```

### ג. תשובות והערות לדיון

אחריות הסיווג נפרדת מניהול רצף.

סף הפער שונה.

רשימת היסטוריה בבנאי יוצרת רשימה עצמאית לכל מופע.

NORMAL מאפסת streak אך הדגל נשאר True.

### ד. פתרון אפשרי

```python
class PairSensor:
    def __init__(self, gap_limit, threshold):
        self.gap_limit = gap_limit
        self.threshold = threshold

    def classify(self, a, b):
        if a < 0 or a > 100 or b < 0 or b > 100:
            return "INVALID"
        gap = b - a
        if gap < 0:
            gap = -gap
        if gap > self.gap_limit:
            return "MISMATCH"
        total = a + b
        average = total // 2
        if average >= self.threshold:
            return "REVIEW"
        return "NORMAL"

class Monitor:
    def __init__(self, sensor, required):
        self.sensor = sensor
        self.required = required
        self.streak = 0
        self.flag = False
        self.history = []

    def sample(self, a, b):
        status = self.sensor.classify(a, b)
        self.history.append(status)
        if status == "REVIEW":
            self.streak += 1
        else:
            self.streak = 0
        if self.streak >= self.required:
            self.flag = True
        return status

    def reset_flag(self):
        self.flag = False
        self.streak = 0

    def faults(self):
        count = 0
        for status in self.history:
            if status == "INVALID" or status == "MISMATCH":
                count += 1
        return count

a = Monitor(PairSensor(8, 70), 2)
b = Monitor(PairSensor(4, 70), 2)
print(a.sample(70, 76))
print(b.sample(70, 76))
print(a.sample(72, 74))
print(b.sample(72, 74))
print(a.flag, a.streak, a.history)
print(b.flag, b.streak, b.history)
a.reset_flag()
print(a.flag, a.streak, a.history, a.faults())
print(b.flag, b.streak, b.history, b.faults())
```

פלט:

```text
REVIEW
MISMATCH
REVIEW
REVIEW
True 2 ['REVIEW', 'REVIEW']
False 1 ['MISMATCH', 'REVIEW']
False 0 ['REVIEW', 'REVIEW'] 0
False 1 ['MISMATCH', 'REVIEW'] 1
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

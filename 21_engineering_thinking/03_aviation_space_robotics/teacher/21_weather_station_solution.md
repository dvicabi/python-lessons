# פתרונות למורה: תחנת מזג אוויר: איך הופכים מדידות לדוח שאפשר לסמוך עליו?

[חזרה למשימת התלמיד](../21_weather_station.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
STATION NORTH | 06
Temperature: 34 points
Rain: 0 points
Data: VALID | DRY
```

### ב. פלט התרחיש השני

```text
STATION  | NORTH | 06
Temperature: 34 points
Rain: 0 points
Data: VALID | DRY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("STATION ", end="")
print("SOUTH", end="")
print(" | 07")
print("Temperature: ", end="")
print("38", end="")
print(" points")
print("Rain: ", end="")
print("5", end="")
print(" points")
print("Data: ", end="")
print("VALID", end="")
print(" | WET")
```

פלט:

```text
STATION SOUTH | 07
Temperature: 38 points
Rain: 5 points
Data: VALID | WET
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
1 24 0
2 30 3 6
3 38 2 8
4 33 6 -5
Average: 31
Rain total: 11
```

### ב. פלט התרחיש השני

```text
1 24 0
2 30 3 6
3 38 2 8
4 29 6 -9
Average: 30
Rain total: 11
```

### ג. תשובות והערות לדיון

previous מאפשר השוואה לערך הקודם.

rain_sum מצטבר מכל החלונות.

חילוק שלם מאבד שבר.

סדרות שונות עשויות לתת אותו ממוצע.

### ד. פתרון אפשרי

```python
temp = 20
rain = 2
temp_sum = temp
rain_sum = rain
previous = temp
temp = 27
rain = 0
temp_sum += temp
rain_sum += rain
print(temp - previous)
previous = temp
temp = 39
rain = 4
temp_sum += temp
rain_sum += rain
print(temp - previous)
previous = temp
temp = 30
rain = 6
temp_sum += temp
rain_sum += rain
print(temp - previous)
print(temp_sum, rain_sum, temp_sum // 4)
```

פלט:

```text
7
12
-9
116 12 29
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Averages: 27 35
Changes: 6 8 -5
Day: 31 11
Trend: 8
End change: 9
```

### ב. פלט התרחיש השני

```text
Averages: 34 28
Changes: -8 -6 9
Day: 31 11
Trend: -6
End change: -5
```

### ג. תשובות והערות לדיון

Trend משווה ממוצעי חצאים, End change משווה קצוות.

ירידה יכולה להיות אמיתית.

הזנת -1 תטה את הסיכום כל עוד לא בדקנו חוקיות.

ניתן להשוות סדר, שינויים וטווח.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
20
2
39
4
30
6
```

```python
t1 = int(input())
r1 = int(input())
t2 = int(input())
r2 = int(input())
t3 = int(input())
r3 = int(input())
sum_t = t1 + t2 + t3
sum_r = r1 + r2 + r3
print("Totals:", sum_t, sum_r)
print("Temperature changes:", t2 - t1, t3 - t2)
print("Rain changes:", r2 - r1, r3 - r2)
print("Average:", sum_t // 3)
print("End:", t3 - t1, r3 - r1)
```

פלט:

```text
Totals: 89 12
Temperature changes: 19 -9
Rain changes: 2 2
Average: 29
End: 10 4
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
VALID
INVALID
Average: 35
1 1 0
```

### ב. פלט התרחיש השני

```text
VALID
VALID
Average: 37
2 1 1
```

### ג. תשובות והערות לדיון

זוג יכול להיות גם חם וגם רטוב.

יש לחשב ממוצע רק מחוקיים.

אם valid=0 אין לחלק.

35 נכלל לפי >=.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
50
20
```

```python
temp = int(input())
rain = int(input())
if temp < 0 or temp > 50 or rain < 0 or rain > 20:
    print("INVALID")
else:
    if temp >= 35:
        print("HOT")
    else:
        print("MILD")
    if rain > 0:
        print("WET")
    else:
        print("DRY")
```

פלט:

```text
HOT
WET
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 30 0
2 35 1
3 40 2
INVALID 4
5 38 1
6 39 2
36 30 40 6
5 1 2
```

### ב. פלט התרחיש השני

```text
1 30 0
2 35 1
3 40 2
4 37 3
5 38 4
6 39 5
36 30 40 6
6 0 5
```

### ג. תשובות והערות לדיון

ערכי התחלה מחוץ לטווח מבטיחים שהחוקי הראשון יעדכן אותם.

streak נוכחי ו-longest שיא שנצפה.

אי אפשר להסיק על רצף כאשר חסר נתון.

ערך סימון אינו מדידה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
30
0
35
2
51
1
38
4
25
0
```

```python
count = int(input())
valid = 0
total = 0
rain_total = 0
wet_hours = 0
hot_hours = 0
for hour in range(count):
    temp = int(input())
    rain = int(input())
    if temp >= 0 and temp <= 50 and rain >= 0 and rain <= 20:
        valid += 1
        total += temp
        rain_total += rain
        if temp >= 35:
            hot_hours += 1
        if rain > 0:
            wet_hours += 1
print(hot_hours, wet_hours, rain_total)
if valid > 0:
    print(total // valid)
else:
    print("NO DATA")
print(valid, count)
```

פלט:

```text
2 2 6
32
4 5
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
2 30
3 35
4 INVALID
5 INVALID
6 INVALID
7 40
8 39
[30, 35, 40, 39]
[2, 3, 7, 8]
Invalid windows: 3
```

### ב. פלט התרחיש השני

```text
2 30
3 35
4 35
5 34
6 35
7 40
8 39
[30, 35, 35, 34, 35, 40, 39]
[2, 3, 4, 5, 6, 7, 8]
Invalid windows: 0
```

### ג. תשובות והערות לדיון

כל חלון מסתיים ב-i וכולל שלושה סמוכים.

מדידה פנימית חסרה פוסלת עד שלושה חלונות.

ends ממפה כל ממוצע לזמן.

ממוצע מחלון חלקי אינו בר-השוואה לכל חלון מלא לפי המפרט.

### ד. פתרון אפשרי

```python
temps = [24, 30, 36, 39, -1, 33, 42, 45, 30]
moving = []
rises = []
for i in range(len(temps)):
    average = -1
    if i >= 2:
        total = 0
        valid = True
        for j in range(3):
            value = temps[i - 2 + j]
            if value < 0 or value > 50:
                valid = False
            else:
                total += value
        if valid:
            average = total // 3
    moving.append(average)
    if i > 0 and average >= 0 and moving[i - 1] >= 0:
        if average - moving[i - 1] >= 5:
            rises.append(i)
print(moving)
print(rises)
```

פלט:

```text
[-1, -1, 30, 35, -1, -1, -1, 40, 39]
[3]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
38
[-1, 24, 32, 43, -1, -1, 35]
[-1, -1, 28, 38, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1]
```

### ב. פלט התרחיש השני

```text
-1
[-1, 24, 32, -1, -1, -1, 35]
[-1, -1, 28, -1, -1, -1, -1]
[-1, -1, -1, -1, -1, -1, -1]
```

### ג. תשובות והערות לדיון

size בלתי חוקי הופך כל בקשת חלון לשגויה.

מדידה בלתי חוקית פוסלת רק חלונות המכילים אותה.

-1 מחוץ לטווח החוקי.

ערך גבול 50 עשוי להשתתף בכמה חלונות;

יש לבדוק התחלה, גבול, חסר וגודל.

### ד. פתרון אפשרי

```python
def valid(value):
    return value >= 0 and value <= 50

def average_at(temps, end, size):
    if size <= 0 or end < size - 1 or end >= len(temps):
        return -1
    total = 0
    ok = True
    for j in range(size):
        value = temps[end - size + 1 + j]
        if valid(value):
            total += value
        else:
            ok = False
    if ok:
        return total // size
    return -1

def report(temps, size):
    if size <= 0:
        return [[], 0, -1]
    result = []
    count = 0
    highest = -1
    for i in range(len(temps)):
        average = average_at(temps, i, size)
        result.append(average)
        if average >= 0:
            count += 1
            if average > highest:
                highest = average
    return [result, count, highest]

print(report([20, 28, 36, 50, -1, 30, 40], 2))
print(report([20, 28, 36, 50, -1, 30, 40], 3))
print(report([20], 0))
```

פלט:

```text
[[-1, 24, 32, 43, -1, -1, 35], 4, 43]
[[-1, -1, 28, 38, -1, -1, -1], 2, 38]
[[], 0, -1]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
30 [3, 4]
33 [3, 5]
0
```

### ב. פלט התרחיש השני

```text
30 [3, 4]
33 [4, 5]
1
```

### ג. תשובות והערות לדיון

מכפלות משוות שברים בלי חילוק ועיגול.

בשוויון נשארת הראשונה.

average חישוב בלבד.

-1 משמש היעדר מידע ואינו ערך חוקי.

### ד. פתרון אפשרי

```python
class WeatherStation:
    def __init__(self, name):
        self.name = name
        self.temps = []
        self.valid_count = 0
        self.total = 0

    def record(self, temp):
        if temp < 0 or temp > 50:
            self.temps.append(-1)
        else:
            self.temps.append(temp)
            self.valid_count += 1
            self.total += temp

    def average(self):
        if self.valid_count == 0:
            return -1
        return self.total // self.valid_count

    def highest(self):
        highest = -1
        for value in self.temps:
            if value > highest:
                highest = value
        return highest

    def coverage(self):
        return [self.valid_count, len(self.temps)]

class Network:
    def __init__(self, stations):
        self.stations = stations

    def best_coverage(self):
        best = -1
        for i in range(len(self.stations)):
            data = self.stations[i].coverage()
            if data[1] > 0:
                if best == -1:
                    best = i
                else:
                    old = self.stations[best].coverage()
                    if data[0] * old[1] > old[0] * data[1]:
                        best = i
        return best

    def best_average(self):
        best = -1
        for i in range(len(self.stations)):
            if self.stations[i].valid_count >= 2:
                if best == -1 or self.stations[i].average() > self.stations[best].average():
                    best = i
        return best

a = WeatherStation("A")
b = WeatherStation("B")
for value in [20, 40, -1, 30]:
    a.record(value)
for value in [30, 30, -1, -1, 40]:
    b.record(value)
network = Network([a, b])
print(a.average(), a.coverage())
print(b.average(), b.coverage())
print(network.best_coverage())
print(a.highest(), b.highest())
print(network.best_average())
```

פלט:

```text
30 [3, 4]
33 [3, 5]
0
40 40
1
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

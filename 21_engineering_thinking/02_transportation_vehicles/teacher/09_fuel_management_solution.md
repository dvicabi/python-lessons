# פתרונות למורה: מערכת דלק ברכב: האם נוכל להגיע ליעד?

[חזרה למשימת התלמיד](../09_fuel_management.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
TRIP | A
Fuel: 18 units | Range: 60
Reserve: 3 | Status: OK
```

### ב. פלט התרחיש השני

```text
TRIP | A
Fuel: 18
 | Range: 45 | Reserve: 3 | Status: OK
```

### ג. תשובות והערות לדיון

הכותרת, דלק וטווח, ורזרבה וסטטוס הם שלוש קבוצות מידע.

בתרחיש השני הטווח יורד שורה והרזרבה מתחברת לטווח.

end ריק לא מוסיף תו;

רווח מפריד בין שדות.

### ד. פתרון אפשרי

```python
print("TRIP", end=" | ")
print("B")
print("Fuel: ", end="")
print("12", end=" units")
print(" | Range: ", end="")
print("40")
print("Reserve: ", end="")
print("3", end=" | ")
print("Status: LOW")
```

פלט:

```text
TRIP | B
Fuel: 12 units | Range: 40
Reserve: 3 | Status: LOW
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
38 12 6
26 24 10
Total: 50
```

### ב. פלט התרחיש השני

```text
38 12 6
22 28 10
Total: 50
```

### ג. תשובות והערות לדיון

עלות המקטע תלויה במרחק ובקצב הנוכחי.

סכום fuel+used נשאר 50.

השמה במקטע השני מוחקת את הצריכה הקודמת, ולכן המאזן יהיה 38 במקום 50.

### ד. פתרון אפשרי

```python
fuel = 65
distance = 0
used = 0
cost = 5 * 2
fuel -= cost
used += cost
distance += 5
print(fuel, used, distance)
cost = 7 * 3
fuel -= cost
used += cost
distance += 7
print(fuel, used, distance)
cost = 3 * 4
fuel -= cost
used += cost
distance += 3
print(fuel, used, distance)
print("Total:", fuel + used)
```

פלט:

```text
55 10 5
34 31 12
22 43 15
Total: 65
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
After 1: 30
After 2: 12
Used: 28
Distance: 11
Available: 9
```

### ב. פלט התרחיש השני

```text
After 1: 12
After 2: -6
Used: 28
Distance: 11
Available: -9
```

### ג. תשובות והערות לדיון

Available הוא הדלק מעל הרזרבה.

ערך שלילי חושף מסלול שאינו אפשרי לפי המודל.

סדר המקטעים משפיע על מצבי הביניים, אך לא על הסכום כאשר הכל מתבצע.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
50
5
4
6
8
```

```python
fuel = int(input())
reserve = int(input())
d1 = int(input())
d2 = int(input())
d3 = int(input())
used = 0
cost = d1 * 2
fuel -= cost
used += cost
print(fuel)
cost = d2 * 2
fuel -= cost
used += cost
print(fuel)
cost = d3 * 2
fuel -= cost
used += cost
print(fuel)
print("Used:", used)
print("Available:", fuel - reserve)
```

פלט:

```text
42
30
14
Used: 36
Available: 9
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
GO 14
DENIED 14
OK
Used: 12
```

### ב. פלט התרחיש השני

```text
GO 15
GO 3
RESERVE
Used: 24
```

### ג. תשובות והערות לדיון

הצריכה נרשמת רק למקטע שבוצע.

27 מאפשר בדיוק 24+3.

בתנאי השני חסרה בדיקת עלות חיובית;

יש להוסיף cost > 0.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
20
-2
17
```

```python
fuel = int(input())
first = int(input())
second = int(input())
used = 0
if first <= 0:
    print("ERROR")
elif fuel - first >= 3:
    fuel -= first
    used += first
    print("GO")
else:
    print("DENIED")
if second <= 0:
    print("ERROR")
elif fuel - second >= 3:
    fuel -= second
    used += second
    print("GO")
else:
    print("DENIED")
print(fuel, used)
```

פלט:

```text
ERROR
GO
3 17
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 23 7
INVALID 2
3 15 15
4 3 27
STOP 5
Done: 3
Left: 3
```

### ב. פלט התרחיש השני

```text
1 21 9
2 12 18
3 3 27
STOP 4
Done: 3
Left: 3
```

### ג. תשובות והערות לדיון

ענף הנתון השגוי מונע את ביצוע העדכונים באותה איטרציה;

running=False מסיים את המסלול משום שתנאי הלולאה כבר אינו מתקיים.

done סופר הצלחות בלבד.

while ללא התקדמות במקרה כשל עלול לחזור לנצח.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
30
4
4
2
5
2
3
3
1
1
```

```python
fuel = int(input())
count = int(input())
done = 0
distance = 0
running = True
index = 0
while index < count and running:
    step = index
    index += 1
    length = int(input())
    rate = int(input())
    if length <= 0 or rate <= 0:
        print("ERROR")
        running = False
    else:
        cost = length * rate
        if fuel - cost < 3:
            print("STOP")
            running = False
        else:
            fuel -= cost
            distance += length
            done += 1
            print(step + 1, fuel)
print(done, distance, fuel)
```

פלט:

```text
1 22
2 12
3 3
STOP
3 12 3
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
1 6 24
2 15 9
3 2 7
STOP 4
[24, 9, 7]
Used: 23
Unread: 2
```

### ב. פלט התרחיש השני

```text
1 6 28
2 15 13
3 2 11
4 8 3
STOP 5
[28, 13, 11, 3]
Used: 31
Unread: 1
```

### ג. תשובות והערות לדיון

האינדקס משייך קצב למקטע הנכון.

Unread הוא מספר המקטעים שלא הושלמו, כולל המקטע שנבדק ונדחה, לכן Remaining מתאים יותר.

יש לבדוק שוויון אורכים.

### ד. פתרון אפשרי

```python
distances = [3, 5, 2, 4, 1]
rates = [2, 3, 1, 2, 4]
fuel = 40
completed = []
costs = []
running = True
index = 0
while index < len(distances) and running:
    i = index
    index += 1
    cost = distances[i] * rates[i]
    if fuel - cost < 3:
        running = False
    else:
        fuel -= cost
        completed.append(i + 1)
        costs.append(cost)
print(completed)
print(costs)
print("Left:", fuel)
```

פלט:

```text
[1, 2, 3, 4, 5]
[6, 15, 2, 8, 4]
Left: 5
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[24, 9, 7]
[34, 19, 17, 9]
True
```

### ב. פלט התרחיש השני

```text
[24, 9, 7]
[34, 19, 17, 9]
False
```

### ג. תשובות והערות לדיון

הפונקציה בודקת בלבד ולכן אינה צורכת משאב.

בדיקת עלות ובדיקת היתכנות אפשר להריץ בנפרד.

עם fuel=15,cost=12,reserve=3 המקטע חוקי;

> דוחה אותו.

### ד. פתרון אפשרי

```python
def segment_cost(distance, rate):
    return distance * rate
def can_drive(fuel, cost, reserve):
    return cost > 0 and fuel - cost >= reserve
def route(distances, rates, fuel, reserve):
    history = []
    if len(distances) != len(rates) or fuel < reserve:
        return history
    running = True
    index = 0
    while index < len(distances) and running:
        i = index
        index += 1
        cost = segment_cost(distances[i], rates[i])
        if not can_drive(fuel, cost, reserve):
            running = False
        else:
            fuel -= cost
            history.append(fuel)
    return history
print(route([3, 5, 2, 4], [2, 3, 1, 2], 30, 3))
print(route([3, 5, 2, 4], [2, 3, 1, 2], 30, 8))
print(route([3, 5], [2], 30, 3))
```

פלט:

```text
[24, 9, 7]
[24, 9]
[]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
True
True
True
False
3 9 [15, 3]
9 5 [9]
```

### ב. פלט התרחיש השני

```text
True
True
True
False
3 9 [15, 3]
6 5 [6]
```

### ג. תשובות והערות לדיון

לכל רכב היסטוריה עצמאית.

בכשל fuel,distance,history אינם משתנים.

פעולה שמחשבת (fuel-reserve)//rate עבור rate חיובי היא קריאה בלבד.

### ד. פתרון אפשרי

```python
class Vehicle:
    def __init__(self, fuel, reserve):
        self.fuel = fuel
        self.reserve = reserve
        self.distance = 0
        self.history = []

    def drive(self, length, rate):
        cost = length * rate
        if length <= 0 or rate <= 0 or self.fuel - cost < self.reserve:
            return False
        self.fuel -= cost
        self.distance += length
        self.history.append(self.fuel)
        return True

    def refuel(self, amount):
        if amount > 0:
            self.fuel += amount
            if self.fuel > 40:
                self.fuel = 40

a = Vehicle(8, 3)
b = Vehicle(20, 3)
print(a.drive(4, 2))
a.refuel(50)
print(a.fuel)
print(a.drive(4, 2))
print(b.drive(3, 2))
print(a.fuel, a.distance, a.history)
print(b.fuel, b.distance, b.history)
```

פלט:

```text
False
40
True
True
32 4 [32]
14 3 [14]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

# פתרונות למורה: פאנלים סולאריים: איך מנהלים אנרגיה לאורך היום?

[חזרה למשימת התלמיד](../06_solar_panels.md)

כל פתרון הוא דרך אפשרית. יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט. מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה. הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Generated: 8 | Demand: 5
Battery: 3
```

המפריד end מאפשר השוואה בשורה אחת.

### ב. שינוי ודיון

Generated: 8Demand: 5; אין מפריד בין שני שדות.

### ג. פתרון אפשרי

```python
print("Generated: 4", end=" | ")
print("Demand: 6")
print("Battery: 0", end=" | ")
print("GRID")
```

פלט:

```text
Generated: 4 | Demand: 6
Battery: 0 | GRID
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
Net: 3
Battery: 5
```

net הוא שינוי אנרגיה בפרק אחד; battery היא כמות מצטברת.

### ב. שינוי ודיון

Net: 7, Battery: 9. קיבולת 6, לכן דרוש תנאי.

### ג. פתרון אפשרי

```python
battery = 1
generated = 5
demand = 3
battery += generated - demand
print(battery)
generated = 4
demand = 1
battery += generated - demand
print(battery)
```

פלט:

```text
3
6
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Net: -3
```

net שלילי מייצג חוסר בפרק; אינו מלאי.

### ב. שינוי ודיון

First: -4, Second: 5, Total: 1; עדיין עלול להיות חוסר בשעה הראשונה.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
1
5
7
3
```

```python
g1 = int(input())
d1 = int(input())
g2 = int(input())
d2 = int(input())
first = g1 - d1
second = g2 - d2
print("First:", first)
print("Second:", second)
print("Total:", first + second)
```

פלט:

```text
First: -4
Second: 4
Total: 0
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
6 0 3
```

סוללה לפני הגבלה 9; צריך לייצא 3 ולהחזיק רק 6.

### ב. שינוי ודיון

0 1 0; נדרש לקנות יחידה אחת אחרי שימוש בארבע שהיו בסוללה.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
3
1
6
```

```python
battery = int(input())
generated = int(input())
demand = int(input())
net = generated - demand
imported = 0
exported = 0
battery += net
if battery > 8:
    exported = battery - 8
    battery = 8
elif battery < 2:
    imported = 2 - battery
    battery = 2
print(battery, imported, exported)
```

פלט:

```text
2 4 0
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
0 2 0
6 2 2
2 2 2
```

הדוח מסכם את כל היום. רק net מתחלף בכל פרק.

### ב. שינוי ודיון

6 0 4; 2 0 4; 0 2 4. אותם ערכי net, תוצאות אגירה וייצוא שונות.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
3
1
5
12
4
0
8
```

```python
count = int(input())
battery = 2
imported = 0
exported = 0
for hour in range(count):
    generated = int(input())
    demand = int(input())
    battery += generated - demand
    if battery > 6:
        exported += battery - 6
        battery = 6
    elif battery < 0:
        imported += -battery
        battery = 0
print(battery, imported, exported)
```

פלט:

```text
0 4 2
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[0, 6, 2, 6, 0]
```

היסטוריית הסוללה לבדה לא מראה מה קנינו ומה ייצאנו.

### ב. שינוי ודיון

עלול להיות IndexError. אם len שונה, דחו את הקלט או הגדירו כלל מפורש לגבי פרקים חסרים.

### ג. פתרון אפשרי

```python
generated = [1, 12, 1, 9, 0]
demand = [5, 4, 5, 3, 8]
battery = 2
history = []
buy = []
sell = []
for i in range(len(generated)):
    battery += generated[i] - demand[i]
    imported = 0
    exported = 0
    if battery > 6:
        exported = battery - 6
        battery = 6
    elif battery < 0:
        imported = -battery
        battery = 0
    history.append(battery)
    buy.append(imported)
    sell.append(exported)
print(history)
print(buy)
print(sell)
```

פלט:

```text
[0, 6, 2, 6, 0]
[2, 0, 0, 0, 2]
[0, 2, 0, 2, 0]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
[0, 3, 0]
[6, 0, 2]
```

אינדקס 0 הוא סוללה; אינדקס 1 מתאר רכישה בפרק הקודם.

### ב. שינוי ודיון

[0,3,0] ואז [4,0,4].

### ג. פתרון אפשרי

```python
def balance(battery, net, capacity):
    imported = 0
    exported = 0
    battery += net
    if battery > capacity:
        exported = battery - capacity
        battery = capacity
    elif battery < 0:
        imported = -battery
        battery = 0
    return [battery, imported, exported]

def day(nets, capacity, battery):
    total_buy = 0
    total_sell = 0
    for net in nets:
        state = balance(battery, net, capacity)
        battery = state[0]
        total_buy += state[1]
        total_sell += state[2]
    return [battery, total_buy, total_sell]

print(day([-4, 8, -4, 6, -8], 6, 2))
```

פלט:

```text
[0, 4, 4]
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
3 0 4
0 4 0
```

כל בניין צריך דוח עצמאי; רכישה של b לא שייכת ל-a.

### ב. שינוי ודיון

a מסיימת 3 0 0; b נותרת 0 4 0.

### ג. פתרון אפשרי

```python
class SolarSystem:
    def __init__(self, capacity, battery, reserve):
        self.capacity = capacity
        self.battery = battery
        self.reserve = reserve
        self.buy = 0
        self.sell = 0

    def period(self, net):
        self.battery += net
        if self.battery > self.capacity:
            self.sell += self.battery - self.capacity
            self.battery = self.capacity
        elif self.battery < self.reserve:
            self.buy += self.reserve - self.battery
            self.battery = self.reserve

a = SolarSystem(6, 3, 2)
b = SolarSystem(4, 1, 1)
a.period(-4)
a.period(5)
b.period(-3)
print(a.battery, a.buy, a.sell)
print(b.battery, b.buy, b.sell)
```

פלט:

```text
6 3 1
1 3 0
```

---

## אתגר מסכם

אין פתרון יחיד. בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית. אין לדרוש נושא תכנות שלא נלמד.

# פתרונות למורה: מערכת ניווט: המסלול הקצר אינו תמיד המסלול המהיר

[חזרה למשימת התלמיד](../14_navigation_system.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
ROUTE A | FAST
Time: 32 min | Distance: 18 km
Toll: 5 | SELECTED
```

### ב. פלט התרחיש השני

```text
ROUTE A | FAST
Time: 32
Distance: 18 km | Toll: 5 | SELECTED
```

### ג. תשובות והערות לדיון

\n מסיים שורה, end ריק לא.

Distance עובר לשורה הבאה ו-Toll נצמד אליו.

זמן ומרחק שונים ולא ניתן להסיק אחד מהשני.

### ד. פתרון אפשרי

```python
print("ROUTE ", end="")
print("B", end=" | ")
print("CHEAP")
print("Time: ", end="")
print("40", end=" min | ")
print("Distance: ", end="")
print("12", end=" km\n")
print("Toll: ", end="")
print("0", end=" | ")
print("SELECTED")
```

פלט:

```text
ROUTE B | CHEAP
Time: 40 min | Distance: 12 km
Toll: 0 | SELECTED
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
17 12 29
21 11 32
Final: 42
```

### ב. פלט התרחיש השני

```text
17 12 29
25 11 36
Final: 46
```

### ג. תשובות והערות לדיון

total_a נגזר מהנתונים המעודכנים.

חישוב ישן יטעה את המשתמש.

זמן בסיס מתאר נסיעה ללא עומס ועיכוב משתנה;

הפרדה מאפשרת עדכון.

### ד. פתרון אפשרי

```python
a1 = 8 + 2
a2 = 12 + 5
a3 = 7 + 1
b1 = 15 + 0
b2 = 9 + 2
a = a1 + a2 + a3
b = b1 + b2
print(a1, a2, a3)
print(b1, b2)
print("A:", a)
print("B:", b)
print("Difference:", a - b)
```

פלט:

```text
10 17 8
15 11
A: 35
B: 26
Difference: 9
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 24 2
B: 28 10
Time gap: -4
Price gap: 8
```

### ב. פלט התרחיש השני

```text
A: 24 -5
B: 28 10
Time gap: -4
Price gap: 15
```

### ג. תשובות והערות לדיון

יתרה שלילית מסלול לא חוקי;

הפרש זמן שלילי מציין A מהיר יותר.

צריך לדעת מהי מטרת הבחירה וכללי שוויון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
18
7
4
12
22
2
0
18
8
```

```python
base_a = int(input())
delay_a = int(input())
toll_a = int(input())
distance_a = int(input())
base_b = int(input())
delay_b = int(input())
toll_b = int(input())
distance_b = int(input())
budget = int(input())
time_a = base_a + delay_a
time_b = base_b + delay_b
print("A:", time_a, budget - toll_a, distance_a)
print("B:", time_b, budget - toll_b, distance_b)
print("Time gap:", time_a - time_b)
print("Distance gap:", distance_a - distance_b)
```

פלט:

```text
A: 25 4 12
B: 24 8 18
Time gap: 1
Distance gap: -6
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
True True
Selected: B
```

### ב. פלט התרחיש השני

```text
False True
Selected: B
```

### ג. תשובות והערות לדיון

מהירות אינה עוקפת תקציב.

<= משאיר את A בשוויון.

למשל תקציב 4 ומחירים 8 ו-5 יגרום ל-NONE.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
20
8
22
4
5
```

```python
time_a = int(input())
toll_a = int(input())
time_b = int(input())
toll_b = int(input())
budget = int(input())
chosen = "NONE"
if toll_a <= budget:
    chosen = "A"
    best_time = time_a
    best_toll = toll_a
if toll_b <= budget:
    if chosen == "NONE":
        chosen = "B"
        best_time = time_b
        best_toll = toll_b
    elif time_b < best_time or (time_b == best_time and toll_b < best_toll):
        chosen = "B"
        best_time = time_b
        best_toll = toll_b
if chosen == "NONE":
    print(chosen)
else:
    print(chosen, best_time, best_toll)
```

פלט:

```text
B 22 4
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
UPDATE 1 30 0
SKIP 2
UPDATE 3 26 5
UPDATE 4 26 3
KEEP 4
Best: 4 26 3
```

### ב. פלט התרחיש השני

```text
SKIP 1
SKIP 2
UPDATE 3 24 5
KEEP 3
UPDATE 5 23 6
Best: 5 23 6
```

### ג. תשובות והערות לדיון

מזהה -1 מאפשר לקלוט מועמד חוקי ראשון גם אם זמן חיובי.

תנאים עם < בלבד לא מחליפים בשוויון מלא.

אם כולם נפסלים מוצג -1 0 0;

עדיף NONE.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
4
8
25
4
12
25
4
10
20
9
5
25
3
15
```

```python
count = int(input())
budget = int(input())
best_id = -1
best_time = 0
best_price = 0
best_distance = 0
skipped = 0
for i in range(count):
    time = int(input())
    price = int(input())
    distance = int(input())
    if price > budget:
        skipped += 1
    else:
        if best_id == -1 or time < best_time or (time == best_time and price < best_price) or (time == best_time and price == best_price and distance < best_distance):
            best_id = i + 1
            best_time = time
            best_price = price
            best_distance = distance
if best_id == -1:
    print("NONE")
else:
    print(best_id, best_time, best_price, best_distance)
print("Skipped:", skipped)
```

פלט:

```text
4 25 3 15
Skipped: 1
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[25, 23, 24, 25]
[0, 2, 3]
Best index: 2
```

### ב. פלט התרחיש השני

```text
[25, 23, 30, 25]
[0, 2, 3]
Best index: 3
```

### ג. תשובות והערות לדיון

times מייצגת את כל המידע, eligible מייצגת חוקיות.

אינדקס מאפשר לחזור למחיר ולמרחק.

אינדקס -1 ניגש לפריט האחרון בפייתון;

תנאי קצר מונע בחירה שגויה.

### ד. פתרון אפשרי

```python
bases = [18, 20, 24, 19]
delays = [7, 3, 0, 6]
prices = [4, 6, 0, 2]
times = []
for i in range(len(bases)):
    times.append(bases[i] + delays[i])
budgets = [0, 2, 5, 10]
choices = []
for budget in budgets:
    best = -1
    for i in range(len(times)):
        if prices[i] <= budget:
            if best == -1 or times[i] < times[best] or (times[i] == times[best] and prices[i] < prices[best]):
                best = i
    choices.append(best)
print(times)
print(choices)
```

פלט:

```text
[25, 23, 24, 25]
[2, 2, 2, 1]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[25, 23, 24]
2
1
2
```

### ב. פלט התרחיש השני

```text
[25, 23, 24]
0
1
-1
```

### ג. תשובות והערות לדיון

אינדקס מזהה את המסלול וכל נתוניו.

-1 מסמן שאין חלופה.

שינוי תקציב משנה בחירה בלבד, לא נתוני המסלול.

### ד. פתרון אפשרי

```python
def choose(times, prices, budget, mode):
    if len(times) != len(prices) or (mode != 1 and mode != 2):
        return -1
    best = -1
    for i in range(len(times)):
        if not (prices[i] > budget):
            if best == -1:
                best = i
            elif mode == 1:
                if times[i] < times[best] or (times[i] == times[best] and prices[i] < prices[best]):
                    best = i
            else:
                if prices[i] < prices[best] or (prices[i] == prices[best] and times[i] < times[best]):
                    best = i
    return best
times = [25, 23, 24]
prices = [4, 6, 2]
print(choose(times, prices, 6, 1))
print(choose(times, prices, 6, 2))
print(choose(times, prices, 1, 1))
print(choose(times, [4], 6, 1))
```

פלט:

```text
1
2
-1
-1
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
2
1
0
1
[2, 0]
[1, 1]
```

### ב. פלט התרחיש השני

```text
2
1
2
1
[2, 2]
[1, 1]
```

### ג. תשובות והערות לדיון

תקציבים שונים מסננים חלופות שונות.

ההיסטוריה שומרת אינדקסים, ולכן שינוי הזמנים אינו מוחק החלטות קודמות.

צריך לבחור שוב לאחר שינוי תקציב.

### ד. פתרון אפשרי

```python
class Navigator:
    def __init__(self, budget):
        self.budget = budget
        self.selected = -1
        self.history = []
        self.changes = 0
    def choose(self, times, prices):
        best = -1
        for i in range(len(times)):
            if not (prices[i] > self.budget):
                if best == -1 or times[i] < times[best] or (times[i] == times[best] and prices[i] < prices[best]):
                    best = i
        if len(self.history) > 0 and self.selected != best:
            self.changes += 1
        self.selected = best
        self.history.append(best)
        return best
    def set_budget(self, amount):
        if amount >= 0:
            self.budget = amount
a = Navigator(5)
b = Navigator(8)
times = [25, 23, 24]
prices = [4, 6, 0]
print(a.choose(times, prices))
print(b.choose(times, prices))
times[2] += 5
print(a.choose(times, prices))
print(b.choose(times, prices))
a.set_budget(8)
a.choose(times, prices)
print(a.history, a.changes)
print(b.history, b.changes)
```

פלט:

```text
2
1
0
1
[2, 0, 1] 2
[1, 1] 0
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

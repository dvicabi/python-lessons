# פתרונות למורה: חברת משלוחים: מי צריך לקבל את החבילה קודם?

[חזרה למשימת התלמיד](../16_delivery_company.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
ORDER 104 | PRIORITY 1
Weight: 4 kg | Time: 12 min
Truck: A | ASSIGNED
```

### ב. פלט התרחיש השני

```text
ORDER 104 | PRIORITY 1
Weight: 4
Time: 12 | Truck: A | ASSIGNED
```

### ג. תשובות והערות לדיון

המשקל והזמן מוצגים בשורה אחת.

end משנה רק את מיקום הטקסט.

בתרחיש השני זמן מתחבר לשדה Truck.

### ד. פתרון אפשרי

```python
print("ORDER ", end="")
print("208", end=" | ")
print("PRIORITY 2")
print("Weight: ", end="")
print("7", end=" kg | ")
print("Time: ", end="")
print("18", end=" min\n")
print("Truck: ", end="")
print("B", end=" | ")
print("WAITING")
```

פלט:

```text
ORDER 208 | PRIORITY 2
Weight: 7 kg | Time: 18 min
Truck: B | WAITING
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
14 33 1
10 18 2
3 8 3
Used: 17 37
```

### ב. פלט התרחיש השני

```text
14 33 1
10 13 2
3 3 3
Used: 17 42
```

### ג. תשובות והערות לדיון

שני משאבים עצמאיים.

צריכה=התחלה-יתרה.

השמה ל-1 מוחקת את מספר ההקצאות המצטבר.

### ד. פתרון אפשרי

```python
weight_left = 25
time_left = 60
assigned = 0
weight_left -= 5
time_left -= 20
assigned += 1
print(weight_left, time_left, assigned)
weight_left -= 8
time_left -= 12
assigned += 1
print(weight_left, time_left, assigned)
weight_left -= 6
time_left -= 18
assigned += 1
print(weight_left, time_left, assigned)
print("Used:", 25 - weight_left, 60 - time_left)
```

פלט:

```text
20 40 1
12 28 2
6 10 3
Used: 19 50
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
After 1: 14 33
After 2: 7 13
Used: 13 32
```

### ב. פלט התרחיש השני

```text
After 1: 14 13
After 2: 7 -7
Used: 13 32
```

### ג. תשובות והערות לדיון

בתרחיש השני זמן הופך שלילי אף שהמשקל מספיק.

שני המשאבים מגבילים באופן עצמאי.

יש לבדוק שניהם לפני הקצאה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
20
45
5
10
8
20
4
16
```

```python
weight_left = int(input())
time_left = int(input())
w1 = int(input())
t1 = int(input())
w2 = int(input())
t2 = int(input())
w3 = int(input())
t3 = int(input())
weight_left -= w1
time_left -= t1
print(weight_left, time_left)
weight_left -= w2
time_left -= t2
print(weight_left, time_left)
weight_left -= w3
time_left -= t3
print(weight_left, time_left)
print("Used:", w1 + w2 + w3, t1 + t2 + t3)
```

פלט:

```text
15 35
7 15
3 -1
Used: 17 46
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
NO
YES
5 10 1
```

### ב. פלט התרחיש השני

```text
YES
NO
3 0 1
```

### ג. תשובות והערות לדיון

AND דורש התאמה בשני משאבים;

OR עלול להקצות למרות חריגה.

שוויון חוקי וזמן פנוי הופך 0.

החבילה השנייה עשויה להיות קטנה יותר.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
10
25
7
30
5
15
```

```python
weight_left = int(input())
time_left = int(input())
w1 = int(input())
t1 = int(input())
w2 = int(input())
t2 = int(input())
assigned = 0
if w1 <= 0 or t1 <= 0:
    print("ERROR")
elif w1 <= weight_left and t1 <= time_left:
    weight_left -= w1
    time_left -= t1
    assigned += 1
    print("ASSIGNED")
else:
    print("WAIT")
if w2 <= 0 or t2 <= 0:
    print("ERROR")
elif w2 <= weight_left and t2 <= time_left:
    weight_left -= w2
    time_left -= t2
    assigned += 1
    print("ASSIGNED")
else:
    print("WAIT")
print(weight_left, time_left, assigned)
```

פלט:

```text
WAIT
ASSIGNED
5 10 1
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 ASSIGNED 11 30
2 ASSIGNED 3 5
3 WAIT
4 ERROR
5 WAIT
6 ASSIGNED 2 3
3 2 1
```

### ב. פלט התרחיש השני

```text
1 ASSIGNED 5 10
2 WAIT
3 ASSIGNED 2 5
4 ASSIGNED 1 4
5 ERROR
6 WAIT
3 2 1
```

### ג. תשובות והערות לדיון

חבילה אחרת עשויה להתאים.

סכום assigned+waiting+errors שווה למספר האירועים שנקראו.

משאבים עלולים להיגמר לפני הגעת חבילה דחופה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
12
30
6
10
2
5
12
1
2
6
1
1
5
3
1
2
2
```

```python
count = int(input())
weight_left = int(input())
time_left = int(input())
assigned = 0
urgent_done = 0
urgent_wait = 0
errors = 0
for i in range(count):
    w = int(input())
    t = int(input())
    priority = int(input())
    if w <= 0 or t <= 0 or (priority != 1 and priority != 2):
        errors += 1
        continue
    if w <= weight_left and t <= time_left:
        assigned += 1
        weight_left -= w
        time_left -= t
        if priority == 1:
            urgent_done += 1
    elif priority == 1:
        urgent_wait += 1
print(assigned, urgent_done, urgent_wait, errors)
print(weight_left, time_left)
```

פלט:

```text
3 1 1 1
0 6
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
4 10 24
2 6 14
3 3 6
[4, 2, 3]
```

### ב. פלט התרחיש השני

```text
4 10 28
2 6 18
1 1 0
[4, 2, 1]
```

### ג. תשובות והערות לדיון

המועמד הטוב תלוי במשאבים אחרי כל הקצאה.

ללא דילוג ניתן להקצות אותה חבילה שוב.

כאשר אין מועמד מתאים נשאר best=-1 ועוצרים;

מספר ההקצאות מוגבל לאורך הרשימה.

שינוי סדר הקריטריונים יכול לבחור חבילה לא דחופה לפני דחופה.

### ד. פתרון אפשרי

```python
weights = [6, 5, 4, 3, 2]
durations = [12, 18, 10, 8, 6]
priorities = [2, 1, 1, 2, 1]
weight_left = 12
time_left = 30
selected = []
urgent = 0
while True:
    best = -1
    for i in range(len(weights)):
        if i in selected or weights[i] > weight_left or durations[i] > time_left:
            continue
        if best == -1 or durations[i] < durations[best] or (durations[i] == durations[best] and priorities[i] < priorities[best]):
            best = i
    if best == -1:
        break
    selected.append(best)
    weight_left -= weights[best]
    time_left -= durations[best]
    if priorities[best] == 1:
        urgent += 1
waiting_indexes = []
for i in range(len(weights)):
    if i not in selected:
        waiting_indexes.append(i)
print(selected)
print(waiting_indexes)
print(weight_left, time_left, urgent)
```

פלט:

```text
[4, 3, 2]
[0, 1]
3 6 2
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[4, 2, 3]
[4, 2, 1]
[]
```

### ב. פלט התרחיש השני

```text
[3, 0, 4]
[3, 0, 4]
[]
```

### ג. תשובות והערות לדיון

choose היא בחירה ללא שינוי.

return מסיים את plan ומחזיר הקצאות.

בדקו אין מועמד, מועמד שכבר נבחר, שוויון עדיפות וזמן, ומועמד שלא מתאים למשאבים.

### ד. פתרון אפשרי

```python
def choose(weights, durations, priorities, selected, w, t):
    best = -1
    for i in range(len(weights)):
        if weights[i] <= 0 or durations[i] <= 0 or priorities[i] <= 0:
            continue
        if i in selected or weights[i] > w or durations[i] > t:
            continue
        if best == -1 or priorities[i] < priorities[best] or (priorities[i] == priorities[best] and durations[i] < durations[best]):
            best = i
    return best

def plan(weights, durations, priorities, w, t):
    if len(weights) != len(durations) or len(weights) != len(priorities) or w < 0 or t < 0:
        return []
    selected = []
    while True:
        i = choose(weights, durations, priorities, selected, w, t)
        if i == -1:
            return [selected, w, t]
        selected.append(i)
        w -= weights[i]
        t -= durations[i]

print(plan([6, 5, 4, 3, 2], [12, 18, 10, 8, 6], [2, 1, 1, 2, 1], 12, 30))
print(plan([6, 5, 4, 3, -2], [12, 18, 10, 8, 6], [2, 1, 1, 2, 1], 12, 30))
```

פלט:

```text
[[4, 2, 3], 3, 6]
[[2, 1], 3, 2]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
True
True
False
False
True
7 12 [104]
0 0 [107, 109]
```

### ב. פלט התרחיש השני

```text
True
True
True
False
True
3 1 [104, 108]
0 0 [107, 109]
```

### ג. תשובות והערות לדיון

can_take היא בדיקה בלבד.

take דוחה מזהה שכבר הוקצה באותו רכב.

כדי למנוע כפילות בין רכבים דרושה רשימת הקצאות מרכזית או בדיקה בשניהם לפני שינוי.

### ד. פתרון אפשרי

```python
class Truck:
    def __init__(self, weight, time):
        self.weight = weight
        self.time = time
        self.assigned = []

    def can_take(self, weight, duration):
        return weight > 0 and duration > 0 and weight <= self.weight and duration <= self.time

    def take(self, order, weight, duration):
        if order in self.assigned or not self.can_take(weight, duration):
            return False
        self.weight -= weight
        self.time -= duration
        self.assigned.append(order)
        return True

class Dispatch:
    def __init__(self, trucks):
        self.trucks = trucks
        self.assigned = []

    def assign(self, order, weight, duration):
        if order in self.assigned:
            return -1
        for i in range(len(self.trucks)):
            if self.trucks[i].take(order, weight, duration):
                self.assigned.append(order)
                return i
        return -1

a = Truck(12, 30)
b = Truck(8, 25)
dispatch = Dispatch([a, b])
print(dispatch.assign(104, 5, 18))
print(dispatch.assign(107, 4, 15))
print(dispatch.assign(104, 1, 1))
print(dispatch.assign(109, 9, 20))
print(dispatch.assign(110, 4, 10))
print(a.weight, a.time, a.assigned)
print(b.weight, b.time, b.assigned)
print(dispatch.assigned)
```

פלט:

```text
0
1
-1
-1
0
3 2 [104, 110]
4 10 [107]
[104, 107, 110]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

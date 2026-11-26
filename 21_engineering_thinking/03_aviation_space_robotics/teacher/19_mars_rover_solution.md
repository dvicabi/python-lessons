# פתרונות למורה: רובוט מחקר במאדים: כמה רחוק אפשר לחקור ועדיין לחזור?

[חזרה למשימת התלמיד](../19_mars_rover.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
ROVER 07 | SIM
Position: 4 units
Energy: 18 | Return: 4
Samples: 2 | READY
```

### ב. פלט התרחיש השני

```text
ROVER  | 07 | SIM
Position: 4 units
Energy: 18 | Return: 4
Samples: 2 | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("ROVER ", end="")
print("08", end="")
print(" | SIM")
print("Position: ", end="")
print("9", end="")
print(" units")
print("Energy: ", end="")
print("11", end="")
print(" | Return: 9")
print("Samples: ", end="")
print("3", end="")
print(" | LIMITED")
```

פלט:

```text
ROVER 08 | SIM
Position: 9 units
Energy: 11 | Return: 9
Samples: 3 | LIMITED
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
4 26 0
4 23 1
9 15 2
Return margin: 6
Check: 30 9
```

### ב. פלט התרחיש השני

```text
4 26 0
4 23 1
10 14 2
Return margin: 4
Check: 30 10
```

### ג. תשובות והערות לדיון

travel הוא מרחק מצטבר;

position מיקום נוכחי.

איסוף צורך משאב ללא תנועה.

energy-position הוא המרווח אחרי החזרה.

מרחק מצטבר אינו מתאפס בחזרה.

### ד. פתרון אפשרי

```python
position = 0
energy = 40
samples = 0
travel = 0
position += 6
energy -= 6
travel += 6
print(position, energy, samples)
energy -= 3
samples += 1
print(position, energy, samples)
position += 4
energy -= 4
travel += 4
print(position, energy, samples)
energy -= 3
samples += 1
print(position, energy, samples)
position -= 7
energy -= 7
travel += 7
print(position, energy, samples)
print(travel, energy - position)
```

פלט:

```text
6 34 0
6 31 1
10 27 1
10 24 2
3 17 2
17 14
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
4 36 32
Sample 1: 33
8 29 21
Sample 2: 26
12 22 10
Sample 3: 19
After return: 7
```

### ב. פלט התרחיש השני

```text
4 21 17
Sample 1: 18
8 14 6
Sample 2: 11
12 7 -5
Sample 3: 4
After return: -8
```

### ג. תשובות והערות לדיון

הרובוט מתחיל מקטע מהמיקום הקודם.

מרווח שלילי מפר את כלל החזרה.

חישוב ללא תנאים לא חוסם פעולה.

במקטע חזרה נדרש מרחק חיובי באמצעות תנאי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
35
3
6
10
```

```python
energy = int(input())
first = int(input())
second = int(input())
third = int(input())
cost1 = first
cost2 = second - first
cost3 = third - second
spent = cost1 + cost2 + cost3 + 9
energy -= spent
print(cost1, cost2, cost3)
print("Collect:", 9)
print("Spent:", spent)
print("Margin:", energy - third)
```

פלט:

```text
3 3 4
Collect: 9
Spent: 19
Margin: 6
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
MOVE 9 10
NO SAMPLE
9 10 1
Margin: 1
```

### ב. פלט התרחיש השני

```text
MOVE 9 9
NO SAMPLE
9 9 1
Margin: 0
```

### ג. תשובות והערות לדיון

תנאי הסף חייב להיבדק לפני שינוי.

איסוף עולה עוד 3 ולכן דורש מרווח נפרד.

בקוד האיסוף מתבצע במיקום הנוכחי גם כשלא בוצעה תנועה;

אם נדרש איסוף רק ביעד יש לשמור דגל הצלחה.

יעד 0 צורך מרחק מהמיקום אך לא דורש יתרת חזרה נוספת.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
4
17
9
```

```python
position = int(input())
energy = int(input())
target = int(input())
samples = 0
distance = target - position
if distance < 0:
    distance = -distance
if target < 0 or target > 12:
    print("INVALID")
elif energy - distance < target:
    print("DENIED")
else:
    position = target
    energy -= distance
    print("MOVE")
    if position == 0 or energy - 3 < position:
        print("NO SAMPLE")
    else:
        energy -= 3
        samples += 1
        print("SAMPLE")
print(position, energy, samples)
```

פלט:

```text
MOVE
SAMPLE
9 9 1
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
MOVE
1 4 23 0
SAMPLE
2 4 20 1
MOVE
3 9 15 1
SAMPLE
4 9 12 2
DENIED MOVE
5 9 12 2
SAMPLE
6 9 9 3
MOVE
7 0 0 3
Denied: 1
```

### ב. פלט התרחיש השני

```text
MOVE
1 4 23 0
SAMPLE
2 4 20 1
MOVE
3 10 14 1
SAMPLE
4 10 11 2
DENIED MOVE
5 10 11 2
DENIED SAMPLE
6 10 11 2
MOVE
7 0 1 2
Denied: 2
```

### ג. תשובות והערות לדיון

הבקשה לאיסוף היא במיקום נוכחי;

אפשר להגדיר קלט שונה לפי סוג.

תמיד energy>=position.

במודל הבדוי לא מוציאים אנרגיה עבור בקשה שלא בוצעה;

במודל אחר אולי יש עלות ניסיון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
27
4
1
9
1
12
1
4
1
0
0
```

```python
count = int(input())
energy = int(input())
position = 0
samples = 0
move_denied = 0
sample_denied = 0
for i in range(count):
    target = int(input())
    collect = int(input())
    distance = target - position
    if distance < 0:
        distance = -distance
    if target < 0 or target > 12 or energy - distance < target:
        move_denied += 1
    else:
        position = target
        energy -= distance
        if collect == 1:
            if position > 0 and energy - 3 >= position:
                energy -= 3
                samples += 1
            else:
                sample_denied += 1
    print(i + 1, position, energy, samples)
print(move_denied, sample_denied)
```

פלט:

```text
1 4 20 1
2 9 12 2
3 9 12 2
4 4 4 3
5 0 0 3
1 0
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
0 4 25 [4]
1 8 18 [4, 8]
2 4 14 [4, 8]
DENIED 3
4 2 9 [4, 8, 2]
5 0 7 [4, 8, 2]
DENIED 6
[4, 8, 4, 2, 0]
[4, 8, 2]
[3, 6]
Margin: 7
```

### ב. פלט התרחיש השני

```text
0 4 22 [4]
1 8 15 [4, 8]
2 4 11 [4, 8]
DENIED 3
4 2 6 [4, 8, 2]
5 0 4 [4, 8, 2]
DENIED 6
[4, 8, 4, 2, 0]
[4, 8, 2]
[3, 6]
Margin: 4
```

### ג. תשובות והערות לדיון

visited היא היסטוריית תנועה, sampled נקודות ייחודיות, denied אינדקסי תנועה שנדחתה.

membership מונע איסוף כפול.

יוצרים רשימת אינדקסים/מסלול חדשה ולא משנים את targets.

### ד. פתרון אפשרי

```python
targets = [4, 8, 4, 10, 2, 0, 7]
values = [5, 12, 30, 15, 4, 0, 9]
energy = 32
position = 0
sampled = []
indexes = []
score = 0
for i in range(len(targets)):
    target = targets[i]
    distance = target - position
    if distance < 0:
        distance = -distance
    if target >= 0 and target <= 12 and energy - distance >= target:
        position = target
        energy -= distance
        if position > 0 and position not in sampled and energy - 3 >= position:
            sampled.append(position)
            indexes.append(i)
            energy -= 3
            score += values[i]
print(sampled)
print(indexes)
print(score, position, energy)
```

פלט:

```text
[4, 8, 2]
[0, 1, 4]
21 0 7
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[9, 10, True]
[9, 9, True]
[[4, 8], [[4, 25], [8, 18], [4, 14], [4, 14], [0, 10]]]
[[4, 8], [[4, 15], [8, 8], [4, 4], [4, 4], [0, 0]]]
```

### ב. פלט התרחיש השני

```text
[9, 10, True]
[4, 14, False]
[[4, 8], [[4, 25], [8, 18], [4, 14], [4, 14], [0, 10]]]
[[4, 8], [[4, 15], [8, 8], [8, 8], [8, 8], [8, 8]]]
```

### ג. תשובות והערות לדיון

הדגל מבדיל תנועה שנדחתה מתנועה ללא שינוי מיקום.

מעבר שבו נשארת בדיוק אנרגיית החזרה חוקי.

רשימה חדשה שומרת צילום מצב עצמאי.

בודקים יעד חוקי, מחוץ לטווח, תנועה חזרה וגבול אנרגיה.

### ד. פתרון אפשרי

```python
def move(position, energy, target):
    distance = target - position
    if distance < 0:
        distance = -distance
    if target < 0 or target > 12 or energy - distance < target:
        return [position, energy, False]
    return [target, energy - distance, True]

def collect(position, energy, sampled):
    if position > 0 and position not in sampled and energy - 3 >= position:
        sampled.append(position)
        return energy - 3
    return energy

def mission(targets, energy):
    position = 0
    sampled = []
    denied = 0
    for target in targets:
        result = move(position, energy, target)
        if result[2]:
            position = result[0]
            energy = collect(position, result[1], sampled)
        else:
            denied += 1
    return [position, energy, sampled, denied]

print(mission([4, 8, 4, 10, 0], 32))
print(mission([4, 8, 4, 10, 0], 22))
```

פלט:

```text
[0, 10, [4, 8], 1]
[0, 0, [4, 8], 1]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[4, 8] [[4, 23], [8, 16], [4, 12], [0, 8]] 0
[4] [[4, 13], [8, 9], [4, 5], [0, 1]] 0
8 1
```

### ב. פלט התרחיש השני

```text
[4, 8] [[4, 23], [8, 16], [4, 12], [0, 8]] 0
[4, 8] [[4, 19], [8, 12], [4, 8], [0, 4]] 0
8 4
```

### ג. תשובות והערות לדיון

move מגינה על תנאי הסף.

אנרגיות התחלתיות שונות יוצרות החלטות שונות.

אותו מופע משותף יוצר תלות מכוונת במצב ולכן יש להבחין בין רובוטים.

sampled מתעדכן רק לאחר collect מוצלחת.

### ד. פתרון אפשרי

```python
class Rover:
    def __init__(self, energy):
        self.energy = energy
        self.position = 0
        self.sampled = []

    def move(self, target):
        distance = target - self.position
        if distance < 0:
            distance = -distance
        if target < 0 or target > 12 or self.energy - distance < target:
            return False
        self.position = target
        self.energy -= distance
        return True

    def collect(self):
        if self.position == 0 or self.position in self.sampled or self.energy - 3 < self.position:
            return False
        self.sampled.append(self.position)
        self.energy -= 3
        return True

    def margin(self):
        return self.energy - self.position

class Mission:
    def __init__(self, rover):
        self.rover = rover
        self.denied = 0
        self.collected = 0
        self.history = []

    def visit(self, target):
        if self.rover.move(target):
            if self.rover.collect():
                self.collected += 1
        else:
            self.denied += 1
        self.history.append([self.rover.position, self.rover.energy])

a = Mission(Rover(30))
b = Mission(Rover(20))
for target in [4, 8, 4, 4, 0]:
    a.visit(target)
    b.visit(target)
print(a.rover.sampled, a.history, a.denied)
print(b.rover.sampled, b.history, b.denied)
print(a.rover.margin(), b.rover.margin())
print(a.collected, b.collected)
```

פלט:

```text
[4, 8] [[4, 23], [8, 16], [4, 12], [4, 12], [0, 8]] 0
[4] [[4, 13], [8, 9], [4, 5], [4, 5], [0, 1]] 0
8 1
2 1
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

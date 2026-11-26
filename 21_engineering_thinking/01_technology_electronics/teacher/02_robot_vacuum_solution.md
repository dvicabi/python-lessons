# פתרונות למורה: שואב אבק רובוטי: איך יודעים איפה כבר ניקינו?

[חזרה למשימת התלמיד](../02_robot_vacuum.md)

כל פתרון הוא דרך אפשרית. יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט. מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה. הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Robot READY
Position: 0
Battery: 10
```

שתי פקודות print עם end=""; ברירת המחדל של השאר היא שורה חדשה.

### ב. שינוי ודיון

Robot -READY; נוצר מפריד נוסף אחרי הרווח שכבר קיים.

### ג. פתרון אפשרי

```python
print("Robot ", end="")
print("BLOCKED")
print("Position: 2", end=" | ")
print("Battery: 5")
```

פלט:

```text
Robot BLOCKED
Position: 2 | Battery: 5
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
2 6
```

מיקום מתאר תא, סוללה מתארת משאב. שני צעדים משפיעים אחרת על כל אחד.

### ב. שינוי ודיון

0 והסוללה 6. מספר הצעדים לא משתנה.

### ג. פתרון אפשרי

```python
position = 2
battery = 9
position -= 1
battery -= 2
print(position, battery)
position += 1
battery -= 2
print(position, battery)
position -= 1
battery -= 2
print(position, battery)
```

פלט:

```text
1 7
2 5
1 3
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Position: 1
Battery: 5
```

זהו שינוי יחסי למיקום. 2 + (-1) = 1.

### ב. שינוי ודיון

Position: 3, Battery: 5. תא 3 חסום ולכן נדרש תנאי.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
0
8
1
-1
```

```python
position = int(input())
battery = int(input())
first = int(input())
second = int(input())
position += first
battery -= 2
print(position, battery)
position += second
battery -= 2
print(position, battery)
```

פלט:

```text
1 6
0 4
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
BLOCKED
2 4
```

הוא מועמד שעדיין לא אושר. עדכון מוקדם יכניס את הרובוט למכשול.

### ב. שינוי ודיון

1: LOW, 2 1. 2: BLOCKED, 2 1.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
2
5
-1
```

```python
position = int(input())
battery = int(input())
direction = int(input())
candidate = position + direction
if direction != 1 and direction != -1:
    print("ERROR")
elif battery < 2:
    print("LOW")
elif candidate < 0 or candidate > 5 or candidate == 3:
    battery -= 1
    print("BLOCKED")
else:
    position = candidate
    battery -= 2
    print("MOVED")
print(position, battery)
```

פלט:

```text
MOVED
1 3
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
1 5
2 3
2 2
2 1
LOW
```

ניסיונות חוזרים לתא 3 חסומים ועולים יחידה כל אחד.

### ב. שינוי ודיון

1 1 ואז LOW; שתי שורות.

### ג. פתרון אפשרי

```python
position = 0
battery = 6
while battery >= 2:
    candidate = position + 1
    if candidate == 3:
        break
    position = candidate
    battery -= 2
    print(position, battery)
print("STOP")
```

פלט:

```text
1 4
2 2
STOP
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[0, 1, 2]
Clean: 3
```

הרובוט חוזר לתאים שכבר ברשימה; מכסים שלושה כולל ההתחלה.

### ב. שינוי ודיון

[0, 1, 2, 1, 2]; Clean: 5, דיווח שגוי.

### ג. פתרון אפשרי

```python
position = 0
battery = 10
visited = [0]
commands = [1, 1, 1, -1, -1, -1]
for direction in commands:
    if battery < 2:
        break
    candidate = position + direction
    if candidate < 0 or candidate > 5 or candidate == 3:
        battery -= 1
    else:
        position = candidate
        battery -= 2
        if position not in visited:
            visited.append(position)
print(visited)
print(position, battery)
```

פלט:

```text
[0, 1, 2]
0 1
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
2
1
0
```

היא מחזירה True/False ולא משנה מיקום; ההחלטה ועדכון המיקום נעשים בחוץ.

### ב. שינוי ודיון

allowed(1) מחזירה True; position הופך 3 אף שזה מכשול. הפלט יהיה 3, 3, 3 כי -1 אינו תא חוקי.

### ג. פתרון אפשרי

```python
def allowed(candidate):
    return 0 <= candidate and candidate <= 5 and candidate != 3

def clean(commands, battery):
    position = 0
    visited = [0]
    for direction in commands:
        if battery < 2:
            break
        if allowed(position + direction):
            position += direction
            battery -= 2
            if position not in visited:
                visited.append(position)
        else:
            battery -= 1
    return visited

print(clean([1, 1, 1, -1, -1], 7))
```

פלט:

```text
[0, 1, 2]
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
[0, 1, 2] 2
[0] 2
```

לכל רובוט היסטוריה עצמאית; אחרת ניקיון אחד ידווח אצל השני.

### ב. שינוי ודיון

a נשאר בתא 2 עם סוללה 1 ורשימה [0, 1, 2]. b ללא שינוי.

### ג. פתרון אפשרי

```python
class Robot:
    def __init__(self, battery):
        self.position = 0
        self.battery = battery
        self.visited = [0]

    def move(self, direction):
        if direction != 1 and direction != -1:
            return
        if self.battery < 2:
            return
        candidate = self.position + direction
        if candidate < 0 or candidate > 5 or candidate == 3:
            self.battery -= 1
        else:
            self.position = candidate
            self.battery -= 2
            if candidate not in self.visited:
                self.visited.append(candidate)

    def charge(self, amount):
        if self.position == 0 and amount > 0:
            self.battery += amount
            if self.battery > 10:
                self.battery = 10

a = Robot(4)
b = Robot(4)
a.move(1)
a.charge(8)
b.charge(8)
print(a.position, a.battery)
print(b.position, b.battery)
```

פלט:

```text
1 2
0 10
```

---

## אתגר מסכם

אין פתרון יחיד. בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית. אין לדרוש נושא תכנות שלא נלמד.

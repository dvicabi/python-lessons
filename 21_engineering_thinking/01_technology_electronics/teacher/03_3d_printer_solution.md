# פתרונות למורה: מדפסת תלת ממד: האם אפשר לסיים את ההדפסה?

[חזרה למשימת התלמיד](../03_3d_printer.md)

כל פתרון הוא דרך אפשרית.

יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט.

מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה.

הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Layer 2/5
Status: PRINTING
```

end="" מחבר בין שתי הפקודות;

print הבא מוסיף ירידת שורה.

### ב. שינוי ודיון

Layer  ולאחר ירידת שורה 2/5;

הכותרת והערך נפרדים.

### ג. פתרון אפשרי

```python
print("Layer ", end="")
print("3/5")
print("Material: 8", end=" | ")
print("PAUSED")
```

פלט:

```text
Layer 3/5
Material: 8 | PAUSED
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
Remaining: 5
```

cost עדיין 4;

צריך לחשב מחדש לפני שכבה שנייה.

הצריכה הרצויה היא 4+6.

### ב. שינוי ודיון

Remaining: 3.

### ג. פתרון אפשרי

```python
stock = 18
start = stock
thickness = 4
stock -= thickness + 1
print(stock)
thickness = 6
stock -= thickness + 1
print(stock)
thickness = 2
stock -= thickness + 1
print(stock)
print("Used:", start - stock)
```

פלט:

```text
13
6
3
Used: 15
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Cost: 5
After: 5
```

stock=10 ו-thickness=4 נקלטים;

cost=5 נגזר והיתרה 5.

### ב. שינוי ודיון

Cost: 5, After: -2;

אי אפשר לצרוך מלאי שאינו קיים.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
15
3
5
```

```python
stock = int(input())
first = int(input())
second = int(input())
used = first + 1 + second + 1
remaining = stock - used
print("Used:", used)
print("Remaining:", remaining)
print("Available:", remaining - 2)
```

פלט:

```text
Used: 10
Remaining: 5
Available: 3
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
PRINTED
2
```

מותר להשאיר בדיוק 2;

> היה דוחה שכבה תקינה.

### ב. שינוי ודיון

6: PAUSED, 8. 4: PRINTED, 3.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
7
5
```

```python
stock = int(input())
thickness = int(input())
cost = thickness + 1
if thickness <= 0 or stock < 2:
    print("ERROR")
elif stock - cost >= 2:
    stock -= cost
    print("PRINTED")
else:
    print("PAUSED")
print(stock)
```

פלט:

```text
PAUSED
7
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
9
5
PAUSED
Layers: 2
```

רק שכבה שהודפסה בהצלחה נכללת בספירה.

### ב. שינוי ודיון

בשכבה השלישית נשאר 1 במקום 5, למרות שלא הודפסה.

יש לבצע את בדיקת stock - cost < 2 לפני הפחתת חומר, ורק אחר כך להפחית פעם אחת.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
13
4
```

```python
stock = int(input())
thickness = int(input())
cost = thickness + 1
printed = 0
while stock - cost >= 2:
    stock -= cost
    printed += 1
    print(stock)
print("Layers:", printed)
```

פלט:

```text
8
3
Layers: 2
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[9, 3]
Next layer: 3
```

len(history) מספק את מספר השכבות שהושלמו, והרשימה המקורית נשמרת להמשך.

### ב. שינוי ודיון

[9, 2], Next layer: 3.

אין שכבה שלישית;

צריך להציג DONE כאשר מספר ההצלחות שווה לאורך.

### ג. פתרון אפשרי

```python
layers = [2, 0, 4, 3]
stock = 12
history = []
status = "DONE"
running = True
index = 0
while index < len(layers) and running:
    thickness = layers[index]
    index += 1
    if thickness <= 0:
        status = "ERROR"
        running = False
    else:
        cost = thickness + 1
        if stock - cost < 2:
            status = "PAUSED"
            running = False
        else:
            stock -= cost
            history.append(stock)
print(history)
print(status, len(history))
```

פלט:

```text
[9]
ERROR 1
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
YES 6
YES 2
NO 2
```

תפקידה לבדוק אפשרות בלבד;

הקוד הקורא מחליט מתי לעדכן.

### ב. שינוי ודיון

YES 6, NO 6, YES 4.

הקוד הנתון מדלג על שכבה שנדחתה;

זו מדיניות שונה מעצירה בשכבה הראשונה.

### ג. פתרון אפשרי

```python
def can_print(stock, thickness, reserve):
    return thickness > 0 and stock - thickness - 1 >= reserve
def plan(layers, stock, reserve):
    history = []
    running = True
    index = 0
    while index < len(layers) and running:
        thickness = layers[index]
        index += 1
        if not can_print(stock, thickness, reserve):
            running = False
        else:
            stock -= thickness + 1
            history.append(stock)
    return history
print(plan([1, 4, 2], 10, 2))
```

פלט:

```text
[8, 3]
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
2 2
6 0
```

כל self מצביע לאובייקט אחר;

אצל b אין מספיק רזרבה.

### ב. שינוי ודיון

2 1;

a נשארת 2 2.

### ג. פתרון אפשרי

```python
class Printer:
    def __init__(self, stock):
        self.stock = stock
        self.printed = 0

    def layer(self, thickness):
        if thickness > 0 and self.stock - thickness - 1 >= 2:
            self.stock -= thickness + 1
            self.printed += 1

    def add_material(self, amount):
        if amount > 0:
            self.stock += amount

a = Printer(6)
b = Printer(7)
a.layer(4)
a.add_material(3)
a.layer(4)
print(a.stock, a.printed)
print(b.stock, b.printed)
```

פלט:

```text
4 1
7 0
```

---

## אתגר מסכם

אין פתרון יחיד.

בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית.

אין לדרוש נושא תכנות שלא נלמד.

# פתרונות למורה: מכונת כביסה: מי מנהל את מחזור הכביסה?

[חזרה למשימת התלמיד](../01_washing_machine.md)

כל פתרון הוא דרך אפשרית.

יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט.

מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה.

הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Stage: FILL
Water: 0/6
```

end="" מונע מעבר שורה.

ההדפסה הבאה משלימה את השורה.

### ב. שינוי ודיון

Stage:  | FILL;

אם מסירים end, Stage: והערך FILL יהיו בשורות נפרדות.

### ג. פתרון אפשרי

```python
print("Stage: ", end="")
print("WASH")
print("Cycles: ", end="")
print("2/3")
```

פלט:

```text
Stage: WASH
Cycles: 2/3
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
Water: 5
Missing: 1
```

אחרת הוא מתאר את המצב הקודם.

הערכים לאחר ההוספה הם water=5 ו-missing=1.

### ב. שינוי ודיון

Water: 5, Missing: 4;

הנתון הישן אינו מתאים למצב החדש.

### ג. פתרון אפשרי

```python
target = 10
water = 3
water += 2
water += 4
missing = target - water
print("Water:", water)
print("Missing:", missing)
```

פלט:

```text
Water: 9
Missing: 1
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Water: 7
Missing: 3
```

10 הוא יעד, 4 מצב נוכחי, 3 אירוע.

input מחזיר טקסט ולכן נדרש int.

### ב. שינוי ודיון

Water: 13, Missing: -3.

המודל זקוק לכלל להגבלת מילוי בשלב הבא.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
12
2
4
2
```

```python
target = int(input())
water = int(input())
first = int(input())
second = int(input())
water += first
water += second
print("Water:", water)
print("Missing:", target - water)
```

פלט:

```text
Water: 8
Missing: 4
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
WASH
Water: 6
```

water=9 לפני ההגבלה;

== היה נכשל ולכן מצב FILL היה שגוי.

### ב. שינוי ודיון

2: WASH ו-6.

1: FILL ו-5.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
6
4
-1
```

```python
target = int(input())
water = int(input())
added = int(input())
if added < 0:
    print("ERROR")
else:
    water += added
    if water >= target:
        water = target
        print("WASH")
    else:
        print("FILL")
print("Water:", water)
```

פלט:

```text
ERROR
Water: 4
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
1 2
2 4
3 6
4 7
WASH
```

מספר הקריאות תלוי ביעד ובקצב.

כאן ארבע קריאות.

ההגבלה מונעת חריגה.

### ב. שינוי ודיון

הלולאה לא תגיע ליעד.

מונה ניסיונות ותנאי ticks < limit מאפשרים לסיים עם TIMEOUT.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
6
3
0
2
3
```

```python
target = int(input())
limit = int(input())
water = 0
for step in range(limit):
    added = int(input())
    water += added
    if water >= target:
        water = target
        break
print("Water:", water)
if water == target:
    print("WASH")
else:
    print("TIMEOUT")
```

פלט:

```text
Water: 5
TIMEOUT
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[2, 2, 5, 6]
Unused: 1
```

readings מתארת תוספות;

used מציגה מצבים מצטברים.

לאחר 4 מדידות לא קוראים את האחרונה.

### ב. שינוי ודיון

[2, 2, 5, 9, 10], Unused: 0;

היעד לא הושג, לכן אין להתחיל שטיפה.

### ג. פתרון אפשרי

```python
readings = [3, -1, 2, 5, 4]
target = 8
water = 0
errors = 0
history = []
for added in readings:
    if added < 0:
        errors += 1
    else:
        water += added
        if water > target:
            water = target
        history.append(water)
        if water == target:
            break
print(history)
print("Errors:", errors)
```

פלט:

```text
[3, 5, 8]
Errors: 1
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
5
5
6
```

הפעולה מחזירה מספר חדש;

ללא השמה המשתנה בחוץ יישאר ללא שינוי.

### ב. שינוי ודיון

2 בכל אחת משלוש האיטרציות.

### ג. פתרון אפשרי

```python
def fill(water, added, target):
    if added < 0:
        return water
    water += added
    if water > target:
        water = target
    return water

def run_fill(readings, target):
    water = 0
    history = []
    for added in readings:
        if added >= 0:
            water = fill(water, added, target)
            history.append(water)
            if water == target:
                break
    return history

print(run_fill([2, -1, 4, 8], 6))
```

פלט:

```text
[2, 6]
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
6 WASH
4 WASH
```

רק b;

לאחר ההגעה ליעד stage הוא WASH ולכן לא נכנסים לתנאי.

### ב. שינוי ודיון

a: 6 WASH;

b: 4 WASH, בעקבות b.fill(2) האחרון.

b מגיעה ליעד בשלב אחר.

### ג. פתרון אפשרי

```python
class Washer:
    def __init__(self, target):
        self.target = target
        self.reset()

    def reset(self):
        self.water = 0
        self.stage = "FILL"

    def fill(self, added):
        if self.stage == "FILL" and added >= 0:
            self.water += added
            if self.water >= self.target:
                self.water = self.target
                self.stage = "WASH"

a = Washer(6)
b = Washer(4)
a.fill(5)
b.fill(4)
b.reset()
b.fill(1)
print(a.water, a.stage)
print(b.water, b.stage)
```

פלט:

```text
5 FILL
1 FILL
```

---

## אתגר מסכם

אין פתרון יחיד.

בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית.

אין לדרוש נושא תכנות שלא נלמד.

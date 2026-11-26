# פתרונות למורה: אוזניות אלחוטיות: שלוש סוללות ומערכת אחת

[חזרה למשימת התלמיד](../04_wireless_earbuds.md)

כל פתרון הוא דרך אפשרית. יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט. מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה. הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
L: 8 | R: 10
Case: 12
```

הראשון מוסיף מפריד עם רווחים; השני אינו מוסיף דבר ואינו יורד שורה.

### ב. שינוי ודיון

L: 8 ו-R: 10 יהיו בשורות נפרדות; Case: 12 נשאר יחד.

### ג. פתרון אפשרי

```python
print("L: 2", end=" | ")
print("R: 5")
print("Case: 0", end=" | ")
print("LOW")
```

פלט:

```text
L: 2 | R: 5
Case: 0 | LOW
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
6 7 6
19 19
```

שתי יחידות נגרעו מהקופסה והתווספו לשמאל; אין הפסדים במודל.

### ב. שינוי ודיון

6 7 8 ואז 19 21. הופיעו שתי יחידות בלי מקור.

### ג. פתרון אפשרי

```python
left = 6
right = 5
case = 10
left -= 2
right -= 2
right += 3
case -= 3
print(left, right, case)
print("Total:", left + right + case)
```

פלט:

```text
4 6 7
Total: 17
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
3 1 8
```

הכמות לכל אוזנייה, לא לזוג כולו; 6-3 ו-4-3.

### ב. שינוי ודיון

3 -1 8; סוללה שלילית לא חוקית, צריך לבדוק שני צדדים לפני השינוי.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
5
4
7
4
```

```python
left = int(input())
right = int(input())
case = int(input())
amount = int(input())
right += amount
case -= amount
print(left, right, case)
print("Total:", left + right + case)
```

פלט:

```text
5 8 3
Total: 16
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
DENIED
6 2
```

התנאי יתקיים בגלל שמאל, וימין יהפוך ל-1-; זו הפרה של הכלל.

### ב. שינוי ודיון

PLAY, 4 0; אפס הוא חוקי.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
9
4
6
2
```

```python
left = int(input())
right = int(input())
case = int(input())
amount = int(input())
if amount < 0:
    print("ERROR")
elif amount <= case and left + amount <= 10:
    left += amount
    case -= amount
    print("CHARGED")
else:
    print("DENIED")
print(left, right, case)
```

פלט:

```text
DENIED
9 4 6
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
3 4 5
4 4 4
5 4 3
5 5 2
6 5 1
```

בכל צעד נבחר הערך הנמוך; אחרי השוואה הבחירה יכולה להשתנות.

### ב. שינוי ודיון

שש העברות בלבד, לאחר מכן case=0. המצב הסופי 6 6 0.

### ג. פתרון אפשרי

```python
left = 7
right = 9
case = 5
while case > 0 and (left < 10 or right < 10):
    if left <= right:
        left += 1
    else:
        right += 1
    case -= 1
    print(left, right, case)
print("Total:", left + right + case)
```

פלט:

```text
8 9 4
9 9 3
10 9 2
10 10 1
Total: 21
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
[2, 1]
3 1
```

אין הפסקת לולאה; בקשה שנדחתה לא משנה סוללה, וממשיכים.

### ב. שינוי ודיון

[2], 4 2; הבקשה 1 לא תיבדק.

### ג. פתרון אפשרי

```python
requests = [3, -1, 2, 1]
left = 6
right = 4
statuses = []
for amount in requests:
    if amount < 0:
        statuses.append("ERROR")
    elif left >= amount and right >= amount:
        left -= amount
        right -= amount
        statuses.append("PLAY")
    else:
        statuses.append("DENIED")
print(statuses)
print(left, right)
```

פלט:

```text
['PLAY', 'ERROR', 'DENIED', 'PLAY']
2 0
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
[3, 2, 0]
[3, 2, 0]
```

המספרים בתוך הפעולה הם מקומיים. הרשימה המוחזרת מתארת מצב חדש.

### ב. שינוי ודיון

[2, 2, 1] ואז [3, 2, 0].

### ג. פתרון אפשרי

```python
def play(state, amount):
    left = state[0]
    right = state[1]
    case = state[2]
    if amount >= 0 and left >= amount and right >= amount:
        left -= amount
        right -= amount
    return [left, right, case]

state = [6, 4, 8]
print(play(state, 3))
print(state)
```

פלט:

```text
[3, 1, 8]
[6, 4, 8]
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
3 1 8
1 1 5
```

ימין של a כבר 1; הבדיקה נעשית על שני הצדדים לפני כל שינוי.

### ב. שינוי ודיון

2 0 8; b נשאר 1 1 5.

### ג. פתרון אפשרי

```python
class Earbuds:
    def __init__(self, left, right, case):
        self.left = left
        self.right = right
        self.case = case

    def play(self, amount):
        if amount >= 0 and self.left >= amount and self.right >= amount:
            self.left -= amount
            self.right -= amount

    def charge(self, budget):
        while budget > 0 and self.case > 0 and (self.left < 10 or self.right < 10):
            if self.left <= self.right:
                self.left += 1
            else:
                self.right += 1
            self.case -= 1
            budget -= 1

a = Earbuds(2, 4, 6)
b = Earbuds(10, 10, 5)
a.charge(5)
b.charge(3)
print(a.left, a.right, a.case)
print(b.left, b.right, b.case)
```

פלט:

```text
6 5 1
10 10 5
```

---

## אתגר מסכם

אין פתרון יחיד. בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית. אין לדרוש נושא תכנות שלא נלמד.

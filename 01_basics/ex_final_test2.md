## גרסה A (20 שאלות)

### שאלה 1

מה יודפס?

```python
def score(s, d={"a": 2, "b": -1, "c": 5, "other": 0}):
    if not s:
        return 0
    head = s[0].lower()
    if head in d:
        return d[head] + score(s[1:], d)
    return d["other"] + score(s[1:], d)

print(score("Abca"))
```

א. 6
ב. 8
ג. 9
ד. שגיאה

### שאלה 2

מה יודפס?

```python
sentence = "I am am a cat"
words = sentence.split()
d = {}
for w in words:
    d[w] = len(w)

k = list(d.keys())
k.sort()
for w in k:
    print(w * d[w])
```

א.

```
I
amam
a
catcatcat
```

ב.

```
I
a
amam
catcatcat
```

ג. שגיאה כי יש כפילות במפתחות
ד. שגיאה כי אי אפשר להכפיל מחרוזת במספר

### שאלה 3

מה צריך להוסיף כדי שהציור יישאר פתוח (ולא ייסגר מיד)?

```python
import turtle
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
```

א. `turtle.up()`
ב. `turtle.done()`
ג. `turtle.begin_fill()`
ד. `turtle.reset()`

### שאלה 4

כמה שורות חובה לתקן כדי שהקוד ירוץ בלי שגיאה?

```python
name = input("Name: ")
age = input("Age: ")

age = float(age)
age++
name[0] = name[0].upper()

print(f"Hi {name}, next year you will be {age}!")
```

א. 2
ב. 1
ג. 3
ד. 0

### שאלה 5

מה יודפס?

```python
import random

class Weather:
    def __init__(self):
        self.condition = "Sunny"

    def forecast(self):
        random.seed(7)
        self.condition = random.choice(["Sunny", "Rainy", "Cloudy"])

w = Weather()
for _ in range(3):
    w.forecast()
    print(w.condition)
```

א.

```
Sunny
Rainy
Cloudy
```

ב.

```
Rainy
Rainy
Rainy
```

ג. 3 ערכים אקראיים שונים בכל פעם
ד. שגיאה

### שאלה 6

נתון:

```python
d = {1: [1,2], 2: [3], 3: [4,5]}
```

אילו שורות עלולות לגרום לשגיאה?

```python
1) s = set(d.keys())
2) s = set(d)
3) s = set(d.values())
4) s = set(list(d.values()))
```

א. 3 בלבד
ב. 3 ו 4
ג. 4 בלבד
ד. אף אחת

### שאלה 7

בהנחה שהקובץ `q.txt` לא קיים, איזה פתיחות לא יגרמו לשגיאה?

```python
1) open("q.txt", "r")
2) open("q.txt", "w")
3) open("q.txt", "a")
4) open("q.txt", "r+")
```

א. 2 בלבד
ב. 2 ו 3
ג. 1 ו 4
ד. 3 בלבד

### שאלה 8

מה יודפס?

```python
x = 1
y = 0

def f1():
    global y
    y = 5

def f2():
    print(x / y)

def main():
    x = 10
    f1()
    f2()

main()
```

א. 2.0
ב. שגיאה חלוקה באפס
ג. שגיאה כי x מוגדר פעמיים
ד. 0.2

### שאלה 9

מה יודפס?

```python
def g(v):
    try:
        n = int(v)
        if n < 0:
            raise KeyError("neg")
        print(10 / n)
    except Exception:
        print("E")
    except ValueError:
        print("V")
    except KeyError:
        print("K")
    except ZeroDivisionError:
        print("Z")

for v in ["2", "abc", "-5", "0"]:
    g(v)
```

א.

```
5.0
V
K
Z
```

ב.

```
5.0
E
E
E
```

ג. תמיד יודפס E ארבע פעמים
ד. שגיאת תחביר בגלל סדר except

### שאלה 10

מה יקרה?

```python
class Book:
    def __init__(self):
        self.title = "X"

    def __init__(self, title):
        self.title = title

b1 = Book("Python")
b2 = Book()
print(b1.title)
```

א. שגיאה ביצירת `b2` ולא יודפס כלום
ב. יודפס Python ואז שגיאה
ג. יודפס X
ד. הכל תקין

### שאלה 11

מה יודפס?

```python
def change_me(s):
    s = "Goodbye"

text = "Hello"
print(text)
change_me(text)
print(text)
```

א.

```
Hello
Goodbye
```

ב.

```
Hello
Hello
```

ג. שגיאה כי מחרוזת לא ניתנת להעברה לפונקציה
ד. כלום

### שאלה 12

מה יקרה?

```python
def h():
    n = 0
    while n < 5:
        if n == 2:
            continue
        print(n)
        n += 1

h()
```

א. לולאה אינסופית (אחרי הדפסת 0 ו 1)
ב. יודפס 0,1,3,4
ג. יודפס 0,1,2,3,4
ד. שגיאת תחביר

### שאלה 13

מה יודפס?

```python
data = list(range(1, 20, 3))
print(data[2:6])
print(data[::2])
print(data[::-1])
```

א.

```
[7, 10, 13, 16]
[1, 7, 13, 19]
[19, 16, 13, 10, 7, 4, 1]
```

ב.

```
[7, 10, 13]
[1, 10, 19]
[1, 4, 7, 10, 13, 16, 19]
```

ג. שגיאה בשורה 2
ד. שגיאה בשורה 3

### שאלה 14

מה יודפס?

```python
def main():
    try:
        f = open("t.txt", "w")
        f.write("hi\n")
        x = f.read()
    except:
        print("Ops")
    finally:
        f.close()

main()
```

א. Ops
ב. hi
ג. לא יודפס כלום
ד. שגיאה שלא נתפסת

### שאלה 15

מה יודפס?

```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def __str__(self):
        return super().__str__() + " studies at " + self.school

arr = []
arr.append(Person("Dana"))
arr.append(Student("Noam", "BIU"))
arr.insert(0, Student("Lior", "TAU"))

print(arr[1])
```

א. Dana
ב. Noam studies at BIU
ג. Lior studies at TAU
ד. שגיאה בגלל insert

### שאלה 16

בחרו את הטענה הלא נכונה על חריגות:
א. תמיד חייבים finally
ב. לא חייבים else
ג. אפשר try בתוך try
ד. יש משמעות לסדר ה except

### שאלה 17

מה נכון לגבי import?
א. אפשר לייבא מודול בשם חלופי עם `as`
ב. ייבוא אותו מודול פעמיים תמיד גורם שגיאה
ג. import מוחק משתנים קיימים
ד. אי אפשר לייבא מתוך קובץ py

### שאלה 18

מה נכון לגבי הרצת קובץ Python?
א. חייבים main כדי שירוץ
ב. הקוד לא רץ מלמעלה למטה
ג. אין אפשרות להשתמש ב `if __name__ == "__main__"`
ד. לא חייבים main כדי להריץ קובץ

### שאלה 19

מה נכון לגבי set?
א. אפשר לשים list בתוך set
ב. set שומר סדר הכנסת איברים
ג. set תמיד מכיל כפילויות
ד. set לא יכול להכיל איברים לא ניתנים לגיבוב

### שאלה 20

בחרו את הטענה הלא נכונה:
א. אפשר ליצור מחלקה בלי `__init__`
ב. אפשר ירושה
ג. אפשר דריסה (override)
ד. חייבים setter לכל שדה כדי שהתוכנית תרוץ

# מפתחות תשובות (לבדיקה אחרי פתרון)

1-ב, 2-ב, 3-ב, 4-א, 5-ב, 6-ב, 7-ב, 8-ד, 9-ב, 10-א, 11-ב, 12-א, 13-א, 14-א, 15-א, 16-א, 17-א, 18-ד, 19-ד, 20-ד

---

## גרסה B (20 שאלות)

### שאלה 1

מה יודפס?

```python
def prod(lst):
    if not lst:
        return 1
    if lst[0] == 0:
        return prod(lst[1:])
    return lst[0] * prod(lst[1:])

print(prod([2, 0, 3, 0, 4]))
```

א. 9
ב. 24
ג. 0
ד. 1

### שאלה 2

מה יודפס?

```python
sentence = "go go stop"
d = {}
for w in sentence.split():
    d[w] = d.get(w, 0) + 1

k = list(d.keys())
k.sort()
for w in k:
    print(w, d[w])
```

א.

```
go 2
stop 1
```

ב.

```
stop 1
go 2
```

ג. שגיאה כי go מופיע פעמיים
ד. יודפס רק go 1

### שאלה 3

מה יקרה?

```python
import turtle
turtle.up()
for _ in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.done()
```

א. יצויר ריבוע
ב. לא יצויר כלום
ג. שגיאה כי up לא חוקי
ד. יצויר משולש

### שאלה 4

מה יקרה?

```python
x = "12a"
print(int(x))
```

א. יודפס 12
ב. יודפס 0
ג. ValueError
ד. TypeError

### שאלה 5

מה יודפס?

```python
import random
random.seed(123)
print(random.randint(1, 3))
print(random.randint(1, 3))
print(random.randint(1, 3))
```

א. תמיד אותו מספר 3 פעמים
ב. רצף דטרמיניסטי (אותו רצף בכל הרצה)
ג. כל הרצה רצף שונה
ד. שגיאה

### שאלה 6

איזו שורה תגרום לשגיאה?

```python
d = {"a": (1,2), "b": [3,4]}
```

א. `set(d.keys())`
ב. `set(d)`
ג. `set(d.values())`
ד. `set([1,2,3])`

### שאלה 7

איזה מצב פתיחה ייצור קובץ אם לא קיים ויכתוב בסוף?
א. `open("log.txt")`
ב. `open("log.txt", "r")`
ג. `open("log.txt", "a")`
ד. `open("log.txt", "r+")`

### שאלה 8

מה יודפס?

```python
x = 0

def inc():
    global x
    x += 1

def main():
    x = 100
    inc()
    print(x)

main()
print(x)
```

א.

```
101
101
```

ב.

```
100
1
```

ג.

```
100
0
```

ד.

```
101
1
```

### שאלה 9

מה יודפס?

```python
def p(v):
    try:
        n = int(v)
        print(10/n)
    except ZeroDivisionError:
        print("Z")
    except ValueError:
        print("V")

for v in ["5", "0", "a"]:
    p(v)
```

א.

```
2.0
Z
V
```

ב.

```
2
Z
V
```

ג.

```
2.0
V
Z
```

ד. שגיאה שלא נתפסת

### שאלה 10

מה יודפס?

```python
class A:
    def __init__(self, x=0):
        self.x = x

a = A()
b = A(5)
print(a.x, b.x)
```

א. 0 5
ב. 5 0
ג. שגיאה כי אין העמסת בנאים
ד. שגיאת תחביר

### שאלה 11

מה יודפס?

```python
def change(lst):
    lst.append(9)

nums = [1,2]
change(nums)
print(nums)
```

א. [1, 2]
ב. [1, 2, 9]
ג. [9]
ד. שגיאה

### שאלה 12

מה יודפס?

```python
n = 0
while n < 4:
    if n == 1:
        n += 1
        continue
    print(n)
    n += 1
```

א. 0,2,3
ב. 0,1,2,3
ג. לולאה אינסופית
ד. שגיאה

### שאלה 13

מה יודפס?

```python
data = [10,20,30,40,50]
print(data[1:4])
print(data[:])
print(data[-2:])
```

א. [20,30,40] ואז [10,20,30,40,50] ואז [40,50]
ב. [20,30] ואז [10,20,30,40] ואז [50]
ג. שגיאה
ד. הדפסה זהה בכל השורות

### שאלה 14

מה יודפס?

```python
f = open("a.txt", "w")
f.write("hello")
f.close()

f = open("a.txt", "r")
print(f.read())
f.close()
```

א. hello
ב. שורה ריקה
ג. שגיאה כי חסר \n
ד. שגיאה כי צריך seek(0)

### שאלה 15

מה יודפס?

```python
def add(x, d={}):
    d[x] = d.get(x, 0) + 1
    return d[x]

print(add("a"), add("a"), add("b"))
```

א. 1 1 1
ב. 1 2 1
ג. 2 2 1
ד. 1 2 2

### שאלה 16

מה נכון לגבי סדר except?
א. `except Exception` בדרך כלל צריך להיות אחרון
ב. אין משמעות לסדר except
ג. `except ValueError` חייב להיות לפני try
ד. finally אסור להשתמש בו

### שאלה 17

מה יודפס?

```python
import math as m
print(m.sqrt(16))
```

א. 4.0
ב. 4
ג. שגיאה כי אסור alias
ד. שגיאת תחביר

### שאלה 18

מה נכון לגבי הרצת קובץ Python?
א. חייבים main
ב. הקוד ברמת הקובץ רץ מלמעלה למטה
ג. import מוחק משתנים גלובליים
ד. אי אפשר להשתמש ב if **name** == "**main**"

### שאלה 19

איזה איבר אי אפשר להכניס ל set?
א. 5
ב. "hi"
ג. (1,2)
ד. [1,2]

### שאלה 20

בחרו את הטענה הלא נכונה:
א. אפשר ירושה
ב. אפשר polymorphism דרך דריסה
ג. לכל מחלקה חייב להיות setter לכל שדה
ד. אפשר בנאי גמיש עם args/kwargs

---
# מפתחות תשובות (לבדיקה אחרי פתרון)
1-ב, 2-א, 3-ב, 4-ג, 5-ב, 6-ג, 7-ג, 8-ב, 9-א, 10-א, 11-ב, 12-א, 13-א, 14-א, 15-ב, 16-א, 17-א, 18-ב, 19-ד, 20-ג

## גרסה C (20 שאלות)

### שאלה 1

מה יודפס?

```python
def count_vowels(s):
    if not s:
        return 0
    first = s[0].lower()
    add = 1 if first in "aeiou" else 0
    return add + count_vowels(s[1:])

print(count_vowels("Education"))
```

א. 4
ב. 5
ג. 6
ד. שגיאה

### שאלה 2

מה יודפס?

```python
text = "red blue red green blue blue"
d = {}
for w in text.split():
    d[w] = d.get(w, 0) + 1

keys = sorted(d.keys())
for k in keys:
    print(k, d[k])
```

א.

```
blue 3
green 1
red 2
```

ב.

```
red 2
blue 3
green 1
```

ג. הסדר תלוי בהרצה
ד. שגיאה כי מילון לא שומר סדר

### שאלה 3

מה יקרה?

```python
name = "noam"
name = name.upper()
print(name)
```

א. יודפס noam
ב. יודפס NOAM
ג. שגיאה כי מחרוזת לא ניתנת לשינוי
ד. שגיאה כי upper לא קיימת

### שאלה 4

מה תוצאת הביטוי?

```python
s = "abcdefg"
print(s[6:1:-2])
```

א. "gec"
ב. "g e c" עם רווחים
ג. "gfd"
ד. "g e c" בלי להבין

### שאלה 5

מה יודפס?

```python
import random
random.seed(7)
print(random.choice(["A","B","C"]))
print(random.choice(["A","B","C"]))
```

א. תמיד אותו תו פעמיים
ב. רצף דטרמיניסטי (אותו רצף בכל הרצה)
ג. כל הרצה שונה
ד. שגיאה

### שאלה 6

איזו שורה תעבוד בלי שגיאה?

```python
a = {1, 2, 3}
b = {3, 4}
```

א. `print(a + b)`
ב. `print(a.union(b))`
ג. `print(a.append(5))`
ד. `print(a[0])`

### שאלה 7

מה יודפס?

```python
try:
    x = int("10")
    y = int("0")
    print(x / y)
except ZeroDivisionError:
    print("Z")
else:
    print("OK")
finally:
    print("F")
```

א.

```
Z
F
```

ב.

```
OK
F
```

ג.

```
Z
OK
F
```

ד. שגיאה שלא נתפסת

### שאלה 8

מה יקרה?

```python
f = open("b.txt", "w")
f.write("hi")
f.close()

f = open("b.txt", "r")
x = f.readline()
y = f.readline()
print(x, y)
f.close()
```

א. יודפס `hi` ואז שורה ריקה
ב. יודפס `hi` ואז `hi`
ג. שגיאה כי אין \n
ד. שגיאה כי readline לא קיים

### שאלה 9

מה יודפס?

```python
x = 5
def foo():
    x = 2
    return x

print(foo(), x)
```

א. 2 2
ב. 5 5
ג. 2 5
ד. שגיאה

### שאלה 10

מה יודפס?

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return self.brand

cars = [Car("Kia"), Car("Mazda")]
print(cars[0])
```

א. <Car object at ...>
ב. Kia
ג. Mazda
ד. שגיאה

### שאלה 11

מה יקרה?

```python
class P:
    def __init__(self, name):
        self.name = name

class S(P):
    def __init__(self, name, grade):
        self.grade = grade

s = S("Dana", 100)
print(s.name)
```

א. יודפס Dana
ב. יודפס 100
ג. AttributeError כי name לא הוגדר
ד. TypeError כי אי אפשר לרשת

### שאלה 12

מה יודפס?

```python
lst = [1,2,3]
lst.insert(1, 9)
lst.append(9)
print(lst)
```

א. [1,2,3,9,9]
ב. [1,9,2,3,9]
ג. [9,1,2,3,9]
ד. שגיאה

### שאלה 13

מה יקרה?

```python
n = 0
while n < 3:
    print(n)
    n -= 1
```

א. יודפס 0,1,2
ב. לולאה אינסופית
ג. שגיאה
ד. יודפס רק 0

### שאלה 14

מה יודפס?

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_div(10, 2), safe_div(10, 0))
```

א. 5.0 None
ב. 5 None
ג. None 5.0
ד. שגיאה

### שאלה 15

מה נכון לגבי `with open(...) as f:` ?
א. הוא סוגר קובץ אוטומטית בסוף הבלוק
ב. הוא פותח קובץ רק לקריאה תמיד
ג. הוא מונע כל חריגה
ד. הוא עובד רק עם קבצי txt

### שאלה 16

מה יודפס?

```python
def f(x):
    if x <= 1:
        return 1
    return f(x-1) + f(x-2)

print(f(4))
```

א. 3
ב. 5
ג. 8
ד. לולאה אינסופית

### שאלה 17

מה יקרה?

```python
t = (1,2)
t[0] = 9
print(t)
```

א. (9,2)
ב. (1,2)
ג. TypeError כי tuple בלתי ניתן לשינוי
ד. SyntaxError

### שאלה 18

מה יודפס?

```python
s = set()
s.add(1)
s.add(1)
s.add(2)
print(len(s))
```

א. 1
ב. 2
ג. 3
ד. שגיאה

### שאלה 19

מה יודפס?

```python
values = ["3", "4", "5"]
nums = [int(x) for x in values]
print(sum(nums))
```

א. 12
ב. 345
ג. שגיאה
ד. 0

### שאלה 20

בחרו את הטענה הלא נכונה:
א. list ניתנת לשינוי
ב. string ניתנת לשינוי
ג. tuple בלתי ניתנת לשינוי
ד. set לא שומר כפילויות

---

# מפתחות תשובות (לבדיקה אחרי פתרון)
1-ב, 2-א, 3-ב, 4-א, 5-ב, 6-ב, 7-א, 8-א, 9-ג, 10-ב, 11-ג, 12-ב, 13-ב, 14-א, 15-א, 16-ב, 17-ג, 18-ב, 19-א, 20-ב

---

# מבחן תרגול 1 (20 שאלות אמריקאיות)

### שאלה 1

בחרו את הטענה המדויקת ביותר לגבי הקוד הבא:

```python
def score(s, d={"a": 2, "b": -1, "c": 5, "other": 0}):
    if len(s) == 0:
        return 0
    head = s[0]
    if head in d:
        return d[head] + score(s[1:], d)
    return d["other"] + score(s[1:], d)

print(score("Abca"))
```

א. יודפס 8
ב. יודפס 9
ג. תתקבל שגיאת זמן ריצה כי יש אות גדולה
ד. יודפס 6

### שאלה 2

בחרו את הטענה המדויקת ביותר לגבי הפלט:

```python
sentence = "I am am a cat"
words = sentence.split(" ")
d = {}
for w in words:
    d[w] = len(w)

k = list(d.keys())
k.sort()
for w in k:
    print(w * d[w])
```

א. יודפס:

```
I
amam
a
catcatcat
```

ב. יודפס:

```
I
a
amam
catcatcat
```

ג. תתקבל שגיאת זמן ריצה כי אי אפשר להכפיל מחרוזת במספר
ד. תתקבל שגיאה כי מילון לא יכול להכיל מפתחות זהים

### שאלה 3

בחרו את הטענה המדויקת ביותר לגבי הקוד הבא:

```python
import turtle

turtle.forward(50)
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(50)
```

א. הקוד תקין ולא יצויר כלום
ב. צריך להוסיף `turtle.done()` כדי שיודפס ריבוע
ג. צריך לתקן שורה אחת כדי שיודפס ריבוע
ד. צריך לתקן שתי שורות כדי שיודפס ריבוע

### שאלה 4

בחרו את הטענה המדויקת ביותר לגבי הקוד:

```python
name = input("Name: ")
age = input("Age: ")

age = float(age)
age++
name[0] = name[0].upper()

print(f"Hi {name}, next year you will be {age}!")
```

א. יש לתקן שתי שורות כדי שלא תתקבל שגיאת זמן ריצה
ב. יש לתקן שורה אחת בלבד כדי שלא תתקבל שגיאת זמן ריצה
ג. הקוד תקין וירוץ
ד. מספיק להחליף `float` ב `int` כדי שהקוד ירוץ

### שאלה 5

בחרו את הטענה המדויקת ביותר:

```python
import random

class Weather:
    def __init__(self):
        self.condition = "Sunny"

    def forecast(self):
        random.seed(7)
        self.condition = random.choice(["Sunny", "Rainy", "Cloudy"])

    def get(self):
        return self.condition

w = Weather()
for _ in range(3):
    w.forecast()
    print(w.get())
```

א. בכל הרצה של התוכנית נקבל תמיד את אותו רצף פלט
ב. בכל הרצה של התוכנית נקבל רצף שונה כי יש random
ג. חסרה פונקציית main ולכן הקוד לא תקין
ד. המחלקה מכילה משתנה מחלקה פרטי

### שאלה 6

הניחו ש־`d = {1: [1,2], 2: [3], 3: [4,5]}`. אילו מהשורות עלולות לגרום לשגיאת זמן ריצה?

```python
1) s = set(d.keys())
2) s = set(d)
3) s = set(d.values())
4) s = set(list(d.values()))
```

א. שורה 3 בלבד
ב. שורות 3 ו־4 בלבד
ג. שורה 4 בלבד
ד. אף שורה לא תגרום לשגיאה

### שאלה 7

איזו שורת קוד לעולם לא תגרום לשגיאת זמן ריצה בהנחה שהקובץ `"q.txt"` לא קיים?

```python
1) f = open("q.txt", "r")
2) f = open("q.txt", "w")
3) f = open("q.txt", "a")
4) f = open("q.txt", "r+")
```

א. שורה 2 בלבד
ב. שורות 2 ו־3 בלבד
ג. שורות 1 ו־4 בלבד
ד. שורה 3 בלבד

### שאלה 8

בחרו את הטענה המדויקת ביותר לגבי הפלט:

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

א. יודפס 2.0
ב. תתקבל שגיאת זמן ריצה (ZeroDivisionError)
ג. תתקבל שגיאת זמן ריצה כי x מוגדר פעמיים
ד. יודפס 0.2

### שאלה 9

בחרו את הטענה המדויקת ביותר לגבי הפלט:

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

א. יודפס: `5.0` ואז `V` ואז `K` ואז `Z`
ב. יודפס: `5.0` ואז `E` ואז `E` ואז `E`
ג. תמיד יודפס `E` 4 פעמים
ד. תתקבל שגיאת קומפילציה בגלל סדר except

### שאלה 10

בחרו את הטענה המדויקת ביותר:

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

א. יודפס Python ואז תיזרק שגיאה ביצירת b2
ב. יודפס X ואז התוכנית תסתיים
ג. לא ניתן להגדיר 2 בנאים בפייתון ולכן שגיאת תחביר
ד. חייבים לשים את המחלקה בקובץ נפרד

### שאלה 11

בחרו את הטענה המדויקת ביותר לגבי הפלט:

```python
def change_me(s):
    s = "Goodbye"

def main():
    text = "Hello"
    print(text)
    change_me(text)
    print(text)

main()
```

א. יודפס:

```
Hello
Goodbye
```

ב. יודפס:

```
Hello
Hello
```

ג. שגיאת זמן ריצה כי text “עובר לפי הפניה”
ד. שגיאה כי change_me מוגדרת אחרי main

### שאלה 12

בחרו את הטענה המדויקת ביותר:

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

א. לולאה אינסופית
ב. יודפס 0,1,3,4
ג. יודפס 0,1 ואז התוכנית תקרוס
ד. יודפס 0,1,2,3,4

### שאלה 13

בחרו את הטענה המדויקת ביותר לגבי הפלט:

```python
data = list(range(1, 20, 3))
print(data[2:6])
print(data[::2])
print(data[::-1])
```

א. שורה 1 מדפיסה 4 איברים, שורה 2 מדפיסה כל 2, שורה 3 הפוך
ב. שורה 1 מדפיסה 5 איברים
ג. שורה 2 מדפיסה את כל האיברים
ד. שורה 3 מדפיסה אותו דבר כמו שורה 2

### שאלה 14

בחרו את הטענה המדויקת ביותר:

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

א. יודפס Ops
ב. יודפס hi
ג. לא יודפס כלום ותוכנית תקינה
ד. תיזרק חריגה שלא נתפוס

### שאלה 15

בחרו את הטענה המדויקת ביותר:

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

א. יודפס Dana
ב. יודפס Noam studies at BIU
ג. יודפס Lior studies at TAU
ד. שגיאת זמן ריצה בגלל insert

### שאלה 16

בחרו את הטענה הלא נכונה על חריגות:
א. תמיד חייבים finally
ב. לא חייבים else
ג. אפשר try בתוך try
ד. יש משמעות לסדר ה־except

### שאלה 17

בחרו את הטענה המדויקת ביותר על מודולים:
א. אפשר לייבא מודול בשם חלופי עם `as`
ב. כל קובץ יכול לשמש כמודול גם בלי סיומת `.py`
ג. ייבוא אותו מודול פעמיים תמיד גורם שגיאת זמן ריצה
ד. import מוחק משתנים גלובליים קיימים

### שאלה 18

בחרו את הטענה המדויקת ביותר על Python כקובץ סקריפט:
א. אפשר להריץ “רק כמה שורות” מתוך קובץ מבחינת השפה עצמה
ב. קיימות טעויות קומפילציה כמו ב־C
ג. אין טיפוסי נתונים שונים בשפה
ד. לא חייבים main כדי להריץ קובץ

### שאלה 19

בחרו את הטענה הנכונה ביותר על sets:
א. אפשר לשים set בתוך set
ב. `add` מוסיף אוסף שלם כמו union
ג. set הוא טיפוס בלתי ניתן לשינוי
ד. set לא יכול להכיל איברים לא ניתנים לגיבוב

### שאלה 20

בחרו את הטענה הלא נכונה על מחלקות:
א. אפשר ליצור מחלקה בלי להגדיר `__init__`
ב. ירושה יכולה להיות מ־0 הורים או יותר
ג. “העמסת בנאים” בפייתון נעשית בדרך כלל עם ברירות מחדל/args
ד. חייבים setter לכל שדה כדי שהקוד ירוץ

---

## מפתח תשובות מבחן תרגול 1

1-ב, 2-ב, 3-ב, 4-א, 5-א, 6-ב, 7-ב, 8-ד, 9-ב, 10-א, 11-ב, 12-א, 13-א, 14-א, 15-א, 16-א, 17-א, 18-ד, 19-ד, 20-ד

---

# מבחן תרגול 2 (20 שאלות אמריקאיות)

### שאלה 1

```python
def f(s, d={"x": 1, "y": 10, "other": -1}):
    if not s:
        return 0
    return (d[s[0]] if s[0] in d else d["other"]) + f(s[1:], d)

print(f("xyZy"))
```

א. יודפס 20
ב. יודפס 21
ג. יודפס 19
ד. שגיאת זמן ריצה כי Z לא במילון

### שאלה 2

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

א. יודפס:

```
go 2
stop 1
```

ב. יודפס:

```
stop 1
go 2
```

ג. תתקבל שגיאה כי go מופיע פעמיים
ד. יודפס רק go 1

### שאלה 3

```python
import turtle
turtle.up()
for _ in range(4):
    turtle.forward(50)
    turtle.left(90)
```

א. יצויר ריבוע
ב. לא יצויר כלום בגלל up
ג. יתקבל שגיאה כי חסר import
ד. צריך להחליף left ב setheading בלבד

### שאלה 4

```python
name = "dvir"
name[0] = "D"
print(name)
```

א. יודפס Dvir
ב. יודפס dvir
ג. שגיאת זמן ריצה בגלל מחרוזת בלתי ניתנת לשינוי
ד. שגיאת תחביר

### שאלה 5

```python
import random
random.seed(123)
print(random.randint(1, 3))
random.seed(123)
print(random.randint(1, 3))
```

א. יודפס אותו מספר פעמיים
ב. יודפס שני מספרים שונים
ג. זה תלוי במחשב
ד. ייזרק ValueError

### שאלה 6

נתון:

```python
d = {"a": (1,2), "b": [3,4]}
```

איזו שורה תגרום לשגיאה?
א. `set(d.keys())`
ב. `set(d)`
ג. `set(d.values())`
ד. `set([1,2,3])`

### שאלה 7

איזו פתיחה תיצור קובץ אם הוא לא קיים וגם תאפשר כתיבה בסוף?
א. `open("log.txt")`
ב. `open("log.txt", "r")`
ג. `open("log.txt", "a")`
ד. `open("log.txt", "r+")`

### שאלה 8

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

א. יודפס 101 ואז 101
ב. יודפס 100 ואז 1
ג. יודפס 100 ואז 0
ד. יודפס 101 ואז 1

### שאלה 9

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

א. יודפס 2.0 ואז Z ואז V
ב. יודפס 2 ואז Z ואז V
ג. יודפס 2.0 ואז V ואז Z
ד. תיזרק חריגה לא נתפסת

### שאלה 10

```python
class A:
    def __init__(self, x=0):
        self.x = x

a = A()
b = A(5)
print(a.x, b.x)
```

א. יודפס 0 5
ב. יודפס 5 0
ג. שגיאת זמן ריצה כי אין העמסת בנאים
ד. שגיאת תחביר

### שאלה 11

```python
def change(lst):
    lst.append(9)

nums = [1,2]
change(nums)
print(nums)
```

א. יודפס [1,2]
ב. יודפס [1,2,9]
ג. שגיאת זמן ריצה
ד. יודפס [9]

### שאלה 12

```python
n = 0
while n < 4:
    if n == 1:
        n += 1
        continue
    print(n)
    n += 1
```

א. יודפס 0,2,3
ב. יודפס 0,1,2,3
ג. לולאה אינסופית
ד. שגיאת זמן ריצה

### שאלה 13

```python
data = [10,20,30,40,50]
print(data[1:4])
print(data[:])
print(data[-2:])
```

א. יודפס [20,30,40] ואז [10,20,30,40,50] ואז [40,50]
ב. יודפס [20,30] ואז [10,20,30,40] ואז [50]
ג. שגיאת זמן ריצה
ד. הדפסה זהה בכל השורות

### שאלה 14

```python
f = open("a.txt", "w")
f.write("hello")
f.close()

f = open("a.txt", "r")
print(f.read())
f.close()
```

א. יודפס hello
ב. יודפס שורה ריקה
ג. תתקבל שגיאה כי חסר \n
ד. תתקבל שגיאה כי צריך seek(0)

### שאלה 15

```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
    def __str__(self):
        return super().__str__() + " works at " + self.company

arr = [Employee("Avi", "Intel"), Person("Gil")]
print(arr[-1])
```

א. יודפס Avi works at Intel
ב. יודפס Gil
ג. יודפס Person
ד. שגיאת זמן ריצה

### שאלה 16

מה נכון לגבי סדר except?
א. `except Exception` צריך להיות אחרון בדרך כלל
ב. אין משמעות לסדר except
ג. `except ValueError` חייב להיות לפני try
ד. finally אסור להשתמש בו

### שאלה 17

```python
import math as m
print(m.sqrt(16))
```

א. יודפס 4.0
ב. יודפס 4
ג. שגיאת זמן ריצה כי אסור alias
ד. שגיאת תחביר

### שאלה 18

מה נכון לגבי הרצת קובץ Python?
א. חייבים main כדי שהקובץ ירוץ
ב. הקוד ברמת הקובץ רץ מלמעלה למטה בעת הרצה
ג. import מוחק את כל המשתנים הגלובליים
ד. אין אפשרות להשתמש ב if **name** == "**main**"

### שאלה 19

איזה איבר לא ניתן להכניס ל־set?
א. 5
ב. "hi"
ג. (1,2)
ד. [1,2]

### שאלה 20

מה הטענה הלא נכונה?
א. אפשר לבצע ירושה בפייתון
ב. אפשר לבצע polymorphism דרך דריסה (override)
ג. לכל מחלקה חייב להיות setter לכל שדה
ד. אפשר לממש “בנאי גמיש” עם args/kwargs

---

## מפתח תשובות מבחן תרגול 2

1-ג, 2-א, 3-ב, 4-ג, 5-א, 6-ג, 7-ג, 8-ב, 9-א, 10-א, 11-ב, 12-א, 13-א, 14-א, 15-ב, 16-א, 17-א, 18-ב, 19-ד, 20-ג





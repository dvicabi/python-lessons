## מבחן בפייתון
שם: ________________________________ כיתה: ________________

----------

1.  מה יודפס במסך לאחר הפעלת הקוד?
    

```python
numbers = [2, 5, 8, 11, 14]
numbers.append(20)
numbers[1] = 7
print(numbers[1], numbers[-1])

```

א. `5 20` ב. `7 20` ג. `7 14` ד. `5 14`

2.  מה תהיה תוצאת ההדפסה לאחר פעולות הרשימה?
    

```python
numbers = [1, 1, 1]
numbers.append(2)
numbers.insert(1, 2)
numbers.pop()
print(numbers)

```

א. `[1, 1, 1, 2]` ב. `[1, 2, 1, 1]` ג. `[1, 2, 1, 2]` ד. `[1, 1, 2, 1]`

3.  מה יודפס בלולאה?
    

```python
colors = ["red", "green", "blue"]
for c in colors:
    print(c, end=" * ")

```

א. `red * green * blue *` ב. `red * green * blue` ג. `["red", "green", "blue"]` ד. `red green blue`

4.  מה יהיה תוכן הרשימה לאחר הריצה?
    

```python
grades = [80, 95, 70, 95, 60]
grades.remove(95)
last = grades.pop()
grades.insert(1, last)
grades.append(100)
print(grades)

```

א. `[80, 70, 95, 60, 100]` ב. `[80, 60, 70, 95, 100]` ג. `[80, 95, 70, 60, 100]` ד. `[60, 80, 70, 95, 100]`

5.  מה יודפס?
    

```python
nums = [3, 9, 12, -2, 9]
max_val = max(nums)
min_val = min(nums)
sum_val = sum(nums)
print(max_val - min_val, sum_val // len(nums))

```

א. `14 6` ב. `10 6` ג. `14 31` ד. `12 6`

6.  כמה מספרים יוכנסו לרשימה?
    

```python
values = []
x = int(input("Enter number: "))
while x >= 0:
    values.append(x)
    x = int(input("Enter number: "))
print(len(values))

```

התלמיד הקליד: `5 10 0 7 -3`

א. `3` ב. `4` ג. `5` ד. `2`

7.  מה יודפס?
    

```python
fruits = ["apple", "banana", "orange"]
fruits.append("kiwi")
print(len(fruits), fruits[0])

```

א. `3 apple` ב. `4 apple` ג. `4 banana` ד. `3 banana`

8.  איזו הודעה תודפס?
    

```python
scores = [100, 85, 90, 100, 70]
count_100 = scores.count(100)
avg = sum(scores) / len(scores)

if count_100 >= 2 and avg >= 90:
    print("Excellent class")
elif count_100 >= 1 and avg >= 80:
    print("Good class")
else:
    print("Keep working")

```

א. `Excellent class` ב. `Good class` ג. `Keep working` ד. לא יודפס דבר

9.  כתוב פונקציה בשם count_pass שמחזירה כמה ציונים ברשימה הם 60 ומעלה.  
    לאחר מכן כתוב קוד שקולט חמישה ציונים, מכניס אותם לרשימה ומדפיס את התוצאה.
    

----------

----------

----------

----------

----------

----------

----------

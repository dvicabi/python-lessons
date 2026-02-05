
## שאלה 1

מה יודפס למסך בסיום הריצה של הקוד הבא?

```python
nums = []

for i in range(5):
    if i % 2 == 0:
        nums.append(i)

print(nums)
```

---

## שאלה 2

מה הפלט הסופי של הקוד הבא?

```python
data = [1, 2, 3, 4]

for x in data:
    if x % 2 == 0:
        data.remove(x)

print(data)
```

---

## שאלה 3

מה יודפס למסך?

```python
lst = [10, 20, 30]

for i in range(len(lst)):
    if lst[i] > 15:
        lst[i] += 5

print(lst)
```

---

## שאלה 4

מה הפלט הסופי של הקוד הבא?

```python
numbers = []

for i in range(1, 6):
    if i <= 3:
        numbers.append(i)
    else:
        numbers.insert(0, i)

print(numbers)
```

---

## שאלה 5

מה יודפס למסך בסיום הריצה?

```python
items = [1, 2, 3, 4, 5]

i = 0
while i < len(items):
    if items[i] % 2 == 1:
        items.pop(i)
    else:
        i += 1

print(items)
```

---

## שאלה 6

מה הפלט שיודפס למסך?

```python
lst = [2, 4, 6]

for i in range(3):
    if len(lst) < 5:
        lst.append(i)
    else:
        lst.pop()

print(lst)
```

---

## שאלה 7

מה יודפס למסך?

```python
nums = [3, 6, 9, 12]

for i in range(len(nums)):
    if nums[i] % 3 == 0 and nums[i] > 6:
        nums[i] //= 3

print(nums)
```

---

## שאלה 8

מה הפלט הסופי?

```python
data = []

for i in range(5):
    if i % 2 == 0:
        data.insert(0, i)
    else:
        data.append(i)

print(data)
```

---

## שאלה 9

מה יודפס למסך בסיום הקוד?

```python
lst = [5, 10, 15]

i = 0
while i < len(lst):
    if lst[i] >= 10:
        lst.append(lst[i] // 5)
    i += 1

print(lst)
```

<!-- DC_HEADER_START -->
<div align="center">

🐍 **Python Learning Series | סדרת לימודי פייתון**  
**Dvir Cabessa | דביר קבסה**  
© 2025 All Rights Reserved | כל הזכויות שמורות

</div>

---
<!-- DC_HEADER_END -->

# 📘 פתרונות – טיפוסים משתנים ולא משתנים (Mutable vs Immutable)

## 🧪 פתרונות לתרגילים

### תרגיל 1
```python
def add_five(num):
    num += 5
    print("Inside function:", num)

x = 10
add_five(x)
print("Outside function:", x)  # Output: 10
````

### תרגיל 2

```python
def add_99(lst):
    lst.append(99)
    print("Inside function:", lst)

my_list = [1, 2, 3]
add_99(my_list)
print("Outside function:", my_list)  # Output: [1, 2, 3, 99]
```

### תרגיל 3

```python
def to_upper(s):
    print("Inside function:", s.upper())

text = "hello"
to_upper(text)
print("Outside function:", text)  # Output: "hello"
```

### תרגיל 4

```python
def update_dict(d):
    d["name"] = "Updated"
    print("Inside function:", d)

person = {"name": "Dvir", "age": 24}
update_dict(person)
print("Outside function:", person)  # Output includes the change
```

### תרגיל 5

```python
def try_to_add(tpl):
    tpl += (100,)
    print("Inside function:", tpl)

my_tuple = (1, 2, 3)
try_to_add(my_tuple)
print("Outside function:", my_tuple)  # Output: (1, 2, 3)
```

### תרגיל 6

```python
def show_ids():
    x = 5
    print("ID before:", id(x))
    x += 1
    print("ID after:", id(x))

    l = [1, 2]
    print("ID before:", id(l))
    l.append(3)
    print("ID after:", id(l))

show_ids()
```

### תרגיל 7

```python
def modify_list(lst):
    if lst:
        lst[0] = "Modified"
    print("Inside function:", lst)

data = ["Original", "Keep"]
modify_list(data)
print("Outside function:", data)  # Output: ["Modified", "Keep"]
```

### תרגיל 8

```python
def lowercase_all(strings):
    for i in range(len(strings)):
        strings[i] = strings[i].lower()
    print("Inside function:", strings)

words = ["HELLO", "WORLD"]
lowercase_all(words)
print("Outside function:", words)  # Output: ["hello", "world"]
```

## 💬 הערות כלליות

* טיפוסים בלתי משתנים כמו `int`, `str`, `tuple` לא משתנים מחוץ לפונקציה – כל שינוי יוצר עותק חדש.
* טיפוסים משתנים כמו `list`, `dict` נשמרים בזיכרון – ושינויים משפיעים גם על המקור.
* השימוש ב־`id()` מאפשר לראות האם האובייקט בזיכרון באמת נשמר או הוחלף.
*

<!-- DC_FOOTER_START -->
---

<div align="center">

✨ **Thank you for learning with Dvir Cabessa** ✨  
✨ **תודה שלמדתם עם דביר קבסה** ✨  

📘 *All Rights Reserved © Dvir Cabessa 2025*  
📘 *כל הזכויות שמורות © דביר קבסה 2025*  

🔗 *For educational purposes only – copying or distribution without permission is prohibited.*  
🔗 *החומר נועד לשימוש חינוכי בלבד — אין להעתיק או להפיץ ללא אישור.*

---

> _"Education is the art of awakening curiosity and guiding it toward creation."_  
> _"החינוך הוא אמנות המעירה את הסקרנות ומכוונת אותה ליצירה."_  
> — **Dvir Cabessa**

</div>
<!-- DC_FOOTER_END -->


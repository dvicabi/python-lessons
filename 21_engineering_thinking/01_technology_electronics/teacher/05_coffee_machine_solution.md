# פתרונות למורה: מכונת קפה: איך הזמנה הופכת לעסקה תקינה?

[חזרה למשימת התלמיד](../05_coffee_machine.md)

כל פתרון הוא דרך אפשרית. יש לדרוש מהתלמידים הסבר ותכנון, ולא רק התאמה לפלט. מומלץ לחשוף כל רמה רק לאחר שנלמד החומר שלה. הפתרונות במאגר ציבורי.

## רמה 1: תצוגה: print ו-end

### א. פלט קריאת הקוד

```text
Drink: LATTE
Paid: 20 | Change: 8
```

end מחליף את ירידת השורה במפריד | עם רווחים.

### ב. שינוי ודיון

Paid: 20 ו-Change: 8 יוצגו בשורות שונות; המידע לא משתנה.

### ג. פתרון אפשרי

```python
print("Drink: ", end="")
print("ESPRESSO")
print("Paid: 10", end=" | ")
print("Change: 2")
```

פלט:

```text
Drink: ESPRESSO
Paid: 10 | Change: 2
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט קריאת הקוד

```text
4 4 3
20
```

אספרסו אינו צורך חלב; לאטה צורך 2.

### ב. שינוי ודיון

הכנסות יוצגו כ-8 במקום 20; השמה מוחקת את הסכום הקודם.

### ג. פתרון אפשרי

```python
coffee = 10
water = 12
milk = 6
revenue = 0
coffee -= 2
water -= 3
milk -= 2
revenue += 12
coffee -= 2
water -= 3
milk -= 2
revenue += 12
coffee -= 1
water -= 2
revenue += 8
print(coffee, water, milk)
print(revenue)
```

פלט:

```text
5 4 2
32
```

---

## רמה 3: קלט מהמשתמש

### א. פלט קריאת הקוד

```text
Price: 12
Change: 8
```

change=0; אין עודף.

### ב. שינוי ודיון

Price: 12, Change: -5. צריך לדחות עסקה שאין לה תשלום מספיק.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
30
```

```python
paid = int(input())
price = 2 * 8 + 12
change = paid - price
print("Price:", price)
print("Change:", change)
```

פלט:

```text
Price: 28
Change: 2
```

---

## רמה 4: תנאים

### א. פלט קריאת הקוד

```text
REJECTED
Refund: 20
5 4 1
```

חסר חלב; and דורש את כל ארבעת התנאים.

### ב. שינוי ודיון

החלב מספיק אך המחיר 12; REJECTED, Refund: 11, מלאי 5 4 2.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
1
10
1
2
0
```

```python
kind = int(input())
paid = int(input())
coffee = int(input())
water = int(input())
milk = int(input())
if kind == 1:
    c = 1
    w = 2
    m = 0
    price = 8
else:
    c = 2
    w = 3
    m = 2
    price = 12
if coffee >= c and water >= w and milk >= m and paid >= price:
    coffee -= c
    water -= w
    milk -= m
    print("SERVED", paid - price)
else:
    print("REJECTED", paid)
print(coffee, water, milk)
```

פלט:

```text
SERVED 2
0 0 0
```

---

## רמה 5: לולאות

### א. פלט קריאת הקוד

```text
SERVED 12
SERVED 24
REJECTED
REJECTED
1 1 0
```

הכנסה נרשמת רק בהצלחה; כאן שתי הזמנות מתוך ארבע.

### ב. שינוי ודיון

אחת; יישארו 3 קפה, 2 מים, 2 חלב והכנסות 12.

### ג. פתרון אפשרי

קלט לבדיקה:

```text
4
10
12
20
15
```

```python
count = int(input())
coffee = 4
water = 6
milk = 4
revenue = 0
for order in range(count):
    paid = int(input())
    if paid >= 12 and coffee >= 2 and water >= 3 and milk >= 2:
        coffee -= 2
        water -= 3
        milk -= 2
        revenue += 12
        print("SERVED")
    else:
        print("REJECTED")
print("Revenue:", revenue)
```

פלט:

```text
REJECTED
SERVED
SERVED
REJECTED
Revenue: 24
```

---

## רמה 6: רשימות בלבד

### א. פלט קריאת הקוד

```text
['SERVED', 'SERVED', 'REJECTED', 'SERVED']
1 0 1
```

משקה אחר עשוי לצרוך פחות משאב חסר; אספרסו אחרון אפשרי.

### ב. שינוי ודיון

['SERVED','REJECTED','SERVED','SERVED']; עדיין שלוש הצלחות, אבל במיקומים אחרים. כדי להראות מקרה שבו הסדר כן משנה את מספר ההצלחות, השתמשו במלאי 2 קפה, 4 מים, 2 חלב: [2,1,1] מאפשר משקה אחד, [1,1,2] מאפשר שניים.

### ג. פתרון אפשרי

```python
orders = [2, 1, 2, 1]
payments = [20, 7, 12, 10]
coffee = 5
water = 7
milk = 3
income = []
refunds = []
for i in range(len(orders)):
    if orders[i] == 1:
        c = 1
        w = 2
        m = 0
        price = 8
    else:
        c = 2
        w = 3
        m = 2
        price = 12
    if payments[i] >= price and coffee >= c and water >= w and milk >= m:
        coffee -= c
        water -= w
        milk -= m
        income.append(price)
        refunds.append(payments[i] - price)
    else:
        income.append(0)
        refunds.append(payments[i])
print(income)
print(refunds)
print(coffee, water, milk)
```

פלט:

```text
[12, 0, 0, 8]
[8, 7, 12, 2]
2 2 1
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט קריאת הקוד

```text
12
ERROR
8
```

משקה לא מוכר מחזיר רשימה ריקה; אינדקס 3 לא קיים.

### ב. שינוי ודיון

12, 12, 8 בשלוש שורות.

### ג. פתרון אפשרי

```python
def recipe(kind):
    if kind == 1:
        return [1, 2, 0, 8]
    if kind == 2:
        return [2, 3, 2, 12]
    return []

def can_serve(kind, paid, stock):
    values = recipe(kind)
    if len(values) == 0:
        return False
    return paid >= values[3] and stock[0] >= values[0] and stock[1] >= values[1] and stock[2] >= values[2]

stock = [3, 4, 1]
for kind in [2, 1, 3]:
    print(can_serve(kind, 15, stock))
print(stock)
```

פלט:

```text
False
True
False
[3, 4, 1]
```

---

## רמה 8: מחלקות

### א. פלט קריאת הקוד

```text
2
10
8 0
```

התשלום המוחזר לבדו אינו סטטוס מפורש; אפשר להחזיר גם מצב ברשימה.

### ב. שינוי ודיון

2, 2, 8 8; כעת גם b מצליחה.

### ג. פתרון אפשרי

```python
def recipe(kind):
    if kind == 1:
        return [1, 2, 0, 8]
    if kind == 2:
        return [2, 3, 2, 12]
    return []

class CoffeeMachine:
    def __init__(self, coffee, water, milk):
        self.stock = [coffee, water, milk]
        self.revenue = 0

    def serve(self, kind, paid):
        values = recipe(kind)
        if len(values) == 0:
            return ["ERROR", paid]
        if paid < values[3] or self.stock[0] < values[0] or self.stock[1] < values[1] or self.stock[2] < values[2]:
            return ["REJECTED", paid]
        for i in range(3):
            self.stock[i] -= values[i]
        self.revenue += values[3]
        return ["SERVED", paid - values[3]]

a = CoffeeMachine(2, 3, 2)
b = CoffeeMachine(1, 2, 0)
print(a.serve(2, 15))
print(a.serve(1, 8))
print(b.serve(1, 8))
print(a.revenue, b.revenue)
```

פלט:

```text
['SERVED', 3]
['REJECTED', 8]
['SERVED', 0]
12 8
```

---

## אתגר מסכם

אין פתרון יחיד. בדקו שהדרישות ברורות, שהכללים נשמרים, שהפתרון נבדק במקרי קצה ושניתן לנמק את הבחירה ההנדסית. אין לדרוש נושא תכנות שלא נלמד.

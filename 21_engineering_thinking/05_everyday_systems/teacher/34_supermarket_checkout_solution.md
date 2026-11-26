# פתרונות למורה: קופה בסופר: איך מבצעים עסקה עם מבצעים ומלאי מוגבל?

[חזרה למשימת התלמיד](../34_supermarket_checkout.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
CHECKOUT 01 | DEMO
Items: 4 units
Subtotal: 40 NIS
Discount: 8 NIS
Total: 32 | READY
```

### ב. פלט התרחיש השני

```text
CHECKOUT  | 01 | DEMO
Items: 4 units
Subtotal: 40 NIS
Discount: 8 NIS
Total: 32 | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("CHECKOUT ", end="")
print("02", end="")
print(" | DEMO")
print("Items: ", end="")
print("2", end="")
print(" units")
print("Subtotal: ", end="")
print("20", end="")
print(" NIS")
print("Discount: ", end="")
print("0", end="")
print(" NIS")
print("Total: ", end="")
print("20", end="")
print(" | READY")
```

פלט:

```text
CHECKOUT 02 | DEMO
Items: 2 units
Subtotal: 20 NIS
Discount: 0 NIS
Total: 20 | READY
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
18 2 20 0
15 5 44 6
11 9 76 14
Check: 20
Gross: 90
```

### ב. פלט התרחיש השני

```text
18 2 20 0
15 5 44 6
10 10 84 16
Check: 20
Gross: 100
```

### ג. תשובות והערות לדיון

כל עסקה עצמאית.

stock+sold=20.

הסכום לפני הנחה מורכב מהנטו ומהנחה.

הנחה שנשארה מעסקה קודמת תחייב בחסר.

### ד. פתרון אפשרי

```python
stock = 15
price = 8
revenue = 0
discount_total = 0
sold = 0
quantity = 1
gross = quantity * price
discount = 0
net = gross - discount
stock -= quantity
sold += quantity
revenue += net
discount_total += discount
print(stock, sold, revenue, discount_total)
quantity = 3
gross = quantity * price
discount = quantity * 2
net = gross - discount
stock -= quantity
sold += quantity
revenue += net
discount_total += discount
print(stock, sold, revenue, discount_total)
quantity = 5
gross = quantity * price
discount = quantity * 2
net = gross - discount
stock -= quantity
sold += quantity
revenue += net
discount_total += discount
print(stock, sold, revenue, discount_total)
print("Check:", stock + sold)
print("Gross:", revenue + discount_total)
```

פלט:

```text
14 1 8 0
11 4 26 6
6 9 56 16
Check: 15
Gross: 72
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
A: 30 24
B: 16 16
Total: 40 Change: 20
Check: 40
```

### ב. פלט התרחיש השני

```text
A: 30 24
B: 16 16
Total: 40 Change: -5
Check: 40
```

### ג. תשובות והערות לדיון

עודף שלילי הוא תשלום חסר.

הנחה שאינה חוקית דורשת בדיקה.

נטו שורות שווה ברוטו פחות הנחה כוללת.

המבצע משפיע על המחיר בפועל.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
10
3
8
2
5
4
14
60
```

```python
p1 = int(input())
q1 = int(input())
p2 = int(input())
q2 = int(input())
p3 = int(input())
q3 = int(input())
discount = int(input())
paid = int(input())
g1 = p1 * q1
g2 = p2 * q2
g3 = p3 * q3
gross = g1 + g2 + g3
net = gross - discount
print(g1, g2, g3)
print(gross, discount, net, paid - net)
```

פלט:

```text
30 16 20
66 14 52 8
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
OK 24 6
Change: 0
2 24
```

### ב. פלט התרחיש השני

```text
NO FUNDS 32 8
Refund: 24
5 0
```

### ג. תשובות והערות לדיון

המחיר האמיתי כולל מבצע.

כל תנאי חייב להתקיים.

3 מקבלת הנחה.

סוגי דחייה שונים.

קלט שלילי אינו תשלום תקף ויש לדווח שגיאה בלי החזר כספי מדומה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
10
3
24
```

```python
stock = int(input())
price = int(input())
quantity = int(input())
paid = int(input())
revenue = 0
discount = 0
total = 0
if quantity <= 0 or paid < 0:
    status = "INVALID"
else:
    gross = price * quantity
    if quantity >= 3:
        discount = quantity * 2
    total = gross - discount
    if quantity > stock:
        status = "NO STOCK"
    elif paid < total:
        status = "NO FUNDS"
    else:
        stock -= quantity
        revenue += total
        status = "OK"
print(status, total, discount)
if status == "OK":
    print("Change:", paid - total)
else:
    print("Refund:", paid)
print(stock, revenue)
if status == "OK":
    print(discount)
else:
    print(0)
```

פלט:

```text
OK 24 6
Change: 0
2 24
6
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 OK 13 20
2 DENIED 13 20
3 OK 10 44
4 OK 6 76
5 DENIED 6 76
6 OK 5 86
7 INVALID 5 86
4 2 1
86 14 10
Check: 15
```

### ב. פלט התרחיש השני

```text
1 OK 13 20
2 OK 10 44
3 OK 7 68
4 OK 3 100
5 DENIED 3 100
6 OK 2 110
7 INVALID 2 110
5 1 1
110 20 13
Check: 15
```

### ג. תשובות והערות לדיון

הנחות בפועל רק לעסקאות מוצלחות.

ok מונה עסקאות ו-sold יחידות.

סכום שלושת המונים שווה למספר אירועים.

עסקה קטנה יותר עשויה להתאים.

מוסיפים ענפי תנאי נפרדים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
7
15
10
2
20
3
23
3
24
4
40
8
80
1
10
0
0
```

```python
count = int(input())
stock = int(input())
price = int(input())
initial = stock
promo = 0
revenue = 0
sold = 0
discount_total = 0
ok = 0
denied = 0
invalid = 0
for i in range(count):
    quantity = int(input())
    paid = int(input())
    if quantity <= 0 or paid < 0:
        invalid += 1
        status = "INVALID"
    else:
        gross = price * quantity
        discount = 0
        if quantity >= 3:
            discount = 2 * quantity
        total = gross - discount
        if quantity > stock or paid < total:
            denied += 1
            status = "DENIED"
        else:
            stock -= quantity
            sold += quantity
            revenue += total
            discount_total += discount
            if quantity >= 3:
                promo += 1
            ok += 1
            status = "OK"
    print(i + 1, status, stock, revenue)
print(ok, denied, invalid)
print(revenue, discount_total, sold)
print("Check:", stock + sold == initial)
print(promo, sold * price == revenue + discount_total)
```

פלט:

```text
1 OK 13 20
2 DENIED 13 20
3 OK 10 44
4 OK 6 76
5 DENIED 6 76
6 OK 5 86
7 INVALID 5 86
4 2 1
86 14 10
Check: True
2 True
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
OK 3
[4, 2, 3]
57 14
[1, 2, 4]
```

### ב. פלט התרחיש השני

```text
DENIED
[4, 2, 3]
57 14
[3, 4, 7]
```

### ג. תשובות והערות לדיון

שורות חוזרות יכולות יחד לחרוג ממלאי.

מוצר 0 מגיע ל-4.

עדכון רק אחרי אימות כל הסל.

מזהה שגוי מסמן כשל.

בדיקה מול needed מגנה על מלאי.

### ד. פתרון אפשרי

```python
prices = [10, 8, 5]
stock = [5, 4, 7]
cart = [[0, 2], [1, 2], [0, 2], [2, 3]]
paid = 60
needed = [0, 0, 0]
valid = True
for row in cart:
    item = row[0]
    qty = row[1]
    if item < 0 or item >= len(prices) or qty <= 0:
        valid = False
    else:
        needed[item] += qty
total = 0
discount = 0
net_prices = []
shortages = []
for i in range(len(prices)):
    if needed[i] > stock[i]:
        valid = False
        shortages.append(i)
    gross = needed[i] * prices[i]
    line_discount = 0
    if needed[i] >= 3:
        line_discount = needed[i] * 2
    discount += line_discount
    net_prices.append(gross - line_discount)
    total += gross
total -= discount
if paid < total:
    valid = False
if valid:
    for i in range(len(stock)):
        stock[i] -= needed[i]
    print("OK", paid - total)
else:
    print("DENIED")
print(needed)
print(total, discount)
print(stock)
print(net_prices, shortages)
```

פלט:

```text
OK 3
[4, 2, 3]
57 14
[1, 2, 4]
[32, 16, 9] []
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
['OK', 40, [3, 2, 0]]
0
[2, 2, 7]
NO STOCK
[2, 2, 7]
```

### ב. פלט התרחיש השני

```text
['OK', 46, [3, 2, 0]]
NO FUNDS
[5, 4, 7]
4
[2, 2, 7]
```

### ג. תשובות והערות לדיון

3 בדיוק זכאית להנחה.

quote שאילתה;

aggregate מאחדת כמויות, quote בודקת ומתמחרת.

שומרים stock לפני ואחרי תשלום חסר.

סל ריק נדחה לפי המפרט.

### ד. פתרון אפשרי

```python
def aggregate(cart, count):
    needed = []
    for i in range(count):
        needed.append(0)
    for row in cart:
        item = row[0]
        qty = row[1]
        if item < 0 or item >= count or qty <= 0:
            return []
        needed[item] += qty
    return needed

def quote(prices, stock, cart):
    needed = aggregate(cart, len(prices))
    if len(cart) == 0 or len(needed) == 0:
        return ["INVALID", 0, []]
    total = 0
    for i in range(len(prices)):
        if needed[i] > stock[i]:
            return ["NO STOCK", 0, needed]
        total += needed[i] * prices[i]
        if needed[i] >= 3:
            total -= needed[i] * 2
    return ["OK", total, needed]

def checkout(prices, stock, cart, paid):
    result = quote(prices, stock, cart)
    if result[0] != "OK":
        return [result[0], paid, 0]
    if paid < result[1]:
        return ["NO FUNDS", paid, 0]
    for i in range(len(stock)):
        stock[i] -= result[2][i]
    return ["OK", paid - result[1], result[1]]

prices = [10, 8, 5]
stock = [5, 4, 7]
cart = [[0, 2], [0, 1], [1, 2]]
print(quote(prices, stock, cart))
print(checkout(prices, stock, cart, 40))
print(stock)
print(checkout(prices, stock, [], 20))
print(checkout(prices, stock, [[9, 1]], 20))
print(checkout(prices, stock, cart, 50))
print(stock)
```

פלט:

```text
['OK', 40, [3, 2, 0]]
['OK', 0, 40]
[2, 2, 7]
['INVALID', 20, 0]
['INVALID', 20, 0]
['NO STOCK', 50, 0]
[2, 2, 7]
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
40 33
OK
DUPLICATE
DENIED
[1, 40, [2, 2, 7]]
[[101, 'OK'], [101, 'DUPLICATE'], [102, 'DENIED']]
```

### ב. פלט התרחיש השני

```text
40 33
OK
DUPLICATE
OK
[2, 73, [0, 2, 4]]
[[101, 'OK'], [101, 'DUPLICATE'], [102, 'OK']]
```

### ג. תשובות והערות לדיון

סל מייצג דרישה, מלאי היצע.

מלאי עשוי להשתנות.

מזהה מונע חיוב כפול.

צילום מצב לא חושף רשימת מלאי לשינוי.

שני סלים מתחרים.

בכשל מלאי והכנסות לא משתנים.

### ד. פתרון אפשרי

```python
class Cart:
    def __init__(self, count):
        self.needed = []
        for i in range(count):
            self.needed.append(0)
        self.units = 0

    def add(self, item, qty):
        if item < 0 or item >= len(self.needed) or qty <= 0:
            return False
        self.needed[item] += qty
        self.units += qty
        return True

class Inventory:
    def __init__(self, prices, stock):
        self.prices = prices
        self.stock = stock

    def quote(self, cart):
        if cart.units == 0 or len(cart.needed) != len(self.stock):
            return -1
        total = 0
        for i in range(len(self.stock)):
            qty = cart.needed[i]
            if qty > self.stock[i]:
                return -1
            total += qty * self.prices[i]
            if qty >= 3:
                total -= qty * 2
        return total

    def take(self, cart):
        if self.quote(cart) == -1:
            return False
        for i in range(len(self.stock)):
            self.stock[i] -= cart.needed[i]
        return True

    def restock(self, item, qty):
        if item < 0 or item >= len(self.stock) or qty <= 0:
            return False
        self.stock[item] += qty
        return True

    def report(self):
        result = []
        for qty in self.stock:
            result.append(qty)
        return result

class Checkout:
    def __init__(self, inventory):
        self.inventory = inventory
        self.revenue = 0
        self.completed = []
        self.history = []
        self.denied = 0

    def pay(self, order, cart, paid):
        price = self.inventory.quote(cart)
        if order in self.completed:
            status = "DUPLICATE"
        elif price == -1:
            status = "DENIED"
        elif paid < price:
            status = "NO FUNDS"
        else:
            self.inventory.take(cart)
            self.revenue += price
            self.completed.append(order)
            status = "OK"
        if status != "OK":
            self.denied += 1
        self.history.append([order, status])
        return status

    def summary(self):
        return [len(self.completed), self.revenue, self.inventory.report()]

inventory = Inventory([10, 8, 5], [5, 4, 7])
register = Checkout(inventory)
a = Cart(3)
b = Cart(3)
a.add(0, 2)
a.add(0, 1)
a.add(1, 2)
b.add(0, 3)
b.add(2, 3)
print(inventory.quote(a), inventory.quote(b))
print(register.pay(101, a, 40))
print(register.pay(101, a, 50))
print(register.pay(102, b, 60))
print(register.summary())
print(register.history)
print(inventory.restock(0, 3))
print(register.pay(102, b, 60))
print(register.summary(), register.denied)
print(register.pay(101, a, 50))
```

פלט:

```text
40 33
OK
DUPLICATE
DENIED
[1, 40, [2, 2, 7]]
[[101, 'OK'], [101, 'DUPLICATE'], [102, 'DENIED']]
True
OK
[2, 73, [2, 2, 4]] 2
DUPLICATE
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

# פתרונות למורה: תחנת דלק: כיצד מנהלים מלאי, מחירים ועסקאות?

[חזרה למשימת התלמיד](../15_gas_station.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
PUMP 03 | TYPE 1
Quantity: 5 | Price: 35
Paid: 40 | Change: 5
```

### ב. פלט התרחיש השני

```text
PUMP 03 | TYPE 1
Quantity: 5 | Price: 35 | Paid: 40
Change: 5
```

### ג. תשובות והערות לדיון

המחיר הוא ערך העסקה, paid הוא כסף שהתקבל לפני עודף.

בתרחיש השני Paid מתחבר למחיר ו-Change יורד שורה.

המפרידים מגדירים מבנה קבלה.

### ד. פתרון אפשרי

```python
print("PUMP ", end="")
print("07", end=" | ")
print("TYPE 2")
print("Quantity: ", end="")
print("4", end=" | ")
print("Price: ", end="")
print("36")
print("Paid: ", end="")
print("50", end=" | ")
print("Change: 14")
```

פלט:

```text
PUMP 07 | TYPE 2
Quantity: 4 | Price: 36
Paid: 50 | Change: 14
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
34 42 8
34 21 78
Check: 78
```

### ב. פלט התרחיש השני

```text
34 42 8
34 22 69
Check: 69
```

### ג. תשובות והערות לדיון

revenue=paid_total-change_total.

בלי עדכון stock2 הדוח לא משקף מכירת סוג 2.

paid_total כולל כסף שיוחזר כעודף.

### ד. פתרון אפשרי

```python
stock1 = 30
stock2 = 20
revenue = 0
change = 0
cost = 3 * 7
stock1 -= 3
revenue += cost
change += 25 - cost
print(stock1, stock2)
cost = 2 * 9
stock2 -= 2
revenue += cost
change += 20 - cost
print(stock1, stock2)
cost = 4 * 7
stock1 -= 4
revenue += cost
change += 30 - cost
print(stock1, stock2)
print(revenue, change)
```

פלט:

```text
27 20
27 18
23 18
67 8
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
Type 1: 26 28 2
Type 2: 17 27 3
Revenue: 55
Net cash: 55
```

### ב. פלט התרחיש השני

```text
Type 1: 26 28 -2
Type 2: -1 27 -7
Revenue: 55
Net cash: 55
```

### ג. תשובות והערות לדיון

עודף שלילי פירושו תשלום חסר.

המשוואה נכונה אלגברית גם במקרה בלתי חוקי ולכן לא מספיקה.

צריך לבדוק כמות חיובית, מלאי ותשלום.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
25
7
3
25
4
30
2
15
```

```python
stock = int(input())
rate = int(input())
q1 = int(input())
p1 = int(input())
q2 = int(input())
p2 = int(input())
q3 = int(input())
p3 = int(input())
cost1 = q1 * rate
stock -= q1
print(cost1, p1 - cost1, stock)
cost2 = q2 * rate
stock -= q2
print(cost2, p2 - cost2, stock)
cost3 = q3 * rate
stock -= q3
print(cost3, p3 - cost3, stock)
print("Revenue:", cost1 + cost2 + cost3)
```

פלט:

```text
21 4 22
28 2 18
14 1 16
Revenue: 63
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
REJECTED 44
12 8 0
```

### ב. פלט התרחיש השני

```text
SERVED 0
12 3 45
```

### ג. תשובות והערות לדיון

stock הוא מספר מקומי, לא הפניה למלאי.

עסקה כושלת אינה משנה מצב.

בגבול התשלום מספיק והעודף 0.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
1
12
84
```

```python
stock1 = 12
stock2 = 8
revenue = 0
kind = int(input())
quantity = int(input())
paid = int(input())
if kind != 1 and kind != 2 or quantity <= 0 or paid < 0:
    print("ERROR")
else:
    if kind == 1:
        price = quantity * 7
        stock = stock1
    else:
        price = quantity * 9
        stock = stock2
    if quantity > stock or paid < price:
        print("REJECTED", paid)
    else:
        if kind == 1:
            stock1 -= quantity
        else:
            stock2 -= quantity
        revenue += price
        print("SERVED", paid - price)
print(stock1, stock2, revenue)
```

פלט:

```text
SERVED 0
0 8 84
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
SERVED 2 11
REJECTED 30
SERVED 0 1
ERROR
SERVED 0 0
3 1 105 0
```

### ב. פלט התרחיש השני

```text
SERVED 0 7
REJECTED 56
SERVED 0 0
REJECTED 7
ERROR
2 2 105 0
```

### ג. תשובות והערות לדיון

שגיאה אינה בקשה תקינה;

דחייה יכולה להיות מחוסר מלאי או תשלום.

עסקה קטנה יותר עשויה להצליח בהמשך.

הפחתה מוקדמת משבשת מלאי גם כשאין מכירה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
10
7
4
3
25
8
56
2
13
7
50
```

```python
stock = int(input())
rate = int(input())
count = int(input())
revenue = 0
refunds = 0
payments = 0
for i in range(count):
    quantity = int(input())
    paid = int(input())
    if quantity <= 0 or paid < 0:
        print("ERROR")
    else:
        cost = quantity * rate
        payments += paid
        if quantity > stock or paid < cost:
            refunds += paid
            print("REJECTED")
        else:
            stock -= quantity
            revenue += cost
            refunds += paid - cost
            print("SERVED")
print(revenue, refunds, payments)
print("Check:", payments - refunds)
print("Stock:", stock)
```

פלט:

```text
SERVED
REJECTED
REJECTED
SERVED
70 74 144
Check: 70
Stock: 0
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[5, 4]
[2, 3, 56, 17, 1]
Revenue: 62
```

### ב. פלט התרחיש השני

```text
[5, 2]
[2, 3, 56, 0, 1]
Revenue: 80
```

### ג. תשובות והערות לדיון

סוגים מתחילים ב-1 ורשימה ב-0.

kind=0 גורם לאינדקס -1 חוקי אך שגוי.

קבלה נשמרת לכל עסקה כדי לשמור התאמה;

אפשר להוסיף רשימת סטטוסים.

### ד. פתרון אפשרי

```python
kinds = [1, 2, 1, 2, 1, 3]
quantities = [4, 3, 8, 2, 1, 1]
payments = [30, 30, 56, 17, 8, 10]
stock = [10, 7]
rates = [7, 9]
income = [0, 0]
statuses = []
receipts = []
for i in range(len(kinds)):
    if kinds[i] < 1 or kinds[i] > 2:
        statuses.append("ERROR")
        receipts.append(payments[i])
    else:
        index = kinds[i] - 1
        cost = quantities[i] * rates[index]
        if quantities[i] > stock[index] or payments[i] < cost:
            statuses.append("REJECTED")
            receipts.append(payments[i])
        else:
            stock[index] -= quantities[i]
            income[index] += cost
            statuses.append("SERVED")
            receipts.append(payments[i] - cost)
print(stock)
print(statuses)
print(income)
print(receipts)
```

פלט:

```text
[5, 4]
['SERVED', 'SERVED', 'REJECTED', 'REJECTED', 'SERVED', 'ERROR']
[35, 27]
[2, 3, 56, 17, 1, 10]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[6, 28, 2, 'SERVED']
[6, 0, 50, 'REJECTED']
[0, 42, 0, 'SERVED']
0 70
```

### ב. פלט התרחיש השני

```text
[6, 28, 2, 'SERVED']
[1, 35, 15, 'SERVED']
[1, 0, 42, 'REJECTED']
1 63
```

### ג. תשובות והערות לדיון

מספרים מועברים כערכים;

החזרה מתארת מצב מוצע.

סטטוס מבדיל שגיאה, החזר ועודף.

צבירה היא אחריות הקוד הקורא.

### ד. פתרון אפשרי

```python
def sell(stock, rate, quantity, paid):
    if quantity <= 0 or paid < 0:
        return [stock, 0, 0, "ERROR"]
    cost = quantity * rate
    if quantity > stock or paid < cost:
        return [stock, 0, paid, "REJECTED"]
    return [stock - quantity, cost, paid - cost, "SERVED"]

def process(stock, rate, quantities, payments):
    if len(quantities) != len(payments):
        return []
    revenue = 0
    statuses = []
    refunds = []
    for i in range(len(quantities)):
        result = sell(stock, rate, quantities[i], payments[i])
        stock = result[0]
        revenue += result[1]
        refunds.append(result[2])
        statuses.append(result[3])
    return [stock, revenue, statuses, refunds]

print(process(10, 7, [4, 7, 6], [30, 50, 42]))
print(process(10, 7, [4], []))
```

פלט:

```text
[0, 70, ['SERVED', 'REJECTED', 'SERVED'], [2, 50, 0]]
[]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
2
3
REJECTED
0
[6, 7] [28, 0] ['SERVED', 'REJECTED']
[0, 7] [35, 27] ['SERVED', 'SERVED']
```

### ב. פלט התרחיש השני

```text
2
3
0
0
[0, 7] [70, 0] ['SERVED', 'SERVED']
[0, 7] [35, 27] ['SERVED', 'SERVED']
```

### ג. תשובות והערות לדיון

רשימה מאפשרת הכנסה לכל סוג.

עודף 0 חוקי.

ERROR אינו נרשם כרגע;

אפשר לשמור סטטוס לכל בקשה, סכום ונתונים.

### ד. פתרון אפשרי

```python
class Station:
    def __init__(self, stock1, stock2):
        self.stock = [stock1, stock2]
        self.rates = [7, 9]
        self.income = [0, 0]
        self.history = []

    def sell(self, kind, quantity, paid):
        if kind < 1 or kind > 2 or quantity <= 0 or paid < 0:
            return "ERROR"
        index = kind - 1
        cost = quantity * self.rates[index]
        if quantity > self.stock[index] or paid < cost:
            self.history.append("REJECTED")
            return "REJECTED"
        self.stock[index] -= quantity
        self.income[index] += cost
        self.history.append("SERVED")
        return paid - cost

    def restock(self, kind, amount):
        if 1 <= kind and kind <= 2 and amount > 0:
            index = kind - 1
            self.stock[index] += amount
            if self.stock[index] > 20:
                self.stock[index] = 20

    def total_income(self):
        return self.income[0] + self.income[1]

a = Station(10, 7)
b = Station(5, 10)
print(a.sell(1, 4, 30))
print(b.sell(2, 3, 30))
print(a.sell(1, 7, 50))
print(b.sell(1, 5, 35))
print(a.stock, a.income, a.history)
print(b.stock, b.income, b.history)
a.restock(1, 30)
print(a.sell(1, 4, 28))
print(a.stock, a.total_income())
print(b.stock, b.total_income())
```

פלט:

```text
2
3
REJECTED
0
[6, 7] [28, 0] ['SERVED', 'REJECTED']
[0, 7] [35, 27] ['SERVED', 'SERVED']
0
[16, 7] 56
[0, 7] 62
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

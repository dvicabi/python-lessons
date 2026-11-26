# פתרונות למורה: מכונת חטיפים: מה קורה אם המוצר לא יוצא או שאין עודף?

[חזרה למשימת התלמיד](../35_vending_machine.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
VEND 01 | DEMO
Product: A | READY
Price: 7 NIS
Paid: 10 NIS
Change: 3 | CHECK
```

### ב. פלט התרחיש השני

```text
VEND  | 01 | DEMO
Product: A | READY
Price: 7 NIS
Paid: 10 NIS
Change: 3 | CHECK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("VEND ", end="")
print("02", end="")
print(" | DEMO")
print("Product: ", end="")
print("B", end="")
print(" | SOLD")
print("Price: ", end="")
print("5", end="")
print(" NIS")
print("Paid: ", end="")
print("5", end="")
print(" NIS")
print("Change: ", end="")
print("0", end="")
print(" | DONE")
```

פלט:

```text
VEND 02 | DEMO
Product: B | SOLD
Price: 5 NIS
Paid: 5 NIS
Change: 0 | DONE
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
7 27 7 10 3
6 22 12 20 8
5 17 19 32 13
Cash check: 30
Sales check: 19
```

### ב. פלט התרחיש השני

```text
7 27 7 10 3
6 22 12 20 8
5 15 19 34 15
Cash check: 30
Sales check: 19
```

### ג. תשובות והערות לדיון

vault הוא מטבעות עודף, revenue הוא תמורת מוצרים.

paid_total-change_total=revenue.

כל עסקה היא מוצר יחיד.

vault+change_total אמור להיות 30.

### ד. פתרון אפשרי

```python
stock = 10
vault = 40
revenue = 0
paid_total = 0
change_total = 0
price = 6
paid = 10
change = paid - price
stock -= 1
vault -= change
revenue += price
paid_total += paid
change_total += change
print(stock, vault, revenue, paid_total, change_total)
price = 8
paid = 8
change = paid - price
stock -= 1
vault -= change
revenue += price
paid_total += paid
change_total += change
print(stock, vault, revenue, paid_total, change_total)
price = 5
paid = 12
change = paid - price
stock -= 1
vault -= change
revenue += price
paid_total += paid
change_total += change
print(stock, vault, revenue, paid_total, change_total)
print("Cash check:", vault + change_total)
print("Sales check:", paid_total - change_total)
```

פלט:

```text
9 36 6 10 4
8 36 14 18 4
7 29 19 30 11
Cash check: 40
Sales check: 19
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
Due: 6 Offered: 6 Gap: 0
Coins: 2
Remaining: -1 3 0
Value: 11 5
```

### ב. פלט התרחיש השני

```text
Due: 6 Offered: 6 Gap: 0
Coins: 3
Remaining: 2 0 1
Value: 13 7
```

### ג. תשובות והערות לדיון

פער אפס פירושו סכום תואם אך לא בהכרח זמין.

מלאי עלול להיות שלילי אחרי הפחתה.

due שלילי הוא תשלום חסר.

ערכי המטבעות שונים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
7
13
2
4
2
2
0
3
```

```python
price = int(input())
paid = int(input())
stock1 = int(input())
stock2 = int(input())
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
due = paid - price
a = a1 + 2 * a2
b = b1 + 2 * b2
print(a, due - a, a1 + a2, stock1 - a1, stock2 - a2)
print(b, due - b, b1 + b2, stock1 - b1, stock2 - b2)
```

פלט:

```text
6 0 4 0 2
6 0 3 2 1
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
JAM
Refund: 13
2 3 0
```

### ב. פלט התרחיש השני

```text
OK
Change: 6
1 0 7
```

### ג. תשובות והערות לדיון

מסירה מדומה חייבת להצליח.

כשל עודף לעומת כשל מסירה שונים.

עודף 0 חוקי אם n2=0.

בדחייה אין עסקה ולכן מחזירים הכל.

הפחתה מוקדמת מאבדת מוצר בדוח.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
2
7
13
3
3
1
```

```python
stock = int(input())
price = int(input())
paid = int(input())
coin2 = int(input())
n2 = int(input())
dispensed = int(input())
revenue = 0
due = paid - price
if paid < price:
    status = "NO FUNDS"
elif stock <= 0:
    status = "SOLD OUT"
elif n2 > coin2 or n2 * 2 != due:
    status = "NO CHANGE"
elif dispensed != 1:
    status = "JAM"
else:
    stock -= 1
    coin2 -= n2
    revenue += price
    status = "OK"
print(status)
if status == "OK":
    print("Change:", due)
else:
    print("Refund:", paid)
print(stock, coin2, revenue)
print("Charged:", revenue)
```

פלט:

```text
OK
Change: 6
1 0 7
Charged: 7
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
0 3 0 3
Best: 0 3 0 3
8 1
```

### ב. פלט התרחיש השני

```text
0 1 1 2
Best: 0 1 1 2
8 1
```

### ג. תשובות והערות לדיון

נותר 1 ואין מטבע 1.

tested הוא מכפלת תחומי הכמויות.

אפס הוא כמות חוקית.

עודף 0 מחזיר שלושה אפסים.

best=-1 לאחר סריקה מציין אין פתרון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
0
3
1
```

```python
due = int(input())
coin1 = int(input())
coin2 = int(input())
coin5 = int(input())
best = -1
best1 = 0
best2 = 0
best5 = 0
tested = 0
matches = 0
for a in range(coin1 + 1):
    for b in range(coin2 + 1):
        for c in range(coin5 + 1):
            tested += 1
            value = a + b * 2 + c * 5
            if value == due:
                matches += 1
                count = a + b + c
                print(a, b, c, count)
                if best == -1 or count < best:
                    best = count
                    best1 = a
                    best2 = b
                    best5 = c
if best == -1:
    print("NO CHANGE")
else:
    print("Best:", best1, best2, best5, best)
    print("Check:", best1 + best2 * 2 + best5 * 5)
print(tested, matches)
```

פלט:

```text
0 3 0 3
Best: 0 3 0 3
Check: 6
8 1
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
0 JAM [2, 2] [0, 3, 1]
0 OK [1, 2] [0, 0, 1]
1 OK [1, 1] [0, 0, 0]
1 NO CHANGE [1, 1] [0, 0, 0]
['JAM', 'OK', 'OK', 'NO CHANGE']
Revenue: 12
```

### ב. פלט התרחיש השני

```text
0 JAM [2, 2] [1, 3, 1]
0 OK [1, 2] [0, 3, 0]
1 NO CHANGE [1, 2] [0, 3, 0]
1 OK [1, 1] [0, 2, 0]
['JAM', 'OK', 'NO CHANGE', 'OK']
Revenue: 12
```

### ג. תשובות והערות לדיון

כל הרכב תלוי במלאי העדכני.

תקלה לא משלימה עסקה.

עודף 0 יוצר [0,0,0].

משאבים שונים.

מזהי מוצר חוקיים ותשלום לא שלילי, ודגל מסירה 0 או 1.

### ד. פתרון אפשרי

```python
prices = [7, 5]
stock = [2, 2]
coins = [0, 3, 1]
orders = [[0, 13, 0], [0, 13, 1], [1, 10, 1], [1, 7, 1]]
revenue = 0
history = []
refunded = 0
change_total = 0
paid_total = 0
for order in orders:
    item = order[0]
    paid = order[1]
    paid_total += paid
    dispensed = order[2]
    due = paid - prices[item]
    best = []
    best_count = -1
    if due < 0 or stock[item] == 0:
        status = "DENIED"
    else:
        for a in range(coins[0] + 1):
            for b in range(coins[1] + 1):
                for c in range(coins[2] + 1):
                    if a + b * 2 + c * 5 == due:
                        count = a + b + c
                        if best_count == -1 or count < best_count:
                            best = [a, b, c]
                            best_count = count
        if len(best) == 0:
            status = "NO CHANGE"
        elif dispensed != 1:
            status = "JAM"
        else:
            stock[item] -= 1
            for i in range(3):
                coins[i] -= best[i]
            revenue += prices[item]
            status = "OK"
    if status == "OK":
        change_total += due
    else:
        refunded += paid
    history.append(status)
    print(item, status, stock, coins)
print(history)
print("Revenue:", revenue)
print(paid_total, refunded, change_total)
print(paid_total == refunded + change_total + revenue)
```

פלט:

```text
0 JAM [2, 2] [0, 3, 1]
0 OK [1, 2] [0, 0, 1]
1 OK [1, 1] [0, 0, 0]
1 NO CHANGE [1, 1] [0, 0, 0]
['JAM', 'OK', 'OK', 'NO CHANGE']
Revenue: 12
43 20 11
True
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
['READY', [0, 3, 0]]
['READY', [0, 0, 0]]
['DENIED', []]
['NO CHANGE', []]
[2, 0] [0, 3, 1]
```

### ב. פלט התרחיש השני

```text
['READY', [1, 0, 1]]
['READY', [0, 0, 0]]
['DENIED', []]
['READY', [1, 0, 0]]
[2, 0] [1, 3, 1]
```

### ג. תשובות והערות לדיון

תכנון ללא התחייבות.

שלושה אפסים הם הרכב תקין.

ריק מציין אין פתרון.

משווים לפני ואחרי.

אינדקס שלילי עלול לגשת למוצר לא נכון.

### ד. פתרון אפשרי

```python
def change(coins, due):
    best = []
    best_count = -1
    for a in range(coins[0] + 1):
        for b in range(coins[1] + 1):
            for c in range(coins[2] + 1):
                if a + b * 2 + c * 5 == due:
                    count = a + b + c
                    if best_count == -1 or count < best_count:
                        best = [a, b, c]
                        best_count = count
    return best

def quote(prices, stock, coins, item, paid):
    if item < 0 or item >= len(prices) or paid < 0:
        return ["INVALID", []]
    if stock[item] == 0 or paid < prices[item]:
        return ["DENIED", []]
    notes = change(coins, paid - prices[item])
    if len(notes) == 0:
        return ["NO CHANGE", []]
    return ["READY", notes]

def commit(prices, stock, coins, item, paid, dispensed):
    result = quote(prices, stock, coins, item, paid)
    if result[0] != "READY":
        return [result[0], paid, 0]
    if dispensed != 1:
        return ["JAM", paid, 0]
    stock[item] -= 1
    for i in range(3):
        coins[i] -= result[1][i]
    return ["OK", paid - prices[item], prices[item]]

prices = [7, 5]
stock = [2, 0]
coins = [0, 3, 1]
print(quote(prices, stock, coins, 0, 13))
print(quote(prices, stock, coins, 0, 7))
print(quote(prices, stock, coins, 1, 10))
print(quote(prices, stock, coins, 0, 8))
print(commit(prices, stock, coins, 0, 13, 0))
print(stock, coins)
print(commit(prices, stock, coins, 0, 13, 1))
print(stock, coins)
```

פלט:

```text
['READY', [0, 3, 0]]
['READY', [0, 0, 0]]
['DENIED', []]
['NO CHANGE', []]
['JAM', 13, 0]
[2, 0] [0, 3, 1]
['OK', 6, 7]
[1, 0] [0, 0, 1]
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
JAM
[True, True]
OK
OK
NO CHANGE
OK
[0, 1] [0, 0, 0]
19 20 11
[[0, 'JAM'], [0, 'OK'], [1, 'OK'], [1, 'NO CHANGE'], [0, 'OK']]
[True, True]
```

### ב. פלט התרחיש השני

```text
JAM
[True, True]
OK
NO CHANGE
OK
OK
[0, 1] [0, 3, 0]
19 23 8
[[0, 'JAM'], [0, 'OK'], [1, 'NO CHANGE'], [1, 'OK'], [0, 'OK']]
[True, True]
```

### ג. תשובות והערות לדיון

תכנון אינו משנה מלאי.

JAM מחזיר תשלום ומשאיר מוצר ומטבעות.

cash_ok בודק ערך קופה, sales_ok את התשלום הכולל.

take מניחה הרכב חוקי.

תשלום מדומה אינו מפרט מטבעות.

השוו דוח לפני ואחרי כשל.

### ד. פתרון אפשרי

```python
class CoinBox:
    def __init__(self, coins):
        self.coins = coins

    def value(self):
        return self.coins[0] + self.coins[1] * 2 + self.coins[2] * 5

    def plan(self, due):
        best = []
        best_count = -1
        for a in range(self.coins[0] + 1):
            for b in range(self.coins[1] + 1):
                for c in range(self.coins[2] + 1):
                    if a + b * 2 + c * 5 == due:
                        count = a + b + c
                        if best_count == -1 or count < best_count:
                            best = [a, b, c]
                            best_count = count
        return best

    def take(self, notes):
        for i in range(3):
            self.coins[i] -= notes[i]

class Vending:
    def __init__(self, prices, stock, box):
        self.prices = prices
        self.stock = stock
        self.box = box
        self.revenue = 0
        self.refunds = 0
        self.changes = 0
        self.paid = 0
        self.history = []
        self.initial = box.value()

    def buy(self, item, paid, dispensed):
        status = "DENIED"
        refund = paid
        if item >= 0 and item < len(self.prices) and paid >= 0:
            due = paid - self.prices[item]
            if due >= 0 and self.stock[item] > 0:
                notes = self.box.plan(due)
                if len(notes) == 0:
                    status = "NO CHANGE"
                elif dispensed != 1:
                    status = "JAM"
                else:
                    self.box.take(notes)
                    self.stock[item] -= 1
                    self.revenue += self.prices[item]
                    self.changes += due
                    refund = 0
                    status = "OK"
        if paid >= 0:
            self.paid += paid
            self.refunds += refund
        self.history.append([item, status])
        return status

    def refill(self, coins):
        if len(coins) != 3:
            return False
        for amount in coins:
            if amount < 0:
                return False
        before = self.box.value()
        for i in range(3):
            self.box.coins[i] += coins[i]
        self.initial += self.box.value() - before
        return True

    def restock(self, item, qty):
        if item < 0 or item >= len(self.stock) or qty <= 0:
            return False
        self.stock[item] += qty
        return True

    def audit(self):
        cash_ok = self.initial == self.box.value() + self.changes
        sales_ok = self.paid == self.revenue + self.changes + self.refunds
        return [cash_ok, sales_ok]

box = CoinBox([0, 3, 1])
machine = Vending([7, 5], [2, 2], box)
print(machine.buy(0, 13, 0))
print(machine.audit())
print(machine.buy(0, 13, 1))
print(machine.buy(1, 10, 1))
print(machine.buy(1, 7, 1))
print(machine.buy(0, 7, 1))
print(machine.stock, box.coins)
print(machine.revenue, machine.refunds, machine.changes)
print(machine.history)
print(machine.audit())
print(machine.refill([1, 3, 1]))
print(machine.restock(1, 2))
print(machine.buy(1, 11, 1))
print(machine.stock, box.coins, machine.audit())
```

פלט:

```text
JAM
[True, True]
OK
OK
NO CHANGE
OK
[0, 1] [0, 0, 0]
19 20 11
[[0, 'JAM'], [0, 'OK'], [1, 'OK'], [1, 'NO CHANGE'], [0, 'OK']]
[True, True]
True
True
OK
[0, 2] [0, 3, 0] [True, True]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

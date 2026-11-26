# פתרונות למורה: כספומט: האם אפשר למשוך את הסכום המבוקש?

[חזרה למשימת התלמיד](../33_atm.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
ATM 01 | SIM
Request: 60 NIS
Notes: 3 x 20
Balance: 140 NIS
Result: APPROVED | DONE
```

### ב. פלט התרחיש השני

```text
ATM  | 01 | SIM
Request: 60 NIS
Notes: 3 x 20
Balance: 140 NIS
Result: APPROVED | DONE
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("ATM ", end="")
print("02", end="")
print(" | SIM")
print("Request: ", end="")
print("90", end="")
print(" NIS")
print("Notes: ", end="")
print("0", end="")
print(" available")
print("Balance: ", end="")
print("200", end="")
print(" NIS")
print("Result: ", end="")
print("DENIED", end="")
print(" | WAIT")
```

פלט:

```text
ATM 02 | SIM
Request: 90 NIS
Notes: 0 available
Balance: 200 NIS
Result: DENIED | WAIT
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
440 7 6 60 3
340 7 4 160 5
270 6 3 230 7
230 4 3 270 9
Check: 500
Vault: 230
```

### ב. פלט התרחיש השני

```text
440 7 6 60 3
340 7 4 160 5
270 6 3 230 7
250 5 3 250 8
Check: 500
Vault: 250
```

### ג. תשובות והערות לדיון

cash הוא מצב, withdrawn סכום מצטבר.

ערך השטרות צריך להיות cash.

מספר שטרות אינו סכום.

בדיקת vault ומאזן התחלתי חושפות עדכון חלקי.

### ד. פתרון אפשרי

```python
cash = 360
notes20 = 8
notes50 = 4
withdrawn = 0
used_notes = 0
cash -= 40
notes20 -= 2
withdrawn += 40
used_notes += 2
print(cash, notes20, notes50, withdrawn, used_notes)
cash -= 100
notes50 -= 2
withdrawn += 100
used_notes += 2
print(cash, notes20, notes50, withdrawn, used_notes)
cash -= 70
notes20 -= 1
notes50 -= 1
withdrawn += 70
used_notes += 2
print(cash, notes20, notes50, withdrawn, used_notes)
cash -= 20
notes20 -= 1
withdrawn += 20
used_notes += 1
print(cash, notes20, notes50, withdrawn, used_notes)
print("Check:", cash + withdrawn)
print("Vault:", notes20 * 20 + notes50 * 50)
```

פלט:

```text
320 6 4 40 2
220 6 2 140 4
150 5 1 210 6
130 4 1 230 7
Check: 360
Vault: 130
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
Value: 180 Gap: 0
Notes: 6
Left: 1 2 2 1
Cash: 700 520
```

### ב. פלט התרחיש השני

```text
Value: 180 Gap: 0
Notes: 6
Left: -1 2 2 1
Cash: 660 480
```

### ג. תשובות והערות לדיון

פער חיובי מציין חוסר;

גם פער אפס עלול לחרוג ממלאי.

ערך שלילי מעיד על שימוש בשטרות שאינם זמינים.

הרכב תלוי בערכים ובכמויות.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
60
4
2
3
0
0
1
```

```python
amount = int(input())
stock20 = int(input())
stock50 = int(input())
a20 = int(input())
a50 = int(input())
b20 = int(input())
b50 = int(input())
value_a = a20 * 20 + a50 * 50
value_b = b20 * 20 + b50 * 50
print(value_a, amount - value_a, a20 + a50, stock20 - a20, stock50 - a50)
print(value_b, amount - value_b, b20 + b50, stock20 - b20, stock50 - b50)
```

פלט:

```text
60 0 3 1 2
50 10 1 4 1
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
OK
30 1 0
Value: 70
Vault: 20
PAID 70
```

### ב. פלט התרחיש השני

```text
WRONG SUM
100 2 1
Value: 20
Vault: 90
PAID 0
```

### ג. תשובות והערות לדיון

עדכון צריך להיות אטומי במודל.

WRONG SUM מתייחס להצעה אחת בלבד.

יתרה שווה חוקית.

מלאי חסר אינו אותו דבר כמו סכום שגוי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
70
70
2
1
1
1
```

```python
amount = int(input())
balance = int(input())
stock20 = int(input())
stock50 = int(input())
n20 = int(input())
n50 = int(input())
value = n20 * 20 + n50 * 50
if amount <= 0 or n20 < 0 or n50 < 0:
    status = "INVALID"
elif amount > balance:
    status = "NO FUNDS"
elif n20 > stock20 or n50 > stock50:
    status = "NO NOTES"
elif value != amount:
    status = "WRONG SUM"
else:
    stock20 -= n20
    stock50 -= n50
    balance -= amount
    status = "OK"
print(status)
print(balance, stock20, stock50)
print("Value:", value)
print("Vault:", stock20 * 20 + stock50 * 50)
if status == "OK":
    print("PAID", amount, n20 + n50)
else:
    print("PAID", 0, 0)
```

פלט:

```text
OK
0 1 0
Value: 70
Vault: 20
PAID 70 2
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
MATCH 3 0 3
Best: 3 0 3
Tested: 18
Matches: 1
```

### ב. פלט התרחיש השני

```text
MATCH 0 2 2
MATCH 5 0 5
Best: 0 2 2
Tested: 18
Matches: 2
```

### ג. תשובות והערות לדיון

אפס והמלאי המלא חוקיים.

פתרון ראשון לא בהכרח מינימלי.

50 משאיר 10 שאין דרך להשלים.

tested=(stock20+1)*(stock50+1).

< שומר ראשון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
120
6
2
1
```

```python
amount = int(input())
stock20 = int(input())
stock50 = int(input())
stock100 = int(input())
best = -1
a = 0
b = 0
c = 0
tested = 0
matches = 0
for n20 in range(stock20 + 1):
    for n50 in range(stock50 + 1):
        for n100 in range(stock100 + 1):
            tested += 1
            value = n20 * 20 + n50 * 50 + n100 * 100
            if value == amount:
                matches += 1
                count = n20 + n50 + n100
                if best == -1 or count < best:
                    best = count
                    a = n20
                    b = n50
                    c = n100
if best == -1:
    print("NO SOLUTION")
else:
    print(a, b, c, best)
print(tested, matches)
```

פלט:

```text
1 0 1 2
42 3
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[[4, 0, 1, 0], [4, 2, 0, 0]]
[4, 0, 1, 0] 5
[0, 2, 0, 1]
Remaining cash: 300
```

### ב. פלט התרחיש השני

```text
[[2, 1, 1, 0]]
[2, 1, 1, 0] 4
[2, 1, 0, 1]
Remaining cash: 290
```

### ג. תשובות והערות לדיון

הרכב כולל ארבע כמויות.

רשימות נפרדות שומרות תוצאות קודמות.

עדכון באמצע משבש מרחב חיפוש.

גבולות range מגבילים כל כמות.

מספר האפשרויות הוא מכפלת גדלי התחומים.

### ד. פתרון אפשרי

```python
values = [20, 50, 100, 200]
stock = [4, 2, 1, 1]
amount = 180
best = []
best_count = -1
matches = []
tested = 0
initial = 0
paid = 0
for i in range(4):
    initial += stock[i] * values[i]
for a in range(stock[0] + 1):
    for b in range(stock[1] + 1):
        for c in range(stock[2] + 1):
            for d in range(stock[3] + 1):
                tested += 1
                counts = [a, b, c, d]
                value = 0
                count = 0
                for i in range(4):
                    value += counts[i] * values[i]
                    count += counts[i]
                if value == amount:
                    matches.append(counts)
                    if best_count == -1 or count < best_count:
                        best = counts
                        best_count = count
print(matches)
print(best, best_count)
if len(best) > 0:
    paid = amount
    for i in range(4):
        stock[i] -= best[i]
print(stock)
cash = 0
for i in range(4):
    cash += stock[i] * values[i]
print("Remaining cash:", cash)
print(tested, paid, initial == cash + paid)
```

פלט:

```text
[[4, 0, 1, 0], [4, 2, 0, 0]]
[4, 0, 1, 0] 5
[0, 2, 0, 1]
Remaining cash: 300
60 180 True
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
['OK', [3, 0, 0, 0]]
['OK', [4, 0, 1, 0]]
['NO NOTES', []]
['NO FUNDS', []]
[4, 2, 1, 1]
```

### ב. פלט התרחיש השני

```text
['OK', [3, 0, 0, 0]]
['NO FUNDS', []]
['NO NOTES', []]
['NO FUNDS', []]
[4, 2, 1, 1]
```

### ג. תשובות והערות לדיון

שאילתה בטוחה לפני התחייבות.

בודקים 60,10,מלאי ריק והרכבים שווים.

סכום שווה ליתרה חוקי.

סכום חיובי אינו מיוצג ברשימה ריקה.

יש לשנות מרחב חיפוש או אלגוריתם כללי.

### ד. פתרון אפשרי

```python
def find_notes(stock, amount):
    if amount <= 0:
        return []
    best = []
    best_count = -1
    for a in range(stock[0] + 1):
        for b in range(stock[1] + 1):
            for c in range(stock[2] + 1):
                for d in range(stock[3] + 1):
                    if a * 20 + b * 50 + c * 100 + d * 200 == amount:
                        count = a + b + c + d
                        if best_count == -1 or count < best_count:
                            best = [a, b, c, d]
                            best_count = count
    return best

def quote(stock, balance, amount):
    if amount <= 0:
        return ["INVALID", []]
    if amount > balance:
        return ["NO FUNDS", []]
    notes = find_notes(stock, amount)
    if len(notes) == 0:
        return ["NO NOTES", []]
    return ["OK", notes]

def value_of(notes):
    values = [20, 50, 100, 200]
    total = 0
    for i in range(4):
        total += notes[i] * values[i]
    return total

def commit(stock, balance, amount):
    result = quote(stock, balance, amount)
    if result[0] == "OK":
        for i in range(4):
            stock[i] -= result[1][i]
        balance -= amount
    return [balance, result[0], result[1]]

stock = [4, 2, 1, 1]
initial = value_of(stock)
balance = 200
for amount in [60, 180, 70]:
    result = commit(stock, balance, amount)
    balance = result[0]
    print(result, stock)
print(initial - value_of(stock), 200 - balance)
```

פלט:

```text
[140, 'OK', [3, 0, 0, 0]] [1, 2, 1, 1]
[140, 'NO FUNDS', []] [1, 2, 1, 1]
[70, 'OK', [1, 1, 0, 0]] [0, 1, 1, 1]
130 130
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
OK
NO NOTES
NO NOTES
OK
140 80
60 20
[0, 2, 1, 1]
[[60, 'OK'], [90, 'NO NOTES'], [140, 'NO NOTES'], [20, 'OK']]
True
True
```

### ב. פלט התרחיש השני

```text
OK
OK
NO NOTES
NO FUNDS
140 10
60 90
[1, 1, 1, 1]
[[60, 'OK'], [90, 'OK'], [140, 'NO NOTES'], [20, 'NO FUNDS']]
True
True
```

### ג. תשובות והערות לדיון

Account מנהלת יתרה.

plan שאילתה.

חיוב חשבון, הפחתת שטרות ומונה paid צריכים להתאים.

רשימה משותפת עלולה לערבב מלאים.

בודקים גם סך חיובי החשבונות מול paid.

שומרים צילום מצב לפני/אחרי כשל.

### ד. פתרון אפשרי

```python
class Account:
    def __init__(self, balance):
        self.balance = balance
        self.withdrawn = 0

    def can_pay(self, amount):
        return amount > 0 and amount <= self.balance

    def debit(self, amount):
        if not self.can_pay(amount):
            return False
        self.balance -= amount
        self.withdrawn += amount
        return True

class ATM:
    def __init__(self, stock):
        self.stock = stock
        self.history = []
        self.paid = 0
        self.initial = self.cash()

    def cash(self):
        values = [20, 50, 100, 200]
        total = 0
        for i in range(4):
            total += self.stock[i] * values[i]
        return total

    def plan(self, amount):
        best = []
        best_count = -1
        for a in range(self.stock[0] + 1):
            for b in range(self.stock[1] + 1):
                for c in range(self.stock[2] + 1):
                    for d in range(self.stock[3] + 1):
                        value = a * 20 + b * 50 + c * 100 + d * 200
                        count = a + b + c + d
                        if value == amount:
                            if best_count == -1 or count < best_count:
                                best = [a, b, c, d]
                                best_count = count
        return best

    def withdraw(self, account, amount):
        if not account.can_pay(amount):
            status = "NO FUNDS"
        else:
            notes = self.plan(amount)
            if len(notes) == 0:
                status = "NO NOTES"
            else:
                account.debit(amount)
                for i in range(4):
                    self.stock[i] -= notes[i]
                self.paid += amount
                status = "OK"
        self.history.append([amount, status])
        return status

    def deposit_notes(self, notes):
        if len(notes) != 4:
            return False
        for amount in notes:
            if amount < 0:
                return False
        before = self.cash()
        for i in range(4):
            self.stock[i] += notes[i]
        self.initial += self.cash() - before
        return True

    def audit(self):
        return self.initial == self.cash() + self.paid

a = Account(200)
b = Account(100)
machine = ATM([4, 2, 1, 1])
print(machine.withdraw(a, 60))
print(machine.withdraw(b, 90))
print(machine.withdraw(a, 140))
print(machine.withdraw(b, 20))
print(a.balance, b.balance)
print(a.withdrawn, b.withdrawn)
print(machine.stock)
print(machine.history)
print(machine.audit())
print(machine.paid == a.withdrawn + b.withdrawn)
print(machine.deposit_notes([5, 2, 1, 0]))
print(machine.withdraw(a, 100))
print(machine.stock, machine.audit())
print(machine.paid == a.withdrawn + b.withdrawn)
```

פלט:

```text
OK
NO NOTES
NO NOTES
OK
140 80
60 20
[0, 2, 1, 1]
[[60, 'OK'], [90, 'NO NOTES'], [140, 'NO NOTES'], [20, 'OK']]
True
True
True
OK
[5, 4, 1, 1] True
True
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

# פתרונות למורה: ניהול דלק במטוס: איך בוחרים משימה בתוך תקציב מדומה?

[חזרה למשימת התלמיד](../18_aircraft_fuel_budget.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
MISSION 04 | A
Budget: 90 points
Return: 20 | Reserve: 10
Score: 65 | READY
```

### ב. פלט התרחיש השני

```text
MISSION  | 04 | A
Budget: 90 points
Return: 20 | Reserve: 10
Score: 65 | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("MISSION ", end="")
print("07", end="")
print(" | B")
print("Budget: ", end="")
print("70", end="")
print(" points")
print("Return: ", end="")
print("30", end="")
print(" | Reserve: 10")
print("Score: ", end="")
print("42", end="")
print(" | CHECK")
```

פלט:

```text
MISSION 07 | B
Budget: 70 points
Return: 30 | Reserve: 10
Score: 42 | CHECK
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
78 12 48 15
60 30 30 39
51 39 14 49
Check: 90
```

### ב. פלט התרחיש השני

```text
78 12 48 15
60 30 30 39
51 39 7 49
Check: 90
```

### ג. תשובות והערות לדיון

available היא יתרה אחרי התחייבויות.

budget+spent נשאר 90.

שינוי עלות חזרה מקטין מרווח אך אינו צריכה שבוצעה.

ניקוד מייצג ערך במשחק, לא צריכת משאב.

### ד. פתרון אפשרי

```python
budget = 110
return_cost = 25
reserve = 12
score = 0
budget -= 14
score += 16
print(budget, budget - return_cost - reserve, score)
budget -= 19
score += 30
return_cost += 4
print(budget, budget - return_cost - reserve, score)
budget -= 11
score += 12
print(budget, budget - return_cost - reserve, score)
print("Spent:", 110 - budget)
```

פלט:

```text
96 59 16
77 36 46
66 25 58
Spent: 44
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 70 20 65
B: 75 15 70
Cost gap: -5
Score gap: -5
Margin gap: 5
```

### ב. פלט התרחיש השני

```text
A: 70 0 65
B: 75 -5 70
Cost gap: -5
Score gap: -5
Margin gap: 5
```

### ג. תשובות והערות לדיון

צריך לכסות גם חזרה ורזרבה.

מרווח שלילי הוא חריגה.

שני ההפרשים בעלי סימנים הפוכים כאשר התקציב זהה.

ניקוד אינו עוקף תנאי סף.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
100
12
25
50
80
40
60
63
95
```

```python
budget = int(input())
reserve = int(input())
return_cost = int(input())
a = int(input())
score_a = int(input())
b = int(input())
score_b = int(input())
c = int(input())
score_c = int(input())
required_a = a + return_cost + reserve
required_b = b + return_cost + reserve
required_c = c + return_cost + reserve
margin_a = budget - required_a
margin_b = budget - required_b
margin_c = budget - required_c
print(required_a, margin_a, score_a)
print(required_b, margin_b, score_b)
print(required_c, margin_c, score_c)
print(margin_a - margin_c)
```

פלט:

```text
87 13 80
77 23 60
100 0 95
13
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
5 13
B 70 13
```

### ב. פלט התרחיש השני

```text
0 8
A 80 0
```

### ג. תשובות והערות לדיון

B בעלת מרווח גדול יותר בתרחיש הראשון.

מרווח אפס חוקי.

> שומר את הראשונה בשוויון מלא.

למשל 66 פוסל גם B שסך התחייבויותיה 67.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
67
10
42
23
80
35
22
70
```

```python
budget = int(input())
reserve = int(input())
cost_a = int(input())
return_a = int(input())
score_a = int(input())
cost_b = int(input())
return_b = int(input())
score_b = int(input())
margin_a = budget - cost_a - return_a - reserve
margin_b = budget - cost_b - return_b - reserve
best = "NONE"
best_score = -1
best_margin = -1
if margin_a >= 0:
    best = "A"
    best_score = score_a
    best_margin = margin_a
if margin_b >= 0:
    if best == "NONE" or score_b > best_score or (score_b == best_score and margin_b > best_margin):
        best = "B"
        best_score = score_b
        best_margin = margin_b
if best == "NONE":
    print(best)
else:
    print(best, best_score, best_margin)
```

פלט:

```text
B 70 0
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 5 60
2 20 55
3 DENIED
4 INVALID
5 20 60
Eligible: 3
Invalid: 1
5 60 20
```

### ב. פלט התרחיש השני

```text
1 5 60
2 20 55
3 DENIED
4 INVALID
5 20 70
Eligible: 3
Invalid: 1
5 70 20
```

### ג. תשובות והערות לדיון

מזהי חלופות מתחילים ב-1.

ענף חוקי מקיים מגבלות.

eligible מספר אפשרויות ולא מספר ביצועים, כי בוחרים חלופה אחת.

השוואות קשיחות בשוויון מלא אינן מעדכנות.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
5
80
10
40
25
60
30
20
55
45
30
90
-1
20
50
35
15
60
```

```python
count = int(input())
budget = int(input())
reserve = int(input())
best_id = 0
best_score = -1
best_margin = -1
invalid = 0
denied = 0
eligible = 0
for i in range(count):
    cost = int(input())
    back = int(input())
    score = int(input())
    margin = budget - cost - back - reserve
    if cost <= 0 or back < 0 or score < 0:
        invalid += 1
    elif margin < 0:
        denied += 1
    else:
        eligible += 1
        if best_id == 0 or score > best_score or (score == best_score and margin > best_margin):
            best_id = i + 1
            best_score = score
            best_margin = margin
print(best_id, best_score, best_margin)
print(invalid, denied, eligible)
print("Check:", invalid + denied + eligible)
```

פלט:

```text
5 60 20
1 1 3
Check: 5
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
50 [3] [-25, -17, -30, 5, -15, -15]
Choice: 3 5
67 [1, 3, 4, 5] [-8, 0, -13, 22, 2, 2]
Choice: 1 0
75 [0, 1, 3, 4, 5] [0, 8, -5, 30, 10, 10]
Choice: 1 8
85 [0, 1, 2, 3, 4, 5] [10, 18, 5, 40, 20, 20]
Choice: 2 5
[3, 1, 1, 2]
```

### ב. פלט התרחיש השני

```text
44 [] [-31, -23, -36, -1, -21, -21]
Choice: -1 -1
66 [3, 4, 5] [-9, -1, -14, 21, 1, 1]
Choice: 4 1
74 [1, 3, 4, 5] [-1, 7, -6, 29, 9, 9]
Choice: 1 7
79 [0, 1, 3, 4, 5] [4, 12, -1, 34, 14, 14]
Choice: 1 12
[-1, 4, 1, 1]
```

### ג. תשובות והערות לדיון

בחירה תלויה בתקציב.

חלופה שנדחתה עשויה להתאים בהמשך.

בשוויון מלא נשארת הראשונה.

כאשר התקציב גדל קבוצת האפשרויות רק מתרחבת, לכן ניקוד מיטבי לא יקטן.

### ד. פתרון אפשרי

```python
costs = [42, 35, 50, 20, 30, 32]
returns = [23, 22, 20, 15, 25, 23]
scores = [70, 70, 90, 35, 60, 60]
reserves = [5, 10, 20]
choices = []
chosen_scores = []
budget = 75
for reserve in reserves:
    best = -1
    best_score = -1
    best_margin = -1
    for i in range(len(costs)):
        margin = budget - costs[i] - returns[i] - reserve
        if margin >= 0:
            if best == -1 or scores[i] > best_score or (scores[i] == best_score and margin > best_margin):
                best = i
                best_score = scores[i]
                best_margin = margin
    choices.append(best)
    chosen_scores.append(best_score)
print(choices)
print(chosen_scores)
```

פלט:

```text
[2, 1, 4]
[90, 70, 60]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
['OK', 0]
['DENIED', -1]
[1, 70, 8]
[2, 90, 0]
```

### ב. פלט התרחיש השני

```text
['DENIED', 0]
['DENIED', -1]
[1, 70, 8]
[1, 70, 13]
```

### ג. תשובות והערות לדיון

מרווח 0 חוקי, לכן 67 חושף את הטעות.

assess אינה מכירה רשימת מועמדים.

רשימות ריקות מחזירות [-1,-1,-1].

כדאי להחזיר סטטוס נפרד כדי להבחין בין ERROR ל-NONE.

### ד. פתרון אפשרי

```python
def assess(budget, reserve, cost, back, score):
    if cost <= 0 or back < 0 or score < 0:
        return ["INVALID", -1]
    margin = budget - reserve - cost - back
    if margin < 0:
        return ["DENIED", margin]
    return ["OK", margin]

def select(costs, returns, scores, budget, reserve, mode):
    if len(costs) != len(returns) or len(costs) != len(scores) or (mode != 1 and mode != 2):
        return ["ERROR", -1, -1, -1]
    best = -1
    best_score = -1
    best_margin = -1
    for i in range(len(costs)):
        result = assess(budget, reserve, costs[i], returns[i], scores[i])
        if result[0] == "OK":
            margin = result[1]
            better = best == -1
            if mode == 1:
                if scores[i] > best_score or (scores[i] == best_score and margin > best_margin):
                    better = True
            else:
                if margin > best_margin or (margin == best_margin and scores[i] > best_score):
                    better = True
            if better:
                best = i
                best_score = scores[i]
                best_margin = margin
    if best == -1:
        return ["NONE", -1, -1, -1]
    return ["OK", best, best_score, best_margin]

print(select([42, 20], [23, 15], [90, 35], 80, 10, 1))
print(select([42, 20], [23, 15], [90, 35], 80, 10, 2))
print(select([42, 20], [23, 15], [90, 35], 30, 10, 1))
```

פלט:

```text
['OK', 0, 90, 5]
['OK', 1, 35, 35]
['NONE', -1, -1, -1]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[1, 70, 8]
[2, 90, 0]
[2, 90, 0]
[1, 2] [2]
80 80
```

### ב. פלט התרחיש השני

```text
[-1, -1, -1]
[2, 90, 0]
[1, 70, 3]
[-1, 1] [2]
70 80
```

### ג. תשובות והערות לדיון

margin היא חישוב בלבד.

Plan מכילה מאפייני חלופה, Planner מדיניות ותקציב.

כל מופע שומר ערכים משלו.

בחירה היא תכנון ולא ביצוע, ולכן אינה צורכת תקציב.

### ד. פתרון אפשרי

```python
class Plan:
    def __init__(self, cost, back, score):
        self.cost = cost
        self.back = back
        self.score = score

    def margin(self, budget, reserve):
        return budget - self.cost - self.back - reserve

class Planner:
    def __init__(self, budget, reserve):
        self.budget = budget
        self.reserve = reserve
        self.selected = -1
        self.history = []
        self.changes = 0

    def choose(self, plans):
        best = -1
        best_score = -1
        best_margin = -1
        for i in range(len(plans)):
            margin = plans[i].margin(self.budget, self.reserve)
            score = plans[i].score
            if margin >= 0:
                if best == -1 or score > best_score or (score == best_score and margin > best_margin):
                    best = i
                    best_score = score
                    best_margin = margin
        if len(self.history) > 0 and self.selected != best:
            self.changes += 1
        self.selected = best
        self.history.append(best)
        return [best, best_score, best_margin]

    def set_reserve(self, amount):
        if amount >= 0:
            self.reserve = amount

plans = [Plan(42, 23, 70), Plan(35, 22, 70), Plan(50, 20, 90)]
a = Planner(75, 10)
b = Planner(80, 10)
print(a.choose(plans))
print(b.choose(plans))
a.budget += 5
print(a.choose(plans))
print(a.history, b.history)
b.set_reserve(20)
print(b.choose(plans))
print(a.history, a.changes)
print(b.history, b.changes)
```

פלט:

```text
[1, 70, 8]
[2, 90, 0]
[2, 90, 0]
[1, 2] [2]
[1, 70, 3]
[1, 2] 1
[2, 1] 1
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

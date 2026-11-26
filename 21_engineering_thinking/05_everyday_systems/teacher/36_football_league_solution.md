# פתרונות למורה: משחק כדורגל: כיצד בונים טבלת ליגה מתוצאות משחקים?

[חזרה למשימת התלמיד](../36_football_league.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
LEAGUE 01 | DEMO
Home: A | 2
Away: B | 1
Points: 3 / 0
State: FINAL | OK
```

### ב. פלט התרחיש השני

```text
LEAGUE  | 01 | DEMO
Home: A | 2
Away: B | 1
Points: 3 / 0
State: FINAL | OK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("LEAGUE ", end="")
print("02", end="")
print(" | DEMO")
print("Home: ", end="")
print("C", end="")
print(" | 1")
print("Away: ", end="")
print("D", end="")
print(" | 1")
print("Points: ", end="")
print("1", end="")
print(" / 1")
print("State: ", end="")
print("FINAL", end="")
print(" | DRAW")
```

פלט:

```text
LEAGUE 02 | DEMO
Home: C | 1
Away: D | 1
Points: 1 / 1
State: FINAL | DRAW
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 3 3 1 2
2 4 5 3 2
3 4 5 5 0
4 7 6 5 1
Losses: 1
Check: 7
```

### ב. פלט התרחיש השני

```text
1 3 4 1 3
2 4 6 3 3
3 4 6 5 1
4 7 7 5 2
Losses: 1
Check: 7
```

### ג. תשובות והערות לדיון

נקודות נגזרות מתוצאות.

הפסדים הם played פחות ניצחונות ותיקו.

הפרש שלילי מציין שספגו יותר משהבקיעו.

שערי חובה משמשים דירוג ומאזן.

### ד. פתרון אפשרי

```python
points = 0
played = 0
goals_for = 0
goals_against = 0
wins = 0
draws = 0
gf = 1
ga = 1
goals_for += gf
goals_against += ga
points += 1
draws += 1
played += 1
print(played, points, goals_for, goals_against, goals_for - goals_against)
gf = 4
ga = 2
goals_for += gf
goals_against += ga
points += 3
wins += 1
played += 1
print(played, points, goals_for, goals_against, goals_for - goals_against)
gf = 0
ga = 1
goals_for += gf
goals_against += ga
played += 1
print(played, points, goals_for, goals_against, goals_for - goals_against)
gf = 3
ga = 0
goals_for += gf
goals_against += ga
points += 3
wins += 1
played += 1
print(played, points, goals_for, goals_against, goals_for - goals_against)
print("Losses:", played - wins - draws)
print("Check:", wins * 3 + draws)
```

פלט:

```text
1 1 1 1 0
2 4 5 3 2
3 4 5 4 1
4 7 8 4 4
Losses: 1
Check: 7
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
A: 4 7 3 8
B: 4 7 3 7
Gaps: 0 0 1
```

### ב. פלט התרחיש השני

```text
A: 4 7 3 8
B: 4 7 5 9
Gaps: 0 -2 -1
```

### ג. תשובות והערות לדיון

נדרשים שוברי שוויון.

אחרי הפרש משווים שערי זכות.

סכומים אינם היסטוריה.

שערי זכות חשובים בשוויון נוסף.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
2
1
8
5
2
1
7
4
1
4
6
6
```

```python
wa = int(input())
da = int(input())
fa = int(input())
aa = int(input())
wb = int(input())
db = int(input())
fb = int(input())
ab = int(input())
wc = int(input())
dc = int(input())
fc = int(input())
ac = int(input())
pa = wa * 3 + da
pb = wb * 3 + db
pc = wc * 3 + dc
print(pa, fa - aa, fa)
print(pb, fb - ab, fb)
print(pc, fc - ac, fc)
print(pa - pc, fa - aa - fc + ac)
```

פלט:

```text
7 3 8
7 3 7
7 0 6
0 3
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
7 3 6
7 3 7
First: B
```

### ב. פלט התרחיש השני

```text
9 4 7
6 2 7
First: A
```

### ג. תשובות והערות לדיון

שער זכות לאחת הוא חובה לאחרת.

נקודות הן קריטריון ראשון.

בשוויון מלא A נשארת ראשונה.

קלט פסול נדחה.

בתרחיש המקורי B מובילה בשערי זכות.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
6
6
5
2
6
3
2
1
```

```python
pa = int(input())
pb = int(input())
fa = int(input())
aa = int(input())
fb = int(input())
ab = int(input())
home = int(input())
away = int(input())
initial = pa + pb
if home < 0 or away < 0:
    print("INVALID")
else:
    fa += home
    aa += away
    fb += away
    ab += home
    if home > away:
        pa += 3
    elif away > home:
        pb += 3
    else:
        pa += 1
        pb += 1
da = fa - aa
db = fb - ab
first = "A"
if pb > pa:
    first = "B"
elif pb == pa:
    if db > da or (db == da and fb > fa):
        first = "B"
print(pa, da, fa)
print(pb, db, fb)
print("First:", first)
print("Points added:", pa + pb - initial)
```

פלט:

```text
9 4 7
6 2 7
First: A
Points added: 3
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 A 3 0 1
2 DRAW 4 1 1
3 A 7 1 4
4 B 7 4 3
5 DRAW 8 5 3
6 INVALID 8 5 3
7 A 11 5 4
8 B 11 8 1
3 2 2 1
Points check: True
Games check: 8
```

### ב. פלט התרחיש השני

```text
1 A 3 0 1
2 B 3 3 0
3 A 6 3 3
4 B 6 6 2
5 DRAW 7 7 2
6 INVALID 7 7 2
7 A 10 7 3
8 B 10 10 0
3 3 1 1
Points check: True
Games check: 8
```

### ג. תשובות והערות לדיון

תיקו מוסיף שתי נקודות ולא שלוש.

סכום תוצאות ו-invalid מכסה קלטים.

הפרש שערים ונקודות מודדים דברים שונים.

פסול אינו משחק.

משווים נקודות אחרי כל המשחקים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
8
2
1
0
0
3
0
1
2
2
2
-1
0
1
0
0
3
```

```python
count = int(input())
streak = 0
longest = 0
points_a = 0
points_b = 0
goals_a = 0
goals_b = 0
wins_a = 0
wins_b = 0
draws = 0
invalid = 0
for i in range(count):
    a = int(input())
    b = int(input())
    if a < 0 or b < 0:
        invalid += 1
        status = "INVALID"
    else:
        goals_a += a
        goals_b += b
        if a > b:
            points_a += 3
            wins_a += 1
            streak += 1
            if streak > longest:
                longest = streak
            status = "A"
        elif b > a:
            points_b += 3
            wins_b += 1
            streak = 0
            status = "B"
        else:
            points_a += 1
            points_b += 1
            draws += 1
            streak = 0
            status = "DRAW"
    print(i + 1, status, points_a, points_b, goals_a - goals_b)
print(wins_a, wins_b, draws, invalid)
print("Points check:", points_a + points_b == (wins_a + wins_b) * 3 + draws * 2)
print("Games check:", wins_a + wins_b + draws + invalid)
print(longest)
```

פלט:

```text
1 A 3 0 1
2 DRAW 4 1 1
3 A 7 1 4
4 B 7 4 3
5 DRAW 8 5 3
6 INVALID 8 5 3
7 A 11 5 4
8 B 11 8 1
3 2 2 1
Points check: True
Games check: 8
1
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[3, 0, 0, 0] [2, 1, 0, 0] [1, 2, 0, 0]
[3, 0, 1, 1] [2, 1, 1, 1] [1, 2, 1, 1]
[3, 0, 4, 1] [2, 1, 3, 1] [3, 2, 1, 1]
[3, 3, 4, 1] [2, 4, 3, 1] [3, 2, 1, 4]
[4, 3, 4, 2] [3, 4, 3, 2] [4, 2, 1, 5]
[4, 4, 5, 2] [3, 6, 5, 2] [4, 4, 3, 5]
[2, 1, 0, 3]
[4, 4, 5, 2] [3, 6, 5, 2] [4, 4, 3, 5]
```

### ב. פלט התרחיש השני

```text
[3, 0, 0, 0] [2, 1, 0, 0] [1, 2, 0, 0]
[3, 0, 1, 1] [2, 1, 1, 1] [1, 2, 1, 1]
[3, 0, 4, 1] [2, 1, 3, 1] [3, 2, 1, 1]
[3, 0, 4, 4] [2, 1, 3, 4] [3, 5, 1, 1]
[4, 0, 4, 5] [3, 1, 3, 5] [4, 5, 1, 2]
[4, 1, 5, 5] [3, 3, 5, 5] [4, 7, 3, 2]
[3, 2, 0, 1]
[4, 1, 5, 5] [3, 3, 5, 5] [4, 7, 3, 2]
```

### ג. תשובות והערות לדיון

אינדקס מקשר את כל השדות.

משחק עצמי פסול, כאן הנתונים מובטחים חוקיים.

ranking היא רשימה נפרדת.

תנאי membership מונע כפילות.

סך gf שווה סך ga.

### ד. פתרון אפשרי

```python
matches = [[0, 1, 2, 1], [2, 3, 1, 1], [0, 2, 0, 2], [1, 3, 3, 0], [3, 0, 1, 1], [1, 2, 2, 2], [0, 0, 1, 2]]
points = [0, 0, 0, 0]
gf = [0, 0, 0, 0]
ga = [0, 0, 0, 0]
for row in matches:
    a = row[0]
    b = row[1]
    x = row[2]
    y = row[3]
    if a >= 0 and a < len(points) and b >= 0 and b < len(points) and a != b and x >= 0 and y >= 0:
        gf[a] += x
        ga[a] += y
        gf[b] += y
        ga[b] += x
        if x > y:
            points[a] += 3
        elif y > x:
            points[b] += 3
        else:
            points[a] += 1
            points[b] += 1
    else:
        print("INVALID")
    print(points, gf, ga)
ranking = []
for turn in range(len(points)):
    best = -1
    for i in range(len(points)):
        if i not in ranking:
            if best == -1:
                best = i
            elif points[i] > points[best]:
                best = i
            elif points[i] == points[best]:
                diff = gf[i] - ga[i]
                old = gf[best] - ga[best]
                if diff > old or (diff == old and gf[i] > gf[best]):
                    best = i
    ranking.append(best)
total_for = 0
total_against = 0
for i in range(len(points)):
    total_for += gf[i]
    total_against += ga[i]
print(total_for == total_against)
print(ranking)
print(points, gf, ga)
```

פלט:

```text
[3, 0, 0, 0] [2, 1, 0, 0] [1, 2, 0, 0]
[3, 0, 1, 1] [2, 1, 1, 1] [1, 2, 1, 1]
[3, 0, 4, 1] [2, 1, 3, 1] [3, 2, 1, 1]
[3, 3, 4, 1] [2, 4, 3, 1] [3, 2, 1, 4]
[4, 3, 4, 2] [3, 4, 3, 2] [4, 2, 1, 5]
[4, 4, 5, 2] [3, 6, 5, 2] [4, 4, 3, 5]
INVALID
[4, 4, 5, 2] [3, 6, 5, 2] [4, 4, 3, 5]
True
[2, 1, 0, 3]
[4, 4, 5, 2] [3, 6, 5, 2] [4, 4, 3, 5]
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
True
True
False
[0, 2, 1, 3]
[3, 0, 3, 0] [2, 1, 2, 1] [1, 2, 1, 2]
```

### ב. פלט התרחיש השני

```text
True
True
False
[2, 0, 3, 1]
[3, 0, 3, 0] [2, 1, 2, 1] [1, 2, 1, 2]
```

### ג. תשובות והערות לדיון

אינדקס מקשר שדות.

>= מעדיף מאוחר בשוויון.

rank יוצרת רשימה בלבד.

בדקו משחק חוקי, עצמי ושלילי וצלמו מצב.

רשימה ריקה תחזיר דירוג ריק.

### ד. פתרון אפשרי

```python
def play(points, gf, ga, a, b, x, y):
    if a < 0 or a >= len(points) or b < 0 or b >= len(points) or a == b or x < 0 or y < 0:
        return False
    gf[a] += x
    ga[a] += y
    gf[b] += y
    ga[b] += x
    if x > y:
        points[a] += 3
    elif y > x:
        points[b] += 3
    else:
        points[a] += 1
        points[b] += 1
    return True

def better(points, gf, ga, i, best):
    if best == -1:
        return True
    if points[i] != points[best]:
        return points[i] > points[best]
    di = gf[i] - ga[i]
    db = gf[best] - ga[best]
    if di != db:
        return di > db
    return gf[i] > gf[best]

def rank(points, gf, ga):
    result = []
    for turn in range(len(points)):
        best = -1
        for i in range(len(points)):
            if i not in result and better(points, gf, ga, i, best):
                best = i
        result.append(best)
    return result

def audit(points, gf, ga):
    if len(points) != len(gf) or len(gf) != len(ga):
        return False
    total_for = 0
    total_against = 0
    for i in range(len(points)):
        total_for += gf[i]
        total_against += ga[i]
    return total_for == total_against

points = [0, 0, 0, 0]
gf = [0, 0, 0, 0]
ga = [0, 0, 0, 0]
print(play(points, gf, ga, 0, 1, 2, 1))
print(play(points, gf, ga, 2, 3, 2, 1))
print(play(points, gf, ga, 0, 0, 3, 0))
print(rank(points, gf, ga))
print(points, gf, ga)
print(audit(points, gf, ga))
print(audit(points, gf, [0, 0, 0, 0]))
```

פלט:

```text
True
True
False
[0, 2, 1, 3]
[3, 0, 3, 0] [2, 1, 2, 1] [1, 2, 1, 2]
True
False
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
OK
OK
DUPLICATE
INVALID
OK
[1, 0, 2, 3]
[['B', 3, 1, 4, 2], ['A', 3, 1, 2, 1], ['C', 3, 1, 2, 1], ['D', 0, -3, 2, 2]]
[[1, 'OK'], [2, 'OK'], [1, 'DUPLICATE'], [3, 'INVALID'], [4, 'OK']]
```

### ב. פלט התרחיש השני

```text
OK
OK
DUPLICATE
INVALID
OK
[2, 1, 0, 3]
[['C', 3, 2, 3, 1], ['B', 3, 1, 4, 2], ['A', 3, 1, 2, 1], ['D', 0, -4, 2, 2]]
[[1, 'OK'], [2, 'OK'], [1, 'DUPLICATE'], [3, 'INVALID'], [4, 'OK']]
```

### ג. תשובות והערות לדיון

League מתאמת שני צדדים.

completed הצלחות בלבד, history כל ניסיונות.

עדכון צד אחד מפר מאזן.

reports שאילתה.

השוואה קשיחה משאירה ראשון.

סוכמים played ומשווים ל-2*len(completed).

### ד. פתרון אפשרי

```python
class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.gf = 0
        self.ga = 0
        self.played = 0

    def record(self, gf, ga):
        self.gf += gf
        self.ga += ga
        self.played += 1
        if gf > ga:
            self.points += 3
        elif gf == ga:
            self.points += 1

    def report(self):
        return [self.name, self.points, self.gf - self.ga, self.gf, self.played]

class League:
    def __init__(self, teams):
        self.teams = teams
        self.completed = []
        self.history = []

    def match(self, order, a, b, x, y):
        if order in self.completed:
            status = "DUPLICATE"
        elif order <= 0 or a < 0 or a >= len(self.teams) or b < 0 or b >= len(self.teams) or a == b or x < 0 or y < 0:
            status = "INVALID"
        else:
            self.teams[a].record(x, y)
            self.teams[b].record(y, x)
            self.completed.append(order)
            status = "OK"
        self.history.append([order, status])
        return status

    def better(self, i, best):
        if best == -1:
            return True
        a = self.teams[i]
        b = self.teams[best]
        if a.points != b.points:
            return a.points > b.points
        da = a.gf - a.ga
        db = b.gf - b.ga
        if da != db:
            return da > db
        return a.gf > b.gf

    def rank(self):
        result = []
        for turn in range(len(self.teams)):
            best = -1
            for i in range(len(self.teams)):
                if i not in result and self.better(i, best):
                    best = i
            result.append(best)
        return result

    def audit(self):
        gf = 0
        ga = 0
        played = 0
        for team in self.teams:
            gf += team.gf
            ga += team.ga
            played += team.played
        return [gf == ga, played == 2 * len(self.completed)]

    def reports(self):
        result = []
        for i in self.rank():
            result.append(self.teams[i].report())
        return result

league = League([Team("A"), Team("B"), Team("C"), Team("D")])
print(league.match(1, 0, 1, 2, 1))
print(league.match(2, 2, 3, 2, 1))
print(league.match(1, 1, 2, 4, 0))
print(league.match(3, 0, 0, 1, 1))
print(league.match(4, 1, 3, 3, 1))
print(league.rank())
print(league.reports())
print(league.history)
print(league.audit())
print(league.match(5, 0, 2, 1, 1))
print(league.audit())
print(league.match(5, 0, 2, 4, 0))
print(league.audit())
```

פלט:

```text
OK
OK
DUPLICATE
INVALID
OK
[1, 0, 2, 3]
[['B', 3, 1, 4, 2], ['A', 3, 1, 2, 1], ['C', 3, 1, 2, 1], ['D', 0, -3, 2, 2]]
[[1, 'OK'], [2, 'OK'], [1, 'DUPLICATE'], [3, 'INVALID'], [4, 'OK']]
[True, True]
OK
[True, True]
DUPLICATE
[True, True]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

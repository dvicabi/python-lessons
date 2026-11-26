# פתרונות למורה: משחק מחשב: איך מנהלים חיים, אנרגיה ועליית רמות?

[חזרה למשימת התלמיד](../39_computer_game.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
PLAYER A | DEMO
Health: 70 / 100
Energy: 12 / 20
XP: 17 | Level: 2
State: ACTIVE | READY
```

### ב. פלט התרחיש השני

```text
PLAYER  | A | DEMO
Health: 70 / 100
Energy: 12 / 20
XP: 17 | Level: 2
State: ACTIVE | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("PLAYER ", end="")
print("B", end="")
print(" | DEMO")
print("Health: ", end="")
print("0", end="")
print(" / 100")
print("Energy: ", end="")
print("8", end="")
print(" / 20")
print("XP: ", end="")
print("30", end="")
print(" | Level: 4")
print("State: ", end="")
print("FINISHED", end="")
print(" | END")
```

פלט:

```text
PLAYER B | DEMO
Health: 0 / 100
Energy: 8 / 20
XP: 30 | Level: 4
State: FINISHED | END
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
70 8 15 2
70 13 15 2
40 13 15 2
60 10 15 2
60 6 22 3
Training: 2
Check: 22
```

### ב. פלט התרחיש השני

```text
70 8 16 2
70 13 16 2
40 13 16 2
60 10 16 2
60 6 23 3
Training: 2
Check: 23
```

### ג. תשובות והערות לדיון

רמה נקבעת לפי עשרות XP.

אימון עשוי לא לחצות גבול רמה.

trained ו-xp לא משתנים במנוחה.

חישוב מוקדם ייתן רמה ישנה.

### ד. פתרון אפשרי

```python
health = 80
energy = 15
xp = 0
level = 1
trained = 0
energy -= 4
xp += 7
trained += 1
level = 1 + xp // 10
print(health, energy, xp, level)
energy -= 4
xp += 7
trained += 1
level = 1 + xp // 10
print(health, energy, xp, level)
health -= 30
level = 1 + xp // 10
print(health, energy, xp, level)
energy -= 3
health += 20
level = 1 + xp // 10
print(health, energy, xp, level)
energy += 5
level = 1 + xp // 10
print(health, energy, xp, level)
print("Training:", trained)
print("Check:", trained * 7)
```

פלט:

```text
80 11 7 1
80 7 14 2
50 7 14 2
70 4 14 2
70 9 14 2
Training: 2
Check: 14
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
Health: 60
Energy: 6
XP and level: 22 3
Energy parts: 11 5
```

### ב. פלט התרחיש השני

```text
Health: 60
Energy: -6
XP and level: 29 3
Energy parts: 15 5
```

### ג. תשובות והערות לדיון

סדר פעולות יכול לגרום לחוסר מוקדם.

מנוחה מוגבלת לתקרה ולכן ייתכן בזבוז.

חיים שליליים אסורים.

XP גדל רק מאימון שהצליח.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
40
12
5
1
1
1
2
1
0
```

```python
health = int(input())
energy = int(input())
xp = int(input())
t1 = int(input())
r1 = int(input())
h1 = int(input())
t2 = int(input())
r2 = int(input())
h2 = int(input())
energy -= t1 * 4 + h1 * 3
energy += r1 * 5
health += h1 * 20
xp += t1 * 7
level = 1 + xp // 10
print(health, energy, xp, level)
energy -= t2 * 4 + h2 * 3
energy += r2 * 5
health += h2 * 20
xp += t2 * 7
level = 1 + xp // 10
print(health, energy, xp, level)
print(t1 * 4 + h1 * 3 + t2 * 4 + h2 * 3)
```

פלט:

```text
60 10 12 2
60 7 26 3
15
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
HEALED 100 0 8 1
```

### ב. פלט התרחיש השני

```text
LOW 90 2 8 1
```

### ג. תשובות והערות לדיון

קדימות חוקיות מוגדרת במפרט.

שוויון מספיק.

חיים לא עוברים 100.

חיים, אנרגיה ו-XP נשמרים בדחייה.

אפשר לחשב רמה כדי למנוע אי התאמה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
90
3
8
4
```

```python
health = int(input())
energy = int(input())
xp = int(input())
action = int(input())
old_health = health
old_energy = energy
old_xp = xp
if action < 1 or action > 4:
    status = "INVALID"
elif health == 0:
    status = "FINISHED"
elif action == 1:
    if energy < 4:
        status = "LOW"
    else:
        energy -= 4
        xp += 7
        status = "TRAINED"
elif action == 2:
    energy += 5
    if energy > 20:
        energy = 20
    status = "RESTED"
elif action == 3:
    health -= 30
    if health < 0:
        health = 0
    status = "OBSTACLE"
elif energy < 3:
    status = "LOW"
else:
    energy -= 3
    health += 20
    if health > 100:
        health = 100
    status = "HEALED"
level = 1 + xp // 10
print(status, health, energy, xp, level)
print(health - old_health, energy - old_energy, xp - old_xp)
```

פלט:

```text
HEALED 100 0 8 1
10 -3 0
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
1 OK 60 6 7 1
2 OK 60 2 14 2
3 LOW 60 2 14 2
4 OK 60 7 14 2
5 OK 80 4 14 2
6 OK 50 4 14 2
7 OK 20 4 14 2
8 OK 20 9 14 2
9 OK 0 9 14 2
10 FINISHED 0 9 14 2
8 2 1
Check: 10
```

### ב. פלט התרחיש השני

```text
1 OK 60 6 7 1
2 OK 60 11 7 1
3 OK 60 7 14 2
4 OK 60 12 14 2
5 OK 80 9 14 2
6 OK 50 9 14 2
7 OK 20 9 14 2
8 OK 20 14 14 2
9 OK 0 14 14 2
10 FINISHED 0 14 14 2
9 1 1
Check: 10
```

### ג. תשובות והערות לדיון

FINISHED חוסם כל פעולה מוכרת.

רמה יכולה לעלות ביותר מאחת במודל מורחב.

מנוחה וריפוי חוקיים גם בתקרה לפי המפרט.

ok+denied מספר האירועים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
10
60
10
0
1
1
1
2
4
3
3
2
3
1
```

```python
count = int(input())
health = int(input())
energy = int(input())
xp = int(input())
level = 1 + xp // 10
low = 0
unchanged = 0
ok = 0
denied = 0
level_ups = 0
for i in range(count):
    action = int(input())
    old_health = health
    old_energy = energy
    old_xp = xp
    status = "OK"
    if action < 1 or action > 4:
        status = "INVALID"
    elif health == 0:
        status = "FINISHED"
    elif action == 1:
        if energy < 4:
            status = "LOW"
        else:
            energy -= 4
            xp += 7
    elif action == 2:
        energy += 5
        if energy > 20:
            energy = 20
    elif action == 3:
        health -= 30
        if health < 0:
            health = 0
    elif energy < 3:
        status = "LOW"
    else:
        energy -= 3
        health += 20
        if health > 100:
            health = 100
    next_level = 1 + xp // 10
    level_ups += next_level - level
    level = next_level
    if status == "OK":
        ok += 1
        if health == old_health and energy == old_energy and xp == old_xp:
            unchanged += 1
    else:
        denied += 1
        if status == "LOW":
            low += 1
    print(i + 1, status, health, energy, xp, level)
print(ok, denied, level_ups)
print("Check:", ok + denied)
print(low, unchanged)
```

פלט:

```text
1 OK 60 6 7 1
2 OK 60 2 14 2
3 LOW 60 2 14 2
4 OK 60 7 14 2
5 OK 80 4 14 2
6 OK 50 4 14 2
7 OK 20 4 14 2
8 OK 20 9 14 2
9 OK 0 9 14 2
10 FINISHED 0 9 14 2
8 2 1
Check: 10
1 0
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
0 OK [60, 100] [6, 20] [7, 8]
1 OK [60, 100] [6, 16] [7, 15]
0 OK [60, 100] [2, 16] [14, 15]
0 OK [30, 100] [2, 16] [14, 15]
1 OK [30, 100] [2, 13] [14, 15]
0 OK [0, 100] [2, 13] [14, 15]
0 FINISHED [0, 100] [2, 13] [14, 15]
1 OK [0, 100] [2, 18] [14, 15]
1 OK [0, 100] [2, 14] [14, 22]
2 UNKNOWN [0, 100] [2, 14] [14, 22]
[2, 3]
[[0, 'OK'], [1, 'OK'], [0, 'OK'], [0, 'OK'], [1, 'OK'], [0, 'OK'], [0, 'FINISHED'], [1, 'OK'], [1, 'OK'], [2, 'UNKNOWN']]
```

### ב. פלט התרחיש השני

```text
0 OK [60, 100] [6, 20] [7, 8]
1 OK [60, 100] [6, 16] [7, 15]
0 OK [60, 100] [2, 16] [14, 15]
0 OK [30, 100] [2, 16] [14, 15]
1 OK [30, 100] [2, 13] [14, 15]
1 OK [30, 70] [2, 13] [14, 15]
0 OK [30, 70] [7, 13] [14, 15]
1 OK [30, 70] [7, 18] [14, 15]
1 OK [30, 70] [7, 14] [14, 22]
2 UNKNOWN [30, 70] [7, 14] [14, 22]
[2, 3]
[[0, 'OK'], [1, 'OK'], [0, 'OK'], [0, 'OK'], [1, 'OK'], [1, 'OK'], [0, 'OK'], [1, 'OK'], [1, 'OK'], [2, 'UNKNOWN']]
```

### ג. תשובות והערות לדיון

אינדקס פסול עלול לקרוא שחקן אחר.

אין השפעה.

levels נגזרת מה-XP.

history מתעד החלטות אך לא כל מדד.

משווים מדדים לפני ואחרי.

### ד. פתרון אפשרי

```python
healths = [60, 100]
energies = [10, 20]
experiences = [0, 8]
events = [[0, 1], [1, 1], [0, 1], [0, 3], [1, 4], [0, 3], [0, 2], [1, 2], [1, 1], [2, 1]]
history = []
counters = [0, 0]
unknown = 0
for event in events:
    player = event[0]
    action = event[1]
    if player < 0 or player >= len(healths):
        status = "UNKNOWN"
        unknown += 1
    elif action < 1 or action > 4:
        status = "INVALID"
    elif healths[player] == 0:
        status = "FINISHED"
    else:
        status = "OK"
        if action == 1:
            if energies[player] >= 4:
                energies[player] -= 4
                experiences[player] += 7
            else:
                status = "LOW"
        elif action == 2:
            energies[player] += 5
            if energies[player] > 20:
                energies[player] = 20
        elif action == 3:
            healths[player] -= 30
            if healths[player] < 0:
                healths[player] = 0
        elif energies[player] >= 3:
            energies[player] -= 3
            healths[player] += 20
            if healths[player] > 100:
                healths[player] = 100
        else:
            status = "LOW"
    if status == "OK":
        counters[player] += 1
    history.append([player, status])
    print(player, status, healths, energies, experiences)
levels = []
for xp in experiences:
    levels.append(1 + xp // 10)
print(levels)
active = []
for i in range(len(healths)):
    if healths[i] > 0:
        active.append(i)
print(history)
print(counters, unknown, active)
```

פלט:

```text
0 OK [60, 100] [6, 20] [7, 8]
1 OK [60, 100] [6, 16] [7, 15]
0 OK [60, 100] [2, 16] [14, 15]
0 OK [30, 100] [2, 16] [14, 15]
1 OK [30, 100] [2, 13] [14, 15]
0 OK [0, 100] [2, 13] [14, 15]
0 FINISHED [0, 100] [2, 13] [14, 15]
1 OK [0, 100] [2, 18] [14, 15]
1 OK [0, 100] [2, 14] [14, 22]
2 UNKNOWN [0, 100] [2, 14] [14, 22]
[2, 3]
[[0, 'OK'], [1, 'OK'], [0, 'OK'], [0, 'OK'], [1, 'OK'], [0, 'OK'], [0, 'FINISHED'], [1, 'OK'], [1, 'OK'], [2, 'UNKNOWN']]
[4, 4] 1 [1]
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[[60, 0, 15], 'OK']
[[60, 1, 22], ['OK', 'LOW', 'OK', 'OK']]
[[60, 1, 22], ['OK', 'OK', 'OK', 'LOW']]
[60, 4, 8]
```

### ב. פלט התרחיש השני

```text
[[60, 4, 8], 'LOW']
[[60, 5, 15], ['LOW', 'LOW', 'OK', 'OK']]
[[60, 1, 22], ['OK', 'OK', 'OK', 'LOW']]
[60, 4, 8]
```

### ג. תשובות והערות לדיון

אנרגיה 4 חוקית לאימון.

משתמשים בערכים מקומיים.

היסטוריה מראה דחיות.

הסדר משפיע על זמינות אנרגיה.

מדפיסים מקור לפני ואחרי.

### ד. פתרון אפשרי

```python
def apply(state, action):
    health = state[0]
    energy = state[1]
    xp = state[2]
    status = "OK"
    if action < 1 or action > 4:
        status = "INVALID"
    elif health == 0:
        status = "FINISHED"
    elif action == 1:
        if energy >= 4:
            energy -= 4
            xp += 7
        else:
            status = "LOW"
    elif action == 2:
        energy += 5
        if energy > 20:
            energy = 20
    elif action == 3:
        health -= 30
        if health < 0:
            health = 0
    elif energy >= 3:
        energy -= 3
        health += 20
        if health > 100:
            health = 100
    else:
        status = "LOW"
    return [[health, energy, xp], status]

def audit(state):
    return state[0] >= 0 and state[0] <= 100 and state[1] >= 0 and state[1] <= 20 and state[2] >= 0

def simulate(state, actions):
    history = []
    checks = []
    for action in actions:
        result = apply(state, action)
        state = result[0]
        history.append(result[1])
        checks.append(audit(state))
    return [state, history, checks]

start = [60, 4, 8]
print(apply(start, 1))
print(simulate(start, [1, 1, 2, 1]))
print(simulate(start, [2, 1, 1, 1]))
print(start)
print(audit([100, 21, 5]))
```

פלט:

```text
[[60, 0, 15], 'OK']
[[60, 1, 22], ['OK', 'LOW', 'OK', 'OK'], [True, True, True, True]]
[[60, 1, 22], ['OK', 'OK', 'OK', 'LOW'], [True, True, True, True]]
[60, 4, 8]
False
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
OK
OK
OK
OK
OK
OK
OK
FINISHED
UNKNOWN
[['A', 0, 0, 14, 2], ['B', 100, 1, 14, 2]]
[1, 0]
[[0, 1, 'OK'], [1, 1, 'OK'], [0, 1, 'OK'], [1, 2, 'OK'], [1, 1, 'OK'], [0, 3, 'OK'], [0, 3, 'OK'], [0, 2, 'FINISHED'], [2, 1, 'UNKNOWN']]
```

### ב. פלט התרחיש השני

```text
OK
LOW
OK
OK
OK
OK
OK
FINISHED
UNKNOWN
[['A', 0, 0, 14, 2], ['B', 100, 4, 7, 1]]
[0, 1]
[[0, 1, 'OK'], [1, 1, 'LOW'], [0, 1, 'OK'], [1, 2, 'OK'], [1, 1, 'OK'], [0, 3, 'OK'], [0, 3, 'OK'], [0, 2, 'FINISHED'], [2, 1, 'UNKNOWN']]
```

### ג. תשובות והערות לדיון

Player אחראית למצבה, Arena לניתוב.

גם מי שסיים מדורג לפי כלל המודל.

אינדקס חוקי מזהה מופע.

דירוג רק קורא.

בשוויון מלא ראשון.

reports ו-rank אינן משנות יומן.

### ד. פתרון אפשרי

```python
class Player:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy
        self.xp = 0

    def act(self, action):
        if action < 1 or action > 4:
            return "INVALID"
        if self.health == 0:
            return "FINISHED"
        if action == 1:
            if self.energy < 4:
                return "LOW"
            self.energy -= 4
            self.xp += 7
        elif action == 2:
            self.energy += 5
            if self.energy > 20:
                self.energy = 20
        elif action == 3:
            self.health -= 30
            if self.health < 0:
                self.health = 0
        elif self.energy < 3:
            return "LOW"
        else:
            self.energy -= 3
            self.health += 20
            if self.health > 100:
                self.health = 100
        return "OK"

    def audit(self):
        return self.health >= 0 and self.health <= 100 and self.energy >= 0 and self.energy <= 20 and self.xp >= 0

    def report(self):
        level = 1 + self.xp // 10
        return [self.name, self.health, self.energy, self.xp, level]

class Arena:
    def __init__(self, players):
        self.players = players
        self.history = []

    def event(self, index, action):
        if index < 0 or index >= len(self.players):
            status = "UNKNOWN"
        else:
            status = self.players[index].act(action)
        self.history.append([index, action, status])
        return status

    def better(self, i, best):
        if best == -1:
            return True
        a = self.players[i]
        b = self.players[best]
        if a.xp != b.xp:
            return a.xp > b.xp
        return a.health > b.health

    def rank(self):
        result = []
        for turn in range(len(self.players)):
            best = -1
            for i in range(len(self.players)):
                if i not in result and self.better(i, best):
                    best = i
            result.append(best)
        return result

    def active_rank(self):
        result = []
        for turn in range(len(self.players)):
            best = -1
            for i in range(len(self.players)):
                if self.players[i].health > 0 and i not in result and self.better(i, best):
                    best = i
            if best != -1:
                result.append(best)
        return result

    def reports(self):
        result = []
        for player in self.players:
            result.append(player.report())
        return result

a = Player("A", 60, 8)
b = Player("B", 100, 4)
arena = Arena([a, b])
for event in [[0, 1], [1, 1], [0, 1], [1, 2], [1, 1], [0, 3], [0, 3], [0, 2], [2, 1]]:
    print(arena.event(event[0], event[1]))
print(arena.reports())
print(arena.rank())
print(arena.history)
print(arena.active_rank())
for player in arena.players:
    print(player.audit())
```

פלט:

```text
OK
OK
OK
OK
OK
OK
OK
FINISHED
UNKNOWN
[['A', 0, 0, 14, 2], ['B', 100, 1, 14, 2]]
[1, 0]
[[0, 1, 'OK'], [1, 1, 'OK'], [0, 1, 'OK'], [1, 2, 'OK'], [1, 1, 'OK'], [0, 3, 'OK'], [0, 3, 'OK'], [0, 2, 'FINISHED'], [2, 1, 'UNKNOWN']]
[1]
True
True
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

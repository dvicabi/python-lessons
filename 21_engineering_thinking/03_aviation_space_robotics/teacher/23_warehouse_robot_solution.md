# פתרונות למורה: רובוט במחסן: איך מנווטים בין מכשולים ואוספים פריטים?

[חזרה למשימת התלמיד](../23_warehouse_robot.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
ROBOT R1 | SIM
Row: 1 | Column: 0
Collected: 2 items
Move: RIGHT | OK
```

### ב. פלט התרחיש השני

```text
ROBOT  | R1 | SIM
Row: 1 | Column: 0
Collected: 2 items
Move: RIGHT | OK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 4.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("ROBOT ", end="")
print("R2", end="")
print(" | SIM")
print("Row: ", end="")
print("2", end="")
print(" | Column: 1")
print("Collected: ", end="")
print("3", end="")
print(" items")
print("Move: ", end="")
print("RIGHT", end="")
print(" | BLOCKED")
```

פלט:

```text
ROBOT R2 | SIM
Row: 2 | Column: 1
Collected: 3 items
Move: RIGHT | BLOCKED
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
0 1 1
1 1 2
1 0 3
3 0 5
3 3 8
Check: 8
Position: 3 3
```

### ב. פלט התרחיש השני

```text
0 1 1
1 1 2
1 0 3
3 0 5
3 4 9
Check: 9
Position: 3 4
```

### ג. תשובות והערות לדיון

תנועות בכיוונים הפוכים מתקזזות במיקום אבל לא במרחק.

steps מצטבר.

תנועה של שתי משבצות כוללת שני צעדים.

המיקום מתאר את נקודת הסיום בלבד.

### ד. פתרון אפשרי

```python
row = 0
col = 0
steps = 0
horizontal = 0
row += 2
steps += 2
print(row, col, steps)
col += 1
steps += 1
horizontal += 1
print(row, col, steps)
row -= 1
steps += 1
print(row, col, steps)
col -= 1
steps += 1
horizontal += 1
print(row, col, steps)
row += 2
steps += 2
print(row, col, steps)
print("Horizontal:", horizontal)
```

פלט:

```text
2 0 2
2 1 3
1 1 4
1 0 5
3 0 7
Horizontal: 2
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
After 1: 0 1
After 2: 1 1
After 3: 1 0
Change: 1 0
Right space: 4
Down space: 2
```

### ב. פלט התרחיש השני

```text
After 1: -1 0
After 2: 0 0
After 3: 0 1
Change: 0 1
Right space: 3
Down space: 3
```

### ג. תשובות והערות לדיון

ערך שלילי מעיד על חריגה מימין.

ייתכן מעבר דרך מצב לא חוקי וחזרה.

צעד אלכסוני או ארוך אינו פקודה במודל.

צריך מפת מכשולים ובדיקת כל יעד.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
1
0
1
0
0
1
1
0
```

```python
row = int(input())
col = int(input())
dr1 = int(input())
dc1 = int(input())
dr2 = int(input())
dc2 = int(input())
dr3 = int(input())
dc3 = int(input())
start_row = row
start_col = col
row += dr1
col += dc1
print(row, col)
row += dr2
col += dc2
print(row, col)
row += dr3
col += dc3
print(row, col)
print(row - start_row, col - start_col)
print(row, 3 - row, col, 4 - col)
```

פלט:

```text
2 0
2 1
3 1
2 1
3 0 1 3
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
BLOCKED
1 1
Candidate: 1 2
```

### ב. פלט התרחיש השני

```text
MOVED
2 1
Candidate: 2 1
```

### ג. תשובות והערות לדיון

המועמד מאפשר לאמת בלי לשנות מצב.

INVALID פקודה לא מוכרת, OUTSIDE חריגה, BLOCKED יעד חסום.

למעלה או שמאלה מ-(0,0) חורגים.

עדכון מוקדם עלול להציב את הרובוט במקום בלתי חוקי.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
0
0
1
```

```python
row = int(input())
col = int(input())
direction = int(input())
next_row = row
next_col = col
valid = True
if direction == 1:
    next_row -= 1
elif direction == 2:
    next_col += 1
elif direction == 3:
    next_row += 1
elif direction == 4:
    next_col -= 1
else:
    valid = False
if not valid:
    print("INVALID")
elif next_row < 0 or next_row > 3 or next_col < 0 or next_col > 4:
    print("OUTSIDE")
elif (next_row == 1 or next_row == 2) and next_col == 2:
    print("BLOCKED")
else:
    row = next_row
    col = next_col
    print("MOVED")
print("Candidate:", next_row, next_col)
print("Final:", row, col)
```

פלט:

```text
OUTSIDE
Candidate: -1 0
Final: 0 0
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 MOVED 0 1
2 MOVED 1 1
3 BLOCKED 1 1
4 MOVED 2 1
5 BLOCKED 2 1
6 MOVED 2 0
7 MOVED 1 0
8 INVALID 1 0
5 2 0 1
Check: 8
```

### ב. פלט התרחיש השני

```text
1 MOVED 0 1
2 MOVED 1 1
3 MOVED 2 1
4 MOVED 3 1
5 MOVED 3 2
6 MOVED 3 3
7 MOVED 3 4
8 INVALID 3 4
7 0 0 1
Check: 8
```

### ג. תשובות והערות לדיון

כל פקודה מקבלת בדיוק סטטוס אחד.

מיקום קודם נשמר בכשל ולכן היעד הבא מחושב ממנו.

מועמד חייב להתאפס למיקום הנוכחי.

אפשר לעבור בשורה 0 או 3.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
9
3
3
3
2
2
2
2
2
1
```

```python
count = int(input())
row = 0
col = 0
moved = 0
denied = 0
reached = 0
for step in range(count):
    direction = int(input())
    nr = row
    nc = col
    valid = True
    if direction == 1:
        nr -= 1
    elif direction == 2:
        nc += 1
    elif direction == 3:
        nr += 1
    elif direction == 4:
        nc -= 1
    else:
        valid = False
    if valid and nr >= 0 and nr <= 3 and nc >= 0 and nc <= 4 and not ((nr == 1 or nr == 2) and nc == 2):
        row = nr
        col = nc
        moved += 1
        if row == 3 and col == 4:
            reached += 1
    else:
        denied += 1
    print(step + 1, row, col)
print(moved, denied, reached)
```

פלט:

```text
1 1 0
2 2 0
3 3 0
4 3 1
5 3 2
6 3 3
7 3 4
8 3 4
9 2 4
8 1 1
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
[[0, 1], [1, 1], [1, 1], [2, 1], [3, 1], [3, 2], [3, 3], [3, 4], [3, 3], [3, 4]]
[[0, 1], [2, 1], [3, 2], [3, 4]]
4
[[0, 0, 0, 0, 0], [0, 0, 1, 2, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
```

### ב. פלט התרחיש השני

```text
[[0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [3, 4], [3, 3], [3, 2], [3, 1]]
[[0, 1], [1, 3], [3, 4], [3, 2]]
4
[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 0, 0, 0, 0]]
```

### ג. תשובות והערות לדיון

אינדקס שלילי עלול לקרוא מהסוף ואינדקס גדול עלול לגרום לשגיאה.

history מתעדת תוצאה לכל פקודה.

הפיכת 2 ל-0 מונעת איסוף כפול.

כל זוג מיוצג ברשימה פנימית.

### ד. פתרון אפשרי

```python
grid = [[0, 2, 0, 0, 0], [0, 0, 1, 2, 0], [0, 2, 1, 0, 0], [0, 0, 2, 0, 2]]
commands = [2, 3, 2, 3, 3, 2, 2, 2, 4, 2]
row = 0
col = 0
statuses = []
picked = []
for direction in commands:
    nr = row
    nc = col
    valid = True
    if direction == 1:
        nr -= 1
    elif direction == 2:
        nc += 1
    elif direction == 3:
        nr += 1
    elif direction == 4:
        nc -= 1
    else:
        valid = False
    if not valid:
        statuses.append("INVALID")
    elif nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]):
        statuses.append("OUTSIDE")
    elif grid[nr][nc] == 1:
        statuses.append("BLOCKED")
    else:
        row = nr
        col = nc
        statuses.append("MOVED")
        if grid[row][col] == 2:
            picked.append([row, col])
            grid[row][col] = 0
remaining = 0
for line in grid:
    for value in line:
        if value == 2:
            remaining += 1
print(statuses)
print(picked)
print(remaining, len(picked) + remaining)
```

פלט:

```text
['MOVED', 'MOVED', 'BLOCKED', 'MOVED', 'MOVED', 'MOVED', 'MOVED', 'MOVED', 'MOVED', 'MOVED']
[[0, 1], [2, 1], [3, 2], [3, 4]]
1 5
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
[1, 1, 'BLOCKED']
[0, 0, 'OUTSIDE']
[['MOVED', 'MOVED', 'BLOCKED', 'MOVED', 'MOVED', 'MOVED'], [[0, 1], [1, 1], [1, 1], [2, 1], [3, 1], [3, 2]]]
[[0, 2, 0, 0, 0], [0, 0, 1, 2, 0], [0, 2, 1, 0, 0], [0, 0, 2, 0, 2]]
```

### ב. פלט התרחיש השני

```text
[1, 2, 'MOVED']
[0, 0, 'OUTSIDE']
[['BLOCKED', 'MOVED', 'MOVED', 'BLOCKED', 'BLOCKED', 'MOVED'], [[0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 2]]]
[[0, 2, 0, 0, 0], [0, 0, 1, 2, 0], [0, 2, 1, 0, 0], [0, 0, 2, 0, 2]]
```

### ג. תשובות והערות לדיון

כך ניתן לעדכן מצב מהתוצאה באופן עקבי.

walk מיועדת לבדיקת תנועה בלבד.

משבצת פריט תידחה ומכשול יאושר.

אפשר לתכנן על המפה בקריאה בלבד ולהפעיל איסוף לאחר אישור.

### ד. פתרון אפשרי

```python
def move(grid, row, col, direction):
    nr = row
    nc = col
    if direction == 1:
        nr -= 1
    elif direction == 2:
        nc += 1
    elif direction == 3:
        nr += 1
    elif direction == 4:
        nc -= 1
    else:
        return [row, col, "INVALID"]
    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]):
        return [row, col, "OUTSIDE"]
    if grid[nr][nc] == 1:
        return [row, col, "BLOCKED"]
    return [nr, nc, "MOVED"]

def pick(grid, row, col):
    if grid[row][col] == 2:
        grid[row][col] = 0
        return True
    return False

def run(grid, commands):
    row = 0
    col = 0
    statuses = []
    picked = []
    for direction in commands:
        result = move(grid, row, col, direction)
        row = result[0]
        col = result[1]
        statuses.append(result[2])
        if result[2] == "MOVED" and pick(grid, row, col):
            picked.append([row, col])
    return [[row, col], statuses, picked]

grid = [[0, 2, 0, 0, 0], [0, 0, 1, 2, 0], [0, 2, 1, 0, 0], [0, 0, 2, 0, 2]]
print(run(grid, [2, 4, 2, 3, 2, 3, 3, 2]))
print(grid)
```

פלט:

```text
[[3, 2], ['MOVED', 'MOVED', 'MOVED', 'MOVED', 'BLOCKED', 'MOVED', 'MOVED', 'MOVED'], [[0, 1], [2, 1], [3, 2]]]
[[0, 0, 0, 0, 0], [0, 0, 1, 2, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
True True
True True
True False
[[0, 1], [2, 1]] []
0 1
[[0, 0, 0], [0, 0, 1], [0, 0, 0]]
```

### ב. פלט התרחיש השני

```text
True True
True True
True False
[[2, 1]] [[0, 1]]
0 1
[[0, 0, 0], [0, 0, 1], [0, 0, 0]]
```

### ג. תשובות והערות לדיון

מלאי משותף הוא חלק מהמפרט;

הפריט הראשון שנאסף כבר אינו קיים לאחר מכן.

רשימת איסופים שייכת לרובוט.

למניעת התנגשות יידרש מנגנון נוסף שמתעד מיקומים, שלא קיים במודל הזה.

### ד. פתרון אפשרי

```python
class Warehouse:
    def __init__(self, grid):
        self.grid = grid

    def allowed(self, row, col):
        if row < 0 or row >= len(self.grid):
            return False
        if col < 0 or col >= len(self.grid[row]):
            return False
        return self.grid[row][col] != 1

    def pick(self, row, col):
        if self.grid[row][col] == 2:
            self.grid[row][col] = 0
            return True
        return False

    def remaining(self):
        count = 0
        for line in self.grid:
            for value in line:
                if value == 2:
                    count += 1
        return count

class Robot:
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.row = 0
        self.col = 0
        self.picked = []
        self.denied = 0
        self.steps = 0

    def move(self, direction):
        nr = self.row
        nc = self.col
        if direction == 1:
            nr -= 1
        elif direction == 2:
            nc += 1
        elif direction == 3:
            nr += 1
        elif direction == 4:
            nc -= 1
        else:
            self.denied += 1
            return False
        if not self.warehouse.allowed(nr, nc):
            self.denied += 1
            return False
        self.row = nr
        self.col = nc
        self.steps += 1
        if self.warehouse.pick(nr, nc):
            self.picked.append([nr, nc])
        return True

warehouse = Warehouse([[0, 2, 0], [0, 0, 1], [0, 2, 0]])
a = Robot(warehouse)
b = Robot(warehouse)
print(a.move(2), b.move(2))
print(a.move(3), b.move(3))
print(a.move(3), b.move(2))
print(a.picked, b.picked)
print(a.denied, b.denied)
print(warehouse.grid)
print(a.steps, b.steps, warehouse.remaining())
print(len(a.picked) + len(b.picked) + warehouse.remaining())
```

פלט:

```text
True True
True True
True False
[[0, 1], [2, 1]] []
0 1
[[0, 0, 0], [0, 0, 1], [0, 0, 0]]
3 2 0
2
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

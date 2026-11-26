# פתרונות למורה: בית קולנוע: איך מוצאים מקומות רצופים לקבוצה בלי לפגוע בהזמנות קיימות?

[חזרה למשימת התלמיד](../40_cinema.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
CINEMA 01 | DEMO
Group: 3 seats
Row: 2 | Start: 4
Available: 12 seats
State: RESERVED | OK
```

### ב. פלט התרחיש השני

```text
CINEMA  | 01 | DEMO
Group: 3 seats
Row: 2 | Start: 4
Available: 12 seats
State: RESERVED | OK
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("CINEMA ", end="")
print("02", end="")
print(" | DEMO")
print("Group: ", end="")
print("5", end="")
print(" seats")
print("Row: ", end="")
print("NONE", end="")
print(" | Start: NONE")
print("Available: ", end="")
print("8", end="")
print(" seats")
print("State: ", end="")
print("DENIED", end="")
print(" | NO BLOCK")
```

פלט:

```text
CINEMA 02 | DEMO
Group: 5 seats
Row: NONE | Start: NONE
Available: 8 seats
State: DENIED | NO BLOCK
```

---

## רמה 2: משתנים ופעולות חשבון

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
4 20 4 0 120
7 17 7 0 210
3 21 7 4 90
8 16 12 4 240
Seats: 8
Cash: 240
```

### ב. פלט התרחיש השני

```text
4 20 4 0 120
7 17 7 0 210
3 21 7 4 90
9 15 13 4 270
Seats: 9
Cash: 270
```

### ג. תשובות והערות לדיון

booked מצטבר.

booked-cancelled=reserved.

החזר נשמר בנפרד לדוח נטו.

מספר פנויים לא מתאר פיזור.

### ד. פתרון אפשרי

```python
capacity = 30
reserved = 0
booked = 0
cancelled = 0
revenue = 0
refunds = 0
price = 25
size = 3
reserved += size
booked += size
revenue += size * price
print(reserved, capacity - reserved, booked, cancelled, revenue - refunds)
size = 6
reserved += size
booked += size
revenue += size * price
print(reserved, capacity - reserved, booked, cancelled, revenue - refunds)
size = 3
reserved -= size
cancelled += size
refunds += size * price
print(reserved, capacity - reserved, booked, cancelled, revenue - refunds)
size = 4
reserved += size
booked += size
revenue += size * price
print(reserved, capacity - reserved, booked, cancelled, revenue - refunds)
print("Seats:", booked - cancelled)
print("Cash:", reserved * price)
```

פלט:

```text
3 27 3 0 75
9 21 9 0 225
6 24 9 3 150
10 20 13 3 250
Seats: 10
Cash: 250
```

---

## רמה 3: קלט והמרה

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
A: 2 -2
B: 3 -1
C: 4 0
Total: 9 5
```

### ב. פלט התרחיש השני

```text
A: 2 -2
B: 4 0
C: 4 0
Total: 10 6
```

### ג. תשובות והערות לדיון

שני הקצוות כלולים.

פער שלילי הוא רצף קצר מדי.

פנויים יכולים להתפזר בין רצפים.

נדרש סדר השורות והמיקום בתוך כל שורה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
1
3
4
7
4
```

```python
start_a = int(input())
end_a = int(input())
start_b = int(input())
end_b = int(input())
group = int(input())
length_a = end_a - start_a + 1
length_b = end_b - start_b + 1
print(length_a, length_a - group, start_a + group - 1)
print(length_b, length_b - group, start_b + group - 1)
```

פלט:

```text
3 -1 4
4 0 7
```

---

## רמה 4: תנאים

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
FOUND 0 5
Last: 8
Free total: 12
```

### ב. פלט התרחיש השני

```text
FOUND 1 0
Last: 3
Free total: 11
```

### ג. תשובות והערות לדיון

B הראשון שמתאים.

if נפרדים עשויים לדרוס את הבחירה.

גודל לא חיובי פסול.

שוויון לאורך מותר.

רצפים מופרדים במושבים תפוסים.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
4
2
3
5
```

```python
group = int(input())
row_a = 0
start_a = 1
length_a = int(input())
row_b = 0
start_b = 5
length_b = int(input())
row_c = 1
start_c = 0
length_c = int(input())
row = -1
start = -1
if group <= 0:
    status = "INVALID"
elif length_a >= group:
    row = row_a
    start = start_a
    status = "FOUND"
elif length_b >= group:
    row = row_b
    start = start_b
    status = "FOUND"
elif length_c >= group:
    row = row_c
    start = start_c
    status = "FOUND"
else:
    status = "DENIED"
print(status, row, start)
if status == "FOUND":
    print("Last:", start + group - 1)
    if row == row_a and start == start_a:
        print(length_a - group)
    elif row == row_b and start == start_b:
        print(length_b - group)
    else:
        print(length_c - group)
else:
    print("No block")
print("Free total:", length_a + length_b + length_c)
```

פלט:

```text
FOUND 1 0
Last: 3
1
Free total: 10
```

---

## רמה 5: לולאות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
0 0 1 -1
1 0 2 -1
2 1 0 -1
3 0 1 -1
4 0 2 -1
5 0 3 3
6 1 0 3
7 0 1 3
8 0 2 3
9 1 0 3
10 0 1 3
11 0 2 3
Free: 9
Longest: 3
Start: 3
Last: 5
```

### ב. פלט התרחיש השני

```text
0 0 1 -1
1 0 2 -1
2 0 3 0
3 0 4 0
4 0 5 0
5 0 6 0
6 1 0 0
7 0 1 0
8 0 2 0
9 1 0 0
10 0 1 0
11 0 2 0
Free: 10
Longest: 6
Start: 0
Last: 2
```

### ג. תשובות והערות לדיון

תפוס קוטע רצף.

first שומר את המועמד הראשון.

longest רציף, free_total מפוזר.

שוויון מספיק.

בודקים רצף שמסתיים באינדקס האחרון.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
12
3
0
0
1
0
0
0
1
0
0
1
0
0
```

```python
count = int(input())
group = int(input())
occupied = 0
streak = 0
longest = 0
first = -1
free_total = 0
for i in range(count):
    seat = int(input())
    if seat == 0:
        streak += 1
        free_total += 1
        if streak > longest:
            longest = streak
        if streak >= group and first == -1:
            first = i - group + 1
    else:
        streak = 0
        occupied += 1
    print(i, seat, streak, first)
print("Free:", free_total)
print("Longest:", longest)
print("Check:", occupied + free_total == count)
if first == -1:
    print("NO BLOCK")
else:
    print("Start:", first)
    print("Last:", first + group - 1)
```

פלט:

```text
0 0 1 -1
1 0 2 -1
2 1 0 -1
3 0 1 -1
4 0 2 -1
5 0 3 3
6 1 0 3
7 0 1 3
8 0 2 3
9 1 0 3
10 0 1 3
11 0 2 3
Free: 9
Longest: 3
Check: True
Start: 3
Last: 5
```

---

## רמה 6: רשימות בלבד

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
0 1 -1 -1
1 1 1 1
2 0 1 1
RESERVED
[[0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1]]
1 1
12 9 3
```

### ב. פלט התרחיש השני

```text
0 1 -1 -1
1 1 -1 -1
2 0 -1 -1
DENIED
[[0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1]]
-1 -1
12 12 0
```

### ג. תשובות והערות לדיון

רצף אינו חוצה שורות.

חיבור כזה מציג הצעה בלתי חוקית.

הראשון נשמר.

בהצלחה הפנויים קטנים ב-group, בכשל לא משתנים.

len(hall[r]) מאפשר אורכי שורות שונים.

### ד. פתרון אפשרי

```python
hall = [[0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1]]
group = 3
chosen_row = -1
chosen_start = -1
free_before = 0
free_by_row = []
longest_by_row = []
for r in range(len(hall)):
    streak = 0
    free_row = 0
    longest = 0
    for c in range(len(hall[r])):
        if hall[r][c] == 0:
            free_before += 1
            streak += 1
            free_row += 1
            if streak > longest:
                longest = streak
            if streak >= group and chosen_row == -1:
                chosen_row = r
                chosen_start = c - group + 1
        else:
            streak = 0
    free_by_row.append(free_row)
    longest_by_row.append(longest)
    print(r, streak, chosen_row, chosen_start)
if chosen_row != -1:
    for offset in range(group):
        hall[chosen_row][chosen_start + offset] = 1
    print("RESERVED")
else:
    print("DENIED")
free_after = 0
for row in hall:
    for seat in row:
        if seat == 0:
            free_after += 1
print(free_by_row, longest_by_row)
print(hall)
print(chosen_row, chosen_start)
print(free_before, free_after, free_before - free_after)
```

פלט:

```text
0 1 -1 -1
1 1 1 1
2 0 1 1
RESERVED
[4, 4, 4] [2, 3, 4]
[[0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1]]
1 1
12 9 3
```

---

## רמה 7: פעולות (פונקציות)

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[1, 1]
[1, 1]
[]
[]
3
[1, 1]
[[0, 0, 1, 0, 0], [1, 12, 12, 12, 0]]
```

### ב. פלט התרחיש השני

```text
[1, 1]
[0, 0]
[1, 1]
[]
2
[]
[[0, 0, 1, 0, 0], [1, 12, 12, 12, 0]]
```

### ג. תשובות והערות לדיון

המפרט מחפש ראשון ולא מיטבי.

[] פירושו אין מועמד, [0,0] מיקום חוקי.

קוד 0 היה מסמן את כל הפנויים.

כפילות נדחית.

כאן רק מזהים פעילים נחסמים, ולכן מזהה שבוטל יכול לשמש שוב;

ברמה 8 נוסיף היסטוריה.

### ד. פתרון אפשרי

```python
def find_block(hall, group):
    if group <= 0:
        return []
    for r in range(len(hall)):
        streak = 0
        for c in range(len(hall[r])):
            if hall[r][c] == 0:
                streak += 1
                if streak == group:
                    return [r, c - group + 1]
            else:
                streak = 0
    return []

def occupied_by(hall, code):
    count = 0
    for row in hall:
        for seat in row:
            if seat == code:
                count += 1
    return count

def reserve(hall, code, group):
    if code <= 0 or occupied_by(hall, code) > 0:
        return []
    result = find_block(hall, group)
    if len(result) != 0:
        for offset in range(group):
            hall[result[0]][result[1] + offset] = code
    return result

def cancel(hall, code):
    if code <= 0:
        return 0
    count = 0
    for r in range(len(hall)):
        for c in range(len(hall[r])):
            if hall[r][c] == code:
                hall[r][c] = 0
                count += 1
    return count

def count_free(hall):
    return occupied_by(hall, 0)

hall = [[0, 0, 0], [0, 1, 0]]
print(count_free(hall))
print(reserve(hall, 21, 3), count_free(hall))
print(reserve(hall, 22, 2), count_free(hall))
print(cancel(hall, 21), count_free(hall))
print(reserve(hall, 22, 2), count_free(hall))
print(hall)
```

פלט:

```text
5
[0, 0] 2
[] 2
3 5
[0, 0] 3
[[22, 22, 0], [0, 1, 0]]
```

---

## רמה 8: מחלקות

**הערכת ניסוי עצמאי:** בדקו שהקלט מתאים למגבלות הרמה, שהתחזית נכתבה לפני הרצה, שהפלט תועד במדויק ושהתלמיד הסביר מה הניסוי מוכיח. יש לקבל יותר מדוגמה אחת אם הנימוק נכון.

### א. פלט התרחיש הראשון

```text
[0, 0]
[1, 0]
[]
[]
[['A', 4, 3], ['B', 2, 3]]
0
3
[]
[0, 0]
[['A', 5, 2], ['B', 2, 3]]
[[14, 14, 0], [0, 0, 0, 0]] [[0, 0], [12, 12, 12]]
[[0, 11, [0, 0]], [1, 12, [1, 0]], [0, 13, []], [0, 14, [0, 0]]]
```

### ב. פלט התרחיש השני

```text
[0, 0]
[1, 0]
[1, 0]
[]
[['A', 0, 7], ['B', 2, 3]]
0
3
[]
[0, 0]
[['A', 1, 6], ['B', 2, 3]]
[[14, 14, 0], [13, 13, 13, 13]] [[0, 0], [12, 12, 12]]
[[0, 11, [0, 0]], [1, 12, [1, 0]], [0, 13, [1, 0]], [0, 14, [0, 0]]]
```

### ג. תשובות והערות לדיון

Cinema מונעת כפילות בין הקרנות.

find היא שאילתה.

ביטול במקום אחר מחזיר אפס.

מזהים חד-פעמיים נשמרים.

לכל הקרנה רשימה עצמאית.

נדרש רצף.

קריאה ישירה עלולה לעקוף מדיניות ייחודיות;

במודל קוראים להזמנות דרך Cinema.

### ד. פתרון אפשרי

```python
class Screening:
    def __init__(self, name, hall):
        self.name = name
        self.hall = hall
        self.booked = 0
        self.cancelled = 0
        self.initial_free = self.free()

    def free(self):
        count = 0
        for row in self.hall:
            for seat in row:
                if seat == 0:
                    count += 1
        return count

    def audit(self):
        return self.initial_free - self.free() == self.booked - self.cancelled

    def find(self, group):
        if group <= 0:
            return []
        for r in range(len(self.hall)):
            streak = 0
            for c in range(len(self.hall[r])):
                if self.hall[r][c] == 0:
                    streak += 1
                    if streak == group:
                        return [r, c - group + 1]
                else:
                    streak = 0
        return []

    def reserve(self, code, group):
        if code <= 0:
            return []
        result = self.find(group)
        if len(result) > 0:
            for offset in range(group):
                self.hall[result[0]][result[1] + offset] = code
            self.booked += group
        return result

    def cancel(self, code):
        count = 0
        if code > 0:
            for r in range(len(self.hall)):
                for c in range(len(self.hall[r])):
                    if self.hall[r][c] == code:
                        self.hall[r][c] = 0
                        count += 1
        self.cancelled += count
        return count

class Cinema:
    def __init__(self, screenings):
        self.screenings = screenings
        self.used = []
        self.history = []

    def book(self, index, code, group):
        if code <= 0 or code in self.used or index < 0 or index >= len(self.screenings):
            return []
        result = self.screenings[index].reserve(code, group)
        if len(result) > 0:
            self.used.append(code)
        self.history.append([index, code, result])
        return result

    def cancel(self, index, code):
        if index < 0 or index >= len(self.screenings) or code not in self.used:
            return 0
        return self.screenings[index].cancel(code)

    def audit_all(self):
        result = []
        for screening in self.screenings:
            result.append(screening.audit())
        return result

    def report(self):
        result = []
        for screening in self.screenings:
            result.append([screening.name, screening.free(), screening.booked - screening.cancelled])
        return result

a = Screening("A", [[0, 0, 0], [0, 0, 0, 0]])
b = Screening("B", [[0, 0], [0, 0, 0]])
cinema = Cinema([a, b])
print(cinema.book(0, 11, 3))
print(cinema.book(1, 12, 3))
print(cinema.book(0, 13, 5))
print(cinema.book(1, 11, 1))
print(cinema.report())
print(cinema.cancel(1, 11))
print(cinema.cancel(0, 11))
print(cinema.book(0, 11, 2))
print(cinema.book(0, 14, 2))
print(cinema.report())
print(a.hall, b.hall)
print(cinema.history)
print(cinema.audit_all())
print(cinema.book(0, 21, 99))
print(cinema.audit_all())
print(cinema.cancel(1, 12))
print(cinema.cancel(1, 12))
print(cinema.book(1, 22, 2))
print(cinema.audit_all())
```

פלט:

```text
[0, 0]
[1, 0]
[]
[]
[['A', 4, 3], ['B', 2, 3]]
0
3
[]
[0, 0]
[['A', 5, 2], ['B', 2, 3]]
[[14, 14, 0], [0, 0, 0, 0]] [[0, 0], [12, 12, 12]]
[[0, 11, [0, 0]], [1, 12, [1, 0]], [0, 13, []], [0, 14, [0, 0]]]
[True, True]
[]
[True, True]
3
0
[0, 0]
[True, True]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

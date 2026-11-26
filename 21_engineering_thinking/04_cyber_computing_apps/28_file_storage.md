# מערכת אחסון קבצים: איך שומרים על מכסת מקום ומידע עקבי?

אפליקציה מדומה מנהלת מקום אחסון לקבצים.

המשתמשים מוסיפים ומוחקים קבצים, והמערכת חייבת למנוע חריגה ולספק דוח מדויק.

אתם מפתחים תוכנת ניהול מלאי של מקום, ולא מערכת קבצים אמיתית.

## כללי הסימולציה

כל הגדלים הם יחידות דמה.

קיבולת חיובית וקובץ בגודל חיובי בלבד.

ברמות הראשונות ידועים רק גדלים;

בהמשך לכל קובץ מזהה מספרי ייחודי.

הוספה מצליחה אם יש מקום והמזהה אינו קיים.

מחיקה מצליחה רק לקובץ קיים ומשחררת בדיוק את גודלו.

דחייה אינה משנה מקום או מלאי.

אין גישה לקבצים אמיתיים.

**מטרת המשימה:** לבנות מערכת שלמה בהדרגה, לא רק להגיע לפלט נכון.

אפשר להתחיל ברמה המתאימה לחומר שנלמד.

אין צורך להכיר את הרמות הבאות.

בכל רמה יש ארבע משימות משנה, עם תרחיש מעקב נוסף, שאלות ביקורת ותכנון ניסויי בדיקה.

אין להריץ את הקוד לפני מעקב ידני.

בחרו בעצמכם כיצד לבנות טבלת מעקב.

לא תינתן תבנית.

## מסלול המשימות

- [רמה 1: print ו-end](#רמה-1)
- [רמה 2: משתנים ופעולות חשבון](#רמה-2)
- [רמה 3: קלט והמרה](#רמה-3)
- [רמה 4: תנאים](#רמה-4)
- [רמה 5: לולאות](#רמה-5)
- [רמה 6: רשימות בלבד](#רמה-6)
- [רמה 7: פעולות (פונקציות)](#רמה-7)
- [רמה 8: מחלקות](#רמה-8)

## רמה 1

**print ו-end | קושי: בסיסית**

תכננו תצוגה קריאה למפעיל המערכת.

בשלב זה המידע קבוע.

רק print ו-end.

ללא משתנים, קלט או תנאים.

### 1.א קריאת קוד

```python
print("STORAGE ", end="")
print("A", end="")
print(" | SIM")
print("Capacity: ", end="")
print("40", end="")
print(" units")
print("Used: ", end="")
print("27", end="")
print(" units")
print("Free: ", end="")
print("13", end="")
print(" units")
print("State: ", end="")
print("READY", end="")
print(" | OK")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("STORAGE ", end="")` ב-`print("STORAGE ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד לקורא דוח האחסון ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`STORAGE B | SIM`

`Capacity: 30 units`

`Used: 30 units`

`Free: 0 units`

`State: FULL | WAIT`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

הוספה ומחיקה של גדלים ידועים.

מונים נפרדים מתארים פעולות ומצב.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
capacity = 40
used = 10
added = 0
removed = 0
files = 2
size = 8
used += size
added += size
files += 1
print(used, capacity - used, files)
size = 5
used += size
added += size
files += 1
print(used, capacity - used, files)
size = 4
used -= size
removed += size
files -= 1
print(used, capacity - used, files)
size = 7
used += size
added += size
files += 1
print(used, capacity - used, files)
print("Totals:", added, removed)
print("Check:", 10 + added - removed)
print("Capacity:", used + capacity - used)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

החליפו את `size = 7` ב-`size = 12`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. מדוע added אינו used?

2. איזו משוואה מתארת את המלאי?

3. למה files משתנה ביחידה ולא ב-size?

4. מה יקרה אם מחיקה תשנה added במקום removed?

5. האם `used + capacity - used` היא בדיקת מאזן עצמאית? הסבירו מדוע היא עשויה להציג ערך תקין גם אם used שגוי.

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו ב-20 תפוס ו-3 קבצים בקיבולת 50.

הוסיפו 9, מחקו 6, הוסיפו 4 ומחקו 8.

הדפיסו מצב אחרי כל פעולה, סכומי הגדלים ומאזן.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קלט של מכסה ושלושה שינויים מתוכננים.

עדיין אין בדיקת חוקיות.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
40
10
18
4
7
```

```python
capacity = int(input())
used = int(input())
initial = used
a1 = int(input())
d1 = int(input())
a2 = int(input())
used += a1
print("Add 1:", used, capacity - used)
used -= d1
print("Delete:", used, capacity - used)
used += a2
print("Add 2:", used, capacity - used)
added = a1 + a2
removed = d1
print("Delta:", added - removed)
print("Check:", initial + added - removed)
print("Total writes:", added)
print("Free:", capacity - used)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
25
15
18
12
1
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. מה אומר מקום פנוי שלילי?

2. האם מצב סופי חוקי מוכיח שכל שלבי הביניים חוקיים?

3. למה אין להסיק קיום קובץ לפי הגודל בלבד?

4. מה נדרש כדי להגן על קיבולת?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו קיבולת, מצב התחלתי, שני גדלי הוספה ושני גדלי מחיקה, בסדר הוספה/מחיקה פעמיים.

הציגו מצב אחרי כל פעולה ומאזן, ללא תנאים.

הקלט לפי סדר ההקלדה:

```text
50
20
9
6
4
8
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

תנאים מגנים על מאזן מקום.

ברמה זו מחיקה מתארת שחרור מקום ידוע, לא מזהה קובץ.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
capacity = 30
used = 24
size = 6
kind = 1
accepted = 0
rejected = 0
if size <= 0 or (kind != 1 and kind != 2):
    print("INVALID")
elif kind == 1:
    if size <= capacity - used:
        used += size
        accepted += 1
        print("ADDED")
    else:
        rejected += 1
        print("NO SPACE")
else:
    if size <= used:
        used -= size
        accepted += 1
        print("REMOVED")
    else:
        rejected += 1
        print("NOT ENOUGH")
print(used, capacity - used)
print(accepted, rejected)
if used == capacity:
    print("FULL")
elif used == 0:
    print("EMPTY")
else:
    print("PARTIAL")
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `size = 6` ב-`size = 7`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה 6 מתקבל בדיוק?

2. למה סוג לא חוקי נבדק קודם?

3. מה קורה במחיקה של יותר מ-used?

4. האם תנאי גודל מספיק ברמה של קבצים מזוהים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו capacity,used,kind,size והשתמשו באותו מפרט.

הדפיסו גם את גודל השינוי בפועל (אפס בדחייה).

הקלט לפי סדר ההקלדה:

```text
30
24
2
8
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

עיבוד סדרה של הקצאות ושחרורים ידועים, עם שיא תפוסה ומאזן.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
1
12
1
9
2
6
1
14
2
50
0
5
1
-1
2
4
```

```python
capacity = 30
used = 10
initial = used
added = 0
removed = 0
ok = 0
rejected = 0
invalid = 0
peak = used
for i in range(8):
    kind = int(input())
    size = int(input())
    if size <= 0 or (kind != 1 and kind != 2):
        invalid += 1
        status = "INVALID"
    elif kind == 1:
        if size <= capacity - used:
            used += size
            added += size
            ok += 1
            status = "ADDED"
        else:
            rejected += 1
            status = "NO SPACE"
    elif size <= used:
        used -= size
        removed += size
        ok += 1
        status = "REMOVED"
    else:
        rejected += 1
        status = "NOT ENOUGH"
    if used > peak:
        peak = used
    print(i + 1, status, used, capacity - used)
print(ok, rejected, invalid)
print(added, removed, peak)
print("Check:", initial + added - removed, used)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
1
12
1
8
2
6
1
6
2
50
0
5
1
-1
2
4
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה peak לא יורד במחיקה?

2. איך המאזן מזהה שינוי באירוע נדחה?

3. האם ok הוא מספר קבצים?

4. איזו בדיקה מבטיחה שכל האירועים נספרו?

5. מה קורה אם כל האירועים לא חוקיים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו מכסה ומצב התחלתי חוקיים ומספר פעולות.

הוסיפו full_count שסופר כמה פעולות מוצלחות הסתיימו במכסה מלאה;

הדפיסו שיא ומונה.

הקלט לפי סדר ההקלדה:

```text
30
10
8
1
12
1
9
2
6
1
14
2
50
0
5
1
-1
2
4
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

רשימות מקבילות מייצגות מזהים, גדלים ודגל קיום.

קובץ שנמחק אינו תופס מקום.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
ids = [10, 20, 30, 40]
sizes = [6, 8, 10, 12]
active = [True, True, False, False]
events = [[1, 30], [1, 40], [2, 20], [1, 40], [1, 30], [2, 99], [2, 10]]
capacity = 30
used = 14
history = []
for event in events:
    kind = event[0]
    target = event[1]
    found = -1
    for i in range(len(ids)):
        if ids[i] == target:
            found = i
    if found == -1 or (kind != 1 and kind != 2):
        status = "INVALID"
    elif kind == 1:
        if active[found]:
            status = "DUPLICATE"
        elif sizes[found] > capacity - used:
            status = "NO SPACE"
        else:
            active[found] = True
            used += sizes[found]
            status = "ADDED"
    elif not active[found]:
        status = "MISSING"
    else:
        active[found] = False
        used -= sizes[found]
        status = "REMOVED"
    history.append(status)
    print(target, status, used, active)
check = 0
for i in range(len(ids)):
    if active[i]:
        check += sizes[i]
print(history)
print("Check:", used, check)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `capacity = 30` ב-`capacity = 26`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. למה בודקים found לפני שימוש בו?

2. מה ההבדל בין MISSING ל-INVALID?

3. למה אין להוסיף קובץ פעיל שוב?

4. כיצד check מאמת את הסכום?

5. מה הסיכון של מזהים כפולים ברשימת ids?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו רשימת מזהים שנשארו פעילים בסוף, וחשבו את גודל הקובץ הפעיל הגדול ביותר (0 אם אין).

הדפיסו את הרשימה, הגדול ביותר והמאזן.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

מפרידים חיפוש מזהה, ביצוע פעולה וחישוב דוח.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def find(ids, target):
    index = -1
    for i in range(len(ids)):
        if ids[i] == target:
            index = i
    return index

def change(ids, sizes, active, capacity, used, kind, target):
    index = find(ids, target)
    if index == -1 or (kind != 1 and kind != 2):
        return [used, "INVALID"]
    if kind == 1:
        if active[index]:
            return [used, "DUPLICATE"]
        if sizes[index] > capacity - used:
            return [used, "NO SPACE"]
        active[index] = True
        return [used + sizes[index], "ADDED"]
    if not active[index]:
        return [used, "MISSING"]
    active[index] = False
    return [used - sizes[index], "REMOVED"]

def total(sizes, active):
    used = 0
    for i in range(len(sizes)):
        if active[i]:
            used += sizes[i]
    return used

ids = [10, 20, 30]
sizes = [6, 8, 10]
active = [True, False, False]
used = total(sizes, active)
for event in [[1, 20], [1, 30], [2, 10], [1, 30]]:
    result = change(ids, sizes, active, 20, used, event[0], event[1])
    used = result[0]
    print(result, active)
print(used, total(sizes, active))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `result = change(ids, sizes, active, 20, used, event[0], event[1])` ב-`result = change(ids, sizes, active, 24, used, event[0], event[1])`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. מדוע change מחזירה used חדש?

2. למה active משתנה אך ids לא?

3. איזו בדיקה בודקת התאמה בין המצב לבין used?

4. מה קורה אם capacity אינה מספיקה?

5. איזה חלק מתאים לבדיקת יחידה מבודדת?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

כתבו audit(sizes,active,used,capacity) שמחזירה True רק אם סך הנפחים תואם ו-used בטווח.

בדקו אחרי כל אירוע;

הציגו גם בדיקה עם used שגוי בכוונה.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

מחלקת Drive שומרת קבצים, ומחלקת StorageLab מנהלת העברה בין מכסות.

בדיקה קודמת לשינוי.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class Drive:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ids = []
        self.sizes = []
        self.active = []
        self.used = 0

    def find(self, target):
        index = -1
        for i in range(len(self.ids)):
            if self.ids[i] == target and self.active[i]:
                index = i
        return index

    def can_add(self, target, size):
        return size > 0 and self.find(target) == -1 and size <= self.capacity - self.used

    def add(self, target, size):
        if not self.can_add(target, size):
            return False
        self.ids.append(target)
        self.sizes.append(size)
        self.active.append(True)
        self.used += size
        return True

    def remove(self, target):
        index = self.find(target)
        if index == -1:
            return False
        self.active[index] = False
        self.used -= self.sizes[index]
        return True

    def report(self):
        items = []
        for i in range(len(self.ids)):
            if self.active[i]:
                items.append(self.ids[i])
        return [self.used, self.capacity - self.used, items]

class StorageLab:
    def __init__(self):
        self.history = []

    def move(self, source, target, item):
        index = source.find(item)
        status = "DENIED"
        if index != -1 and source != target:
            size = source.sizes[index]
            if target.can_add(item, size):
                target.add(item, size)
                source.remove(item)
                status = "MOVED"
        self.history.append([item, status])
        return status

a = Drive(30)
b = Drive(12)
lab = StorageLab()
print(a.add(10, 8), a.add(20, 9), b.add(30, 5))
print(lab.move(a, b, 10))
print(lab.move(a, b, 20))
print(b.remove(30))
print(lab.move(a, b, 10))
print(lab.move(a, b, 20))
print(a.report(), b.report())
print(lab.history)
print("Combined:", a.used + b.used)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `b = Drive(12)` ב-`b = Drive(16)`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. למה can_add אינה משנה את היעד?

2. מדוע צריך לבדוק source != target?

3. מה קורה כשאין מקום ביעד?

4. כיצד מוכיחים שהעברה שומרת סך נפח?

5. מה ההבדל בין מחיקה להעברה?

6. מה עשוי להשתבש אם remove מתבצעת לפני בדיקת היעד?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו Drive.audit() שמשווה used לסכום גדלים פעילים.

הוסיפו StorageLab.count_moved() שסופרת MOVED.

הדפיסו את בדיקות התקינות לפני ואחרי ניסיון העברה נוסף.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו מנהל אחסון עם שתי מכסות עצמאיות ויומן.

תכננו העברה בין מכסות: רק אם המקור מכיל את הקובץ והיעד יכול לקבלו, בצעו את שני העדכונים.

אחרת אין שינוי.

הוכיחו שפעולה כושלת אינה מאבדת קובץ ושסכום המקום התפוס מתאים לסכומי הגדלים.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

# מערכת גיבוי: האם הקובץ המעודכן באמת נמצא גם בגיבוי?

אתם מתכננים מערכת גיבוי לימודית.

לכל פריט יש גרסה במקור וגרסה בגיבוי.

לא מספיק לדעת שקיים עותק: יש לדעת אם הוא עדכני.

בכל הרצה יש תקציב העברה מוגבל, ולכן יש לזהות פריטים שממתינים לסנכרון.

## כללי הסימולציה

אין גישה לקבצים אמיתיים, למחיקת מידע או לשירות גיבוי.

כל הנתונים מספריים ודמיוניים.

גרסת מקור חיובית;

גרסת גיבוי 0 מציינת שאין עותק.

גודל חיובי.

אם גיבוי גדול מגרסת מקור, CONFLICT ואסור להוריד גרסה אוטומטית.

שוויון = CURRENT.

אם גיבוי קטן ממקור, נדרשת העברה של הגודל המלא.

אם התקציב אינו מספיק, WAIT ללא שינוי.

העברה מוצלחת צורכת תקציב ומעדכנת את גרסת הגיבוי בדיוק לגרסת המקור.

בסריקה עוברים לפי סדר הנתונים, ופריט שממתין לא מונע בדיקה של הבאים.

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
print("BACKUP ", end="")
print("01", end="")
print(" | SIM")
print("Source: ", end="")
print("5", end="")
print(" version")
print("Copy: ", end="")
print("3", end="")
print(" version")
print("Budget: ", end="")
print("12", end="")
print(" units")
print("State: ", end="")
print("STALE", end="")
print(" | WAIT")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("BACKUP ", end="")` ב-`print("BACKUP ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד למנהל הגיבויים ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`BACKUP 02 | SIM`

`Source: 7 version`

`Copy: 7 version`

`Budget: 4 units`

`State: CURRENT | OK`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

מדמים שינוי גרסאות והעברה ידועה.

מפרידים גרסה מתקציב.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
source = 2
copy = 1
budget = 40
size = 6
transferred = 0
updates = 0
print(source, copy, budget, source - copy)
source += 1
print(source, copy, budget, source - copy)
copy = source
budget -= size
transferred += size
updates += 1
print(source, copy, budget, source - copy)
source += 2
size += 4
print(source, copy, budget, source - copy)
copy = source
budget -= size
transferred += size
updates += 1
print(source, copy, budget, source - copy)
print("Updates:", updates)
print("Transferred:", transferred)
print("Check:", budget + transferred)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

החליפו את `size += 4` ב-`size += 8`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. למה source משתנה בלי ש-copy משתנה מיד?

2. מדוע copy=source ולא copy+=1 בעת גיבוי?

3. איזו משוואה בודקת תקציב?

4. למה מספר העברות אינו גודל מצטבר?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו מקור 3, גיבוי 0, תקציב 50 וגודל 7.

בצעו גיבוי, הגדילו גרסת מקור ב-3 וגודל ב-2, גבו שוב, ואז הגדילו מקור ב-1 בלי לגבות.

הציגו פערי גרסאות ותקציב אחרי כל אירוע.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קולטים שלושה פריטים ותכנון העברה.

בשלב זה מחשבים דרישה תיאורטית בלבד.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
5
3
6
2
2
4
3
0
8
15
```

```python
source_a = int(input())
copy_a = int(input())
size_a = int(input())
source_b = int(input())
copy_b = int(input())
size_b = int(input())
source_c = int(input())
copy_c = int(input())
size_c = int(input())
budget = int(input())
gap_a = source_a - copy_a
gap_b = source_b - copy_b
gap_c = source_c - copy_c
all_size = size_a + size_b + size_c
print("A:", gap_a, size_a)
print("B:", gap_b, size_b)
print("C:", gap_c, size_c)
print("All sizes:", all_size)
print("Remaining:", budget - all_size)
print("Version gaps:", gap_a + gap_b + gap_c)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
5
3
6
2
4
4
3
0
8
10
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. מה משמעות פער גרסה 0?

2. מה משמעות פער גרסה שלילי?

3. מדוע all_size אינו בהכרח כמות ההעברה הנדרשת?

4. למה סכום פערי גרסאות עלול להסתיר CONFLICT?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו שני פריטים ותקציב.

חשבו פערי גרסאות, סך גודל ותכנון יתרות אם מעבירים את שניהם לפי הסדר.

ללא תנאים.

הקלט לפי סדר ההקלדה:

```text
5
1
6
3
0
8
12
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

בודקים חוקיות, סכסוך גרסאות, עדכניות ותקציב לפי סדר קבוע.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
source = 5
copy = 2
size = 8
budget = 8
initial = budget
transferred = 0
if source <= 0 or copy < 0 or size <= 0 or budget < 0:
    status = "INVALID"
elif copy > source:
    status = "CONFLICT"
elif copy == source:
    status = "CURRENT"
elif size > budget:
    status = "WAIT"
else:
    budget -= size
    transferred = size
    copy = source
    status = "COPIED"
print(status)
print(source, copy, source - copy)
print(budget, transferred)
print("Check:", initial == budget + transferred)
if source == copy:
    print("UP TO DATE")
else:
    print("NOT CURRENT")
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `budget = 8` ב-`budget = 7`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה CONFLICT נבדק לפני CURRENT?

2. מה קורה כש-size שווה בדיוק לתקציב?

3. למה copy נשמרת בדחייה?

4. מה אם המקור שגוי אך copy==source?

5. למה אי אפשר להשתמש בפער גרסאות כגודל העברה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו source,copy,size,budget.

יישמו את אותו מפרט.

הדפיסו בנוסף כמה יחידות תקציב חסרות במקרה WAIT, ואפס בכל מקרה אחר.

הקלט לפי סדר ההקלדה:

```text
5
2
9
4
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

סורקים שבעה פריטים.

מונים נפרדים מאפשרים לוודא שכל רשומה קיבלה סטטוס.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
5
2
8
3
3
4
4
5
2
4
0
14
2
1
4
3
0
7
0
0
2
```

```python
budget = 20
initial = budget
copied = 0
current = 0
waiting = 0
conflicts = 0
invalid = 0
transferred = 0
for i in range(7):
    source = int(input())
    copy = int(input())
    size = int(input())
    if source <= 0 or copy < 0 or size <= 0:
        status = "INVALID"
        invalid += 1
    elif copy > source:
        status = "CONFLICT"
        conflicts += 1
    elif copy == source:
        status = "CURRENT"
        current += 1
    elif size > budget:
        status = "WAIT"
        waiting += 1
    else:
        copy = source
        budget -= size
        transferred += size
        copied += 1
        status = "COPIED"
    print(i + 1, status, source, copy, budget)
print(copied, current, waiting, conflicts, invalid)
print("Check:", copied + current + waiting + conflicts + invalid)
print(transferred, budget, initial == transferred + budget)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
5
2
7
3
3
4
4
5
2
4
0
14
2
1
4
3
0
7
0
0
2
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה CURRENT לא צורך תקציב?

2. למה WAIT לא עוצר את הסריקה?

3. איך מזהים שכל הרשומות סווגו?

4. איזה מידע אובד אם שומרים רק copied?

5. מה קורה כש-budget=0 ויש פריטים עדכניים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו count ותקציב.

חשבו בנוסף סך גודל פריטים WAIT, ואינדקס ראשון של פריט WAIT (0 אם אין).

הדפיסו שני מדדים.

אין להקטין תקציב על WAIT.

הקלט לפי סדר ההקלדה:

```text
20
7
5
2
8
3
3
4
4
5
2
4
0
14
2
1
4
3
0
7
0
0
2
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

שומרים רשימות גרסאות ומריצים שני סבבים.

כל סבב מקבל תקציב חדש.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
ids = [101, 102, 103, 104, 105, 106]
sources = [5, 3, 4, 4, 2, 3]
copies = [2, 3, 5, 0, 1, 0]
sizes = [8, 4, 2, 14, 4, 7]
budgets = [12, 16]
history = []
for budget in budgets:
    statuses = []
    moved = []
    for i in range(len(ids)):
        if sources[i] <= 0 or copies[i] < 0 or sizes[i] <= 0:
            status = "INVALID"
        elif copies[i] > sources[i]:
            status = "CONFLICT"
        elif copies[i] == sources[i]:
            status = "CURRENT"
        elif sizes[i] > budget:
            status = "WAIT"
        else:
            copies[i] = sources[i]
            budget -= sizes[i]
            moved.append(ids[i])
            status = "COPIED"
        statuses.append(status)
    history.append([statuses, moved, budget])
    print(statuses)
    print(moved, budget)
    print(copies)
pending = []
for i in range(len(ids)):
    if copies[i] < sources[i]:
        pending.append(ids[i])
print(history)
print("Pending:", pending)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `budgets = [12, 16]` ב-`budgets = [12, 21]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. למה פריט COPIED בסבב ראשון אמור להיות CURRENT בשני?

2. מה ההבדל בין CONFLICT ל-Pending?

3. למה statuses ו-moved נוצרות מחדש בכל סבב?

4. איך מוכיחים שאין העברה חוזרת כשאין שינוי מקור?

5. מדוע אין למחוק רשומה שהמתינה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו בסוף רשימת CURRENT, רשימת CONFLICT ורשימת WAIT שנותרה.

חשבו סך גודל נדרש להשלמת כל Pending (הנתונים חוקיים), והדפיסו את כל הרשימות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

פעולה מסווגת פריט;

פעולה אחרת מנהלת סריקה תוך שמירה על רשימת המקור.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def sync(source, copy, size, budget):
    if source <= 0 or copy < 0 or size <= 0 or budget < 0:
        return [copy, budget, "INVALID"]
    if copy > source:
        return [copy, budget, "CONFLICT"]
    if copy == source:
        return [copy, budget, "CURRENT"]
    if size > budget:
        return [copy, budget, "WAIT"]
    return [source, budget - size, "COPIED"]

def batch(sources, copies, sizes, budget):
    if len(sources) != len(copies) or len(sources) != len(sizes) or budget < 0:
        return []
    statuses = []
    new_copies = []
    initial = budget
    for i in range(len(sources)):
        result = sync(sources[i], copies[i], sizes[i], budget)
        new_copies.append(result[0])
        budget = result[1]
        statuses.append(result[2])
    return [new_copies, statuses, budget, initial - budget]

sources = [5, 3, 4, 2]
copies = [2, 3, 0, 4]
sizes = [8, 4, 12, 1]
first = batch(sources, copies, sizes, 8)
second = batch(sources, first[0], sizes, 12)
print(first)
print(second)
print(copies)
print(batch(sources, [], sizes, 10))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `if size > budget:` ב-`if size >= budget:`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. איזה קלט חושף טעות בשוויון?

2. למה batch מחזירה new_copies ולא משנה copies?

3. כיצד הסבב השני משתמש בתוצאת הראשון?

4. מה קורה אם אורכי רשימות שונים?

5. למה חשוב ש-sync תחזיר budget מקורי בכשל?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הרחיבו batch כך שתחזיר גם רשימת אינדקסים שהועתקו ורשימת אינדקסים הממתינים.

הוסיפו דוגמה עם קלט ריק ושמרו על אי-שינוי copies.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

FileRecord שומר גרסאות;

BackupJob מנהלת תקציב לכל סבב, יומן וסיכום.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class FileRecord:
    def __init__(self, name, source, copy, size):
        self.name = name
        self.source = source
        self.copy = copy
        self.size = size

    def status(self):
        if self.source <= 0 or self.copy < 0 or self.size <= 0:
            return "INVALID"
        if self.copy > self.source:
            return "CONFLICT"
        if self.copy == self.source:
            return "CURRENT"
        return "STALE"

    def edit(self, version, size):
        if version <= self.source or size <= 0:
            return False
        self.source = version
        self.size = size
        return True

    def synchronize(self, budget):
        status = self.status()
        if status != "STALE":
            return [budget, status]
        if self.size > budget:
            return [budget, "WAIT"]
        self.copy = self.source
        return [budget - self.size, "COPIED"]

    def report(self):
        return [self.name, self.source, self.copy, self.status()]

class BackupJob:
    def __init__(self, files):
        self.files = files
        self.history = []
        self.transferred = 0

    def run(self, budget):
        if budget < 0:
            return []
        initial = budget
        events = []
        for file in self.files:
            result = file.synchronize(budget)
            budget = result[0]
            events.append([file.name, result[1]])
        amount = initial - budget
        self.transferred += amount
        report = [events, amount, budget]
        self.history.append(report)
        return report

    def reports(self):
        result = []
        for file in self.files:
            result.append(file.report())
        return result

a = FileRecord("A", 5, 2, 8)
b = FileRecord("B", 3, 3, 4)
c = FileRecord("C", 4, 0, 12)
d = FileRecord("D", 2, 4, 1)
job = BackupJob([a, b, c, d])
print(job.run(8))
print(job.run(12))
print(a.edit(6, 7))
print(job.run(6))
print(job.run(7))
print(job.reports())
print(job.transferred)
print(job.history)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `print(job.run(6))` ב-`print(job.run(7))`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. למה status היא שאילתה בלבד?

2. מדוע edit חייבת לבדוק גרסה חדשה?

3. למה היסטוריית הסבבים נפרדת?

4. איך בודקים שסבב חוזר אינו מעתיק פריט עדכני?

5. מדוע FileRecord אינה אחראית על תקציב של כל הקטלוג?

6. מה קורה כש-CONFLICT נשאר אחרי כל הסבבים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו ל-BackupJob pending_size() שסוכמת גדלים של STALE בלבד, ו-current_count() שסופרת CURRENT.

הדפיסו לפני הסבב הראשון, אחרי השני ואחרי האחרון.

ודאו שהשאילתות אינן משנות היסטוריה.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו מערכת עם שתי משימות גיבוי עצמאיות.

אפשרו הרצה נוספת עם תקציב חדש ומצאו אם הועתקו רק פריטים שעדיין אינם עדכניים.

תכננו דוח לפי מזהה, גרסה ומצב, והוכיחו ששגיאה או מגבלת תקציב אינה מוחקת גיבוי קיים.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

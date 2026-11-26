# מערכת התחברות: האם כל ניסיון משנה את מצב החשבון?

במעבדה מתקבלים אירועי אימות מדומים.

אתם בונים מערכת שמנהלת מצבים, מונים ויומן נפרד לכל חשבון.

המערכת צריכה להבדיל בין כישלון, הצלחה, אירוע שגוי וחשבון נעול.

## כללי הסימולציה

אין להזין סיסמאות אמיתיות או להתחבר לשירות חיצוני.

קוד 1 מציין תוצאת אימות מוצלחת, 0 כושלת, כל ערך אחר שגוי.

שלושה כישלונות רצופים נועלים חשבון.

הצלחה לפני נעילה מאפסת רצף.

אחרי נעילה, תוצאה חוקית מדווחת LOCKED ואינה משנה מצב.

INVALID אינו משנה מצב.

כל הפעולות הן סימולציה בלבד, ואינן מנגנון אבטחה אמיתי.

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
print("LOGIN ", end="")
print("A01", end="")
print(" | SIM")
print("Attempts: ", end="")
print("2", end="")
print(" / 3")
print("Account: ", end="")
print("OPEN", end="")
print(" | READY")
print("Result: ", end="")
print("FAIL", end="")
print(" | RETRY")
print("Event: ", end="")
print("07", end="")
print(" | LOG")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("LOGIN ", end="")` ב-`print("LOGIN ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד לקורא מסך הסטטוס ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`LOGIN B02 | SIM`

`Attempts: 3 / 3`

`Account: LOCKED | REVIEW`

`Result: DENIED | WAIT`

`Event: 08 | LOG`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

מבדילים בין כישלונות מצטברים לרצף נוכחי.

התוצאות ידועות מראש.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
attempts = 0
failures = 0
successes = 0
streak = 0
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
attempts += 1
successes += 1
streak = 0
print(attempts, failures, successes, streak)
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
attempts += 1
failures += 1
streak += 1
print(attempts, failures, successes, streak)
remaining = 3 - streak
print("Remaining:", remaining)
print("Check:", failures + successes)
print("Difference:", failures - streak)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

במקטע שמתחיל ב-`successes += 1`, שנו את השורה `streak = 0` ל-`streak = 1`.

השאירו את פקודת ההדפסה שאחריה ללא שינוי.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. מדוע failures ו-streak שונים?

2. מהו המאזן בין שלושת המונים הראשונים?

3. איזו טעות יוצר השינוי?

4. אילו מונים צריכים להישאר קבועים בעת דיווח?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

הדמו רצף 0,1,0,0,1,0.

הדפיסו את ארבעת המונים אחרי כל אירוע ואת המרווח לסף בסוף.

ללא תנאים.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קלט של מוני שני חשבונות.

עדיין אין החלטה אוטומטית.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
5
3
2
2
7
1
3
```

```python
a_fail = int(input())
a_ok = int(input())
a_streak = int(input())
b_fail = int(input())
b_ok = int(input())
b_streak = int(input())
limit = int(input())
a_total = a_fail + a_ok
b_total = b_fail + b_ok
all_fail = a_fail + b_fail
all_ok = a_ok + b_ok
total = all_fail + all_ok
a_left = limit - a_streak
b_left = limit - b_streak
print("A:", a_total, a_streak, a_left)
print("B:", b_total, b_streak, b_left)
print("Totals:", total, all_fail, all_ok)
print("Account gap:", a_total - b_total)
print("Check:", a_total + b_total)
print("Streak gap:", a_streak - b_streak)
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
2
6
1
3
3
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. למה סך כישלונות לא מספיק להסקת נעילה?

2. מה משמעות מרווח 0?

3. האם a_streak יכול להיות גדול מ-a_fail במצב חוקי?

4. למה סכום משותף מסתיר את מצב החשבון?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו שלושה חשבונות: כישלונות, הצלחות ורצף לכל אחד, ואז סף.

הדפיסו סך ניסיונות ומרווח לכל חשבון ואת המאזן הכללי.

הקלט לפי סדר ההקלדה:

```text
5
3
2
2
7
1
4
2
3
3
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

בודקים חוקיות, נעילה, ואז תוצאת אימות.

שני אירועים עוקבים.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
streak = 2
locked = False
successes = 0
failures = 0
event = 0
if event != 0 and event != 1:
    print("INVALID")
elif locked:
    print("LOCKED")
elif event == 1:
    successes += 1
    streak = 0
    print("SUCCESS")
else:
    failures += 1
    streak += 1
    if streak >= 3:
        locked = True
    print("FAIL", locked)
event = 1
if event != 0 and event != 1:
    print("INVALID")
elif locked:
    print("LOCKED")
elif event == 1:
    successes += 1
    streak = 0
    print("SUCCESS")
else:
    failures += 1
    streak += 1
    if streak >= 3:
        locked = True
    print("FAIL", locked)
print(streak, locked, successes, failures)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `streak = 2` ב-`streak = 1`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. מדוע locked נבדק לפני הצלחה?

2. האם אירוע INVALID הוא כישלון אימות?

3. האם כל אירוע מגדיל מונה הצלחה או כישלון?

4. מהו מקרה הגבול לנעילה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו רצף התחלתי 0–2, וסדר שני אירועים.

יישמו אותו מפרט.

הוסיפו מונה חסומים ומונה שגויים והדפיסו ארבעת המונים והמצב הסופי.

הקלט לפי סדר ההקלדה:

```text
2
0
1
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

זרם אירועים;

מונים וסימון רגע נעילה.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
0
0
1
0
2
0
0
1
0
2
```

```python
streak = 0
locked = False
successes = 0
failures = 0
blocked = 0
invalid = 0
lock_index = 0
for i in range(10):
    event = int(input())
    if event != 0 and event != 1:
        invalid += 1
        status = "INVALID"
    elif locked:
        blocked += 1
        status = "LOCKED"
    elif event == 1:
        successes += 1
        streak = 0
        status = "SUCCESS"
    else:
        failures += 1
        streak += 1
        status = "FAIL"
        if streak == 3:
            locked = True
            lock_index = i + 1
    print(i + 1, status, streak, locked)
print("Counters:", successes, failures, blocked, invalid)
print("Check:", successes + failures + blocked + invalid)
print("Lock index:", lock_index)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
0
0
0
0
2
0
0
1
0
2
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה lock_index אינו משתנה באירוע חסום?

2. איך בודקים שכל האירועים סווגו?

3. למה INVALID אינו מאפס רצף?

4. תנו רצף של 6 כישלונות מצטברים שלא יוביל לנעילה.

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו count וסף חיובי.

שנו את המערכת לסף זה, והוסיפו שיא רצף כישלונות.

הדפיסו גם את השיא.

הקלט לפי סדר ההקלדה:

```text
10
4
0
0
1
0
0
2
0
0
1
0
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

שני חשבונות באותו יומן;

רשימות מצב מקבילות.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
accounts = [0, 1, 0, 1, 0, 0, 1, 1, 2, 0]
events = [0, 0, 0, 1, 0, 1, 0, 0, 1, 2]
streaks = [0, 0]
locked = [False, False]
failures = [0, 0]
successes = [0, 0]
history = []
for i in range(len(accounts)):
    account = accounts[i]
    event = events[i]
    if account < 0 or account >= len(streaks):
        status = "UNKNOWN"
    elif event != 0 and event != 1:
        status = "INVALID"
    elif locked[account]:
        status = "LOCKED"
    elif event == 1:
        streaks[account] = 0
        successes[account] += 1
        status = "SUCCESS"
    else:
        failures[account] += 1
        streaks[account] += 1
        status = "FAIL"
        if streaks[account] >= 3:
            locked[account] = True
    history.append(status)
    print(i, account, status, streaks, locked)
print("History:", history)
print("Failures:", failures)
print("Successes:", successes)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `events = [0, 0, 0, 1, 0, 1, 0, 0, 1, 2]` ב-`events = [0, 0, 0, 0, 1, 1, 0, 0, 1, 2]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. מדוע חייבים לבדוק אינדקס לפני גישה?

2. מה הקשר בין account לבין כל רשימת מצב?

3. למה כישלון של A אינו משפיע על B?

4. מה יקרה אם נשתמש במשתנה streak משותף?

5. איך מוסיפים חשבון שלישי?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו מונה חסומים לכל חשבון, מונה מזהים לא מוכרים ורשימת אינדקסי אירוע שבהם חשבון ננעל.

הדפיסו את כל הדוחות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

פעולה אחת מחזירה מצב ותוצאה;

פעולה נוספת בונה דוח.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def evaluate(streak, locked, event, limit):
    if event != 0 and event != 1:
        return [streak, locked, "INVALID"]
    if locked:
        return [streak, locked, "LOCKED"]
    if event == 1:
        return [0, False, "SUCCESS"]
    streak += 1
    return [streak, streak >= limit, "FAIL"]

def report(events, limit):
    if limit <= 0:
        return ["ERROR", []]
    streak = 0
    locked = False
    history = []
    first_lock = -1
    for i in range(len(events)):
        old_locked = locked
        result = evaluate(streak, locked, events[i], limit)
        streak = result[0]
        locked = result[1]
        history.append(result[2])
        if locked and not old_locked:
            first_lock = i
        print(i, result)
    return [history, streak, locked, first_lock]

print(evaluate(2, False, 0, 3))
print(evaluate(3, True, 1, 3))
print(report([0, 0, 1, 0, 0, 0, 1, 2], 3))
print(report([0], 0))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `return [streak, streak >= limit, "FAIL"]` ב-`return [streak, streak > limit, "FAIL"]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. למה evaluate אינה משנה מצב חיצוני?

2. איזו בדיקה חושפת את שינוי הגבול?

3. למה first_lock אינו מספר אירועים חסומים?

4. מה תוצאת רשימה ריקה?

5. למה שומרים old_locked?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הוסיפו ל-report ארבעה מונים לפי סדר SUCCESS, FAIL, LOCKED, INVALID ומספר האירועים.

הדגימו גם רשימה ריקה.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

Account אחראית למצב;

LoginLab מנתבת ומתעדת.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class Account:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.streak = 0
        self.locked = False
        self.history = []
        self.failures = 0
        self.successes = 0

    def event(self, code):
        if code != 0 and code != 1:
            status = "INVALID"
        elif self.locked:
            status = "LOCKED"
        elif code == 1:
            self.streak = 0
            self.successes += 1
            status = "SUCCESS"
        else:
            self.streak += 1
            self.failures += 1
            status = "FAIL"
            if self.streak >= self.limit:
                self.locked = True
        self.history.append(status)
        return status

    def snapshot(self):
        return [self.name, self.streak, self.locked, self.successes, self.failures]

class LoginLab:
    def __init__(self, accounts):
        self.accounts = accounts
        self.audit = []

    def process(self, index, code):
        if index < 0 or index >= len(self.accounts):
            status = "UNKNOWN"
        else:
            status = self.accounts[index].event(code)
        self.audit.append([index, code, status])
        return status

    def locked_count(self):
        count = 0
        for account in self.accounts:
            if account.locked:
                count += 1
        return count

a = Account("A", 3)
b = Account("B", 2)
lab = LoginLab([a, b])
print(lab.process(0, 0))
print(lab.process(1, 0))
print(lab.process(0, 0))
print(lab.process(1, 0))
print(lab.process(0, 1))
print(lab.process(1, 1))
print(lab.process(2, 1))
print(lab.process(0, 2))
print(lab.process(1, 0))
print(a.snapshot(), b.snapshot())
print(a.history)
print(b.history)
print(lab.audit)
print("Locked:", lab.locked_count())
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `b = Account("B", 2)` ב-`b = Account("B", 3)`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. מדוע Account לא מכירה את שאר החשבונות?

2. כיצד היומן המרכזי שונה מהיסטוריה?

3. למה snapshot מחזירה רשימה חדשה?

4. איך בודקים עצמאות של הספים?

5. מה קורה אם מעבירים אותו מופע פעמיים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הרחיבו את Account עם reset_for_demo() לאירוע מנהל מדומה בלבד, שמאפס רצף ונעילה ומוסיף RESET להיסטוריה בלי למחוק מונים.

הוסיפו פעולה ב-LoginLab שמאפשרת את אירוע המנהל הנפרד רק לאינדקס חוקי ומתעדת אותו.

אפסו B בלבד ובדקו את שני המצבים.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו שלושה חשבונות עם ספים שונים ויומן מרכזי.

תכננו אירוע מנהל מדומה ומפורש לאיפוס נעילה בלי למחוק מונים.

הציגו דוגמה לכישלונות מצטברים רבים ללא נעילה, ודוגמה לנעילה שנשמרת למרות אירוע הצלחה.

בדקו עצמאות חשבונות, קלט שגוי וסדר אירועים.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

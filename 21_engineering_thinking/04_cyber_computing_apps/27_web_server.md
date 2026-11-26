# שרת אינטרנט: איך מנהלים תור תחת עומס?

במערכת לימודית שרת מקבל בקשות עבודה בכל חלון זמן.

הוא יכול להחזיק מספר מוגבל של בקשות ממתינות ולעבד מספר מוגבל בכל חלון.

אתם צריכים לתכנן ניהול עומס, לשמור על סדר הגעה ולדווח על בקשות שלא התקבלו.

## כללי הסימולציה

אין שליחת בקשות לרשת או בדיקת שרתים אמיתיים.

כל אירוע הוא קלט מקומי מדומה.

הקיבולת מגדירה מספר ממתינים מרבי.

בחלון קולטים תחילה ואז מעבדים.

בקשה שלא נכנסה לתור נדחית.

קצב עיבוד הוא מספר מרבי, לא הבטחה.

בשלבים מתקדמים לכל בקשה מזהה ייחודי, ותור FIFO מעבד לפי סדר הקבלה.

קצב אפס משמעו שאין עיבוד בחלון.

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
print("SERVER ", end="")
print("S1", end="")
print(" | SIM")
print("Queue: ", end="")
print("4", end="")
print(" / 6")
print("Rate: ", end="")
print("2", end="")
print(" jobs")
print("Done: ", end="")
print("15", end="")
print(" total")
print("State: ", end="")
print("BUSY", end="")
print(" | OK")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("SERVER ", end="")` ב-`print("SERVER ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד למנהל העומס ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`SERVER S2 | SIM`

`Queue: 6 / 6`

`Rate: 0 jobs`

`Done: 20 total`

`State: FULL | WAIT`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

כל פעולות הקליטה והעיבוד ידועות מראש וחוקיות.

מנהלים מאזן של תור.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
waiting = 2
accepted = 0
done = 0
arrivals = 3
processed = 2
waiting += arrivals
accepted += arrivals
print("Before:", waiting)
waiting -= processed
done += processed
print(waiting, accepted, done)
arrivals = 2
processed = 1
waiting += arrivals
accepted += arrivals
print("Before:", waiting)
waiting -= processed
done += processed
print(waiting, accepted, done)
arrivals = 1
processed = 4
waiting += arrivals
accepted += arrivals
print("Before:", waiting)
waiting -= processed
done += processed
print(waiting, accepted, done)
print("Check:", 2 + accepted - done)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

החליפו את `processed = 4` ב-`processed = 3`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. מה ההבדל בין waiting ל-accepted?

2. איזו משוואת שימור מתאימה לתור?

3. למה מדפיסים גם לפני עיבוד?

4. מה משתבש אם done מתעדכן בהשמה ולא בצבירה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו ב-1 ממתין.

בשלושה חלונות נקלטות 3,2,1 בקשות ומעובדות 2,1,3.

הדפיסו לפני ואחרי כל עיבוד, סך קליטות ועיבודים ומאזן.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קולטים קיבולת, תור התחלתי ושני חלונות.

עדיין לא מגבילים מספרים.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
6
2
3
2
2
1
```

```python
capacity = int(input())
waiting = int(input())
initial = waiting
a1 = int(input())
r1 = int(input())
a2 = int(input())
r2 = int(input())
waiting += a1
free1 = capacity - waiting
print("Before 1:", waiting, free1)
waiting -= r1
print("After 1:", waiting)
waiting += a2
free2 = capacity - waiting
print("Before 2:", waiting, free2)
waiting -= r2
print("After 2:", waiting)
total_arrivals = a1 + a2
total_rate = r1 + r2
print("Totals:", total_arrivals, total_rate)
print("Check:", initial + total_arrivals - total_rate)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
4
3
3
4
2
1
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. מה אומר מקום פנוי שלילי?

2. האם תור חוקי בסוף מוכיח שלא הייתה חריגה באמצע?

3. למה rate אינו בהכרח done?

4. מה נדרש כדי לטפל בקלט שלילי?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו שלושה חלונות במקום שניים.

חשבו מצב לפני ואחרי עיבוד בכל חלון, מקום פנוי ומאזן.

בלי תנאים.

הקלט לפי סדר ההקלדה:

```text
6
1
3
2
2
1
1
3
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

תנאי הקיבולת מגביל קליטה, ותנאי העיבוד מגביל עבודה לפי התור.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
capacity = 6
waiting = 5
arrivals = 4
rate = 3
initial = waiting
if arrivals < 0 or rate < 0:
    print("INVALID")
else:
    accepted = arrivals
    if accepted > capacity - waiting:
        accepted = capacity - waiting
    rejected = arrivals - accepted
    waiting += accepted
    peak = waiting
    done = rate
    if done > waiting:
        done = waiting
    waiting -= done
    print("Accepted:", accepted)
    print("Rejected:", rejected)
    print("Done:", done)
    print("Waiting:", waiting)
    if rate == 0:
        print("OFFLINE")
    elif waiting == 0:
        print("EMPTY")
    else:
        print("BUSY")
    print("Peak:", peak)
    print("Check:", initial + accepted, waiting + done)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `rate = 3` ב-`rate = 8`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה קליטה קודמת לעיבוד?

2. מה השגיאה אם accepted תמיד שווה arrivals?

3. למה done קטן מ-rate לפעמים?

4. האם rejected נכלל במאזן התור?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו capacity חיובי, waiting חוקי, arrivals ו-rate.

יישמו את אותו מפרט, והדפיסו גם קיבולת פנויה אחרי העיבוד וסך בקשות שהגיעו כבדיקת accepted+rejected.

הקלט לפי סדר ההקלדה:

```text
6
5
4
8
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

שבעה חלונות כולל קלט שגוי.

שומרים שיא עומס, מונים וזמן שהשרת ריק.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
4
1
5
0
2
2
-1
1
3
3
1
0
0
4
```

```python
capacity = 6
waiting = 0
accepted_total = 0
rejected_total = 0
done_total = 0
offline = 0
invalid = 0
peak = 0
for i in range(7):
    arrivals = int(input())
    rate = int(input())
    if arrivals < 0 or rate < 0:
        invalid += 1
        print(i + 1, "INVALID")
    else:
        accepted = arrivals
        if accepted > capacity - waiting:
            accepted = capacity - waiting
        waiting += accepted
        rejected = arrivals - accepted
        if waiting > peak:
            peak = waiting
        done = rate
        if done > waiting:
            done = waiting
        waiting -= done
        accepted_total += accepted
        rejected_total += rejected
        done_total += done
        if rate == 0:
            offline += 1
        print(i + 1, accepted, rejected, done, waiting)
print(accepted_total, rejected_total, done_total)
print(offline, invalid, peak, waiting)
print("Check:", accepted_total - done_total)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
4
4
5
0
2
2
-1
1
3
3
1
0
0
4
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. מדוע peak נבדק לפני עיבוד?

2. האם חלון לא מקוון תמיד דוחה בקשות?

3. למה מאזן מתייחס רק לחוקיות?

4. איך בודקים אם שיא עומס היה בקיבולת?

5. מה יקרה אם מאפסים מוני צבירה בתוך הלולאה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו קיבולת ומספר חלונות, והוסיפו full_windows שסופר חלונות מלאים לפני עיבוד ו-empty_windows אחרי עיבוד.

הדפיסו את שני המונים ומאזן.

הקלט לפי סדר ההקלדה:

```text
6
7
4
1
5
0
2
2
-1
1
3
3
1
0
0
4
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

תור מזהים לפי סדר הגעה.

רשימה נשמרת והאינדקס first מציין את הבא.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
arrivals = [101, 102, 103, 104, 105, 106, 107, 108, 109]
rates = [0, 0, 0, 0, 2, 1, 0, 2, 5]
capacity = 4
queue = []
first = 0
processed = []
rejected = []
waiting_log = []
for i in range(len(arrivals)):
    if len(queue) - first < capacity:
        queue.append(arrivals[i])
    else:
        rejected.append(arrivals[i])
    before = len(queue) - first
    done = 0
    while done < rates[i] and first < len(queue):
        processed.append(queue[first])
        first += 1
        done += 1
    after = len(queue) - first
    waiting_log.append([before, after])
    print(i + 1, before, done, after)
pending = []
for j in range(len(queue)):
    if j >= first:
        pending.append(queue[j])
print(processed)
print(rejected)
print(pending)
print(waiting_log)
print("Check:", len(processed) + len(rejected) + len(pending))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `rates = [0, 0, 0, 0, 2, 1, 0, 2, 5]` ב-`rates = [0, 0, 0, 1, 2, 1, 0, 2, 5]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. למה len(queue) אינו מספר הממתינים?

2. איך first שומר סדר FIFO?

3. למה דחוי לא נוסף ל-queue?

4. מה הסיכון של זיכרון גדל ללא ניקוי?

5. איך מוכיחים שכל מזהה מופיע פעם אחת בדוח הסופי?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו רשימת windows, שבה לכל מזהה שעובד מספר החלון.

הוסיפו מונה full לפני עיבוד והדפיסו אותם.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

מפרידים קליטה, עיבוד והפקת דוח.

כל פעולה נבדקת בנפרד.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def receive(queue, first, message, capacity):
    if len(queue) - first >= capacity:
        return False
    queue.append(message)
    return True

def process(queue, first, rate, processed):
    count = 0
    while count < rate and first < len(queue):
        processed.append(queue[first])
        first += 1
        count += 1
    return first

def simulate(arrivals, rates, capacity):
    if len(arrivals) != len(rates) or capacity <= 0:
        return ["ERROR", [], [], []]
    queue = []
    rejected = []
    processed = []
    first = 0
    for i in range(len(arrivals)):
        if not receive(queue, first, arrivals[i], capacity):
            rejected.append(arrivals[i])
        first = process(queue, first, rates[i], processed)
    pending = []
    for i in range(len(queue)):
        if i >= first:
            pending.append(queue[i])
    return ["OK", processed, rejected, pending]

print(simulate([1, 2, 3, 4, 5, 6], [0, 0, 0, 1, 2, 1], 3))
print(simulate([1, 2, 3], [0, 0, 0], 2))
print(simulate([1], [], 3))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `if len(queue) - first >= capacity:` ב-`if len(queue) - first > capacity:`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. איזה גבול חושף את התנאי השגוי?

2. למה process מחזירה first?

3. האם simulate משנה arrivals?

4. מה דרוש לטיפול בקצב שלילי?

5. מה ההבדל בין דוח ERROR לתור ריק?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הרחיבו simulate כך שתדחה קצב שלילי לפני עיבוד כלשהו.

הוסיפו לדוח מונה סך בקשות ומונה נקלטו.

הדגימו גם קצב שלילי.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

מחלקת Server שומרת תור.

LoadBalancer בוחר שרת בעל פחות ממתינים בלי לחרוג מקיבולת.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class Server:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.first = 0
        self.done = []

    def pending(self):
        return len(self.queue) - self.first

    def available(self):
        return self.pending() < self.capacity

    def receive(self, message):
        if not self.available():
            return False
        self.queue.append(message)
        return True

    def process(self, rate):
        count = 0
        while count < rate and self.first < len(self.queue):
            self.done.append(self.queue[self.first])
            self.first += 1
            count += 1
        return count

    def report(self):
        return [self.pending(), len(self.done), self.capacity]

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.history = []
        self.rejected = []

    def submit(self, message):
        best = -1
        for i in range(len(self.servers)):
            server = self.servers[i]
            if server.available():
                if best == -1 or server.pending() < self.servers[best].pending():
                    best = i
        if best == -1:
            self.rejected.append(message)
        else:
            self.servers[best].receive(message)
        self.history.append([message, best])
        return best

    def reports(self):
        result = []
        for server in self.servers:
            result.append(server.report())
        return result

a = Server(2)
b = Server(3)
lab = LoadBalancer([a, b])
for message in [11, 12, 13, 14, 15, 16]:
    print(message, lab.submit(message))
print(lab.reports())
print(a.process(1), b.process(2))
print(lab.submit(17))
print(lab.submit(18))
print(lab.history)
print(lab.rejected)
print(a.done, b.done)
print(lab.reports())
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `a = Server(2)` ב-`a = Server(3)`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. למה הבחירה מבוצעת בלי לעדכן תור במהלך הסריקה?

2. מה קורה כששני השרתים באותו עומס?

3. מדוע history כוללת -1?

4. האם reports מעבדת בקשות?

5. איך נבדוק שאותה בקשה לא הוקצתה לשני שרתים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו מונה כולל של accepted ופעולה balance() המחזירה [הוקצו, נדחו, ממתינים בכל השרתים, עובדו בכל השרתים].

הדפיסו מאזן אחרי כל סבב ואחרי העיבוד.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

תכננו מערכת עם שני שרתים בעלי עומס וקיבולת שונים.

ניתוב מבוסס על מספר הממתינים, בשוויון הראשון.

אם אף שרת אינו יכול לקבל בקשה, רשמו דחייה.

הוכיחו שקריאת דוח אינה מעבדת בקשות, ושכל בקשה שהגיעה נמצאת במצב יחיד.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

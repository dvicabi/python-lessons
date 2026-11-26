# וואטסאפ מדומה: האם מספר ההתראות שווה למספר ההודעות שלא נקראו?

באפליקציית הודעות מדומה יש כמה שיחות, ולכל שיחה מספר הודעות שלא נקראו.

חלק מהשיחות מושתקות.

עליכם לבנות מנגנון שבו השתקה משפיעה על התראות בלבד, ולא על קבלת הודעות או מצב הקריאה.

## כללי הסימולציה

אין חיבור לוואטסאפ, חשבונות, אנשי קשר או הודעות אמיתיות.

משתמשים במספרים ובשמות דמה.

אירוע 1 מקבל כמות הודעות חיובית;

אירוע 2 קורא עד כמות ההודעות שלא נקראו;

אירוע 3 מחליף מצב השתקה (כמות 0 בלבד).

אירוע שגוי אינו משנה מצב.

כאשר שיחה אינה מושתקת, כל הודעה נכנסת יוצרת התראה אחת.

מונה ההתראות הוא מצטבר, גם אחרי קריאה.

השתקה אינה משנה את unread.

בכל שיחה שהתחילה ריקה: received=read_total+unread.

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
print("CHAT ", end="")
print("A", end="")
print(" | SIM")
print("Unread: ", end="")
print("5", end="")
print(" messages")
print("Received: ", end="")
print("12", end="")
print(" total")
print("Alerts: ", end="")
print("7", end="")
print(" total")
print("State: ", end="")
print("MUTED", end="")
print(" | READY")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("CHAT ", end="")` ב-`print("CHAT ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד למשתמש מסך ההודעות ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`CHAT B | SIM`

`Unread: 0 messages`

`Received: 9 total`

`Alerts: 9 total`

`State: SOUND | READ`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

מעדכנים קבלה, קריאה והתראות באירועים חוקיים ידועים.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
unread = 0
received = 0
read_total = 0
alerts = 0
unread += 4
received += 4
alerts += 4
print(unread, received, read_total, alerts)
unread -= 2
read_total += 2
print(unread, received, read_total, alerts)
unread += 3
received += 3
print(unread, received, read_total, alerts)
unread -= 4
read_total += 4
print(unread, received, read_total, alerts)
unread += 2
received += 2
alerts += 2
print(unread, received, read_total, alerts)
print("Check:", received - read_total)
print("Silent arrivals:", received - alerts)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

שנו את `unread += 3` ל-`unread += 5`.

שנו גם את `received += 3` ל-`received += 5`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. למה alerts לא גדל בכל קבלה?

2. איזו משוואה מקשרת unread,received,read_total?

3. למה קריאה אינה מפחיתה את alerts?

4. מה מייצג received-alerts?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו ריק.

קבלו 5 עם קול, קראו 2, קבלו 4 בהשתקה, קראו 3, קבלו 1 עם קול.

הדפיסו את ארבעת המונים בכל שלב ומאזן בסוף.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קולטים דוחות של שלוש שיחות ומחשבים סכומים ופערים.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
12
7
7
9
9
9
6
2
0
```

```python
a_received = int(input())
a_read = int(input())
a_alerts = int(input())
b_received = int(input())
b_read = int(input())
b_alerts = int(input())
c_received = int(input())
c_read = int(input())
c_alerts = int(input())
a_unread = a_received - a_read
b_unread = b_received - b_read
c_unread = c_received - c_read
total_received = a_received + b_received + c_received
total_read = a_read + b_read + c_read
total_alerts = a_alerts + b_alerts + c_alerts
print("A:", a_unread, a_received - a_alerts)
print("B:", b_unread, b_received - b_alerts)
print("C:", c_unread, c_received - c_alerts)
print("Total:", total_received - total_read)
print("Check:", a_unread + b_unread + c_unread)
print("Alerts:", total_alerts)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
12
5
7
9
9
9
6
2
4
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. מה משמעות unread שלילי?

2. מדוע סך alerts אינו זהה לסך unread?

3. מה ניתן להסיק על השתקה בעבר?

4. האם אפשר לדעת אם שיחה מושתקת עכשיו מהסכומים בלבד?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו שני דוחות, שכל אחד מכיל received, read_total ו-alerts.

חשבו מספר שלא נקראו, קבלות ללא התראות וסך כל אחד מהמדדים.

הדפיסו פער בין unread של שתי השיחות.

הקלט לפי סדר ההקלדה:

```text
12
7
7
9
9
9
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

מנהלים אירוע אחד עם בדיקת חוקיות והגבלת קריאה.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
unread = 5
received = 12
read_total = 7
alerts = 7
muted = True
kind = 2
amount = 8
if kind == 1 and amount > 0:
    unread += amount
    received += amount
    if not muted:
        alerts += amount
    print("RECEIVED")
elif kind == 2 and amount > 0:
    actual = amount
    if actual > unread:
        actual = unread
    unread -= actual
    read_total += actual
    print("READ", actual)
elif kind == 3 and amount == 0:
    muted = not muted
    print("MUTE", muted)
else:
    print("INVALID")
print(unread, received, read_total, alerts)
print("Check:", received - read_total)
if unread == 0:
    print("CLEAR")
else:
    print("PENDING")
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `kind = 2` ב-`kind = 1`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה actual מוגבל ל-unread?

2. מדוע muted לא מונע קבלה?

3. למה amount=0 חוקי רק לסוג 3?

4. האם קבלה בזמן השתקה משנה alerts?

5. מה נשאר קבוע באירוע INVALID?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו kind ו-amount על מצב התחלתי זהה.

יישמו אותו מפרט והדפיסו גם כמה הודעות נקראו בפועל וכמה קבלות יצרו התראה באירוע (אפס כשלא מתאים).

הקלט לפי סדר ההקלדה:

```text
2
10
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

מעבדים רצף של אירועים ומודדים שיא של הודעות לא נקראות.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
1
4
3
0
1
3
2
2
2
9
2
1
3
0
1
5
9
0
```

```python
unread = 0
received = 0
read_total = 0
alerts = 0
muted = False
invalid = 0
peak = 0
mute_changes = 0
for i in range(9):
    kind = int(input())
    amount = int(input())
    if kind == 1 and amount > 0:
        unread += amount
        received += amount
        if not muted:
            alerts += amount
        status = "RECEIVED"
    elif kind == 2 and amount > 0:
        actual = amount
        if actual > unread:
            actual = unread
        unread -= actual
        read_total += actual
        status = "READ"
    elif kind == 3 and amount == 0:
        muted = not muted
        mute_changes += 1
        status = "MUTE"
    else:
        invalid += 1
        status = "INVALID"
    if unread > peak:
        peak = unread
    print(i + 1, status, unread, alerts, muted)
print(received, read_total, unread)
print(peak, mute_changes, invalid)
print("Check:", received - read_total)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
1
4
3
0
1
3
2
2
2
9
2
1
3
1
1
5
9
0
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה peak נשמר גם אחרי קריאה?

2. מדוע השתקה פעמיים מחזירה מצב מקורי?

3. איך בודקים שקריאה מופרזת לא יצרה unread שלילי?

4. מה ההבדל בין מספר אירועי קריאה למספר הודעות שנקראו?

5. מה שגוי אם מאפסים alerts כאשר פותחים שיחה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו מספר אירועים.

הוסיפו מונה received_while_muted וסך אירועי READ שלא קראו אף הודעה.

הדפיסו את שני המונים ואת בדיקת received=alerts+received_while_muted.

הקלט לפי סדר ההקלדה:

```text
9
1
4
3
0
1
3
2
2
2
9
2
1
3
0
1
5
9
0
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

כמה שיחות עם רשימות מצב מקבילות.

מזהה שיחה משייך את האירוע למצב הנכון.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
events = [[0, 1, 5], [1, 1, 3], [0, 3, 0], [0, 1, 4], [1, 2, 2], [2, 1, 8], [0, 2, 12], [1, 3, 0], [1, 1, 2]]
unread = [0, 0]
received = [0, 0]
read_total = [0, 0]
alerts = [0, 0]
muted = [False, False]
history = []
for event in events:
    chat = event[0]
    kind = event[1]
    amount = event[2]
    if chat < 0 or chat >= len(unread):
        status = "UNKNOWN"
    elif kind == 1 and amount > 0:
        unread[chat] += amount
        received[chat] += amount
        if not muted[chat]:
            alerts[chat] += amount
        status = "RECEIVED"
    elif kind == 2 and amount > 0:
        actual = amount
        if actual > unread[chat]:
            actual = unread[chat]
        unread[chat] -= actual
        read_total[chat] += actual
        status = "READ"
    elif kind == 3 and amount == 0:
        muted[chat] = not muted[chat]
        status = "MUTE"
    else:
        status = "INVALID"
    history.append([chat, status])
    print(chat, status, unread, muted)
checks = []
for i in range(len(unread)):
    checks.append(received[i] - read_total[i] == unread[i])
print(alerts, received, read_total)
print(history)
print(checks)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `[0, 3, 0], [0, 1, 4]` ב-`[1, 3, 0], [0, 1, 4]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. למה בודקים chat לפני אינדקס?

2. למה unread ו-muted הן רשימות נפרדות?

3. מה קורה אם שני אירועים שונים שייכים לאותה שיחה?

4. איזו משוואה נבדקת לכל אינדקס?

5. איך מציגים רק שיחות שיש בהן הודעות לא נקראות?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו בסוף רשימת אינדקסים עם unread>0 ורשימת אינדקסים מושתקים.

בנו דוח מצטבר של unread ו-alerts בלי לשנות את סדר השיחות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

פעולה מחזירה צילום מצב חדש לאירוע, בלי לשנות את רשימת הקלט.

פעולה אחרת מנהלת רצף.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def update(state, kind, amount):
    unread = state[0]
    muted = state[1]
    received = state[2]
    read_total = state[3]
    alerts = state[4]
    if kind == 1 and amount > 0:
        unread += amount
        received += amount
        if not muted:
            alerts += amount
        status = "RECEIVED"
    elif kind == 2 and amount > 0:
        actual = amount
        if actual > unread:
            actual = unread
        unread -= actual
        read_total += actual
        status = "READ"
    elif kind == 3 and amount == 0:
        muted = not muted
        status = "MUTE"
    else:
        status = "INVALID"
    return [[unread, muted, received, read_total, alerts], status]

def simulate(events):
    state = [0, False, 0, 0, 0]
    history = []
    for event in events:
        result = update(state, event[0], event[1])
        state = result[0]
        history.append(result[1])
    return [state, history]

print(update([4, False, 4, 0, 4], 2, 9))
print(simulate([[1, 5], [3, 0], [1, 3], [2, 4]]))
print(simulate([[1, 5], [3, 0], [1, 3], [2, 12]]))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `if not muted:` ב-`if muted:`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. מדוע update מחזירה רשימה חדשה?

2. מה הטעות בתרחיש השני?

3. כיצד בודקים אי-שינוי של state המקורית?

4. למה simulate לא צריכה להכיר פרטי כל תנאי?

5. איזה מקרה מדגים קריאה מופרזת?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הוסיפו audit(state) שבודקת מאזן unread וטווחי מונים.

simulate תחזיר גם רשימת תוצאות audit אחרי כל אירוע.

בדקו גם מצב פגום בכוונה.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

כל שיחה אובייקט עצמאי;

Inbox מנתבת ומחשבת תג כולל.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class Chat:
    def __init__(self, name):
        self.name = name
        self.unread = 0
        self.received = 0
        self.read_total = 0
        self.alerts = 0
        self.muted = False

    def receive(self, amount):
        if amount <= 0:
            return False
        self.unread += amount
        self.received += amount
        if not self.muted:
            self.alerts += amount
        return True

    def read(self, amount):
        if amount <= 0:
            return 0
        actual = amount
        if actual > self.unread:
            actual = self.unread
        self.unread -= actual
        self.read_total += actual
        return actual

    def toggle(self):
        self.muted = not self.muted

    def report(self):
        return [self.name, self.unread, self.alerts, self.muted]

class Inbox:
    def __init__(self, chats):
        self.chats = chats
        self.history = []

    def deliver(self, index, amount):
        status = "UNKNOWN"
        if index >= 0 and index < len(self.chats):
            if self.chats[index].receive(amount):
                status = "RECEIVED"
            else:
                status = "INVALID"
        self.history.append([index, status])
        return status

    def badge(self):
        total = 0
        for chat in self.chats:
            total += chat.unread
        return total

    def reports(self):
        result = []
        for chat in self.chats:
            result.append(chat.report())
        return result

a = Chat("A")
b = Chat("B")
inbox = Inbox([a, b])
print(inbox.deliver(0, 5))
b.toggle()
print(inbox.deliver(1, 7))
print(a.read(3))
print(inbox.deliver(2, 1))
print(inbox.deliver(0, 2))
print(b.read(10))
print(inbox.reports())
print(inbox.badge(), inbox.history)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `b.toggle()` ב-`a.toggle()`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. למה Chat לא צריכה להכיר את Inbox?

2. האם badge כוללת שיחה מושתקת?

3. מה קורה אם deliver מקבלת אינדקס שלילי?

4. למה read לא משנה alerts?

5. איך שומרים עצמאות בין שתי שיחות?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו ל-Inbox visible() שמחזירה דוחות של שיחות עם unread>0 בלבד ו-muted_count() שסופרת שיחות מושתקות.

הדפיסו את התוצאות לפני ואחרי קבלת 4 הודעות ב-B.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו מערכת שיחות עם תיבת דואר נכנס מרכזית.

הוסיפו סינון שיחות שלא נקראו ודוח של מושתקות בנפרד.

תכננו מיון תצוגה לפי מספר הודעות שלא נקראו, בלי לשנות את סדר הרשימות המקוריות.

הציגו תרחיש שבו מספר ההתראות הכולל אינו שווה למספר שלא נקראו, ובדקו אירוע כפול או מזהה שיחה לא מוכר.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

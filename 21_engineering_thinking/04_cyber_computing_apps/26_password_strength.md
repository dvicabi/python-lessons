# בדיקת חוזק סיסמה: מה מדד פשוט יודע ומה הוא מפספס?

אתם מפתחים כלי לימודי להערכת מאפיינים של מחרוזות דמה.

מטרתכם לחשב מדד ולבחון מגבלותיו, בלי לשמור מידע סודי.

## כללי הסימולציה

אין להזין סיסמאות אמיתיות.

משתמשים רק בדוגמאות ASCII שבקובץ.

ניקוד דמיוני = פעמיים האורך ועוד 3 לכל קבוצת תווים קיימת: אות קטנה, גדולה, ספרה או סימן אחר.

PASS_DEMO רק באורך לפחות 8 ובשלוש קבוצות לפחות.

זה אינו מדד אמיתי לחוזק: לא נבדקים דליפות, אקראיות או דפוסים חוזרים.

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
print("CHECK ", end="")
print("01", end="")
print(" | DEMO")
print("Length: ", end="")
print("8", end="")
print(" chars")
print("Groups: ", end="")
print("3", end="")
print(" / 4")
print("Score: ", end="")
print("25", end="")
print(" points")
print("Result: ", end="")
print("PASS_DEMO", end="")
print(" | RULE")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("CHECK ", end="")` ב-`print("CHECK ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד לקורא דוח המאפיינים ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`CHECK 02 | DEMO`

`Length: 6 chars`

`Groups: 2 / 4`

`Score: 18 points`

`Result: REVIEW | RULE`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

שינוי ספירת תווים וקבוצות לאורך שלושה אירועים ידועים.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
lower = 3
upper = 2
digits = 2
symbols = 1
groups = 4
length = lower + upper + digits + symbols
score = length * 2 + groups * 3
print(length, groups, score)
lower += 2
length = lower + upper + digits + symbols
score = length * 2 + groups * 3
print(length, groups, score)
symbols -= 1
groups -= 1
length = lower + upper + digits + symbols
score = length * 2 + groups * 3
print(length, groups, score)
digits += 3
length = lower + upper + digits + symbols
score = length * 2 + groups * 3
print(length, groups, score)
print("Length part:", length * 2)
print("Group part:", groups * 3)
print("Check:", lower + upper + digits + symbols)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

החליפו את `lower += 2` ב-`lower += 4`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. מדוע הוספת אות קטנה אינה בהכרח קבוצה חדשה?

2. מדוע הסרת הסימן היחיד מורידה קבוצה?

3. מה קורה אם לא מעדכנים score?

4. האם ניקוד גבוה מוכיח חוזק אמיתי?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו ב-4 קטנות, גדולה אחת, 2 ספרות ואפס סימנים.

הוסיפו 2 סימנים, הסירו את הגדולה והוסיפו ספרה.

הציגו אורך, קבוצות וניקוד אחרי כל שלב.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קולטים ספירות ידועות, סף אורך וסף קבוצות.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
3
2
2
1
4
8
3
```

```python
lower = int(input())
upper = int(input())
digits = int(input())
symbols = int(input())
groups = int(input())
min_length = int(input())
min_groups = int(input())
length = lower + upper + digits + symbols
length_part = length * 2
group_part = groups * 3
score = length_part + group_part
length_gap = length - min_length
group_gap = groups - min_groups
print("Features:", lower, upper, digits, symbols)
print("Length:", length)
print("Score:", score)
print("Parts:", length_part, group_part)
print("Gaps:", length_gap, group_gap)
print("Check:", length_part + group_part)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
5
0
2
0
2
8
3
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. מה מציין פער שלילי?

2. למה groups שהוזן עלול להיות שגוי?

3. האם ניקוד גבוה מפצה על תנאי סף חסר?

4. איזה נתון ניתן לגזור במקום לקלוט?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו שני זוגות אורך וקבוצות ושני ספים.

חשבו ניקוד ופערים לכל זוג, וכן הפרש ניקודים.

הקלט לפי סדר ההקלדה:

```text
9
2
8
3
8
3
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

מחשבים קבוצות בפועל ובודקים שני תנאי סף נפרדים.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
lower = 4
upper = 1
digits = 3
symbols = 0
groups = 0
score = -1
if lower < 0 or upper < 0 or digits < 0 or symbols < 0:
    print("INVALID")
else:
    if lower > 0:
        groups += 1
    if upper > 0:
        groups += 1
    if digits > 0:
        groups += 1
    if symbols > 0:
        groups += 1
    length = lower + upper + digits + symbols
    score = length * 2 + groups * 3
    if length < 8:
        print("SHORT")
    if groups < 3:
        print("FEW GROUPS")
    if length >= 8 and groups >= 3:
        print("PASS_DEMO")
    else:
        print("REVIEW")
    print(length, groups)
print("Score:", score)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `upper = 1` ב-`upper = 0`.

החליפו את `digits = 3` ב-`digits = 4`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה בדיקות הקבוצות נפרדות?

2. למה שני הספים מחוברים ב-and?

3. האם ניקוד 25 תמיד מספיק?

4. מהו מקרה הגבול?

5. למה ספירה שלילית אינה מקבלת ניקוד?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו ארבע ספירות ושני ספים חיוביים.

חשבו דוח עם סיבות נפרדות והחלטה.

טפלו בספירה שלילית.

הקלט לפי סדר ההקלדה:

```text
6
1
1
0
12
3
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

מעבדים חמש דוגמאות של מאפיינים, עם מונים ושיא.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
4
1
3
0
10
0
0
0
-1
2
3
1
3
2
2
1
1
1
1
1
```

```python
count = 5
passed = 0
review = 0
invalid = 0
best = -1
best_index = 0
for i in range(count):
    lower = int(input())
    upper = int(input())
    digits = int(input())
    symbols = int(input())
    if lower < 0 or upper < 0 or digits < 0 or symbols < 0:
        invalid += 1
        print(i + 1, "INVALID")
    else:
        length = lower + upper + digits + symbols
        groups = 0
        if lower > 0:
            groups += 1
        if upper > 0:
            groups += 1
        if digits > 0:
            groups += 1
        if symbols > 0:
            groups += 1
        score = length * 2 + groups * 3
        if length >= 8 and groups >= 3:
            passed += 1
            status = "PASS_DEMO"
        else:
            review += 1
            status = "REVIEW"
        if score > best:
            best = score
            best_index = i + 1
        print(i + 1, length, groups, score, status)
print(passed, review, invalid)
print("Best score:", best_index, best)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
4
0
4
0
10
0
0
0
-1
2
3
1
3
2
2
1
1
1
1
1
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה groups מתאפס בכל דוגמה?

2. מה קורה בשוויון ניקוד?

3. האם בעל הניקוד הגבוה עבר בהכרח?

4. איך מזהים דוח ללא שום דוגמה חוקית?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו count וספים.

הוסיפו מונים לחוסר אורך וחוסר קבוצות (אפשר שניהם), ומצאו שיא רק מבין דוגמאות שעברו.

הקלט לפי סדר ההקלדה:

```text
5
8
3
4
1
3
0
10
0
0
0
-1
2
3
1
3
2
2
1
1
1
1
1
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

עובדים רק על מחרוזות דמה קבועות;

שומרים מאפיינים ולא מחרוזות בדוח.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
samples = ["aaBB11!!", "abcdefgh", "Ab12", "QQQQQQ99", "Xy9!Xy9!", ""]
scores = []
statuses = []
features = []
for sample in samples:
    lower = 0
    upper = 0
    digits = 0
    symbols = 0
    for ch in sample:
        if ch >= "a" and ch <= "z":
            lower += 1
        elif ch >= "A" and ch <= "Z":
            upper += 1
        elif ch >= "0" and ch <= "9":
            digits += 1
        else:
            symbols += 1
    groups = 0
    counts = [lower, upper, digits, symbols]
    for amount in counts:
        if amount > 0:
            groups += 1
    length = len(sample)
    score = length * 2 + groups * 3
    if length >= 8 and groups >= 3:
        status = "PASS_DEMO"
    else:
        status = "REVIEW"
    features.append([length, groups])
    scores.append(score)
    statuses.append(status)
print(features)
print(scores)
print(statuses)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `QQQQQQ99` ב-`QQQQQq99`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. למה כל תו נספר בקבוצה אחת?

2. מדוע features לא מכילה טקסט?

3. איזו דוגמה חוזרת על תבנית ובכל זאת עוברת?

4. מה קורה במחרוזת ריקה?

5. למה מגבלת ASCII חשובה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו לכל דוגמה רשימת חסרים לא שליליים: כמה תווים וכמה קבוצות חסרים לסף.

הדפיסו גם אינדקסים שעברו, בלי להדפיס את המחרוזות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

מפרידים איסוף מאפיינים, הערכה והפקת דוח.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def features(sample):
    counts = [0, 0, 0, 0]
    for ch in sample:
        if ch >= "a" and ch <= "z":
            counts[0] += 1
        elif ch >= "A" and ch <= "Z":
            counts[1] += 1
        elif ch >= "0" and ch <= "9":
            counts[2] += 1
        else:
            counts[3] += 1
    groups = 0
    for value in counts:
        if value > 0:
            groups += 1
    return [len(sample), groups]

def evaluate(data, min_length, min_groups):
    length = data[0]
    groups = data[1]
    score = length * 2 + groups * 3
    if length >= min_length and groups >= min_groups:
        return [score, "PASS_DEMO"]
    return [score, "REVIEW"]

def compare(samples, min_length, min_groups):
    result = []
    for sample in samples:
        data = features(sample)
        result.append([data, evaluate(data, min_length, min_groups)])
    return result

samples = ["Abcdef12", "abcdefgh", "AAAA1111", "xyXY00!!"]
print(compare(samples, 8, 3))
print(compare(samples, 12, 2))
print(evaluate([8, 3], 8, 3))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `if length >= min_length and groups >= min_groups:` ב-`if length > min_length and groups >= min_groups:`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. למה evaluate אינה צריכה מחרוזת?

2. איזה גבול חושף את התקלה?

3. למה compare מחזירה רשימה חדשה?

4. איך משווים שתי מדיניות בלי לשמור סודות?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הרחיבו evaluate עם שני חסרים לא שליליים.

compare תחזיר [דוחות, מספר שעברו].

הדגימו שתי מדיניות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

מדיניות נפרדת ממפקח דוחות;

שני אובייקטים בודקים אותן דוגמאות.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class Policy:
    def __init__(self, min_length, min_groups):
        self.min_length = min_length
        self.min_groups = min_groups

    def assess(self, length, groups):
        score = length * 2 + groups * 3
        if length >= self.min_length and groups >= self.min_groups:
            return [score, "PASS_DEMO"]
        return [score, "REVIEW"]

class Inspector:
    def __init__(self, policy):
        self.policy = policy
        self.reports = []
        self.passed = 0

    def inspect(self, sample):
        counts = [0, 0, 0, 0]
        for ch in sample:
            if ch >= "a" and ch <= "z":
                counts[0] += 1
            elif ch >= "A" and ch <= "Z":
                counts[1] += 1
            elif ch >= "0" and ch <= "9":
                counts[2] += 1
            else:
                counts[3] += 1
        groups = 0
        for value in counts:
            if value > 0:
                groups += 1
        length = len(sample)
        result = self.policy.assess(length, groups)
        report = [length, groups, result[0], result[1]]
        self.reports.append(report)
        if result[1] == "PASS_DEMO":
            self.passed += 1
        return report

    def summary(self):
        return [len(self.reports), self.passed, len(self.reports) - self.passed]

    def gap(self, report):
        length_gap = self.policy.min_length - report[0]
        groups_gap = self.policy.min_groups - report[1]
        if length_gap < 0:
            length_gap = 0
        if groups_gap < 0:
            groups_gap = 0
        return [length_gap, groups_gap]

a = Inspector(Policy(8, 3))
b = Inspector(Policy(12, 2))
samples = ["Abcdef12", "abcdefgh", "ABCDEFGHIJ12", "xyXY00!!"]
for sample in samples:
    first = a.inspect(sample)
    second = b.inspect(sample)
    print(first, a.gap(first))
    print(second, b.gap(second))
print(a.summary(), b.summary())
print(a.reports)
print(b.reports)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `b = Inspector(Policy(12, 2))` ב-`b = Inspector(Policy(8, 2))`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. מדוע sample לא נשמר באובייקט?

2. למה Policy נפרדת?

3. מה אם שני מפקחים חולקים מדיניות אחת שמשתנה?

4. האם שינוי סף צריך לשנות דוחות ישנים?

5. איזה מבחן מוכיח שאין טקסט בדוח?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו לכל Inspector רשימת reasons עם SHORT ו/או FEW_GROUPS לכל דוגמה.

הוסיפו פעולה שמחזירה ספים.

הדפיסו שני הדוחות והסיבות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו שתי מדיניות דמה בעלות ספים שונים.

הציגו דוח מאפיינים בלבד והשוו החלטות על אותן דוגמאות.

מצאו שתי מחרוזות בעלות ניקוד זהה אך דפוס שונה, והסבירו מדוע אי אפשר להסיק אבטחה מהניקוד.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

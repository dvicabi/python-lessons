# מערכת לזיהוי ספאם: מתי התראה שגויה מזיקה יותר מהחמצה?

מערכת הודעות מדומה מקבלת מאפיינים מספריים של הודעות.

היא מסמנת הודעות לבדיקה לפי ניקוד.

המטרה אינה לחסום אוטומטית, אלא לבנות דוח ולהבין את מחיר הטעויות.

אתם בודקים את ההחלטות מול תוויות שהוגדרו מראש.

## כללי הסימולציה

אין הודעות אמיתיות, קישורים אמיתיים או חיבור לתיבת דואר.

מאפיינים דמיוניים: flags בין 0 ל-3, links בין 0 ל-3, unknown שווה 0 או 1.

ניקוד = 3*flags+2*links+4*unknown.

ניקוד 8 ומעלה מסומן REVIEW, אחרת NORMAL.

זוהי החלטת דמה בלבד, ולא קביעה שהודעה מסוכנת.

תווית אמת מדומה 1 = ספאם, 0 = הודעה תקינה.

נגדיר TP כספאם שסומן, FP כהודעה תקינה שסומנה, FN כספאם שלא סומן ו-TN כתקינה שלא סומנה.

נתון לא חוקי אינו נכלל בארבעת המונים.

בהשוואת מדיניות נגדיר מחיר דמיוני 2 ל-FP ו-5 ל-FN.

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
print("MESSAGE ", end="")
print("12", end="")
print(" | DEMO")
print("Flags: ", end="")
print("2", end="")
print(" / 3")
print("Links: ", end="")
print("1", end="")
print(" / 3")
print("Score: ", end="")
print("8", end="")
print(" points")
print("Decision: ", end="")
print("REVIEW", end="")
print(" | CHECK")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("MESSAGE ", end="")` ב-`print("MESSAGE ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד לבודק הדוח ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`MESSAGE 13 | DEMO`

`Flags: 1 / 3`

`Links: 0 / 3`

`Score: 3 points`

`Decision: NORMAL | READY`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

מחשבים ניקוד אחרי שינוי מאפיינים.

אין החלטת סף עדיין.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
flags = 1
links = 0
unknown = 1
flag_part = flags * 3
link_part = links * 2
unknown_part = unknown * 4
score = flag_part + link_part + unknown_part
first = score
print(flags, links, unknown, score)
flags += 1
links += 2
flag_part = flags * 3
link_part = links * 2
score = flag_part + link_part + unknown_part
print(flags, links, unknown, score)
unknown = 0
unknown_part = unknown * 4
score = flag_part + link_part + unknown_part
print(flags, links, unknown, score)
links -= 1
link_part = links * 2
score = flag_part + link_part + unknown_part
print(flags, links, unknown, score)
print("Parts:", flag_part, link_part, unknown_part)
print("Change:", score - first)
print("Check:", flag_part + link_part + unknown_part)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

החליפו את `links += 2` ב-`links += 3`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. למה unknown_part מתעדכן אחרי unknown?

2. איזה מאפיין משנה ניקוד בצורה הגדולה ביותר ליחידה?

3. מה משתבש אם מחברים שוב score לרכיבים?

4. האם ניקוד גבוה מוכיח ספאם?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו flags=0,links=1,unknown=0.

הוסיפו 2 ל-flags, שנו unknown ל-1, הוסיפו קישור ואז הסירו flag אחד.

הציגו את שלושת הרכיבים והניקוד אחרי כל שינוי ואת ההפרש מההתחלה.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קולטים מאפיינים של שני פריטים וסף.

מדווחים פערים, ללא סיווג.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
2
1
0
1
0
1
8
```

```python
flags_a = int(input())
links_a = int(input())
unknown_a = int(input())
flags_b = int(input())
links_b = int(input())
unknown_b = int(input())
threshold = int(input())
score_a = flags_a * 3 + links_a * 2 + unknown_a * 4
score_b = flags_b * 3 + links_b * 2 + unknown_b * 4
gap_a = score_a - threshold
gap_b = score_b - threshold
print("A:", score_a, gap_a)
print("B:", score_b, gap_b)
print("Score gap:", score_a - score_b)
print("Flag gap:", flags_a - flags_b)
print("Link gap:", links_a - links_b)
print("Unknown gap:", unknown_a - unknown_b)
print("Total:", score_a + score_b)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
2
2
1
1
0
1
10
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. מה אומר gap=0?

2. למה פער שלילי אינו נתון שגוי?

3. האם שני פריטים עם ניקוד זהה בהכרח בעלי אותם מאפיינים?

4. איזה נתון חסר כדי למדוד טעויות סיווג?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו שלושה פריטים (שלושה מאפיינים לכל אחד) וסף.

חשבו ניקודים ופערי סף, וסך ניקוד וממוצע שלם.

הניחו קלט חוקי.

הקלט לפי סדר ההקלדה:

```text
2
1
0
1
0
1
3
2
1
8
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

בודקים חוקיות, החלטה ותווית אמת.

החלטת REVIEW היא רק סימון לבדיקה.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
flags = 2
links = 1
unknown = 0
truth = 0
threshold = 8
score = -1
if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
    outcome = "INVALID"
else:
    score = flags * 3 + links * 2 + unknown * 4
    predicted = score >= threshold
    if predicted:
        print("REVIEW")
        if truth == 1:
            outcome = "TP"
        else:
            outcome = "FP"
    else:
        print("NORMAL")
        if truth == 1:
            outcome = "FN"
        else:
            outcome = "TN"
print(score, outcome)
cost = 0
if outcome == "FP":
    cost = 2
elif outcome == "FN":
    cost = 5
print("Cost:", cost)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `threshold = 8` ב-`threshold = 9`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה predicted נפרד מ-truth?

2. איזו טעות נוצרת בתרחיש הראשון?

3. למה הסף כולל שוויון?

4. מה ההבדל בין FP ל-FN?

5. למה INVALID לא נספר כאחת מארבע התוצאות?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו flags,links,unknown,truth,threshold.

יישמו אותו סיווג, והדפיסו בנוסף האם ההחלטה תאמה לתווית (True/False) רק בנתון חוקי.

הקלט לפי סדר ההקלדה:

```text
1
0
1
1
8
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

מעריכים שמונה פריטים ומחשבים מוני איכות ועלות טעויות.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
2
1
0
0
1
0
1
1
3
2
1
1
0
1
0
0
1
2
0
1
2
2
0
0
4
0
0
1
0
0
0
0
```

```python
threshold = 8
tp = 0
fp = 0
fn = 0
tn = 0
invalid = 0
for i in range(8):
    flags = int(input())
    links = int(input())
    unknown = int(input())
    truth = int(input())
    if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
        invalid += 1
        print(i + 1, "INVALID")
    else:
        score = flags * 3 + links * 2 + unknown * 4
        if score >= threshold:
            if truth == 1:
                tp += 1
                outcome = "TP"
            else:
                fp += 1
                outcome = "FP"
        elif truth == 1:
            fn += 1
            outcome = "FN"
        else:
            tn += 1
            outcome = "TN"
        print(i + 1, score, outcome)
valid = tp + fp + fn + tn
cost = fp * 2 + fn * 5
print(tp, fp, fn, tn)
print("Valid:", valid, "Invalid:", invalid)
print("Cost:", cost)
if valid > 0:
    correct = (tp + tn) * 100
    print("Correct percent:", correct // valid)
else:
    print("NO DATA")
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
2
1
0
1
1
0
1
0
3
2
1
1
0
1
0
0
1
2
0
1
2
2
0
0
4
0
0
1
0
0
0
0
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה valid לא כולל invalid?

2. מדוע accuracy גבוהה אינה בהכרח עלות נמוכה?

3. איזו משוואה בודקת את מספר האירועים?

4. מה קורה כשאין פריט חוקי?

5. כיצד החלטה של סף גבוה יותר עשויה לשנות FP ו-FN?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו count,threshold,מחיר FP ומחיר FN.

חשבו מונים, עלות ואחוז הצלחה.

הדפיסו גם מספר הודעות שסומנו (TP+FP) ומספר הודעות ספאם אמיתי בדמה (TP+FN).

הקלט לפי סדר ההקלדה:

```text
8
8
2
5
2
1
0
0
1
0
1
1
3
2
1
1
0
1
0
0
1
2
0
1
2
2
0
0
4
0
0
1
0
0
0
0
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

אותה רשימת נתוני דמה נבדקת בשלושה ספים.

מעקב אחר תוצאות כל מדיניות.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
messages = [[2, 1, 0, 0], [1, 0, 1, 1], [3, 2, 1, 1], [0, 1, 0, 0], [1, 2, 0, 1], [2, 2, 0, 0], [4, 0, 0, 1], [0, 0, 0, 0]]
thresholds = [6, 8, 10]
reports = []
best = -1
best_cost = -1
for threshold in thresholds:
    counts = [0, 0, 0, 0]
    invalid = 0
    for row in messages:
        flags = row[0]
        links = row[1]
        unknown = row[2]
        truth = row[3]
        if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
            invalid += 1
        else:
            score = flags * 3 + links * 2 + unknown * 4
            if score >= threshold:
                if truth == 1:
                    counts[0] += 1
                else:
                    counts[1] += 1
            elif truth == 1:
                counts[2] += 1
            else:
                counts[3] += 1
    cost = counts[1] * 2 + counts[2] * 5
    reports.append([threshold, counts, invalid, cost])
    if best == -1 or cost < best_cost:
        best = threshold
        best_cost = cost
    print(threshold, counts, invalid, cost)
print("Best:", best, best_cost)
print(reports)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `cost = counts[1] * 2 + counts[2] * 5` ב-`cost = counts[1] * 5 + counts[2] * 2`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. מדוע counts מתאפסת לכל סף?

2. איך כל אינדקס במונה מתייחס לתוצאה?

3. כיצד מחיר שונה משנה את ההחלטה?

4. למה best נשמר מחוץ ללולאת הספים?

5. מה קורה בשוויון עלות?

6. מדוע יש לבדוק סף נבחר על אוסף נוסף?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

הוסיפו לכל דוח שני מדדים: אחוז הצלחה שלם ומספר שגיאות כולל.

בחרו בנפרד את הסף עם העלות הנמוכה ואת הסף עם מספר הטעויות הנמוך;

בשוויון הראשון.

הדפיסו את שני הנבחרים.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

פעולה אחת מחשבת תוצאה לרשומה;

פעולה שנייה מחשבת דוח;

פעולה שלישית בוחרת סף.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def classify(row, threshold):
    flags = row[0]
    links = row[1]
    unknown = row[2]
    truth = row[3]
    if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
        return -1
    score = flags * 3 + links * 2 + unknown * 4
    if score >= threshold:
        if truth == 1:
            return 0
        return 1
    if truth == 1:
        return 2
    return 3

def evaluate(messages, threshold, fp_cost, fn_cost):
    counts = [0, 0, 0, 0]
    invalid = 0
    for row in messages:
        index = classify(row, threshold)
        if index == -1:
            invalid += 1
        else:
            counts[index] += 1
    cost = counts[1] * fp_cost + counts[2] * fn_cost
    return [threshold, counts, invalid, cost]

def choose(messages, thresholds, fp_cost, fn_cost):
    best = []
    reports = []
    for threshold in thresholds:
        result = evaluate(messages, threshold, fp_cost, fn_cost)
        reports.append(result)
        if len(best) == 0 or result[3] < best[3]:
            best = result
    return [best, reports]

messages = [[2, 1, 0, 0], [1, 0, 1, 1], [3, 2, 1, 1], [0, 1, 0, 0], [1, 2, 0, 1], [2, 2, 0, 0]]
print(classify([2, 1, 0, 0], 8))
print(choose(messages, [6, 8, 10], 2, 5))
print(choose(messages, [6, 8, 10], 5, 2))
print(choose(messages, [], 2, 5))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `if score >= threshold:` ב-`if score > threshold:`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. למה classify מחזירה אינדקס ולא שם?

2. מה הסכנה של counts[-1] אם לא בודקים INVALID?

3. איזה ערך גבול חושף שינוי >?

4. למה evaluate אינה בוחרת סף?

5. האם choose משנה messages?

6. מה חוזר כשאין ספים?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הוסיפו ל-evaluate מדד אחוז הצלחה או -1 כאשר אין נתונים תקינים.

כתבו compare_on_new שמקבלת אוסף בדיקה נפרד ואת תוצאת choose ומחזירה דוח של הסף שנבחר או [].

הדגימו אוסף נוסף.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

מחלקת ReviewPolicy אחראית להחלטה.

Experiment בודקת מדיניות על רשומות ומרכזת תוצאות.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class ReviewPolicy:
    def __init__(self, threshold):
        self.threshold = threshold

    def outcome(self, row):
        flags = row[0]
        links = row[1]
        unknown = row[2]
        truth = row[3]
        if flags < 0 or flags > 3 or links < 0 or links > 3 or (unknown != 0 and unknown != 1) or (truth != 0 and truth != 1):
            return -1
        score = flags * 3 + links * 2 + unknown * 4
        if score >= self.threshold:
            if truth == 1:
                return 0
            return 1
        if truth == 1:
            return 2
        return 3

class Experiment:
    def __init__(self, policies, fp_cost, fn_cost):
        self.policies = policies
        self.fp_cost = fp_cost
        self.fn_cost = fn_cost
        self.history = []

    def report(self, policy, messages):
        counts = [0, 0, 0, 0]
        invalid = 0
        for row in messages:
            result = policy.outcome(row)
            if result == -1:
                invalid += 1
            else:
                counts[result] += 1
        cost = counts[1] * self.fp_cost + counts[2] * self.fn_cost
        return [policy.threshold, counts, invalid, cost]

    def run(self, messages):
        reports = []
        best = -1
        for i in range(len(self.policies)):
            result = self.report(self.policies[i], messages)
            reports.append(result)
            if best == -1 or result[3] < reports[best][3]:
                best = i
        self.history.append(reports)
        return [best, reports]

    def review_selected(self, messages, index):
        if index < 0 or index >= len(self.policies):
            return []
        return self.report(self.policies[index], messages)

a = ReviewPolicy(6)
b = ReviewPolicy(8)
c = ReviewPolicy(10)
lab = Experiment([a, b, c], 2, 5)
other = Experiment([a, b, c], 5, 2)
messages = [[2, 1, 0, 0], [1, 0, 1, 1], [3, 2, 1, 1], [0, 1, 0, 0], [1, 2, 0, 1], [2, 2, 0, 0]]
test = [[0, 1, 1, 0], [2, 0, 0, 1], [3, 1, 0, 1]]
first = lab.run(messages)
second = other.run(messages)
print(first)
print(second)
print(lab.review_selected(test, first[0]))
print(other.review_selected(test, second[0]))
print(lab.review_selected(test, -1))
print(len(lab.history), len(other.history))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `lab = Experiment([a, b, c], 2, 5)` ב-`lab = Experiment([a, b, c], 8, 1)`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. למה שתי מעבדות יכולות לשתף אובייקטי מדיניות בלי לשתף history?

2. מה המשמעות של שני מחירי טעויות שונים?

3. למה review_selected לא בוחרת מחדש סף?

4. מה קורה אם משתמשים באותה רשימה לבחירה ולבדיקה?

5. איך מוודאים שכל דוח מונה אירועים בדיוק פעם אחת?

6. האם תוצאה טובה במשחק מוכיחה סינון מוצלח של דואר אמיתי?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו ל-Experiment audit(report,count) הבודקת מאזן אירועים, ו-summary() המחזירה מספר הרצות ומספר הדוחות שהופקו.

הדפיסו בדיקת מאזן לכל דוח בשתי המעבדות ולדוח בדיקה נפרד.

ודאו ש-review_selected לא הגדילה את history.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו מערכת המשווה ספים 6,8,10 על אותו אוסף רשומות דמה.

הציגו ארבעה מוני תוצאות לכל סף ועלות טעויות.

בחרו סף לפי עלות נמוכה, בשוויון הסף הראשון.

בדקו בנפרד אוסף נוסף שלא שימש לבחירה והסבירו מדוע הצלחה על אוסף אחד לא מוכיחה הצלחה כללית.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

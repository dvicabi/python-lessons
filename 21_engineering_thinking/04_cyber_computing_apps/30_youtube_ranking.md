# יוטיוב מדומה: האם הסרטון עם הכי הרבה צפיות צריך להופיע ראשון?

אתם מתכננים מסך דירוג סרטונים במערכת מדומה.

סרטון פופולרי לא בהכרח מקבל יחס מעורבות גבוה.

נבנה מדד לימודי ונשווה מדיניות דירוג שונות.

## כללי הסימולציה

הנתונים בדויים לחלוטין ואין שימוש בשירות יוטיוב או באלגוריתם האמיתי שלו.

מדידה חוקית: צפיות לא שליליות, לייקים ותגובות בין 0 למספר הצפיות.

סרטון עם פחות מ-10 צפיות אינו מועמד לדירוג.

ניקוד לימודי הוא (4*likes+6*comments)*100//views עבור מועמד חוקי.

דירוג: ניקוד גבוה קודם, בשוויון יותר צפיות, בשוויון מלא המועמד הראשון.

ערך -1 מסמן לא מדורג, לא ניקוד אמיתי.

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
print("VIDEO ", end="")
print("17", end="")
print(" | DEMO")
print("Views: ", end="")
print("100", end="")
print(" count")
print("Likes: ", end="")
print("20", end="")
print(" count")
print("Score: ", end="")
print("110", end="")
print(" points")
print("Rank: ", end="")
print("2", end="")
print(" | READY")
```

כתבו את הפלט המדויק כולל רווחים, תווים וירידות שורה.

סמנו איזו פקודה מסיימת כל שורת תצוגה.

### 1.ב תרחיש שני

החליפו את `print("VIDEO ", end="")` ב-`print("VIDEO ", end=" | ")`.

כתבו שוב את הפלט המדויק.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 1.ג ביקורת וחשיבה הנדסית

1. כמה שורות מתקבלות בפועל?

2. אילו פקודות מחברות בין שדות בלי להוסיף רווח או שורה חדשה?

3. מה בדיוק משתנה בתרחיש השני, והאם המספרים עצמם משתנים?

4. איזה פרט בתצוגה חשוב במיוחד לקורא מסך הדירוג ומדוע?

הציעו תצוגה אחרת לאותו המידע.

נמקו איזו ברורה יותר למפעיל.

### 1.ד כתיבה עצמאית

בנו את המסך הבא בדיוק כפי שהוא מופיע, באמצעות print ו-end בלבד.

`VIDEO 18 | DEMO`

`Views: 50 count`

`Likes: 15 count`

`Score: 180 points`

`Rank: 1 | READY`

השתמשו ב-15 פקודות לפחות.

אין להדפיס שורה שלמה באמצעות פקודה אחת.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו שכל התווים מופיעים במקומם ושאף שדה אינו מחובר בטעות לשדה אחר.

---

## רמה 2

**משתנים ופעולות חשבון | קושי: בסיסית+**

עוקבים אחרי מצטברים ועדכוני מדד לאחר שלושה סבבי פעילות.

השמה, פעולות חשבון ו-print.

ללא קלט ותנאים.

### 2.א קריאת קוד

```python
views = 20
likes = 4
comments = 1
weighted = likes * 4 + comments * 6
scaled = weighted * 100
score = scaled // views
print(views, likes, comments, score)
views += 10
likes += 3
comments += 2
weighted = likes * 4 + comments * 6
scaled = weighted * 100
score = scaled // views
print(views, likes, comments, score)
views += 20
likes += 1
comments += 1
weighted = likes * 4 + comments * 6
scaled = weighted * 100
score = scaled // views
print(views, likes, comments, score)
print("Weighted:", weighted)
print("Check:", likes * 4 + comments * 6)
print("Unscaled:", scaled)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 2.ב תרחיש שני

החליפו את `views += 20` ב-`views += 40`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 2.ג ביקורת וחשיבה הנדסית

1. למה score יכול לרדת אף ש-likes ו-comments גדלים?

2. למה צריך לחשב weighted ו-scaled מחדש?

3. מה המשמעות של חילוק שלם?

4. מה ההבדל בין כמות פעילות לבין יחס פעילות?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 2.ד כתיבה עצמאית

התחילו ב-30 צפיות, 6 לייקים ו-2 תגובות.

הוסיפו בסבב אחד 10,2,1 ובסבב שני 20,5,1.

הציגו ניקוד בכל שלב והפרש בין הניקוד הסופי להתחלה.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 3

**קלט והמרה | קושי: בסיסית+**

קולטים שני סרטונים בעלי צפיות חיוביות ומחשבים השוואה, ללא בחירה.

מותר input ו-int נוסף על החומר הקודם.

אין תנאים או לולאות.

### 3.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
100
20
5
50
15
5
```

```python
views_a = int(input())
likes_a = int(input())
comments_a = int(input())
views_b = int(input())
likes_b = int(input())
comments_b = int(input())
weight_a = likes_a * 4 + comments_a * 6
weight_b = likes_b * 4 + comments_b * 6
scaled_a = weight_a * 100
scaled_b = weight_b * 100
score_a = scaled_a // views_a
score_b = scaled_b // views_b
print("A:", views_a, weight_a, score_a)
print("B:", views_b, weight_b, score_b)
print("Views gap:", views_a - views_b)
print("Activity gap:", weight_a - weight_b)
print("Score gap:", score_a - score_b)
print("Combined views:", views_a + views_b)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 3.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
100
20
5
50
5
1
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 3.ג ביקורת וחשיבה הנדסית

1. איך סרטון עם פחות צפיות יכול לקבל יותר ניקוד?

2. למה לא מחלקים כאשר views=0?

3. האם משקל תגובות גבוה יותר הוא אמת מוחלטת?

4. למה השוואת score שונה מהשוואת weight?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 3.ד כתיבה עצמאית

קלטו נתוני שלושה סרטונים עם צפיות חיוביות.

חשבו לכל אחד משקל וניקוד, וסך צפיות.

הדפיסו הפרש בין A ל-C לפי צפיות ולפי ניקוד.

הקלט לפי סדר ההקלדה:

```text
100
20
5
50
15
5
20
3
2
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 4

**תנאים | קושי: בינונית**

סיווג מדידה ולאחר מכן החלטה בין שני סרטונים.

מותר if, elif, else וביטויים לוגיים.

אין לולאות.

### 4.א קריאת קוד

```python
views_a = 20
likes_a = 5
comments_a = 0
views_b = 40
likes_b = 10
comments_b = 0
score_a = -1
score_b = -1
if views_a >= 10 and likes_a >= 0 and likes_a <= views_a and comments_a >= 0 and comments_a <= views_a:
    scaled = (likes_a * 4 + comments_a * 6) * 100
    score_a = scaled // views_a
if views_b >= 10 and likes_b >= 0 and likes_b <= views_b and comments_b >= 0 and comments_b <= views_b:
    scaled = (likes_b * 4 + comments_b * 6) * 100
    score_b = scaled // views_b
best = "NONE"
if score_a >= 0:
    best = "A"
if score_b >= 0:
    if best == "NONE" or score_b > score_a or (score_b == score_a and views_b > views_a):
        best = "B"
print(score_a, score_b)
print("Selected:", best)
if best == "A":
    print(views_a, score_a)
elif best == "B":
    print(views_b, score_b)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 4.ב תרחיש שני

החליפו את `comments_a = 0` ב-`comments_a = 1`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 4.ג ביקורת וחשיבה הנדסית

1. למה שתי בדיקות חוקיות נפרדות?

2. למה בתרחיש הראשון B מנצח בשוויון?

3. מה קורה אם לשניהם ניקוד -1?

4. מהי בדיקת גבול עבור צפיות 9 ו-10?

5. למה אין לחשב ניקוד לסרטון בעל 0 צפיות?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 4.ד כתיבה עצמאית

קלטו שני סרטונים (צפיות, לייקים, תגובות לכל אחד).

יישמו בחירה לפי ניקוד ולאחריו צפיות.

הציגו גם סיבת אי-דירוג לכל סרטון: INVALID עבור נתון מחוץ לטווח, SMALL אם חוקי אך פחות מ-10 צפיות.

הקלט לפי סדר ההקלדה:

```text
9
4
1
30
5
2
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 5

**לולאות | קושי: בינונית+**

סורקים סדרת סרטונים ומנהלים שני דירוגים: חשיפה וניקוד.

מותר להשתמש ב-for, while ו-range.

סיום לולאה באמצעות התנאי ומשתנה מצב.

אין רשימות או פעולות שהגדרתם.

### 5.א קריאת קוד

הקלט לפי סדר ההקלדה:

```text
100
20
5
50
15
5
9
4
1
20
30
0
40
10
0
20
5
0
```

```python
best_score = -1
best_score_views = -1
best_score_index = 0
most_views = -1
most_views_index = 0
valid = 0
small = 0
invalid = 0
for i in range(6):
    views = int(input())
    likes = int(input())
    comments = int(input())
    if views < 0 or likes < 0 or likes > views or comments < 0 or comments > views:
        invalid += 1
        print(i + 1, "INVALID")
    elif views < 10:
        small += 1
        print(i + 1, "SMALL")
    else:
        valid += 1
        scaled = (likes * 4 + comments * 6) * 100
        score = scaled // views
        if score > best_score or (score == best_score and views > best_score_views):
            best_score = score
            best_score_views = views
            best_score_index = i + 1
        if views > most_views:
            most_views = views
            most_views_index = i + 1
        print(i + 1, views, score)
print("Score rank:", best_score_index, best_score)
print("Views rank:", most_views_index, most_views)
print(valid, small, invalid)
print("Check:", valid + small + invalid)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 5.ב תרחיש שני

הקלט לפי סדר ההקלדה:

```text
100
20
5
50
1
1
9
4
1
20
30
0
40
10
0
20
5
0
```

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 5.ג ביקורת וחשיבה הנדסית

1. למה שומרים שני אינדקסים נפרדים?

2. למה best_score_views דרוש בשוויון?

3. איך ייתכן שמנצח צפיות שונה ממנצח ניקוד?

4. מה מציין אינדקס 0 בסוף?

5. מה הסיכון אם משנים > ל->= בחשיפה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 5.ד כתיבה עצמאית

קלטו count ו-min_views חיובי.

הוסיפו סכום ניקודי מועמדים וממוצע שלם (או NO DATA).

שמרו שני דירוגים והציגו אם הם בחרו באותו אינדקס.

הקלט לפי סדר ההקלדה:

```text
6
20
100
20
5
50
15
5
9
4
1
20
30
0
40
10
0
20
5
0
```

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 6

**רשימות בלבד | קושי: מתקדמת**

רשימת רשימות מחזיקה מדידות.

מדרגים שלושה מועמדים בלי לשנות את המקור.

מותר רשימות, אינדקסים, len ו-append.

אין מילונים, סטים או טאפל.

אין def.

### 6.א קריאת קוד

```python
videos = [[100, 20, 5], [50, 15, 5], [9, 4, 1], [20, 30, 0], [40, 10, 0], [20, 5, 0], [40, 10, 0]]
scores = []
eligible = []
for i in range(len(videos)):
    views = videos[i][0]
    likes = videos[i][1]
    comments = videos[i][2]
    score = -1
    if views >= 10 and likes >= 0 and likes <= views and comments >= 0 and comments <= views:
        scaled = (likes * 4 + comments * 6) * 100
        score = scaled // views
        eligible.append(i)
    scores.append(score)
ranking = []
for turn in range(3):
    best = -1
    for i in eligible:
        if i not in ranking:
            if best == -1:
                best = i
            elif scores[i] > scores[best]:
                best = i
            elif scores[i] == scores[best] and videos[i][0] > videos[best][0]:
                best = i
    if best != -1:
        ranking.append(best)
        print(turn + 1, best, scores[best], videos[best][0])
print(scores)
print(eligible)
print(ranking)
print(videos)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 6.ב תרחיש שני

החליפו את `[50, 15, 5]` ב-`[50, 1, 1]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 6.ג ביקורת וחשיבה הנדסית

1. למה ranking מכילה אינדקסים ולא רשומות?

2. למה צריך i not in ranking?

3. איזה סרטונים נפסלו ומדוע?

4. מה קורה כאשר רק שני מועמדים חוקיים?

5. למה עדיף לא לשנות videos עצמה?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 6.ד כתיבה עצמאית

חשבו דירוג נוסף לפי צפיות בלבד, בשוויון לפי סדר המקור.

הדפיסו שלושה אינדקסים לכל מדיניות ורשימת אינדקסים שמופיעים בשתיהן.

אין למיין באמצעות ספריות.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 7

**פעולות (פונקציות) | קושי: מתקדמת+**

מפרידים הערכת נתון, השוואת מועמדים והפקת דירוג.

מותר def, פרמטרים ו-return.

החזירו ערך יחיד או רשימה בלבד.

### 7.א קריאת קוד

```python
def evaluate(video):
    views = video[0]
    likes = video[1]
    comments = video[2]
    if views < 0 or likes < 0 or likes > views or comments < 0 or comments > views:
        return ["INVALID", -1]
    if views < 10:
        return ["SMALL", -1]
    scaled = (likes * 4 + comments * 6) * 100
    return ["OK", scaled // views]

def better(videos, scores, i, best):
    if best == -1:
        return True
    if scores[i] != scores[best]:
        return scores[i] > scores[best]
    return videos[i][0] > videos[best][0]

def rank(videos, count):
    scores = []
    for video in videos:
        result = evaluate(video)
        scores.append(result[1])
    ranking = []
    for turn in range(count):
        best = -1
        for i in range(len(videos)):
            if scores[i] >= 0 and i not in ranking:
                if better(videos, scores, i, best):
                    best = i
        if best != -1:
            ranking.append(best)
    return [scores, ranking]

videos = [[20, 5, 0], [40, 10, 0], [40, 10, 0], [0, 0, 0], [50, 15, 5]]
print(evaluate([10, 0, 0]))
print(evaluate([9, 0, 0]))
print(rank(videos, 5))
print(rank(videos, 2))
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 7.ב תרחיש שני

החליפו את `return videos[i][0] > videos[best][0]` ב-`return videos[i][0] >= videos[best][0]`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 7.ג ביקורת וחשיבה הנדסית

1. איך אפשר לבדוק evaluate באופן עצמאי?

2. מה התקלה בשוויון מלא בתרחיש השני?

3. למה better אינה משנה ranking?

4. מה קורה ב-count גדול מהכמות החוקית?

5. מה ההבדל בין רשימת scores לדירוג?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 7.ד כתיבה עצמאית

הוסיפו mode ל-rank ול-better: 1 ניקוד ואחריו צפיות, 2 צפיות ואחריהן ניקוד.

mode אחר מחזיר [].

בדקו שתי מדיניות ו-mode שגוי.

בשוויון מלא ראשון.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## רמה 8

**מחלקות | קושי: אתגר**

Video מחזיקה נתונים;

Ranking מחזיקה מדיניות וקטלוג.

כל קריאה מפיקה דירוג חדש.

מותר class, __init__, self ופעולות.

רשימות בלבד כמבנה נתונים.

### 8.א קריאת קוד

```python
class Video:
    def __init__(self, name, views, likes, comments):
        self.name = name
        self.views = views
        self.likes = likes
        self.comments = comments

    def score(self):
        if self.views < 10 or self.likes < 0 or self.likes > self.views or self.comments < 0 or self.comments > self.views:
            return -1
        scaled = (self.likes * 4 + self.comments * 6) * 100
        return scaled // self.views

    def add(self, views, likes, comments):
        if views < 0 or likes < 0 or comments < 0:
            return False
        next_views = self.views + views
        next_likes = self.likes + likes
        next_comments = self.comments + comments
        if next_likes > next_views or next_comments > next_views:
            return False
        self.views = next_views
        self.likes = next_likes
        self.comments = next_comments
        return True

    def report(self):
        return [self.name, self.views, self.score()]

class Ranking:
    def __init__(self, videos):
        self.videos = videos
        self.history = []

    def better(self, i, best):
        if best == -1:
            return True
        a = self.videos[i]
        b = self.videos[best]
        if a.score() != b.score():
            return a.score() > b.score()
        return a.views > b.views

    def top(self, count):
        indexes = []
        for turn in range(count):
            best = -1
            for i in range(len(self.videos)):
                if self.videos[i].score() >= 0 and i not in indexes:
                    if self.better(i, best):
                        best = i
            if best != -1:
                indexes.append(best)
        self.history.append(indexes)
        return indexes

    def reports(self):
        result = []
        for video in self.videos:
            result.append(video.report())
        return result

a = Video("A", 100, 20, 5)
b = Video("B", 50, 15, 5)
c = Video("C", 9, 4, 1)
d = Video("D", 40, 10, 0)
catalog = Ranking([a, b, c, d])
print(catalog.reports())
print(catalog.top(3))
print(a.add(20, 12, 4))
print(b.add(50, 0, 0))
print(c.add(1, 1, 0))
print(d.add(0, 100, 0))
print(catalog.reports())
print(catalog.top(3))
print(catalog.history)
```

הכינו טבלת מעקב מלאה בעצמכם.

כתבו את הפלט המדויק.

בחרו שני רגעים שבהם שינוי משתנה משפיע על החלטה או חישוב מאוחר יותר.

הסבירו את הקשר.

### 8.ב תרחיש שני

החליפו את `print(b.add(50, 0, 0))` ב-`print(b.add(50, 20, 5))`.

הכינו טבלת מעקב חדשה.

באיזו נקודה נוצר ההבדל הראשון מהתרחיש המקורי, אם נוצר?

הסבירו גם מה נשאר ללא שינוי.

### 8.ג ביקורת וחשיבה הנדסית

1. מדוע add בודקת מצב מועמד לפני עדכון?

2. למה c יכולה להיכנס לדירוג לאחר עדכון?

3. האם score משנה נתונים?

4. למה history מחזיקה דירוג נפרד לכל קריאה?

5. איזה חישוב חוזר מיותר מתבצע ב-better?

6. כיצד תבדקו ששינוי דירוג לא שינה את videos?

הציעו מקרה קצה נוסף שמתאים לחומר ברמה זו.

חזו את התוצאה לפני הרצה.

### 8.ד כתיבה עצמאית

הוסיפו מצב דירוג לבנאי (1 ניקוד, 2 צפיות ואחריהן ניקוד).

צרו שני אובייקטי Ranking שחולקים את אותם סרטונים אך שומרים היסטוריות נפרדות.

הדפיסו דירוגים לפני ואחרי העדכונים.

כתבו קודם את סדר הפעולות במילים, ורק אחר כך כתבו קוד בעצמכם.

בדקו את התוצאה והציעו קלט או נתון נוסף שמאתגר את הפתרון.

הסבירו מדוע בחרתם בו.

---

## אתגר הנדסי מסכם

בנו קטלוג מדומה עם שתי מדיניות: צפיות או ניקוד המעורבות, ואפשרו למשתמש לבחור סדר.

אל תשנו את הרשימה המקורית.

השוו מקרים שבהם מדיניות משנה סדר או יוצרת שוויון.

בדקו שאף סרטון פסול אינו מופיע בדירוג.

הגדירו דרישות, תכננו לפני כתיבה, בנו פתרון בעזרת החומר שכבר נלמד.

הציגו לפחות ארבעה מקרי בדיקה: רגיל, גבול, תקלה ושינוי סדר אירועים.

הכינו טבלת מעקב לקוד שלכם.

השוו בין שתי חלופות ותארו יתרון וחיסרון של כל אחת.

## הגשה

- קוד Python עובד.
- טבלאות מעקב עצמאיות ופלטים.
- תשובות מנומקות ובדיקות.
- הסבר קצר על ההחלטה ההנדסית שלכם.

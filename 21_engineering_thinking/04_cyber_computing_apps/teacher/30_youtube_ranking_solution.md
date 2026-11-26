# פתרונות למורה: יוטיוב מדומה: האם הסרטון עם הכי הרבה צפיות צריך להופיע ראשון?

[חזרה למשימת התלמיד](../30_youtube_ranking.md)

הפתרונות הם דרך אפשרית אחת.

יש לבדוק גם נימוק, תקינות ואופן החשיבה.

## רמה 1: print ו-end

### א. פלט התרחיש הראשון

```text
VIDEO 17 | DEMO
Views: 100 count
Likes: 20 count
Score: 110 points
Rank: 2 | READY
```

### ב. פלט התרחיש השני

```text
VIDEO  | 17 | DEMO
Views: 100 count
Likes: 20 count
Score: 110 points
Rank: 2 | READY
```

### ג. תשובות והערות לדיון

מספר השורות הוא 5.

כל שורת תצוגה בנויה ממספר פקודות;

end="" מונע ירידת שורה.

השינוי מוסיף מפריד רק במקום שנבחר ואינו משנה את הנתונים.

יש להעדיף תוויות חד-משמעיות, להציג את יחידות המדידה ולהפריד בין ערך לבין סטטוס.

### ד. פתרון אפשרי

```python
print("VIDEO ", end="")
print("18", end="")
print(" | DEMO")
print("Views: ", end="")
print("50", end="")
print(" count")
print("Likes: ", end="")
print("15", end="")
print(" count")
print("Score: ", end="")
print("180", end="")
print(" points")
print("Rank: ", end="")
print("1", end="")
print(" | READY")
```

פלט:

```text
VIDEO 18 | DEMO
Views: 50 count
Likes: 15 count
Score: 180 points
Rank: 1 | READY
```

---

## רמה 2: משתנים ופעולות חשבון

### א. פלט התרחיש הראשון

```text
20 4 1 110
30 7 3 153
50 8 4 112
Weighted: 56
Check: 56
Unscaled: 5600
```

### ב. פלט התרחיש השני

```text
20 4 1 110
30 7 3 153
70 8 4 80
Weighted: 56
Check: 56
Unscaled: 5600
```

### ג. תשובות והערות לדיון

צפיות במכנה עשויות לגדול מהר יותר.

מדדים נגזרים מהנתונים החדשים.

חילוק שלם מעגל מטה.

כמות מתארת היקף, יחס מנרמל לפי צפיות.

### ד. פתרון אפשרי

```python
views = 30
likes = 6
comments = 2
weighted = likes * 4 + comments * 6
scaled = weighted * 100
first_score = scaled // views
print(views, likes, comments, first_score)
views += 10
likes += 2
comments += 1
weighted = likes * 4 + comments * 6
scaled = weighted * 100
score = scaled // views
print(views, likes, comments, score)
views += 20
likes += 5
comments += 1
weighted = likes * 4 + comments * 6
scaled = weighted * 100
score = scaled // views
print(views, likes, comments, score)
print(score - first_score)
```

פלט:

```text
30 6 2 120
40 8 3 125
60 13 4 126
6
```

---

## רמה 3: קלט והמרה

### א. פלט התרחיש הראשון

```text
A: 100 110 110
B: 50 90 180
Views gap: 50
Activity gap: 20
Score gap: -70
Combined views: 150
```

### ב. פלט התרחיש השני

```text
A: 100 110 110
B: 50 26 52
Views gap: 50
Activity gap: 84
Score gap: 58
Combined views: 150
```

### ג. תשובות והערות לדיון

מדד מנורמל לפי צפיות.

חלוקה באפס אינה מוגדרת.

המשקלים הם החלטת תכנון דמיונית.

weight אינו מביא בחשבון חשיפה.

### ד. פתרון אפשרי

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

```python
views_a = int(input())
likes_a = int(input())
comments_a = int(input())
views_b = int(input())
likes_b = int(input())
comments_b = int(input())
views_c = int(input())
likes_c = int(input())
comments_c = int(input())
scaled_a = (likes_a * 4 + comments_a * 6) * 100
scaled_b = (likes_b * 4 + comments_b * 6) * 100
scaled_c = (likes_c * 4 + comments_c * 6) * 100
score_a = scaled_a // views_a
score_b = scaled_b // views_b
score_c = scaled_c // views_c
print(views_a, score_a)
print(views_b, score_b)
print(views_c, score_c)
print("Total:", views_a + views_b + views_c)
print(views_a - views_c, score_a - score_c)
```

פלט:

```text
100 110
50 180
20 120
Total: 170
80 -10
```

---

## רמה 4: תנאים

### א. פלט התרחיש הראשון

```text
100 100
Selected: B
40 100
```

### ב. פלט התרחיש השני

```text
130 100
Selected: A
20 130
```

### ג. תשובות והערות לדיון

כל סרטון נבדק עצמאית.

ניקוד שווה וב-B יותר צפיות.

NONE כשאין חוקי.

9 לא מועמד, 10 מועמד אם שאר הנתונים תקינים.

חלוקה באפס אסורה.

### ד. פתרון אפשרי

הקלט לפי סדר ההקלדה:

```text
9
4
1
30
5
2
```

```python
views_a = int(input())
likes_a = int(input())
comments_a = int(input())
views_b = int(input())
likes_b = int(input())
comments_b = int(input())
score_a = -1
score_b = -1
if views_a < 0 or likes_a < 0 or likes_a > views_a or comments_a < 0 or comments_a > views_a:
    print("A INVALID")
elif views_a < 10:
    print("A SMALL")
else:
    scaled = (likes_a * 4 + comments_a * 6) * 100
    score_a = scaled // views_a
if views_b < 0 or likes_b < 0 or likes_b > views_b or comments_b < 0 or comments_b > views_b:
    print("B INVALID")
elif views_b < 10:
    print("B SMALL")
else:
    scaled = (likes_b * 4 + comments_b * 6) * 100
    score_b = scaled // views_b
best = "NONE"
if score_a >= 0:
    best = "A"
if score_b >= 0:
    if best == "NONE" or score_b > score_a or (score_b == score_a and views_b > views_a):
        best = "B"
print(score_a, score_b, best)
```

פלט:

```text
A SMALL
-1 106 B
```

---

## רמה 5: לולאות

### א. פלט התרחיש הראשון

```text
1 100 110
2 50 180
3 SMALL
4 INVALID
5 40 100
6 20 100
Score rank: 2 180
Views rank: 1 100
4 1 1
Check: 6
```

### ב. פלט התרחיש השני

```text
1 100 110
2 50 20
3 SMALL
4 INVALID
5 40 100
6 20 100
Score rank: 1 110
Views rank: 1 100
4 1 1
Check: 6
```

### ג. תשובות והערות לדיון

הקריטריונים שונים.

שדה צפיות שובר שוויון.

חשיפה רבה אינה מבטיחה יחס מעורבות גבוה.

0 מציין שאין מועמד.

>= מעדכן למועמד המאוחר בשוויון.

### ד. פתרון אפשרי

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

```python
count = int(input())
min_views = int(input())
total_score = 0
best_score = -1
best_score_views = -1
best_score_index = 0
most_views = -1
most_views_index = 0
valid = 0
small = 0
invalid = 0
for i in range(count):
    views = int(input())
    likes = int(input())
    comments = int(input())
    if views < 0 or likes < 0 or likes > views or comments < 0 or comments > views:
        invalid += 1
        print(i + 1, "INVALID")
    elif views < min_views:
        small += 1
        print(i + 1, "SMALL")
    else:
        valid += 1
        scaled = (likes * 4 + comments * 6) * 100
        score = scaled // views
        total_score += score
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
if valid > 0:
    print(total_score // valid)
    print(best_score_index == most_views_index)
else:
    print("NO DATA")
```

פלט:

```text
1 100 110
2 50 180
3 SMALL
4 INVALID
5 40 100
6 20 100
Score rank: 2 180
Views rank: 1 100
4 1 1
Check: 6
122
False
```

---

## רמה 6: רשימות בלבד

### א. פלט התרחיש הראשון

```text
1 1 180 50
2 0 110 100
3 4 100 40
[110, 180, -1, -1, 100, 100, 100]
[0, 1, 4, 5, 6]
[1, 0, 4]
[[100, 20, 5], [50, 15, 5], [9, 4, 1], [20, 30, 0], [40, 10, 0], [20, 5, 0], [40, 10, 0]]
```

### ב. פלט התרחיש השני

```text
1 0 110 100
2 4 100 40
3 6 100 40
[110, 20, -1, -1, 100, 100, 100]
[0, 1, 4, 5, 6]
[0, 4, 6]
[[100, 20, 5], [50, 1, 1], [9, 4, 1], [20, 30, 0], [40, 10, 0], [20, 5, 0], [40, 10, 0]]
```

### ג. תשובות והערות לדיון

אינדקס מקשר לרשומה.

התנאי מונע כפילות.

סרטון קטן או נתון פסול אינו מועמד.

יתווספו רק שניים.

שמירה על המקור מאפשרת להפיק דירוג אחר.

### ד. פתרון אפשרי

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
views_rank = []
for turn in range(3):
    best = -1
    for i in eligible:
        if i not in views_rank:
            if best == -1 or videos[i][0] > videos[best][0]:
                best = i
    if best != -1:
        views_rank.append(best)
common = []
for i in ranking:
    if i in views_rank:
        common.append(i)
print(scores)
print(eligible)
print(ranking)
print(views_rank)
print(common)
```

פלט:

```text
1 1 180 50
2 0 110 100
3 4 100 40
[110, 180, -1, -1, 100, 100, 100]
[0, 1, 4, 5, 6]
[1, 0, 4]
[0, 1, 4]
[1, 0, 4]
```

---

## רמה 7: פעולות (פונקציות)

### א. פלט התרחיש הראשון

```text
['OK', 0]
['SMALL', -1]
[[100, 100, 100, -1, 180], [4, 1, 2, 0]]
[[100, 100, 100, -1, 180], [4, 1]]
```

### ב. פלט התרחיש השני

```text
['OK', 0]
['SMALL', -1]
[[100, 100, 100, -1, 180], [4, 2, 1, 0]]
[[100, 100, 100, -1, 180], [4, 2]]
```

### ג. תשובות והערות לדיון

בדקו גבולות 9,10, נתון לא חוקי ואפס מעורבות.

>= בוחר מאוחר בשוויון.

better משווה בלבד.

לא יתווספו מועמדים כפולים.

scores שומרת התאמה לכל קלט, ranking רק נבחרים.

### ד. פתרון אפשרי

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

def better(videos, scores, i, best, mode):
    if best == -1:
        return True
    if mode == 2 and videos[i][0] != videos[best][0]:
        return videos[i][0] > videos[best][0]
    if scores[i] != scores[best]:
        return scores[i] > scores[best]
    return videos[i][0] > videos[best][0]

def rank(videos, count, mode):
    if mode != 1 and mode != 2:
        return []
    scores = []
    for video in videos:
        result = evaluate(video)
        scores.append(result[1])
    ranking = []
    for turn in range(count):
        best = -1
        for i in range(len(videos)):
            if scores[i] >= 0 and i not in ranking:
                if better(videos, scores, i, best, mode):
                    best = i
        if best != -1:
            ranking.append(best)
    return [scores, ranking]

videos = [[20, 5, 0], [40, 10, 0], [40, 10, 0], [0, 0, 0], [50, 15, 5]]
print(evaluate([10, 0, 0]))
print(evaluate([9, 0, 0]))
print(rank(videos, 5, 1))
print(rank(videos, 5, 2))
print(rank(videos, 2, 0))
```

פלט:

```text
['OK', 0]
['SMALL', -1]
[[100, 100, 100, -1, 180], [4, 1, 2, 0]]
[[100, 100, 100, -1, 180], [4, 1, 2, 0]]
[]
```

---

## רמה 8: מחלקות

### א. פלט התרחיש הראשון

```text
[['A', 100, 110], ['B', 50, 180], ['C', 9, -1], ['D', 40, 100]]
[1, 0, 3]
True
True
True
False
[['A', 120, 151], ['B', 100, 90], ['C', 10, 260], ['D', 40, 100]]
[2, 0, 3]
[[1, 0, 3], [2, 0, 3]]
```

### ב. פלט התרחיש השני

```text
[['A', 100, 110], ['B', 50, 180], ['C', 9, -1], ['D', 40, 100]]
[1, 0, 3]
True
True
True
False
[['A', 120, 151], ['B', 100, 200], ['C', 10, 260], ['D', 40, 100]]
[2, 1, 0]
[[1, 0, 3], [2, 1, 0]]
```

### ג. תשובות והערות לדיון

עדכון אסור לא יפגע במצב.

c מגיעה ל-10.

score שאילתה בלבד.

כל top בונה רשימה חדשה.

חישוב score יכול להישמר פעם אחת בסריקה.

השוו סדר ושדות לפני ואחרי top.

### ד. פתרון אפשרי

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
    def __init__(self, videos, mode):
        self.mode = mode
        self.videos = videos
        self.history = []

    def better(self, i, best):
        if best == -1:
            return True
        a = self.videos[i]
        b = self.videos[best]
        if self.mode == 2 and a.views != b.views:
            return a.views > b.views
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
catalog = Ranking([a, b, c, d], 1)
views_catalog = Ranking([a, b, c, d], 2)
print(views_catalog.top(3))
print(catalog.reports())
print(catalog.top(3))
print(a.add(20, 12, 4))
print(b.add(50, 0, 0))
print(c.add(1, 1, 0))
print(d.add(0, 100, 0))
print(catalog.reports())
print(catalog.top(3))
print(catalog.history)
print(views_catalog.top(3))
print(views_catalog.history)
```

פלט:

```text
[0, 1, 3]
[['A', 100, 110], ['B', 50, 180], ['C', 9, -1], ['D', 40, 100]]
[1, 0, 3]
True
True
True
False
[['A', 120, 151], ['B', 100, 90], ['C', 10, 260], ['D', 40, 100]]
[2, 0, 3]
[[1, 0, 3], [2, 0, 3]]
[0, 1, 3]
[[0, 1, 3], [0, 1, 3]]
```

---

## אתגר הנדסי מסכם

בדקו שהפתרון מיישם את הדרישות שהוגדרו, שכל מקרי הקצה נבדקו ושהתלמידים מסוגלים להצדיק את החלופה שבחרו.

אין תשובה יחידה לאתגר הפתוח.

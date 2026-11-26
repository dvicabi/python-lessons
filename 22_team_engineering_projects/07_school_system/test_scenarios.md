# תרחישי קבלה

העתיקו את נתוני ההתחלה מקובץ `starter/scenario.py`. בכל ניסוי הפעילו את הקוד מחדש, עם השינויים בלבד שמפורטים להלן.

## תרחיש 1: שיבוץ ראשון

חלון 0, מורה 1, חדר 2.

השתמשו בנתוני ההתחלה ללא שינוי.

**תוצאה נדרשת בסוף:**

```text
result = "OK"
slot = 0
teacher = 1
room = 2
teacher_after = [[False, True, True], [False, False, True], [True, True, True]]
room_after = [[True, True, True], [False, True, True], [False, True, False]]
group_after = [[False, True, True], [True, False, True]]
tquota_after = [2, 0, 3]
gquota_after = [1, 2]
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 2: מורים ללא מכסה

אין מורה פייתון בעל מכסה.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
teacher_quota = [0, 0, 3]
```

**תוצאה נדרשת בסוף:**

```text
result = "TEACHER"
slot = -1
teacher = -1
room = -1
teacher_after = [[False, True, True], [True, False, True], [True, True, True]]
room_after = [[True, True, True], [False, True, True], [True, True, False]]
group_after = [[True, True, True], [True, False, True]]
tquota_after = [0, 0, 3]
gquota_after = [2, 2]
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 3: חדרים קטנים

אין חדר ל-28 תלמידים.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
room_caps = [24, 25, 27]
```

**תוצאה נדרשת בסוף:**

```text
result = "ROOM"
slot = -1
teacher = -1
room = -1
teacher_after = [[False, True, True], [True, False, True], [True, True, True]]
room_after = [[True, True, True], [False, True, True], [True, True, False]]
group_after = [[True, True, True], [True, False, True]]
tquota_after = [2, 1, 3]
gquota_after = [2, 2]
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 4: אין זמן משותף

הקבוצה לא פנויה בכל חלון.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
group_free = [[False, False, False], [True, False, True]]
```

**תוצאה נדרשת בסוף:**

```text
result = "TIME"
slot = -1
teacher = -1
room = -1
teacher_after = [[False, True, True], [True, False, True], [True, True, True]]
room_after = [[True, True, True], [False, True, True], [True, True, False]]
group_after = [[False, False, False], [True, False, True]]
tquota_after = [2, 1, 3]
gquota_after = [2, 2]
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 5: מכסת קבוצה נגמרה

נמצא שילוב, אך השיעור אינו מאושר.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
group_quota = [0, 2]
```

**תוצאה נדרשת בסוף:**

```text
result = "QUOTA"
slot = 0
teacher = 1
room = 2
teacher_after = [[False, True, True], [True, False, True], [True, True, True]]
room_after = [[True, True, True], [False, True, True], [True, True, False]]
group_after = [[True, True, True], [True, False, True]]
tquota_after = [2, 1, 3]
gquota_after = [0, 2]
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

## ניסוי עצמאי של הצוות

המציאו שני תרחישים נוספים: אחד בגבול החוקי, ואחד שבו רכיב בודד נכשל למרות שכל הרכיבים האחרים חוקיים.

כתבו מראש את התוצאה הרצויה. הכינו טבלת מעקב לפי בחירתכם. הוכיחו שלא בוצע שינוי חלקי במצב כאשר העסקה או הבקשה נדחתה.

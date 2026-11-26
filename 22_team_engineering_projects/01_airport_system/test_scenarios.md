# תרחישי קבלה

העתיקו את נתוני ההתחלה מקובץ `starter/scenario.py`. בכל ניסוי הפעילו את הקוד מחדש, עם השינויים בלבד שמפורטים להלן.

## תרחיש 1: אישור מלא

כל התנאים מתקיימים; שער 1 הוא הקטן הפנוי המתאים.

השתמשו בנתוני ההתחלה ללא שינוי.

**תוצאה נדרשת בסוף:**

```text
flight_ok = True
passenger_ready = True
bag_ready = True
gate_index = 1
ready_at = 29
slot_ok = True
result = "OK"
gate_busy_after = [False, True, True]
departed_id = 41
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 2: נוסע חסר

אין לבצע שיבוץ גם אם קיים שער פנוי.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
checked = 4
```

**תוצאה נדרשת בסוף:**

```text
flight_ok = True
passenger_ready = False
bag_ready = False
gate_index = -1
ready_at = -1
slot_ok = False
result = "PASSENGERS"
gate_busy_after = [False, False, True]
departed_id = -1
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 3: מטען שגוי

תיק אחד חורג מהטווח.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
bag_weights = [10, 21]
```

**תוצאה נדרשת בסוף:**

```text
flight_ok = True
passenger_ready = True
bag_ready = False
gate_index = -1
ready_at = -1
slot_ok = False
result = "BAGS"
gate_busy_after = [False, False, True]
departed_id = -1
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 4: אין שער

כל השערים תפוסים.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
gate_busy = [True, True, True]
```

**תוצאה נדרשת בסוף:**

```text
flight_ok = True
passenger_ready = True
bag_ready = True
gate_index = -1
ready_at = -1
slot_ok = False
result = "GATE"
gate_busy_after = [True, True, True]
departed_id = -1
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 5: איחור

שער מועמד נמצא אך לא מעודכן.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
now = 24
```

**תוצאה נדרשת בסוף:**

```text
flight_ok = True
passenger_ready = True
bag_ready = True
gate_index = 1
ready_at = 33
slot_ok = False
result = "TIME"
gate_busy_after = [False, False, True]
departed_id = -1
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

---

## תרחיש 6: טיסה לא קיימת

אין לנסות לקרוא אינדקס -1.

החליפו את הערכים הבאים בנתוני ההתחלה:

```python
requested = 999
```

**תוצאה נדרשת בסוף:**

```text
flight_ok = False
passenger_ready = False
bag_ready = False
gate_index = -1
ready_at = -1
slot_ok = False
result = "FLIGHT"
gate_busy_after = [False, False, True]
departed_id = -1
```

לפני ההרצה, כל בעל רכיב כותב מה הוא צופה שיקרה אצלו ומה הוא אמור להעביר לרכיב אחר. לאחר הרצה תעדו את הפלט בפועל ואת הסיבה לכל הבדל.

## ניסוי עצמאי של הצוות

המציאו שני תרחישים נוספים: אחד בגבול החוקי, ואחד שבו רכיב בודד נכשל למרות שכל הרכיבים האחרים חוקיים.

כתבו מראש את התוצאה הרצויה. הכינו טבלת מעקב לפי בחירתכם. הוכיחו שלא בוצע שינוי חלקי במצב כאשר העסקה או הבקשה נדחתה.

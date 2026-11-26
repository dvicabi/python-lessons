# פתרון והערות למורה: מדפסת תלת ממד: האם אפשר לסיים את ההדפסה?

[חזרה למשימת התלמיד](../03_3d_printer.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 PRINTED 4 9 1
2 PRINTED 6 3 2
3 PAUSED 5 3 2
FINAL 3 2
```

קלט שני:

```text
1 PRINTED 4 9 1
2 PRINTED 7 2 2
3 PAUSED 2 2 2
FINAL 2 2
```

### טבלאות מעקב מלאות

**קלט ראשון**

| שכבה | layer | cost | חומר לפני | החלטה | חומר אחרי | printed |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 4 | 13 | PRINTED | 9 | 1 |
| 2 | 5 | 6 | 9 | PRINTED | 3 | 2 |
| 3 | 4 | 5 | 3 | PAUSED | 3 | 2 |
| 4 | 6 | — | — | לא נקראה | — | — |
| 5 | 2 | — | — | לא נקראה | — | — |

**קלט שני**

| שכבה | layer | cost | חומר לפני | החלטה | חומר אחרי | printed |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 4 | 13 | PRINTED | 9 | 1 |
| 2 | 6 | 7 | 9 | PRINTED | 2 | 2 |
| 3 | 1 | 2 | 2 | PAUSED | 2 | 2 |

**מעקב שורה-אחר-שורה לדוגמה:** שכבה 3 בקלט הראשון: cost=5; הביטוי 3-5<2 מתקיים; remaining נשאר 3 ו-printed נשאר 2; break מדלג על שאר השכבות.

## תשובות והנחיות לדיון

FINAL הוא סיכום, גם אחרי עצירה. בקלט השני לאחר שכבה 2 נשארות בדיוק 2 יחידות, ולכן מותר לבצע אותה; <= היה עוצר מוקדם. הפחתה לפני בדיקה משבשת מלאי ללא הדפסה. שכבה בעובי 11 עולה 12 ומשאירה 1: התנאי השגוי מאשר אותה. בדיקה מראש מונעת התחלה של משימה שלא תושלם; בדיקה לכל שכבה מאפשרת עצירה והמשך מתוכננים.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def plan_print(layers, stock, reserve):
    if stock < 0 or reserve < 0 or stock < reserve:
        return 0, stock, "ERROR", 0
    printed = 0
    remaining = stock
    for index, layer in enumerate(layers, 1):
        if layer <= 0:
            return printed, remaining, "ERROR", index
        cost = layer + 1
        if remaining - cost < reserve:
            return printed, remaining, "PAUSED", index
        remaining -= cost
        printed += 1
    return printed, remaining, "DONE", None
```

## בדיקות אוטומטיות

```python
assert plan_print([3,5,4,6,2], 13, 2) == (2, 3, "PAUSED", 3)
assert plan_print([3,6], 13, 2) == (2, 2, "DONE", None)
assert plan_print([2,0,3], 10, 2) == (1, 7, "ERROR", 2)
assert plan_print([], 2, 2) == (0, 2, "DONE", None)
assert plan_print([1], 1, 2) == (0, 1, "ERROR", 0)
assert plan_print([1,2], 7, 2) == (2, 2, "DONE", None)
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

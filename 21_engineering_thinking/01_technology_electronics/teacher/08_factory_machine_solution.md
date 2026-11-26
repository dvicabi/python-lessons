# פתרון והערות למורה: מכונה במפעל: מתי חריגה בודדת הופכת לתקלה?

[חזרה למשימת התלמיד](../08_factory_machine.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 48 0 NORMAL
2 75 1 WARNING
3 78 2 WARNING
4 65 0 NORMAL
5 82 1 WARNING
6 83 2 WARNING
7 84 3 STOPPED
8 60 3 STOPPED
```

קלט שני:

```text
1 75 1 WARNING
2 74 0 NORMAL
3 75 1 WARNING
4 74 0 NORMAL
5 75 1 WARNING
6 75 2 WARNING
7 74 0 NORMAL
8 75 1 WARNING
```

### טבלאות מעקב מלאות

**קלט ראשון**

| מדידה | value | חריגה? | streak | stopped | status |
| --- | --- | --- | --- | --- | --- |
| 1 | 48 | לא | 0 | False | NORMAL |
| 2 | 75 | כן | 1 | False | WARNING |
| 3 | 78 | כן | 2 | False | WARNING |
| 4 | 65 | לא | 0 | False | NORMAL |
| 5 | 82 | כן | 1 | False | WARNING |
| 6 | 83 | כן | 2 | False | WARNING |
| 7 | 84 | כן | 3 | True | STOPPED |
| 8 | 60 | לא, לא נבדק לאחר עצירה | 3 | True | STOPPED |

**קלט שני**

| מדידה | value | חריגה? | streak | stopped | status |
| --- | --- | --- | --- | --- | --- |
| 1 | 75 | כן | 1 | False | WARNING |
| 2 | 74 | לא | 0 | False | NORMAL |
| 3 | 75 | כן | 1 | False | WARNING |
| 4 | 74 | לא | 0 | False | NORMAL |
| 5 | 75 | כן | 1 | False | WARNING |
| 6 | 75 | כן | 2 | False | WARNING |
| 7 | 74 | לא | 0 | False | NORMAL |
| 8 | 75 | כן | 1 | False | WARNING |

**מעקב שורה-אחר-שורה לדוגמה:** מדידה 7 בקלט הראשון: streak מ-2 ל-3, stopped מ-False ל-True, status=STOPPED. במדידה 8 תנאי not stopped נכשל, ולכן הרצף אינו מתאפס.

## תשובות והנחיות לדיון

העצירה בקלט הראשון במדידה 7, והתקלה נשמרת. בקלט השני חמש חריגות (1,3,5,6,8) והרצף הארוך ביותר 2. בלי איפוס הרצף עצירה שגויה במדידה 5. אם מונה מגיע כבר ל-4, ==3 לא יזהה את המצב ו-`>=3` כן. דוגמת חלון: חריג, חריג, תקין, חריג, חריג יגרום לחלון לעצור אך לא לרצף; שלוש חריגות רצופות בתחילת קלט עוצרות ברצף לפני שיש חלון מלא של חמש.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def monitor(readings):
    streak = 0
    for index, (load, vibration) in enumerate(readings, 1):
        if not (0 <= load <= 100 and 0 <= vibration <= 20):
            return "STOPPED", streak, index, "INVALID"
        if load >= 90 or vibration >= 12:
            return "STOPPED", streak, index, "CRITICAL"
        if load >= 75 or vibration >= 8:
            streak += 1
        else:
            streak = 0
        if streak >= 3:
            return "STOPPED", streak, index, "STREAK"
    return ("WARNING" if streak else "NORMAL"), streak, None, None
```

## בדיקות אוטומטיות

```python
assert monitor([(75,2),(70,8),(76,1),(0,0)]) == ("STOPPED",3,3,"STREAK")
assert monitor([(75,2),(70,2),(75,2)]) == ("WARNING",1,None,None)
assert monitor([(75,1),(90,0),(0,0)]) == ("STOPPED",1,2,"CRITICAL")
assert monitor([(80,1),(-1,12)]) == ("STOPPED",1,2,"INVALID")
assert monitor([]) == ("NORMAL",0,None,None)
assert monitor([(74,7),(74,8),(74,7)]) == ("NORMAL",0,None,None)
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

# פתרון והערות למורה: דוד חשמל מדומה: איך מונעים הפעלה וכיבוי ללא הפסקה?

[חזרה למשימת התלמיד](../07_water_heater.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 42 True False 1
2 45 True False 2
3 49 True False 3
4 50 False False 3
5 48 False False 3
6 44 True False 4
7 43 True False 5
8 99 False True 5
9 42 False True 5
```

קלט שני:

```text
1 47 False False 0
2 45 True False 1
3 46 True False 2
4 49 True False 3
5 50 False False 3
6 46 False False 3
7 45 True False 4
```

### טבלאות מעקב מלאות

**קלט ראשון**

| מדידה | value | heater לפני | heater אחרי | fault | active |
| --- | --- | --- | --- | --- | --- |
| 1 | 42 | False | True | False | 1 |
| 2 | 45 | True | True | False | 2 |
| 3 | 49 | True | True | False | 3 |
| 4 | 50 | True | False | False | 3 |
| 5 | 48 | False | False | False | 3 |
| 6 | 44 | False | True | False | 4 |
| 7 | 43 | True | True | False | 5 |
| 8 | 99 | True | False | True | 5 |
| 9 | 42 | False | False | True | 5 |

**קלט שני**

| מדידה | value | heater לפני | heater אחרי | fault | active |
| --- | --- | --- | --- | --- | --- |
| 1 | 47 | False | False | False | 0 |
| 2 | 45 | False | True | False | 1 |
| 3 | 46 | True | True | False | 2 |
| 4 | 49 | True | True | False | 3 |
| 5 | 50 | True | False | False | 3 |
| 6 | 46 | False | False | False | 3 |
| 7 | 45 | False | True | False | 4 |

**מעקב שורה-אחר-שורה לדוגמה:** מדידה 8: value=99 לא חוקי, fault הופך True; heater משתנה מ-True ל-False; active נשאר 5. במדידה 9 fault עדיין True ולכן לא מחממים.

## תשובות והנחיות לדיון

ב-49 החימום היה פעיל קודם ונשמר; ב-48 היה כבוי ונשמר. active הוא צובר ולא מצב. איפוס fault בכל סיבוב יאפשר במדידה 9 חימום בניגוד לכלל. בקלט השני בקר שני ספים עובר OFF→ON בצעד 2, ON→OFF בצעד 5, OFF→ON בצעד 7 (3). בקר סף 48: ON בצעד 1, OFF בצעד 4, ON בצעד 6 (3); למרות אותו מספר מעברים, הוא מחליף מוקדם יותר. דוגמה חזקה להבדל: [47,48,47,48] מתחילת OFF, שני ספים נשאר כבוי, סף יחיד משנה מצב 4 פעמים.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def heater_control(events, max_run):
    if max_run <= 0:
        return False, True, 0, 0
    heater = fault = False
    active = run = 0
    for value in events:
        if value == "RESET":
            heater = fault = False
            run = 0
            continue
        if not 0 <= value <= 80:
            fault = True
        if fault:
            heater = False
        elif value <= 45:
            heater = True
        elif value >= 50:
            heater = False
        if heater and run >= max_run:
            heater = False
            fault = True
        if heater:
            active += 1
            run += 1
        else:
            run = 0
    return heater, fault, active, run
```

## בדיקות אוטומטיות

```python
assert heater_control([42,45,49,48], 3) == (False,True,3,0)
assert heater_control([99,42,"RESET",44,50], 3) == (False,False,1,0)
assert heater_control([45,50,45], 1) == (True,False,2,1)
assert heater_control([80,0,81], 3) == (False,True,1,0)
assert heater_control([], 3) == (False,False,0,0)
assert heater_control([45], 0) == (False,True,0,0)
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

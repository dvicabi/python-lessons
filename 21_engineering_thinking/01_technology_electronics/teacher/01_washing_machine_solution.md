# פתרון והערות למורה: מכונת כביסה: מי מנהל את מחזור הכביסה?

[חזרה למשימת התלמיד](../01_washing_machine.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 FILL 3 0
2 WASH 6 0
3 WASH 6 1
4 DRAIN 6 2
5 DRAIN 2 2
6 DONE 0 2
7 DONE 0 2
8 DONE 0 2
```

קלט שני:

```text
1 WASH 6 0
2 WASH 6 1
3 DRAIN 6 2
4 DRAIN 4 2
5 DONE 0 2
```

### טבלאות מעקב מלאות

**קלט ראשון**

| מדידה | amount | stage בסוף | water | washed | מעבר מצב? |
| --- | --- | --- | --- | --- | --- |
| 1 | 3 | FILL | 3 | 0 | לא |
| 2 | 4 | WASH | 6 | 0 | כן |
| 3 | 2 | WASH | 6 | 1 | לא |
| 4 | 6 | DRAIN | 6 | 2 | כן |
| 5 | 4 | DRAIN | 2 | 2 | לא |
| 6 | 4 | DONE | 0 | 2 | כן |
| 7 | 3 | DONE | 0 | 2 | לא |
| 8 | 1 | DONE | 0 | 2 | לא |

**קלט שני**

| מדידה | amount | stage בסוף | water | washed | מעבר מצב? |
| --- | --- | --- | --- | --- | --- |
| 1 | 6 | WASH | 6 | 0 | כן |
| 2 | 0 | WASH | 6 | 1 | לא |
| 3 | 0 | DRAIN | 6 | 2 | כן |
| 4 | 2 | DRAIN | 4 | 2 | לא |
| 5 | 4 | DONE | 0 | 2 | כן |

**מעקב שורה-אחר-שורה לדוגמה:** מדידה 2: water משתנה מ-3 ל-6; stage משתנה מ-FILL ל-WASH; washed נשאר 0. הקוד אינו נכנס ל-elif באותה איטרציה.

## תשובות והנחיות לדיון

השטיפה הראשונה מתרחשת במדידה 3; מעבר המצב בסוף מדידה 2. החלפת elif ב-if מפעילה את WASH באותה מדידה 2, ולכן washed יהיה 1 במקום 0. min מונע למשל 7 יחידות במקום 6; max מונע למשל מינוס 2 יחידות אחרי ריקון 4 מ-2. אם רשימה נגמרת בריקון, המצב נשאר DRAIN. בתכנון השהיה יש לשמור previous_stage בנפרד; אף פעולה לא מתבצעת כשהדלת פתוחה.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def run_cycle(readings, target, wash_ticks):
    if target <= 0 or wash_ticks <= 0:
        return "ERROR", 0, 0, 0
    stage, water, washed, used = "FILL", 0, 0, 0
    for amount in readings:
        used += 1
        if amount < 0:
            return "ERROR", water, washed, used
        if stage == "FILL":
            water = min(target, water + amount)
            if water == target:
                stage = "WASH"
        elif stage == "WASH":
            washed += 1
            if washed == wash_ticks:
                stage = "DRAIN"
        elif stage == "DRAIN":
            water = max(0, water - amount)
            if water == 0:
                stage = "DONE"
                break
    return stage, water, washed, used
```

## בדיקות אוטומטיות

```python
assert run_cycle([3, 4, 2, 6, 4, 4, 3, 1], 6, 2) == ("DONE", 0, 2, 6)
assert run_cycle([2, -1, 8], 6, 2) == ("ERROR", 2, 0, 2)
assert run_cycle([6, 0], 6, 2) == ("WASH", 6, 1, 2)
assert run_cycle([], 6, 2) == ("FILL", 0, 0, 0)
assert run_cycle([5], 0, 2) == ("ERROR", 0, 0, 0)
assert run_cycle([2, 0, 2], 2, 1) == ("DONE", 0, 1, 3)
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

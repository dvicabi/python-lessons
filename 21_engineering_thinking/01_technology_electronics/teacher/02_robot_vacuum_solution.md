# פתרון והערות למורה: שואב אבק רובוטי: הדרך הקצרה אינה תמיד הדרך הטובה

[חזרה למשימת התלמיד](../02_robot_vacuum.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 MOVED (0, 1) 8 2
2 BLOCKED (0, 1) 6 2
3 MOVED (1, 1) 4 3
4 MOVED (1, 0) 2 4
5 MOVED (2, 0) 0 5
6 STOP (2, 0) 0 5
```

קלט שני:

```text
1 BLOCKED (0, 0) 8 1
2 MOVED (1, 0) 6 2
3 MOVED (0, 0) 4 2
4 MOVED (0, 1) 2 3
5 MOVED (0, 0) 0 3
```

### טבלאות מעקב מלאות

**קלט ראשון**

| צעד | פקודה | מיקום מועמד | status | position | battery | מספר משבצות |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | R | (0,1) | MOVED | (0,1) | 8 | 2 |
| 2 | R | (0,2) | BLOCKED | (0,1) | 6 | 2 |
| 3 | D | (1,1) | MOVED | (1,1) | 4 | 3 |
| 4 | L | (1,0) | MOVED | (1,0) | 2 | 4 |
| 5 | D | (2,0) | MOVED | (2,0) | 0 | 5 |
| 6 | R | לא חושב | STOP | (2,0) | 0 | 5 |
| 7 | U | לא נקרא | — | — | — | — |

**קלט שני**

| צעד | פקודה | מיקום מועמד | status | position | battery | מספר משבצות |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L | (0,-1) | BLOCKED | (0,0) | 8 | 1 |
| 2 | D | (1,0) | MOVED | (1,0) | 6 | 2 |
| 3 | U | (0,0) | MOVED | (0,0) | 4 | 2 |
| 4 | R | (0,1) | MOVED | (0,1) | 2 | 3 |
| 5 | L | (0,0) | MOVED | (0,0) | 0 | 3 |

**מעקב שורה-אחר-שורה לדוגמה:** צעד 2 בקלט הראשון: candidate=(0,2), battery מ-8 ל-6; תנאי המכשול נכשל, לכן position ו-visited לא משתנים.

## תשובות והנחיות לדיון

צעד 6 מודפס STOP והלולאה נשברת; צעד 7 לא נקרא. בקלט השני, לאחר D ואז U חזרנו לנקודת ההתחלה והכיסוי נשאר 2. הסרת הבדיקה גורמת כבר בצעד 3 לכיסוי שגוי. 10 יחידות מאפשרות לכל היותר 5 ניסיונות, כלומר לכל היותר 6 משבצות כולל ההתחלה, ופחות אם יש חסימות/חזרות.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def vacuum(commands, battery):
    moves = {"R": (0, 1), "L": (0, -1),
             "D": (1, 0), "U": (-1, 0)}
    position = (0, 0)
    visited = [position]
    if not 0 <= battery <= 10:
        return position, battery, visited, "ERROR"
    for command in commands:
        if command not in moves:
            return position, battery, visited, "ERROR"
        if battery < 2:
            return position, battery, visited, "LOW"
        dr, dc = moves[command]
        r, c = position[0] + dr, position[1] + dc
        if 0 <= r < 3 and 0 <= c < 3 and (r, c) != (0, 2):
            battery -= 2
            position = (r, c)
            if position not in visited:
                visited.append(position)
        else:
            battery -= 1
    return position, battery, visited, "COMPLETE"
```

## בדיקות אוטומטיות

```python
assert vacuum(["R","R","D","L","D","R","U"], 10) == ((2, 0), 1, [(0, 0),(0, 1),(1, 1),(1, 0),(2, 0)], "LOW")
assert vacuum(["L","D","U"], 5) == ((0, 0), 0, [(0, 0),(1, 0)], "COMPLETE")
assert vacuum(["X"], 0) == ((0, 0), 0, [(0, 0)], "ERROR")
assert vacuum([], 1) == ((0, 0), 1, [(0, 0)], "COMPLETE")
assert vacuum(["R"], 1) == ((0, 0), 1, [(0, 0)], "LOW")
assert vacuum(["D"], 11) == ((0, 0), 11, [(0, 0)], "ERROR")
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

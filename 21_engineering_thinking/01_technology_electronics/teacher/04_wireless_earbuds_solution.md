# פתרון והערות למורה: אוזניות אלחוטיות: שלוש סוללות, מערכת אחת

[חזרה למשימת התלמיד](../04_wireless_earbuds.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 B OK 5 7 8
2 L OK 1 7 8
3 B DENIED 1 7 8
4 C OK 6 10 0
5 R OK 6 3 0
6 B OK 4 1 0
```

קלט שני:

```text
1 L OK 0 10 8
2 R OK 0 4 8
3 C OK 6 6 0
4 B OK 2 2 0
5 C OK 2 2 0
```

### טבלאות מעקב מלאות

**קלט ראשון**

| צעד | mode, amount | status | left | right | case | סך אנרגיה |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | B,3 | OK | 5 | 7 | 8 | 20 |
| 2 | L,4 | OK | 1 | 7 | 8 | 16 |
| 3 | B,4 | DENIED | 1 | 7 | 8 | 16 |
| 4 | C,5 | OK | 6 | 10 | 0 | 16 |
| 5 | R,7 | OK | 6 | 3 | 0 | 9 |
| 6 | B,2 | OK | 4 | 1 | 0 | 5 |

**קלט שני**

| צעד | mode, amount | status | left | right | case | סך אנרגיה |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L,8 | OK | 0 | 10 | 8 | 18 |
| 2 | R,6 | OK | 0 | 4 | 8 | 12 |
| 3 | C,6 | OK | 6 | 6 | 0 | 12 |
| 4 | B,4 | OK | 2 | 2 | 0 | 4 |
| 5 | C,3 | OK | 2 | 2 | 0 | 4 |

**מעקב שורה-אחר-שורה לדוגמה:** צעד 4 בקלט הראשון: transfer ראשון 5, left=6, case=3; transfer שני min(5,3,3)=3, right=10, case=0; סכום האנרגיה נשמר.

## תשובות והנחיות לדיון

B נבדק בשני הצדדים לפני הפחתה ולכן נדחה אטומית. לפני ואחרי צעד 4 הסכום 16 (1+7+8 ואז 6+10+0). לדוגמה left=4,right=0,case=2,amount=2: שמאל תחילה מגדיל את הפער מ-4 ל-6; טעינה לימין מקטינה ל-2. חישוב שתי העברות מ-case=5 ללא עדכון ביניהן עלול להעביר 10 ולהגיע ל-case=-5.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def manage_earbuds(events, left, right, case):
    denied = 0
    if not (0 <= left <= 10 and 0 <= right <= 10 and 0 <= case <= 20):
        return left, right, case, denied, "ERROR"
    for mode, amount in events:
        if mode not in ("B", "L", "R", "C") or amount < 0:
            return left, right, case, denied, "ERROR"
        if mode == "C":
            while amount > 0 and case > 0 and (left < 10 or right < 10):
                if left <= right:
                    left += 1
                else:
                    right += 1
                amount -= 1
                case -= 1
        else:
            use_left = mode in ("B", "L")
            use_right = mode in ("B", "R")
            if (use_left and left < amount) or (use_right and right < amount):
                denied += 1
            else:
                if use_left:
                    left -= amount
                if use_right:
                    right -= amount
    return left, right, case, denied, "DONE"
```

## בדיקות אוטומטיות

```python
assert manage_earbuds([("C",5)], 0, 0, 5) == (3, 2, 0, 0, "DONE")
assert manage_earbuds([("C",8)], 8, 9, 10) == (10, 10, 7, 0, "DONE")
assert manage_earbuds([("B",4),("L",1)], 3, 10, 5) == (2, 10, 5, 1, "DONE")
assert manage_earbuds([("R",2),("C",-1)], 3, 3, 5) == (3, 1, 5, 0, "ERROR")
assert manage_earbuds([("C",4)], 10, 10, 5) == (10, 10, 5, 0, "DONE")
assert manage_earbuds([], 11, 0, 5) == (11, 0, 5, 0, "ERROR")
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

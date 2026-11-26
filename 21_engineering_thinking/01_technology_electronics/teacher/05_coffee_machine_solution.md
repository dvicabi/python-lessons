# פתרון והערות למורה: מכונת קפה: הזמנה היא לא רק לחיצה על כפתור

[חזרה למשימת התלמיד](../05_coffee_machine.md)

## פלט מדויק ומעקב

קלט ראשון:

```text
1 L SERVED 5 6 3 1
2 E SERVED 4 4 3 2
3 L SERVED 2 1 1 3
4 G REJECTED 2 1 1 3
5 E REJECTED 2 1 1 3
```

קלט שני:

```text
1 G SERVED 4 5 2 1
2 G REJECTED 4 5 2 1
3 E SERVED 3 3 2 2
4 L SERVED 1 0 0 3
```

### טבלאות מעקב מלאות

**קלט ראשון**

| הזמנה | סוג | דרישות c,w,m | status | coffee | water | milk | served |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L | (2,3,2) | SERVED | 5 | 6 | 3 | 1 |
| 2 | E | (1,2,0) | SERVED | 4 | 4 | 3 | 2 |
| 3 | L | (2,3,2) | SERVED | 2 | 1 | 1 | 3 |
| 4 | G | (3,4,3) | REJECTED | 2 | 1 | 1 | 3 |
| 5 | E | (1,2,0) | REJECTED | 2 | 1 | 1 | 3 |

**קלט שני**

| הזמנה | סוג | דרישות c,w,m | status | coffee | water | milk | served |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | G | (3,4,3) | SERVED | 4 | 5 | 2 | 1 |
| 2 | G | (3,4,3) | REJECTED | 4 | 5 | 2 | 1 |
| 3 | E | (1,2,0) | SERVED | 3 | 3 | 2 | 2 |
| 4 | L | (2,3,2) | SERVED | 1 | 0 | 0 | 3 |

**מעקב שורה-אחר-שורה לדוגמה:** הזמנה 2 בקלט השני: c=3,w=4,m=3. התנאים הראשונים מתקיימים אך milk=2 קטן מ-3. אין לעדכן אף רכיב; served נשאר 1.

## תשובות והנחיות לדיון

בהזמנה 5 יש 2 קפה ו-1 מים בלבד. בהזמנה 4 אף רכיב אינו מספיק ולכן גם or דוחה אותה; זו אינה הוכחה שהשינוי תקין. בהזמנה 5 קפה מספיק וחלב נדרש 0, ולכן or היה מקבל את ההזמנה ומוריד את המים למינוס 1. אספרסו דורש 0 חלב. דוגמת סדר: מלאי (3,4,3), הזמנות G,E,E: G ראשון נותן משקה אחד; E,E,G נותן שניים. בקלט השני אחרי G ראשון, G שני נדחה בגלל חלב, ולכן הפחתת קפה מוקדמת מורידה מ-4 ל-1 ללא עסקה. באתגר עודף, 5 לא מאפשר להשלים 1, אבל 2+2+2 מצליח.

מומלץ לבקש מהתלמידים לנמק את הבחירה לפני הצגת הפתרון. בדקו במיוחד את ההבדל בין תוצאה מקרית נכונה לבין פתרון שעומד בכל הדרישות. בהרחבה ניתן לקבל יותר מתכנון אחד אם הכללים והבדיקות מנומקים.

## פתרון אפשרי לכתיבה העצמאית

```python
def serve(orders, stock):
    recipes = {"E": (1, 2, 0, 8), "L": (2, 3, 2, 12),
               "G": (3, 4, 3, 15)}
    coffee, water, milk = stock
    revenue, receipts = 0, []
    if min(stock) < 0:
        return stock, revenue, receipts
    for order, paid in orders:
        if order not in recipes or paid < 0:
            receipts.append(("REJECTED", max(0, paid)))
            continue
        c, w, m, price = recipes[order]
        if paid < price or coffee < c or water < w or milk < m:
            receipts.append(("REJECTED", paid))
            continue
        coffee -= c
        water -= w
        milk -= m
        revenue += price
        receipts.append(("SERVED", paid - price))
    return (coffee, water, milk), revenue, receipts
```

## בדיקות אוטומטיות

```python
assert serve([("L",20),("E",7),("G",15)], (7,9,5)) == ((2, 2, 0), 27, [("SERVED",8),("REJECTED",7),("SERVED",0)])
assert serve([("G",20),("G",20)], (3,4,3)) == ((0,0,0), 15, [("SERVED",5),("REJECTED",20)])
assert serve([("E",8)], (1,2,0)) == ((0,0,0), 8, [("SERVED",0)])
assert serve([("X",10),("E",-1)], (2,2,0)) == ((2,2,0), 0, [("REJECTED",10),("REJECTED",0)])
assert serve([], (0,0,0)) == ((0,0,0), 0, [])
assert serve([("E",8)], (-1,2,0)) == ((-1,2,0), 0, [])
print("All 6 acceptance tests passed")
```

העתיקו את הבדיקות מתחת לפונקציה. אפשר לקבל פתרונות אחרים שמחזירים את אותם ערכים ושומרים על הכללים. אין צורך בממשק משתמש או בחומרה.

# פתרונות תרגילים 61–80 | רקורסיה ואתגרים מתקדמים

## תרגיל 61 | רקורסיה: הדפסה בירידה ובעלייה
[פתיחה](./exercise_61.py)
```text
Down 3
Down 2
Down 1
ZERO
Up 1
Up 2
Up 3
DONE
```

## תרגיל 62 | רקורסיה: הדפסה בירידה ובעלייה
[פתיחה](./exercise_62.py)
```text
Down 4
Down 3
Down 2
Down 1
ZERO
Up 1
Up 2
Up 3
Up 4
DONE
```

## תרגיל 63 | רקורסיה עם return אחרי חזרת הקריאה
[פתיחה](./exercise_63.py)
```text
Base 1
Return 2 2
Return 3 6
Return 4 24
FINAL 24
```
ערכים: `factorial=24`

## תרגיל 64 | רקורסיה עם return אחרי חזרת הקריאה
[פתיחה](./exercise_64.py)
```text
Base 1
Return 2 2
Return 3 6
Return 4 24
Return 5 120
FINAL 120
```
ערכים: `factorial=120`

## תרגיל 65 | עץ קריאות של פיבונאצ'י
[פתיחה](./exercise_65.py)
```text
Call 4
Call 3
Call 2
Call 1
Call 0
Call 1
Call 2
Call 1
Call 0
FINAL 3
```
ערכים: `fib=3`

## תרגיל 66 | עץ קריאות של פיבונאצ'י
[פתיחה](./exercise_66.py)
```text
Call 5
Call 4
Call 3
Call 2
Call 1
Call 0
Call 1
Call 2
Call 1
Call 0
Call 3
Call 2
Call 1
Call 0
Call 1
FINAL 5
```
ערכים: `fib=5`

## תרגיל 67 | סכום רשימה ברקורסיה ושורות החזרה
[פתיחה](./exercise_67.py)
```text
3 7
2 9
1 14
0 17
FINAL 17
```
ערכים: `numbers=[3, 5, 2, 7]`

## תרגיל 68 | סכום רשימה ברקורסיה ושורות החזרה
[פתיחה](./exercise_68.py)
```text
3 8
2 11
1 17
0 21
FINAL 21
```
ערכים: `numbers=[4, 6, 3, 8]`

## תרגיל 69 | רקורסיה על ספרות של מספר
[פתיחה](./exercise_69.py)
```text
Last 2
Digit 3 Sum 5
Digit 4 Sum 9
FINAL 9
```
ערכים: `sum=9`

## תרגיל 70 | רקורסיה על ספרות של מספר
[פתיחה](./exercise_70.py)
```text
Last 3
Digit 4 Sum 7
Digit 5 Sum 12
FINAL 12
```
ערכים: `sum=12`

## תרגיל 71 | רקורסיה שבונה רשימה הפוכה בלי לשנות מקור
[פתיחה](./exercise_71.py)
```text
Step [4]
Step [4, 8]
Step [4, 8, 5]
Step [4, 8, 5, 2]
Reverse [4, 8, 5, 2]
Original [2, 5, 8, 4]
```
ערכים: `numbers=[2, 5, 8, 4]`

## תרגיל 72 | רקורסיה שבונה רשימה הפוכה בלי לשנות מקור
[פתיחה](./exercise_72.py)
```text
Step [5]
Step [5, 9]
Step [5, 9, 6]
Step [5, 9, 6, 3]
Reverse [5, 9, 6, 3]
Original [3, 6, 9, 5]
```
ערכים: `numbers=[3, 6, 9, 5]`

## תרגיל 73 | שתי פונקציות רקורסיביות שקוראות זו לזו
[פתיחה](./exercise_73.py)
```text
Even? 4
Odd? 3
Even? 2
Odd? 1
Even? 0
FINAL True
```

## תרגיל 74 | שתי פונקציות רקורסיביות שקוראות זו לזו
[פתיחה](./exercise_74.py)
```text
Even? 5
Odd? 4
Even? 3
Odd? 2
Even? 1
Odd? 0
FINAL False
```

## תרגיל 75 | פונקציה רקורסיבית עם לולאה בתוך כל קריאה
[פתיחה](./exercise_75.py)
```text
1 1 1
2 3 4
3 6 10
FINAL 10
```

## תרגיל 76 | פונקציה רקורסיבית עם לולאה בתוך כל קריאה
[פתיחה](./exercise_76.py)
```text
1 1 1
2 3 4
3 6 10
4 10 20
FINAL 20
```

## תרגיל 77 | פונקציה פנימית עם nonlocal ומונה קריאות
[פתיחה](./exercise_77.py)
```text
Enter 3 1
Enter 2 2
Enter 1 3
Enter 0 4
Exit 1 4
Exit 2 4
Exit 3 4
First 4
Enter 1 5
Enter 0 6
Exit 1 6
Second 6
```
ערכים: `number of calls=6`

## תרגיל 78 | פונקציה פנימית עם nonlocal ומונה קריאות
[פתיחה](./exercise_78.py)
```text
Enter 4 1
Enter 3 2
Enter 2 3
Enter 1 4
Enter 0 5
Exit 1 5
Exit 2 5
Exit 3 5
Exit 4 5
First 5
Enter 2 6
Enter 1 7
Enter 0 8
Exit 1 8
Exit 2 8
Second 8
```
ערכים: `number of calls=8`

## תרגיל 79 | רקורסיה שמנתחת שורות במטריצה
[פתיחה](./exercise_79.py)
```text
Row 2 9 0
Row 1 8 9
Row 0 6 17
TOTAL 23
ROWS 3
```
ערכים: `matrix=[[2, 4], [7, 1], [3, 6]]`

## תרגיל 80 | רקורסיה שמנתחת שורות במטריצה
[פתיחה](./exercise_80.py)
```text
Row 2 11 0
Row 1 10 11
Row 0 8 21
TOTAL 29
ROWS 3
```
ערכים: `matrix=[[3, 5], [8, 2], [4, 7]]`

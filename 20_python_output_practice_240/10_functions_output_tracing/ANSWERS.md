# פתרונות סופיים | 80 תרגילי פונקציות

**הערה לתלמידים:** כל תשובה מופיעה גם בתחתית קובץ התרגיל כתגובות; חשבו לפני ההרצה.

## 01–20 | הגדרת פונקציות וקריאות

## תרגיל 01 | הגדרה וקריאות חוזרות
[פתיחה](./01_basic_def_calls/exercise_01.py)
```text
Hello Dana
Hello Dana
Done
```
ערכים: `name in last call=Dana`

## תרגיל 02 | הגדרה וקריאות חוזרות
[פתיחה](./01_basic_def_calls/exercise_02.py)
```text
Hello Avi
Hello Avi
Hello Avi
Done
```
ערכים: `name in last call=Avi`

## תרגיל 03 | הדפסה מתוך פעולה עם פרמטר
[פתיחה](./01_basic_def_calls/exercise_03.py)
```text
Value: 3
Next: 5
Value: 6
Next: 8
```

## תרגיל 04 | הדפסה מתוך פעולה עם פרמטר
[פתיחה](./01_basic_def_calls/exercise_04.py)
```text
Value: 4
Next: 6
Value: 8
Next: 10
```

## תרגיל 05 | ערך מוחזר באמצעות return
[פתיחה](./01_basic_def_calls/exercise_05.py)
```text
11
13
8
```
ערכים: `x=11`

## תרגיל 06 | ערך מוחזר באמצעות return
[פתיחה](./01_basic_def_calls/exercise_06.py)
```text
13
16
10
```
ערכים: `x=13`

## תרגיל 07 | ההבדל בין print לבין return
[פתיחה](./01_basic_def_calls/exercise_07.py)
```text
6
12
None
End
```
ערכים: `result=None`

## תרגיל 08 | ההבדל בין print לבין return
[פתיחה](./01_basic_def_calls/exercise_08.py)
```text
7
14
None
End
```
ערכים: `result=None`

## תרגיל 09 | פרמטרים והדפסת מחרוזות
[פתיחה](./01_basic_def_calls/exercise_09.py)
```text
PyPyPy
!!
```

## תרגיל 10 | פרמטרים והדפסת מחרוזות
[פתיחה](./01_basic_def_calls/exercise_10.py)
```text
GoGoGoGo
!!!
```

## תרגיל 11 | שתי פונקציות עם return
[פתיחה](./01_basic_def_calls/exercise_11.py)
```text
8
6
12
```

## תרגיל 12 | שתי פונקציות עם return
[פתיחה](./01_basic_def_calls/exercise_12.py)
```text
12
7
14
```

## תרגיל 13 | תנאים בתוך פונקציה
[פתיחה](./01_basic_def_calls/exercise_13.py)
```text
ODD
EVEN
ODD
```

## תרגיל 14 | תנאים בתוך פונקציה
[פתיחה](./01_basic_def_calls/exercise_14.py)
```text
EVEN
ODD
EVEN
```

## תרגיל 15 | פונקציה שסוכמת בעזרת for
[פתיחה](./01_basic_def_calls/exercise_15.py)
```text
10
21
```

## תרגיל 16 | פונקציה שסוכמת בעזרת for
[פתיחה](./01_basic_def_calls/exercise_16.py)
```text
15
28
```

## תרגיל 17 | משתנה מקומי מול משתנה מחוץ לפונקציה
[פתיחה](./01_basic_def_calls/exercise_17.py)
```text
Inside 9
Outside 5
```
ערכים: `number outside=5`

## תרגיל 18 | משתנה מקומי מול משתנה מחוץ לפונקציה
[פתיחה](./01_basic_def_calls/exercise_18.py)
```text
Inside 10
Outside 6
```
ערכים: `number outside=6`

## תרגיל 19 | סדר הקריאה וההדפסה
[פתיחה](./01_basic_def_calls/exercise_19.py)
```text
Start 3
Finish 5
Result 15
```
ערכים: `x=15`

## תרגיל 20 | סדר הקריאה וההדפסה
[פתיחה](./01_basic_def_calls/exercise_20.py)
```text
Start 4
Finish 6
Result 18
```
ערכים: `x=18`

## 21–40 | פרמטרים, return, Lambda ו־Scope

## תרגיל 21 | פרמטר עם ערך ברירת מחדל
[פתיחה](./02_arguments_returns_scope/exercise_21.py)
```text
16
27
4
```

## תרגיל 22 | פרמטר עם ערך ברירת מחדל
[פתיחה](./02_arguments_returns_scope/exercise_22.py)
```text
25
64
5
```

## תרגיל 23 | העברת פרמטרים לפי שמות ובסדר שונה
[פתיחה](./02_arguments_returns_scope/exercise_23.py)
```text
-1
-1
23
```

## תרגיל 24 | העברת פרמטרים לפי שמות ובסדר שונה
[פתיחה](./02_arguments_returns_scope/exercise_24.py)
```text
0
5
25
```

## תרגיל 25 | *args מקבל מספר משתנה של ארגומנטים
[פתיחה](./02_arguments_returns_scope/exercise_25.py)
```text
3 10
20
2 8
```
ערכים: `x=10`

## תרגיל 26 | *args מקבל מספר משתנה של ארגומנטים
[פתיחה](./02_arguments_returns_scope/exercise_26.py)
```text
3 13
26
2 10
```
ערכים: `x=13`

## תרגיל 27 | **kwargs ומילון מפתחות
[פתיחה](./02_arguments_returns_scope/exercise_27.py)
```text
age 16
city Haifa
name Dan
Fields 3
```
ערכים: `count=3`

## תרגיל 28 | **kwargs ומילון מפתחות
[פתיחה](./02_arguments_returns_scope/exercise_28.py)
```text
age 17
city Eilat
name Noa
Fields 3
```
ערכים: `count=3`

## תרגיל 29 | פונקציה שמחזירה שני ערכים
[פתיחה](./02_arguments_returns_scope/exercise_29.py)
```text
4 1
5
(4, 2)
```
ערכים: `q=4, r=1`

## תרגיל 30 | פונקציה שמחזירה שני ערכים
[פתיחה](./02_arguments_returns_scope/exercise_30.py)
```text
4 0
4
(4, 1)
```
ערכים: `q=4, r=0`

## תרגיל 31 | lambda ושילוב פונקציות
[פתיחה](./02_arguments_returns_scope/exercise_31.py)
```text
12
13
10
```

## תרגיל 32 | lambda ושילוב פונקציות
[פתיחה](./02_arguments_returns_scope/exercise_32.py)
```text
15
16
10
```

## תרגיל 33 | global לעומת משתנה מקומי
[פתיחה](./02_arguments_returns_scope/exercise_33.py)
```text
Local 8
Before 5
Global 7
After 7
```
ערכים: `global value=7`

## תרגיל 34 | global לעומת משתנה מקומי
[פתיחה](./02_arguments_returns_scope/exercise_34.py)
```text
Local 9
Before 6
Global 8
After 8
```
ערכים: `global value=8`

## תרגיל 35 | פונקציה שמחזירה פונקציה אחרת (Closure)
[פתיחה](./02_arguments_returns_scope/exercise_35.py)
```text
5
6
7
```

## תרגיל 36 | פונקציה שמחזירה פונקציה אחרת (Closure)
[פתיחה](./02_arguments_returns_scope/exercise_36.py)
```text
7
7
9
```

## תרגיל 37 | סדר חישוב הארגומנטים עם הדפסה
[פתיחה](./02_arguments_returns_scope/exercise_37.py)
```text
A 2
B 3
Combine 3 4
Result 12
```
ערכים: `x=12`

## תרגיל 38 | סדר חישוב הארגומנטים עם הדפסה
[פתיחה](./02_arguments_returns_scope/exercise_38.py)
```text
A 3
B 4
Combine 4 5
Result 20
```
ערכים: `x=20`

## תרגיל 39 | פונקציה כארגומנט ושינוי התנהגות
[פתיחה](./02_arguments_returns_scope/exercise_39.py)
```text
[4, 7, 6]
[4, 25, 16]
[2, 5, 4]
```

## תרגיל 40 | פונקציה כארגומנט ושינוי התנהגות
[פתיחה](./02_arguments_returns_scope/exercise_40.py)
```text
[6, 9, 8]
[9, 36, 25]
[3, 6, 5]
```

## 41–60 | פונקציות עם רשימות ומטריצות

## תרגיל 41 | פונקציה שסוכמת ערכים לפי תנאי
[פתיחה](./03_functions_with_lists/exercise_41.py)
```text
14
10
[2, 5, 3, 8, 4]
```
ערכים: `numbers=[2, 5, 3, 8, 4]`

## תרגיל 42 | פונקציה שסוכמת ערכים לפי תנאי
[פתיחה](./03_functions_with_lists/exercise_42.py)
```text
10
10
[3, 6, 4, 9, 5]
```
ערכים: `numbers=[3, 6, 4, 9, 5]`

## תרגיל 43 | שינוי רשימה בתוך פונקציה וערך None
[פתיחה](./03_functions_with_lists/exercise_43.py)
```text
[5, 8, 6, 11]
None
[6, 9, 7, 12]
```
ערכים: `numbers=[6, 9, 7, 12], result=None`

## תרגיל 44 | שינוי רשימה בתוך פונקציה וערך None
[פתיחה](./03_functions_with_lists/exercise_44.py)
```text
[7, 10, 8, 13]
None
[8, 11, 9, 14]
```
ערכים: `numbers=[8, 11, 9, 14], result=None`

## תרגיל 45 | פונקציה שמחזירה רשימה חדשה בלי לשנות את המקור
[פתיחה](./03_functions_with_lists/exercise_45.py)
```text
[4, 4, 6, 7, 8]
[2, 5, 3, 8, 4]
[8, 8, 5, 6, 7]
```
ערכים: `original=[2, 5, 3, 8, 4], copy=[4, 4, 6, 7, 8]`

## תרגיל 46 | פונקציה שמחזירה רשימה חדשה בלי לשנות את המקור
[פתיחה](./03_functions_with_lists/exercise_46.py)
```text
[6, 5, 8, 8, 10]
[3, 6, 4, 9, 5]
[5, 10, 7, 7, 9]
```
ערכים: `original=[3, 6, 4, 9, 5], copy=[6, 5, 8, 8, 10]`

## תרגיל 47 | לשנות רשימה ולשמור הפניה (Alias)
[פתיחה](./03_functions_with_lists/exercise_47.py)
```text
4
[4, 3, 7, 11]
[4, 3, 7, 11, 3]
```
ערכים: `items=[4, 3, 7, 11, 3], alias refers to items`

## תרגיל 48 | לשנות רשימה ולשמור הפניה (Alias)
[פתיחה](./03_functions_with_lists/exercise_48.py)
```text
4
[5, 4, 8, 13]
[5, 4, 8, 13, 4]
```
ערכים: `items=[5, 4, 8, 13, 4], alias refers to items`

## תרגיל 49 | לשנות עותק ולא את הרשימה המקורית
[פתיחה](./03_functions_with_lists/exercise_49.py)
```text
[7, 1, 4, -2]
[7, 2, 6, 1]
10
```
ערכים: `numbers=[7, 2, 6, 1], new_numbers=[7, 1, 4, -2]`

## תרגיל 50 | לשנות עותק ולא את הרשימה המקורית
[פתיחה](./03_functions_with_lists/exercise_50.py)
```text
[8, 2, 5, -1]
[8, 3, 7, 2]
14
```
ערכים: `numbers=[8, 3, 7, 2], new_numbers=[8, 2, 5, -1]`

## תרגיל 51 | פונקציה שסופרת התאמות בין שתי רשימות
[פתיחה](./03_functions_with_lists/exercise_51.py)
```text
3
5
```
ערכים: `a=[2, 5, 8], b=[3, 4, 6]`

## תרגיל 52 | פונקציה שסופרת התאמות בין שתי רשימות
[פתיחה](./03_functions_with_lists/exercise_52.py)
```text
2
5
```
ערכים: `a=[3, 6, 9], b=[4, 5, 7]`

## תרגיל 53 | פונקציה שמחזירה ערך מינימום ומקסימום
[פתיחה](./03_functions_with_lists/exercise_53.py)
```text
2 9
7
(2, 9)
```
ערכים: `lo=2, hi=9`

## תרגיל 54 | פונקציה שמחזירה ערך מינימום ומקסימום
[פתיחה](./03_functions_with_lists/exercise_54.py)
```text
3 10
7
(3, 10)
```
ערכים: `lo=3, hi=10`

## תרגיל 55 | פונקציה שבונה מטריצה מרשימה
[פתיחה](./03_functions_with_lists/exercise_55.py)
```text
[[2, 5], [4, 7], [6, 9]]
7
[2, 4, 6]
```
ערכים: `rows=[[2, 5], [4, 7], [6, 9]], values=[2, 4, 6]`

## תרגיל 56 | פונקציה שבונה מטריצה מרשימה
[פתיחה](./03_functions_with_lists/exercise_56.py)
```text
[[3, 7], [5, 9], [7, 11]]
9
[3, 5, 7]
```
ערכים: `rows=[[3, 7], [5, 9], [7, 11]], values=[3, 5, 7]`

## תרגיל 57 | פונקציה שמשנה תאים במטריצה
[פתיחה](./03_functions_with_lists/exercise_57.py)
```text
25
[[4, 6], [10, 5]]
29
[[5, 6], [12, 6]]
```
ערכים: `matrix=[[5, 6], [12, 6]]`

## תרגיל 58 | פונקציה שמשנה תאים במטריצה
[פתיחה](./03_functions_with_lists/exercise_58.py)
```text
33
[[6, 8], [12, 7]]
37
[[7, 8], [14, 8]]
```
ערכים: `matrix=[[7, 8], [14, 8]]`

## תרגיל 59 | שתי פונקציות שקוראות אחת לשנייה ועובדות על רשימה
[פתיחה](./03_functions_with_lists/exercise_59.py)
```text
[2, 8]
20
16
```
ערכים: `numbers=[2, 5, 8, 3]`

## תרגיל 60 | שתי פונקציות שקוראות אחת לשנייה ועובדות על רשימה
[פתיחה](./03_functions_with_lists/exercise_60.py)
```text
[6, 4]
20
20
```
ערכים: `numbers=[3, 6, 9, 4]`

## 61–80 | רקורסיה, עץ קריאות ופונקציות מתקדמות

## תרגיל 61 | רקורסיה: הדפסה בירידה ובעלייה
[פתיחה](./04_recursion_advanced/exercise_61.py)
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
[פתיחה](./04_recursion_advanced/exercise_62.py)
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
[פתיחה](./04_recursion_advanced/exercise_63.py)
```text
Base 1
Return 2 2
Return 3 6
Return 4 24
FINAL 24
```
ערכים: `factorial=24`

## תרגיל 64 | רקורסיה עם return אחרי חזרת הקריאה
[פתיחה](./04_recursion_advanced/exercise_64.py)
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
[פתיחה](./04_recursion_advanced/exercise_65.py)
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
[פתיחה](./04_recursion_advanced/exercise_66.py)
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
[פתיחה](./04_recursion_advanced/exercise_67.py)
```text
3 7
2 9
1 14
0 17
FINAL 17
```
ערכים: `numbers=[3, 5, 2, 7]`

## תרגיל 68 | סכום רשימה ברקורסיה ושורות החזרה
[פתיחה](./04_recursion_advanced/exercise_68.py)
```text
3 8
2 11
1 17
0 21
FINAL 21
```
ערכים: `numbers=[4, 6, 3, 8]`

## תרגיל 69 | רקורסיה על ספרות של מספר
[פתיחה](./04_recursion_advanced/exercise_69.py)
```text
Last 2
Digit 3 Sum 5
Digit 4 Sum 9
FINAL 9
```
ערכים: `sum=9`

## תרגיל 70 | רקורסיה על ספרות של מספר
[פתיחה](./04_recursion_advanced/exercise_70.py)
```text
Last 3
Digit 4 Sum 7
Digit 5 Sum 12
FINAL 12
```
ערכים: `sum=12`

## תרגיל 71 | רקורסיה שבונה רשימה הפוכה בלי לשנות מקור
[פתיחה](./04_recursion_advanced/exercise_71.py)
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
[פתיחה](./04_recursion_advanced/exercise_72.py)
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
[פתיחה](./04_recursion_advanced/exercise_73.py)
```text
Even? 4
Odd? 3
Even? 2
Odd? 1
Even? 0
FINAL True
```

## תרגיל 74 | שתי פונקציות רקורסיביות שקוראות זו לזו
[פתיחה](./04_recursion_advanced/exercise_74.py)
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
[פתיחה](./04_recursion_advanced/exercise_75.py)
```text
1 1 1
2 3 4
3 6 10
FINAL 10
```

## תרגיל 76 | פונקציה רקורסיבית עם לולאה בתוך כל קריאה
[פתיחה](./04_recursion_advanced/exercise_76.py)
```text
1 1 1
2 3 4
3 6 10
4 10 20
FINAL 20
```

## תרגיל 77 | פונקציה פנימית עם nonlocal ומונה קריאות
[פתיחה](./04_recursion_advanced/exercise_77.py)
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
[פתיחה](./04_recursion_advanced/exercise_78.py)
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
[פתיחה](./04_recursion_advanced/exercise_79.py)
```text
Row 2 9 0
Row 1 8 9
Row 0 6 17
TOTAL 23
ROWS 3
```
ערכים: `matrix=[[2, 4], [7, 1], [3, 6]]`

## תרגיל 80 | רקורסיה שמנתחת שורות במטריצה
[פתיחה](./04_recursion_advanced/exercise_80.py)
```text
Row 2 11 0
Row 1 10 11
Row 0 8 21
TOTAL 29
ROWS 3
```
ערכים: `matrix=[[3, 5], [8, 2], [4, 7]]`

# 📘 פתרונות – NumPy Introduction

## 🧪 פתרונות לתרגילים

### תרגיל 1
```python
import numpy as np
```

### תרגיל 2
```python
arr = np.array([5, 10, 15, 20])
print(arr)  # Output: [ 5 10 15 20]
```

### תרגיל 3
```python
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

### תרגיל 4
```python
a = np.array([2, 4, 6])
print(a * 3)  # Output: [ 6 12 18]
```

### תרגיל 5
```python
b = np.array([8, 6, 4, 2])
print(np.mean(b))  # Output: 5.0
```

### תרגיל 6
```python
zeros_arr = np.zeros(5)
print(zeros_arr)  # Output: [0. 0. 0. 0. 0.]
```

### תרגיל 7
```python
evens = np.arange(0, 21, 2)
print(evens)  # Output: [ 0  2  4  6  8 10 12 14 16 18 20]
```

### תרגיל 8
```python
nums = np.array([9, 3, 7, 1, 5])
print(np.max(nums))  # Output: 9
print(np.min(nums))  # Output: 1
```

## 💬 הערות כלליות

* `NumPy` משפרת משמעותית את מהירות החישובים לעומת רשימות רגילות.
* כל פונקציה שפועלת על מערך שלם – מתבצעת במכה אחת וללא לולאות.
* מומלץ להשתמש בה בכל עבודה עם נתונים מספריים או מטריצות.

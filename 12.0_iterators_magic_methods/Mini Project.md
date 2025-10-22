<!-- DC_HEADER_START -->
<div align="center">

🐍 **Python Learning Series | סדרת לימודי פייתון**  
**Dvir Cabessa | דביר קבסה**  
© 2025 All Rights Reserved | כל הזכויות שמורות

</div>

---
<!-- DC_HEADER_END -->

🚀 ניהול קובץ תרגומים אינטראקטיבי - Mini Project
📘 שם הפרויקט:
SmartTranslationDict

🎯 מטרת הפרויקט:
יצירת אובייקט חכם שמתנהג כמו מילון דו־לשוני (עברית–אנגלית), תומך בגישה לפי מילה, חיפוש הפוך, הדפסות קריאות, שימוש בלולאות, פעולות חיבור, בדיקות קיום, ועוד – הכול דרך מתודות קסומות בלבד.

🔹 פונקציונליות נדרשת:
מתודה קסומה	תפקיד
__init__	אתחול עם מילון תרגום
__getitem__	קבלת תרגום (obj["שלום"])
__setitem__	הוספת תרגום חדש (obj["חתול"] = "cat")
__delitem__	מחיקת תרגום
__contains__	"חתול" in obj או "cat" in obj
__len__	מספר תרגומים
__iter__ / __next__	מעבר על המילים העבריות בלבד
__str__ / __repr__	הצגה יפה של כל זוגות המילים
__call__	תרגום מיידי (לכיוון הפוך) – לדוגמה obj("cat") → "חתול"
__add__	שילוב עם אובייקט תרגום נוסף (obj1 + obj2)
__eq__	השוואה בין שני מילוני תרגום לפי תוכן
__bool__	אם יש בכלל תרגומים או שהמילון ריק
__enter__ / __exit__	ניהול מצב טעינה ושמירה של קובץ JSON אוטומטית ב־with
__del__	הדפסה על סיום חיים של האובייקט

💡 תוספות אופציונליות:
שימוש ב־__index__ כדי לתמוך ב־range(translation_obj) (לדוגמה, כמה מילים עד כה)

תמיכה בשמירת ההיסטוריה של חיפושים

הדפסת המילון ב־table מיידית

📦 מבנה קוד לדוגמה (ראשוני בלבד):
```python
Copy
Edit
t = SmartTranslationDict({
    "שלום": "hello",
    "חתול": "cat"
})

print(t["שלום"])        # hello
t["כלב"] = "dog"
print("cat" in t)       # True
print(len(t))           # 3
for word in t:
    print(word)         # שלום, חתול, כלב

print(t("dog"))         # כלב
with t:
    print("📝 Using translation context")

print(t)                # תצוגה יפה של כל הזוגות
````

🔧 שלבים לביצוע:
---

🔢 שלב 1 – הגדרת __init__, __str__, __repr__

🔢 שלב 2 – מימוש __getitem__, __setitem__, __contains__

🔢 שלב 3 – איטרציה מלאה + len

🔢 שלב 4 – __call__ לתרגום הפוך

🔢 שלב 5 – ניהול עם __enter__, __exit__

🔢 שלב 6 – חיבורים, השוואות, מחיקות

🔢 שלב 7 – בונוסים (range, hash, format...)






```python
import json

class SmartTranslationDict:
    def __init__(self, translations=None):
        self.translations = translations or {}
        self.reverse = {v: k for k, v in self.translations.items()}

    def __str__(self):
        return "\n".join(f"{k} → {v}" for k, v in self.translations.items())

    def __repr__(self):
        return f"SmartTranslationDict({self.translations})"

    def __getitem__(self, key):
        return self.translations[key]

    def __setitem__(self, key, value):
        self.translations[key] = value
        self.reverse[value] = key

    def __delitem__(self, key):
        val = self.translations.pop(key)
        self.reverse.pop(val, None)

    def __contains__(self, item):
        return item in self.translations or item in self.reverse

    def __len__(self):
        return len(self.translations)

    def __iter__(self):
        self._iter_keys = iter(self.translations)
        return self

    def __next__(self):
        return next(self._iter_keys)

    def __call__(self, word):
        if word in self.reverse:
            return self.reverse[word]
        elif word in self.translations:
            return self.translations[word]
        raise KeyError(f"No translation for '{word}'")

    def __add__(self, other):
        if not isinstance(other, SmartTranslationDict):
            return NotImplemented
        merged = self.translations.copy()
        merged.update(other.translations)
        return SmartTranslationDict(merged)

    def __eq__(self, other):
        if not isinstance(other, SmartTranslationDict):
            return False
        return self.translations == other.translations

    def __bool__(self):
        return bool(self.translations)

    def __enter__(self):
        print("🔓 Translation context started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🔒 Translation context ended")
        with open("translations.json", "w", encoding="utf-8") as f:
            json.dump(self.translations, f, ensure_ascii=False, indent=2)

    def __del__(self):
        print("🗑️ Translation object deleted")

    def __index__(self):
        return len(self.translations)

# Demo usage
if __name__ == "__main__":
    t = SmartTranslationDict({"שלום": "hello", "חתול": "cat"})
    print(t["שלום"])
    t["כלב"] = "dog"
    print("dog" in t)
    print(len(t))

    for word in t:
        print(word)

    print(t("dog"))

    with t:
        print("📝 Translating...")

    print(t)
    print(repr(t))
    print(bool(t))
    print(range(t.__index__()))
````

<!-- DC_FOOTER_START -->
---

<div align="center">

✨ **Thank you for learning with Dvir Cabessa** ✨  
✨ **תודה שלמדתם עם דביר קבסה** ✨  

📘 *All Rights Reserved © Dvir Cabessa 2025*  
📘 *כל הזכויות שמורות © דביר קבסה 2025*  

🔗 *For educational purposes only – copying or distribution without permission is prohibited.*  
🔗 *החומר נועד לשימוש חינוכי בלבד — אין להעתיק או להפיץ ללא אישור.*

---

> _"Education is the art of awakening curiosity and guiding it toward creation."_  
> _"החינוך הוא אמנות המעירה את הסקרנות ומכוונת אותה ליצירה."_  
> — **Dvir Cabessa**

</div>
<!-- DC_FOOTER_END -->


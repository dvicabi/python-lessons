# 📘 מדריך מקצועי: שימוש ב־Git ו־GitHub בתוך PyCharm – לכל פרויקט

מדריך זה מתאים לכל מפתח שרוצה לנהל קוד עם Git ולהעלות אותו ל־GitHub – בכל פרויקט עתידי, בצורה מסודרת ומקצועית.

---

## 🚩 שלב 1: יצירת פרויקט חדש או פתיחת קיים

### ב־PyCharm:
- `File > New Project` או `Open`
- בחר Python / Django / אחר
- ודא שיש לפחות קובץ קוד אחד (למשל: `main.py`)

---

## 🔄 שלב 2: הפעלת מערכת ניהול גרסאות (Git)

- תפריט עליון: `VCS > Enable Version Control Integration`
- בחר `Git` → לחץ `OK`

> כעת PyCharm ייצור תיקיית `.git` נסתרת לניהול היסטוריית גרסאות הקוד שלך.

---

## 📁 שלב 3: יצירת קובץ `.gitignore`

### תפקיד:
להחריג קבצים רגישים או זמניים – שלא ייכנסו למערכת ניהול הגרסאות.

### יצירה:
- קליק ימני על התיקייה הראשית > `New > File`
- שם הקובץ: `.gitignore`

### תוכן בסיסי מומלץ:

```gitignore
# Virtual environment
.venv/
env/

# PyCharm
.idea/
*.iml

# Python cache
__pycache__/
*.pyc

# Logs
*.log

# Sensitive files
*.json
*.env
*.pem
token.*
````

---

## 💾 שלב 4: ביצוע Commit ראשון

1. `Git > Commit`
2. סמן את הקבצים הרצויים (קוד בלבד, לא קבצים רגישים)
3. הוסף הודעה, לדוגמה:

```
initial commit: setup basic project structure
```

4. לחץ `Commit`

---

## ☁️ שלב 5: יצירת ריפו חדש ב־GitHub

1. היכנס ל־[https://github.com/new](https://github.com/new)
2. בחר שם לריפו
3. **בטל** את הסימון של `Initialize with README`
4. לחץ `Create repository`
5. העתק את כתובת הריפו (HTTPS), למשל:

```
https://github.com/username/project-name.git
```

---

## 🔗 שלב 6: חיבור Git המקומי ל־GitHub

ב־Terminal של PyCharm:

```bash
git remote add origin https://github.com/username/project-name.git
git branch -M main
git push -u origin main
```

> `origin` – הכינוי של הריפו בענן
> `main` – הסניף הראשי בפרויקט

---

## 🔐 שלב 7: התחברות ל־GitHub מתוך PyCharm

1. ייתכן שתתבקש לבחור התחברות:

   * בחר `Sign in with browser`
2. אשר את ההרשאה בדפדפן
3. PyCharm יחובר אוטומטית לחשבון שלך

---

## 🔁 שלב 8: המשך עבודה שוטפת

### בכל שינוי עתידי:

```bash
git add .
git commit -m "תיאור השינוי"
git push
```

או דרך PyCharm:

* `Git > Commit`
* ולאחר מכן `Git > Push`

---

## 🧠 דגשים חשובים

| נושא         | הסבר                                 |
| ------------ | ------------------------------------ |
| `.gitignore` | שומר על פרטיות – מונע דליפת מידע     |
| `commit`     | שמירה של נקודת שינוי עם תיאור        |
| `push`       | מעלה את השינויים ל־GitHub            |
| `pull`       | מושך עדכונים מהענן (אם עובדים בצוות) |
| `branch`     | סניפים לפיתוח פיצ'רים בצורה מבודדת   |

---

## 🧾 הודעות Commit מקצועיות לדוגמה

```text
add: create user model
fix: resolve login error
refactor: clean up form logic
update: change default settings
remove: unused import
wip: testing image upload
```

---

## ✅ סיכום

🎯 עכשיו אתה יודע:

* איך לנהל פרויקט בעזרת Git
* איך להעלות אותו ל־GitHub
* איך לשמור על היסטוריית שינויים מסודרת ומקצועית

---

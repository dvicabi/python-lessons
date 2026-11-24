# -*- coding: utf-8 -*-
# תרגיל 28 | המתודה המיוחדת __len__
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)

p = Playlist()
p.songs.append("A")
p.songs.append("B")
print(len(p), p.songs[-1])

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 2 B
# <<< END EXPECTED OUTPUT
# ערכים סופיים: p.songs=['A', 'B']

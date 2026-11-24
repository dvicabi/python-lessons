# -*- coding: utf-8 -*-
# תרגיל 39 | הרכבה: אובייקט שמכיל אובייקטים אחרים
# חשבו את כל שורות הפלט לפני ההרצה.
# מומלץ להכין טבלת מעקב לכל אובייקט ולכל משתנה.

class Song:
    def __init__(self, duration):
        self.duration = duration

class Album:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def minutes(self):
        return sum(song.duration for song in self.songs)

album = Album()
first = Song(3)
album.add(first)
album.add(Song(5))
first.duration += 2
print(album.minutes(), len(album.songs))

# ------------------------------------------------------------
# פתרון סופי (כהערה בלבד):
# >>> EXPECTED OUTPUT
# 10 2
# <<< END EXPECTED OUTPUT
# ערכים סופיים: first.duration=5; album has 2 songs

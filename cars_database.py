import csv
import sqlite3
with open('cars.csv', 'r', encoding='utf-8') as f:
    f = csv.reader(f)
    for i in f:
        i = ";".join(i)
        i = i.split(';')

        conn = sqlite3.connect('cars.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tab1(id INTEGER PRIMARY KEY AUTOINCREMENT, car TEXT, MPG TEXT,
         Cylinders INTEGER, Displacement INTEGER, Horse INTEGER, Weight INTEGER, Acceleration INTEGER,
         Model REAL, Origin TEXT)''')

        cursor.execute('''INSERT INTO tab1(car, MPG, Cylinders, Displacement, Horse, Weight, Acceleration, Model,
        Origin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        conn.commit()
        cursor.execute('''SELECT*FROM tab1''')
        k = cursor.fetchall()
        print(k)
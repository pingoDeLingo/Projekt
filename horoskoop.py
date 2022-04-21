import sqlite3
from random import randint
from datetime import datetime
import random

d0 = datetime(2010, 5, 12)
d1 = datetime.now()
delta = d1 - d0
#  

random.seed(delta.days)
# print(random.randint(1, 2103))

sisemus = "Jäär, Sõnn, Kaksikud, Vähk, Lõvi, Neitsi, Kaalud, Skorpion, Ambur, Kaljukits, Veevalaja, Kalad"

tahtkuju = input("Mis on sinu tähtkuju? ")
if tahtkuju in sisemus:

    num = randint(1, 2102)
#     print(num)
    conn = sqlite3.connect('horoskoop.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [num])
    ds = c.fetchone()
    if tahtkuju == "Jäär":
        d0 = datetime(2010, 5, 20)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        mdea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [mdea])
        sd = c.fetchone()
        print("Teie horoskoop on: " + str(sd))
    if tahtkuju == "Skorpion":
        d0 = datetime(2005, 2, 20)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))
        
    if tahtkuju == "Kaksikud":
        d0 = datetime(2007, 6, 26)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))
    
    if tahtkuju == "Veevalaja":
        d0 = datetime(2002, 7, 13)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))
    if tahtkuju == "Sõnn":
        d0 = datetime(2016, 1, 1)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))

    if tahtkuju == "Vähk":
        d0 = datetime(2022, 4, 21)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))
    
    if tahtkuju == "Kaalud":
        d0 = datetime(2000, 5, 15)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))

    if tahtkuju == "Lõvi":
        d0 = datetime(2013, 1, 7)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))

    if tahtkuju == "Neitsi":
        d0 = datetime(2001, 12, 13)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))

    if tahtkuju == "Ambur":
        d0 = datetime(2020, 2, 20)
        d1 = datetime.now()
        delta = d1 - d0
         

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))

    if tahtkuju == "Kalad":
        d0 = datetime(1999, 12, 13)
        d1 = datetime.now()
        delta = d1 - d0

        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))
    if tahtkuju == "Kaljukits":
        d0 = datetime(1912, 6, 23)
        d1 = datetime.now()
        delta = d1 - d0


        random.seed(delta.days)
        saitea = random.randint(1, 2103)
        c.execute(f"SELECT * FROM horoskoop WHERE _rowid_ = ?", [saitea])
        std = c.fetchone()
        print("Teie horoskoop on: " + str(std))

   # print("Teie horoskoop on: " + str(ds))
else:
    print("Pole olemas")

# c.execute('''DROP TABLE field1''')


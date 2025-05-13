import sqlite3
import hashlib

def hash_kode(kode):
    return hashlib.sha256(kode.encode()).hexdigest()

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS brugere (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brugernavn TEXT UNIQUE,
    kode TEXT,
    rolle TEXT
)
""")

brugere = [
    ("admin", hash_kode("admin123"), "admin"),
    ("bruger1", hash_kode("test123"), "bruger"),
    ("bruger2", hash_kode("kode321"), "bruger")
]

for b in brugere:
    try:
        cursor.execute("INSERT INTO brugere (brugernavn, kode, rolle) VALUES (?, ?, ?)", b)
    except:
        pass

conn.commit()
conn.close()
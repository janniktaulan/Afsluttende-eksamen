## DETTE SCRIPT SLETTER ALT DATA FRA "data.db"

import sqlite3

# Forbind til databasen
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Slet alle rækker i tabellen 'målinger'
cursor.execute("DELETE FROM målinger")
conn.commit()

# (valgfrit) nulstil auto-increment id
cursor.execute("DELETE FROM sqlite_sequence WHERE name='målinger'")
conn.commit()

conn.close()

print("✅ Alle målinger er nu slettet fra databasen.")

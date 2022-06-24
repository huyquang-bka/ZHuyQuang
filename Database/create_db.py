import sqlite3

conn = sqlite3.connect('atin.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS test")
c.execute(
    """CREATE TABLE test (id INTEGER PRIMARY KEY AUTOINCREMENT, camera_id TEXT, rtsp TEXT, features TEXT, display INTEGER)""")

# c.execute("INSERT INTO parking VALUES (1, 'ABC123', 'RED', 'TOYOTA', '2020-01-01', '2020-01-01', 'image/path')")

# conn.commit()

# get all columns name of table
# c.execute("PRAGMA table_info(parking)")
# columns = c.fetchall()
# print(columns)
#
# c.execute("SELECT * FROM parking")
# rows = c.fetchall()
# print(rows)

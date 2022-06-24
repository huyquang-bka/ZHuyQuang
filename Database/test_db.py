import sqlite3

conn = sqlite3.connect('atin.db')
c = conn.cursor()

# command = f"insert into test(camera_id, rtsp, features, display) values('123', '123', '123', '123')"
command = "select * from test"
c.execute(command)
conn.commit()
datas = c.fetchall()
for data in datas:
    print(data)

import pymysql


# connection 정보
conn = pymysql.connect(
    host = 'localhost', # host name
    user = 'root', # user name
    password = 'A1b2c3d4e5!', # password
    db='test',
    charset = 'utf8'
)
cursor = conn.cursor()

sql = "SELECT * FROM test1"
cursor.execute(sql)
res = cursor.fetchall()

for data in res:
        print(data)

conn.commit()
conn.close()

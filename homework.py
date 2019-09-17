import pymysql
#连接数据库
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset  = 'utf8'
                     )
#获取游标
cur = db.cursor()
#执行语句
sql = 'select * from classstudent'
cur.execute(sql)
db.commit()
cur.close()
db.close()
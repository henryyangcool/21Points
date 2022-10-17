import pymysql

# db = pymysql.connect(host='localhost',port=3306,user='root',passwd='1111',db='20220928',charset='utf8')
db = pymysql.connect("localhost","root","root","30days")

cursor = db.cursor()

sql = 'SELECT VERSION()'

cursor.execute(sql)

data = cursor.fetchone()

print("Database version: %s" %data)

db.close
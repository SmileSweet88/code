
import pymysql
# 连接数据库
connect = pymysql.connect(host='localhost', user='root', password="root",
                          database='zll_py_connect_db_exercise', port=3306)

# 获取游标
cur = connect.cursor()

# 执行sql语句
sql = 'select version();'
cur.execute(sql)

# 获取结果
print(cur.fetchone())

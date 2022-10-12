# -* - coding: UTF-8 -* -
# !/usr/bin/python3

import psycopg2
#连接数据库
conn = psycopg2.connect(database='test',user='postg',
                 password='y0',host='10.13.108.5',port='5432')

cursor = conn.cursor()   #创建一个游标

#execuet方法是针对数据库的请求
cursor.execute('create table test_1(id int,name varchar(20) )')
cursor.execute("insert into test_1 values(1,'lg')")
cursor.execute("drop table test_1")

conn.commit()  #提交
cursor.execute("select * from test_1")
rows = cursor.fetchall()   #返回所有行的元组
for row in rows:
    print(row[0],row[1])
cursor.close()
conn.close()

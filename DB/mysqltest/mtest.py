import pymysql
conn = pymysql.connect(host="localhost",  user="root", passwd="" , db="test1")
cur = conn.cursor()



#cur.execute("select * from tbl1 where id > 1 and id < 4 ")
#cur.execute("select * from tbl1 where id > %s and id < %s ",(1,5))

'''
for r in cur:
    if r[1]== 'hadi':
        print("hello")
        r =(7,'hhh')
    print(r)
'''

#sql = "INSERT INTO tbl1 (id,name) VALUES (%s, %s)"
#tid = input()
#tid = int(tid)
#tname = input()
#print(type(tid))

#sql = "INSERT INTO tbl1 (id,name) VALUES (2, 'reza')"

#cur.execute( sql ,(tid,tname))

'''
sql = "UPDATE  tbl1  SET name = %s WHERE id = %s"
tname = input()
tid = input()
tid=int(tid)
cur.execute( sql, ( tname,tid) )
'''
sql = "DELETE  FROM tbl1 WHERE id = %s"
tid = input()
tid=int(tid)
cur.execute( sql, (tid) )

'''
sql = "SELECT table_schema ,Round(Sum(data_length + index_length) , 1) FROM   information_schema.tables WHERE table_schema='tbl1' "
cur.execute(sql)
for r in cur:
    print(r[0])
    print(r[1])
'''
cur.close()
conn.commit()
conn.close()

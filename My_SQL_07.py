import mysql.connector as conn 
mydb = conn.connect(host = 'localhost' , user = 'root' , passwd = 'Anu@77852286')

#print(mydb)

cursor = mydb.cursor()

#cursor.execute("select job , education from ineuron.bulk_insert where age >52")
#cursor.execute("select * from ineuron.bulk_insert where marital = 'single' ")
#cursor.execute('select distinct job from ineuron.bulk_insert')
#cursor.execute("select * from ineuron.bulk_insert where job = 'retired' and balance >100")
#cursor.execute("select * from ineuron.bulk_insert order by age desc")
#cursor.execute("select* from ineuron.bulk_insert order by age desc")
#cursor.execute("select count(*) from ineuron.bulk_insert age")
#cursor.execute("select sum(balance) from ineuron.bulk_insert")
#cursor.execute("select  avg(balance)from ineuron.bulk_insert")
#cursor.execute("select  max(balance)from ineuron.bulk_insert")
#cursor.execute("select  min(balance)from ineuron.bulk_insert")
#cursor.execute("select * from ineuron.bulk_insert where balance = (select  min(balance)from ineuron.bulk_insert)")
#cursor.execute("select marital,count(*) from ineuron.bulk_insert group by marital")
#cursor.execute("select marital , count(*) , sum(balance), avg (balance) from ineuron.bulk_insert group by marital")
#cursor.execute("select marital , count(*) , sum(balance), avg (balance) from ineuron.bulk_insert group by marital having sum(balance) >5300")

#cursor.execute("update ineuron.bulk_insert set balance = 0 where job  = 'unknow'  ")
#mydb.commit()
# delete some record
cursor.execute("delete from ineuron.bulk_insert where job = 'unknown' ")
mydb.commit()







for i in cursor.fetchall():
    print(i)
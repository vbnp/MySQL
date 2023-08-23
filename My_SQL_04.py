import mysql.connector as conn 

mydb = conn.connect(host = 'localhost' , user = 'root' , passwd = 'Anu@77852286')
#print(mydb)

cursor = mydb.cursor()
#cursor.execute("create database TTL")



#cursor.execute("create table TTL.details(emp_ID int(10),emp_Name varchar(30),department varchar (20), salary int(10))")
cursor.execute("insert into TTL.details values(12435, 'Kunal Gupta', 'CAE', 1200000)")
cursor.execute("insert into TTL.details values(12224, 'Kunfl Gupta', 'CAE', 1300000)")
cursor.execute("insert into TTL.details values(12543, 'Kunfl Gupta', 'CAE', 1400000)")
cursor.execute("insert into TTL.details values(12346, 'Kunfl Gupta', 'CAE', 1500000)")
cursor.execute("insert into TTL.details values(12345, 'Kunfl Gupta', 'CAE', 1600000)")
cursor.execute("insert into TTL.details values(12324, 'Kunfl Gupta', 'CAE', 1400000)")
cursor.execute("insert into TTL.details values(12634, 'Kunfl Gupta', 'CAE', 1400000)")
cursor.execute("insert into TTL.details values(12234, 'Kunfl Gupta', 'CAE', 1100000)")
cursor.execute("insert into TTL.details values(12134, 'Kunfl Gupta', 'CAE', 1300000)")
cursor.execute("insert into TTL.details values(12384, 'Kunfl Gupta', 'CAE', 1800000)")
cursor.execute("insert into TTL.details values(12934, 'Kunfl Gupta', 'CAE', 1900000)")
mydb.commit()
# to show table
cursor.execute('select * from TTL.details')
for i in cursor.fetchall():
    print(i)


"""
 to show databases
cursor.execute('show databases')
print(cursor.fetchall())
"""
import mysql.connector as conn
 
mydb = conn.connect( host = "localhost" , user = "root" , passwd = "Anu@77852286")

#  print(mydb)

cursor = mydb.cursor()

#cursor.execute("create database ineuron")

#cursor.execute("create table ineuron.bank_details(age int(3),job varchar(30),marital varchar(30),education varchar (30),`default` varchar(30),balance int(10),housing varchar(30),loan varchar(30),contact varchar(30),`day` int(20),`month` varchar(30),duration int(3),campaign int(10),pdays int(10),previous int(10),poutcome varchar(30),y varchar(30))")
cursor.execute("insert into ineuron.bank_details values(33,'entrepreneur','married','secondary','no',2,'yes','yes','unknown',5,'may',76,1,-1,0,'unknown','no')")
mydb.commit()
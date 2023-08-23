import mysql.connector as conn 

# To stablish the connection between python and Mysql

mydb = conn.connect(host = "localhost" , user = "root" , passwd = "Anu@77852286")

# TO insert the data with respect to table
cursor = mydb.cursor()
cursor.execute("insert into viaan.details values(1001, 'vishal kumar', 'vishal@gmail.com', 150000 ,30 )")
mydb.commit()

# for fetching the table

cursor.execute("select * from viaan.details")
for i in cursor.fetchall():
    print(i)
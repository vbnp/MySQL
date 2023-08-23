import mysql.connector as conn 

mydb = conn.connect(host = "localhost" , user = "root" , passwd = "Anu@77852286")
#print(mydb)

cursor = mydb.cursor()
cursor.execute("select employe_id, emp_mailid , emp_salary from viaan.details")
l= []
for i in cursor.fetchall():
    l.append(i)
    
print(l)
print(type(l[0]))

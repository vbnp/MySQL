import mysql.connector as conn

# To stablish the connection between python and Mysql
mydb = conn.connect(host = "localhost", user = "root" , passwd = "Anu@77852286")
print(mydb)

# create a Database
cursor = mydb.cursor()
#cursor.execute("create database viaan")
#create table
cursor.execute("create table viaan.details(employe_id int(10) , emp_name varchar(100) ,emp_mailid varchar(20) ,emp_salary int(6) , emp_atten int(3))")
#to show database
cursor.execute("show databases")
print(cursor.fetchall())
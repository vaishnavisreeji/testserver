"""import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password")
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
#mycursor.execute("create database myfirstdb")
#print(mydb)"""

a=100
b=200
for i in range(a,b+1):
    if i>1:
        for num in range(2,i):
            if i%num==0:
                break
        else:
            print(i)
                


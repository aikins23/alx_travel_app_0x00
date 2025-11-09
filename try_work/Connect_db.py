import mysql.connector
mydb_ALX = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="employeemanagement1"

)
my_cursor = mydb_ALX.cursor()
my_cursor.execute("SELECT * FROM employees")
for x in my_cursor:
    print(x)
print("Connected to MySQL Server version:", mydb_ALX.server_info)
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="danielle",
    password="mypass",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE mydatabase")
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="danielle",
    password="mypass",
    database="mydatabase"
)
my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
my_cursor.execute(sql, val)
my_cursor.execute("SELECT * FROM customers")
myresult = my_cursor.fetchall()

for x in myresult:
  print(x)



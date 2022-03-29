import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="mydatabase"
)

myCursor = mydb.cursor()

# myCursor.execute("CREATE DATABASE mydatabase")
# myCursor.execute("SHOW DATABASES")


"""Create a table named customers"""
# myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

"""Create a table named customers with primary key"""
# sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
# myCursor.execute(sql)

"""Add primary key to existing table"""
# myCursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# myCursor.execute("SHOW TABLES")

"""Insert single row"""
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# myCursor.execute(sql, val)
# mydb.commit()
# print(myCursor.rowcount, "record inserted.")

"""Insert multiple rows"""
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
#
# myCursor.executemany(sql, val)
# mydb.commit()
#
# print(myCursor.rowcount, "are inserted.")
# print("1 record inserted, ID:", myCursor.lastrowid)

"""Display data in a table"""
# myCursor.execute("SELECT * FROM customers")  # Select rows
# myCursor.execute("SELECT name, address FROM customers")  # Select columns
# myCursor.execute("SELECT * FROM customers WHERE address = 'Park lane 38'")
# myCursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")

"""Use placeholders to escape query values and prevent SQL injection"""
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# myCursor.execute(sql, adr)

"""Sort the result"""
# sql = "SELECT * FROM customers ORDER BY name"
# sql = "SELECT * FROM customers ORDER BY name DESC"
# myCursor.execute(sql)

"""Delete records"""
# sql = "DELETE FROM customers WHERE address = %s"  # Without 'WHERE' deletes everything
# adr = "Mountain 21"
# myCursor.execute(sql, adr)
# mydb.commit()
# print(myCursor.rowcount, "record(s) deleted")

"""Delete table"""
# sql = "DROP TABLE customers"
# sql = "DROP TABLE IF EXISTS customers"
# myCursor.execute(sql)

"""Update table"""
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# adr = ("Canyon 22", "Valley 345")
# myCursor.execute(sql, adr)
# mydb.commit()

"""Limit selection to specific amount or start from a specific place"""
# sql = "SELECT * FROM customers LIMIT 5"
# sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
# myCursor.execute(sql)


myResult = myCursor.fetchall()  # fetchone() to selecta  single row
for x in myResult:
    print(x)

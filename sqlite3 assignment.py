import sqlite3
connection = sqlite3.connect("C:/Users/Student/Desktop/test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstNAME TEXT, LastName TEXT, Age INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")

connection.close()



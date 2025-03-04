import pymssql

server = "localhost"  # Use your Docker container IP or 'localhost'
database = "master"
username = "sa"
password = "Ea989571287!"

conn = pymssql.connect(server=server, user=username, password=password, database=database)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sys.databases;")

for row in cursor.fetchall():
    print(row)

conn.close()

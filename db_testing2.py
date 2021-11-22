import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234")

cur = conn.cursor()

print("Checking if the table files exists")
try:
    cur.execute('SELECT * FROM files')
    result = cur.fetchone()
    print(result)
    print('the table files doesnt exists')
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print('the table files doesnt exist')
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
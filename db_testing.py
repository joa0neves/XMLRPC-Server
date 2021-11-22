import psycopg2

try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234")
		
    # create a cursor
    cur = conn.cursor()
        
	# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT * FROM files')

    # display the PostgreSQL database server version
    result = cur.fetchone()
    print(result)
       
	# close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')


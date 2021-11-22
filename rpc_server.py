from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import csv
import xml.etree.ElementTree as ET
import convert_to_xml as converter
import psycopg2
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 9000),requestHandler=RequestHandler) as server:
    conn=psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234")
    server.register_introspection_functions()
    @server.register_function(name='uploadcsv')
    def remainder_function(csv_file):
        with open("csv_file.csv", "wb") as handle:
            handle.write(csv_file.data)
        try:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS files(id serial PRIMARY KEY, content XML NOT NULL, datetime timestamp NOT NULL)')
            cur.close()

            with open("csv_file.csv", "r") as file:
                xml = converter.convert_to_xml(file)

            cur = conn.cursor()
            statement= 'INSERT INTO files (content) VALUES(%s)'
            cur.execute(statement,xml)
            
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        return 'Upload Successful'
    @server.register_function(name='upload')
    def remainder_function(xml):
        try:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS files(id serial PRIMARY KEY, content XML NOT NULL, datetime timestamp NOT NULL)')
            cur.close()

            cur = conn.cursor()
            statement= 'INSERT INTO files (content) VALUES(%s)'
            cur.execute(statement,xml)
            
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        return 'Upload Successful'
    @server.register_function(name='download')
    def remainder_function():
        try:
            cur = conn.cursor()
            cur.execute('SELECT * FROM  files')
            result=cur.fetchone()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        return result
    server.serve_forever()


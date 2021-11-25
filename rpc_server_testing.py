from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from io import StringIO 
import xml.etree.ElementTree as ET
import xml.etree
import convert_to_xml as converter
from lxml import etree
import psycopg2
from datetime import datetime, timezone

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 9000),requestHandler=RequestHandler) as server:
    conn=psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234")
    server.register_introspection_functions()
    @server.register_function(name='upload')
    def remainder_function(name,xml):
        try:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS files(id serial PRIMARY KEY,name varchar(255) NOT NULL, content XML NOT NULL, datetime timestamp NOT NULL)')
            cur.close()

            cur = conn.cursor()
            dt = datetime.now(timezone.utc)
            statement= "INSERT INTO files (name,content,datetime) VALUES('{}' , '{}','{}')".format(name,xml,dt)
            cur.execute(statement)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        return 'Upload Successful'
    @server.register_function(name='get_Males')
    def remainder_function():
        n = 0
        try:
            cur = conn.cursor()
            cur.execute('SELECT * FROM  files')
            temp=cur.fetchone()
            xml_str = temp[2]
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error

        xml_temp= StringIO(xml_str)
        xml = ET.parse(xml_temp)
        result=xml.findall("./ocurrence[@gender='Male']")
        return result
    @server.register_function(name='get_Females')
    def remainder_function():
        result = []
        n = 0
        try:
            cur = conn.cursor()
            cur.execute('SELECT * FROM  files')
            temp=cur.fetchone()
            xml_str = temp[2]
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error

        xml_temp= StringIO(xml_str)
        xml = ET.parse(xml_temp)
        for ocurrence in xml.findall(".//database//ocurrence[@gender='Female']..."):
            result[n]=ocurrence
            n += 1
        return result
    server.serve_forever()


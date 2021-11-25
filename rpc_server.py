from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import csv
import xml.etree.ElementTree as ET
import convert_to_xml as converter
import psycopg2
from io import StringIO 
from lxml import etree
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
    @server.register_function(name='validate')
    def remainder_function(xmlstr):
        xml= StringIO(xmlstr)
        xml_doc = etree.parse(xml)
        xml_validator = etree.XMLSchema(file="schema.xsd")

        is_valid = xml_validator.validate(xml_doc)
        
        return is_valid
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
    @server.register_function(name='download')
    def remainder_function():
        try:
            cur = conn.cursor()
            cur.execute('SELECT * FROM  files')
            temp=cur.fetchone()
            result = temp[2]
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        return result
    server.serve_forever()


from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import csv
import xml.etree.ElementTree as ET
import convert_to_xml as converter
import psycopg2
from lxml import etree

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
    def remainder_function(xml):
        xml_file = lxml.etree.parse(xml)

        xml_validator = lxml.etree.XMLSchema(file="schema.xsd")

        is_valid = xml_validator.validate(xml_file)

        print(is_valid)
    server.serve_forever()


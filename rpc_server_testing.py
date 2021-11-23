from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET
import xml.etree
import convert_to_xml as converter
#from lxml import etree

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 9000),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    @server.register_function(name='validate')
    def remainder_function(xml):
        xml_file = xml.etree.parse(xml)

        xml_validator = xml.etree.XMLSchema(file="schema.xsd")

        is_valid = xml_validator.validate(xml_file)

        print(is_valid)
    server.serve_forever()


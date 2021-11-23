import xmlrpc.client
import xmlrpc
import convert_to_xml as converter

s = xmlrpc.client.ServerProxy('http://localhost:9000')
#with open("dataset2.csv", "r") as handle:
    #csv_file = xmlrpclib.Binary(handle.read())
#print(s.upload_csv(csv_file))
with open("csv_file.csv", "r") as file:
    xml = converter.convert_to_xml(file)
    print(s.validate(xml))
# Print list of available methods
print(s.system.listMethods())
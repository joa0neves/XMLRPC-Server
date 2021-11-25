import xmlrpc.client
import xmlrpc
import convert_to_xml as converter

s = xmlrpc.client.ServerProxy('http://localhost:9000')
#with open("testdataset.csv", "r") as file:
    #xml = converter.convert_to_xml(file)
    #print(s.upload("testdataset.csv",xml))
#print(s.download())
print(s.get_Males())
print(s.get_Females())
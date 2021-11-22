import xmlrpc.client
import xmlrpc
s = xmlrpc.client.ServerProxy('http://localhost:9000')
#with open("dataset2.csv", "r") as handle:
    #csv_file = xmlrpclib.Binary(handle.read())
#print(s.upload_csv(csv_file))
print(s.download())
# Print list of available methods
print(s.system.listMethods())
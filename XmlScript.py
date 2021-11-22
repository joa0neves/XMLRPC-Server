from xml.dom import minidom
import os 
import csv
  
  
root = minidom.Document()
  
xml = root.createElement('root') 
root.appendChild(xml)
  
ocurrenceChild = root.createElement('Ocurrence')
ocurrenceChild.setAttribute('name', 'Geeks for Geeks')
  
xml.appendChild(productChild)
  
xml_str = root.toprettyxml(indent ="\t") 
  
save_path_file = "test.xml"
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
import csv
import xml.etree.ElementTree as ET

def convert_to_xml(csv_file):
    database = ET.Element('database')
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_line = True 
    for row in csv_reader:
        ocurrence = ET.SubElement(database, 'Ocurrence')
        if first_line:
            first_line = False
        else:
            if row[0]!="" and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!="" and row[8]!="" and row[9]!="" and row[10]!="" and row[11]!="" and row[12]!="" and row[13]!="" and row[14]!="":
                uniqueID=ET.SubElement(ocurrence,'unique_id')
                uniqueID.text=row[0]
                name=ET.SubElement(ocurrence,'name')
                name.text=row[1]
                age=ET.SubElement(ocurrence,'age')
                age.text=row[2]
                race=ET.SubElement(ocurrence,'race')
                race.text=row[3]
                gender=ET.SubElement(ocurrence,'gender')
                gender.text=row[4]
                race_with_imputation=ET.SubElement(ocurrence,'race_with_imputation')
                race_with_imputation.text=row[5]
                date_of_injury=ET.SubElement(ocurrence,'date_of_injury')
                date_of_injury.text=row[8].replace("/","-")
                location_of_injury=ET.SubElement(ocurrence,'location_of_injury')
                location_of_injury.text=row[9]
                city_of_death=ET.SubElement(ocurrence,'city_of_death')
                city_of_death.text=row[10]
                state=ET.SubElement(ocurrence,'state')
                state.text=row[11]
                zipcode_of_death=ET.SubElement(ocurrence,'zipcode_of_death')
                zipcode_of_death.text=row[12]
                county_of_death=ET.SubElement(ocurrence,'county_of_death')
                county_of_death.text=row[13]
                full_address=ET.SubElement(ocurrence,'full_address')
                full_address.text=row[14]
    return ET.tostring(database,encoding='UTF-8',method='xml')
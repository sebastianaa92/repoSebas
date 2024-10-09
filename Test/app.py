import json
import xmltodict

with open ("/home/sebastian/Downloads/Biblioteca_Reporte.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    
    json_data = json.dumps(data_dict)

    with open("data.json","w") as json_file:
        json_file.write(json_data)
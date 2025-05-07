# WPS Execute Operation

import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\coordinate_transforms.xml").read()


wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s3439887/gpw/wps.py?" 
#wpsServerUrl = "https://mara.rangelands.itc.utwente.nl/geoserver/ows?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)
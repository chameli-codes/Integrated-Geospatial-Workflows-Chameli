# WPS Execute Operation

import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\bbox_execute.xml").read()

wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s3439887/gpw/wps.py?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)
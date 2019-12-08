import requests
import xml.etree.ElementTree as ET
response = requests.get('https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=08.12.2019&channel=ct24')
root = ET.fromstring(response.text)
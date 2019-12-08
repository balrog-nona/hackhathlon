import requests
import xml.etree.ElementTree as ET
response = requests.get('https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=08.12.2019&channel=ct24')
response.encoding='utf-8'
root = ET.fromstring(response.text)

for porad in root:
  nazev = porad.find('nazvy').find('nazev')
  cas=porad.find('cas')
  print(nazev.text, cas.text)
import requests
import xml.etree.ElementTree as ET
response = requests.get('https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=08.12.2019&channel=ct24')
response.encoding='utf-8'
root = ET.fromstring(response.text)

datum = root.attrib.get('datum_vysilani')
kanal = root.attrib.get('kanal')
seznam_poradu = ['Regiony']

for porad in root:
  nazev = porad.find('nazvy').find('nazev')
  if 'Zprávy' in nazev.text:
    cas=porad.find('cas')
  #if nazev in seznam_poradu:
    print(datum, kanal, cas.text, nazev.text)
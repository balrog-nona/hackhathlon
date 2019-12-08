import smtplib
import requests
import xml.etree.ElementTree as ET

response = requests.get('https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=08.12.2019&channel=ct24')
response.encoding='utf-8'
root = ET.fromstring(response.text)

datum = root.attrib.get('datum_vysilani')
kanal = root.attrib.get('kanal')

# vyzva uzivateli k zadani filmu a emailu
seznam_filmu = []
while True:
    film = input('Zadej nazev filmu (i s diakritikou): ')
    if film == "":
        break
    seznam_filmu.append(film)

text = list()
# vyhledani jednotlivych filmu v programu
for porad in root:
  nazev = porad.find('nazvy').find('nazev')
  for film in seznam_filmu:
    if film in nazev.text:
        cas=porad.find('cas')
        radek = (datum, kanal, cas.text, nazev.text)
        text.append(radek)


# notifikacni email s vysledkem
zaslat_email = input('Prejes si zaslat email s vysledkem? a/n ')

for radek in text:
    text_emailu = 

text_emailu = 'zprava'  # vytvori se po vyhodnoceni programu

if zaslat_email == 'a':
    email_uzivatele = input('Zadej svuj email: ')
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login('hlidejfilmy@gmail.com', 'hlidacfilmu88')
    smtpObj.sendmail('hlidejfilmy@gmail.com', email_uzivatele, text_emailu)
    smtpObj.quit()
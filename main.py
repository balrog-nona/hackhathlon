import smtplib
import requests
import xml.etree.ElementTree as ET
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# tvorba url adres pro ruzne dny a druzne kanaly
dates = ('08.12.2019', '09.12.2019', '10.12.2019', '11.12.2019')
channels = ('ct1', 'ct2', 'ct24', 'ct4', 'ct5', 'ct6')
url_first = 'https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date='
url_last = '&channel='

seznam_url = []
for channel in channels:
    for date in dates:
        url = url_first + date + url_last + channel
        seznam_url.append(url)

# vyzva uzivateli k zadani filmu a emailu
seznam_filmu = []
while True:
    film = input('Zadej nazev filmu (i s diakritikou): ')
    if film == "":
        break
    seznam_filmu.append(film)

zaslat_email = input('Prejes si zaslat email s vysledkem? a/n ')
if zaslat_email == 'a':
    email_uzivatele = input('Zadej svuj email: ')

# vyhledani filmu v programu

def vyhledej_film():
    text = list()
    for url in seznam_url:
        response = requests.get(url)
        response.encoding = 'utf-8'
        root = ET.fromstring(response.text)
        datum = root.attrib.get('datum_vysilani')
        kanal = root.attrib.get('kanal')
        for porad in root:
            nazev = porad.find('nazvy').find('nazev')
            for film in seznam_filmu:
                if film.lower() in nazev.text.lower():
                    cas = porad.find('cas')
                    radek = [datum, kanal, cas.text, nazev.text]
                    text.append(radek)
    return text


# notifikacni email s vysledkem
text_emailu = ""
vysledky = vyhledej_film()
for radek in vysledky:
    radek_string = "Dne {} na {} v {} dávají {}.\n".format(*radek)
    text_emailu = text_emailu + radek_string

print(text_emailu)

if zaslat_email == 'a':
    sender = 'hlidejfilmy@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = 'hlidejfilmy@gmail.com'
    msg['To'] = email_uzivatele
    msg['Subject'] = 'No response - seznam filmu'
    body = text_emailu
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string().encode('utf-8')

    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login('hlidejfilmy@gmail.com', 'hlidacfilmu88')
    smtpObj.sendmail('hlidejfilmy@gmail.com', email_uzivatele, text)
    smtpObj.quit()

import requests

# tvorba url adres pro ruzne dny a druzne kanaly
dates = ('08.12.2019', '09.12.2019', '10.12.2019', '11.12.2019')
channels = ('ct1', 'ct2', 'ct24', 'ct4', 'ct5', 'ct6')
url_first = 'https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date='
url_last = '&channel='

seznam_url_souboru = []
for channel in channels:
    for date in dates:
        url = url_first + date + url_last + channel
        soubor = "{}{}.xml".format(date, channel)
        item = [url, soubor]
        seznam_url_souboru.append(item)

for item in seznam_url_souboru:
    response = requests.get(item[0])
    response.encoding = 'utf-8'
    with open('soubory/{}'.format(item[1]), 'w', encoding='utf-8') as file:
        text = response.text
        file.write(text)



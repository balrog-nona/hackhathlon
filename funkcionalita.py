import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# vyzva uzivateli k zadani filmu a emailu
seznam_filmu = []
while True:
    film = input('Zadej nazev filmu (i s diakritikou): ')
    if film == "":
        break
    seznam_filmu.append(film)

email = input('Zadej svuj email: ')
password = input('Zadej sve heslo na email: ')
print(seznam_filmu)

# vyhledani jednotlivych filmu v programu
def hledani_filmu():
    pass


# notifikacni email s vysledkem
text_emailu = None  # vytvori se po vyhodnoceni programu
if 'gmail.com' in email:
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login(email, password)
    smtpObj.sendmail(email, email, text_emailu)
    smtpObj.quit()
elif 'seznam.cz' in email:
    sender = email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = sender
    msg['Subject'] = 'TV program'
    body = text_emailu
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    smtpObj = smtplib.SMTP_SSL('smtp.seznam.cz', 465)
    smtpObj.ehlo()
    smtpObj.login(email, password)
    smtpObj.sendmail(sender, sender, text)
    smtpObj.quit()





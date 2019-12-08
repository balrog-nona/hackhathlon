import smtplib

# vyzva uzivateli k zadani filmu a emailu
seznam_filmu = []
while True:
    film = input('Zadej nazev filmu (i s diakritikou): ')
    if film == "":
        break
    seznam_filmu.append(film)


# vyhledani jednotlivych filmu v programu
def hledani_filmu():
    pass


# notifikacni email s vysledkem
zaslat_email = input('Prejes si zaslat email s vysledkem? a/n ')
text_emailu = 'zprava'  # vytvori se po vyhodnoceni programu

if zaslat_email == 'a':
    email_uzivatele = input('Zadej svuj email: ')
    print(email_uzivatele)
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.set_debuglevel(True)
    smtpObj.ehlo()
    smtpObj.login('hlidejfilmy@gmail.com', 'hlidacfilmu88')
    smtpObj.sendmail('hlidejfilmy@gmail.com', email_uzivatele, text_emailu)
    smtpObj.quit()





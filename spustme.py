from flask import Flask, request
import main
from flask_mako import MakoTemplates, render_template

app = Flask(__name__)
mako = MakoTemplates(app)
app.template_folder = "templates"
'''
vysledek = [
  {
    'nazev': 'Zpravy',
    'datum': '2019-12-08',
    'kanal': 'CT1',
    'cas': '12:00' 
  },
  {
    'nazev': 'Byznys',
    'datum': '2019-12-08',
    'kanal': 'CT1',
    'cas': '14:00' 
  },
  {
    'nazev': 'Vecernicek',
    'datum': '2019-12-08',
    'kanal': 'CT1',
    'cas': '19:40' 
  }
    ]
'''

@app.route('/')
def hello():
  return render_template('homepage.mako',)


@app.route('/hledani', methods=['POST'])
def hledej():
  dotaz = request.form['seznam_filmu']
  result = [film.strip() for film in dotaz.split('\n')]
  vysledek = main.vyhledej_film(result)
  return render_template('hledani.mako', vysledek=vysledek, dotaz=dotaz)

@app.route('/posli', methods=['POST'])
def posli_mail():
  email = request.form['email'].strip()
  dotaz = request.form['dotaz']
  result = [film.strip() for film in dotaz.split('\n')]
  vysledek = main.vyhledej_film(result)
  print(vysledek)
  main.posli_email(email, vysledek)
  print(email)

  #vysledek = fceOdNony(result)
  return render_template('posli.mako', email=email)


app.run()
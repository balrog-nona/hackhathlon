from flask import Flask
#import main
from flask_mako import MakoTemplates, render_template

app = Flask(__name__)
mako = MakoTemplates(app)
app.template_folder = "templates"

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

@app.route('/')
def hello():
  return render_template('homepage.mako', name='Peta a Anet')

@app.route('/hledani')
def vysledky():
  return render_template('hledani.mako', vysledek=vysledek)

app.run()
from flask import Flask
#import main
from flask_mako import MakoTemplates, render_template

app = Flask(__name__)
mako = MakoTemplates(app)
app.template_folder = "templates"

@app.route('/')
def hello():
  return render_template('homepage.mako', name='Peta a Anet')



app.run()
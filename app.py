from flask import Flask,render_template
import requests

app = Flask(__name__)

def get_pokemon_data(pokemon):
    url=f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url).json()
    return r

@app.route("/")
def home():
    return render_template('pokemon.html')

@app.route("/home1")
def home1():
    return render_template('detalle.html')

@app.route("/prueba")
def prueba():
    return get_pokemon_data('pikachu')
           
if __name__=='__main__':
    app.run(debug=True)
    
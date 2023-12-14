from flask import Flask,render_template,requests
from dotenv import load_dotenv, dotenv_values


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


app = Flask(__name__)
app.config["SQL"]


def get_pokemon_data(pokemon):
    url=f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url).json()
    return r

@app.route("/")
def prueba():
    data = get_pokemon_data('lucario')
    pokemon={'id':data.get('id'), 
             'name':data.get('name').upper(),
             'height': data.get('height'), #con esta sentencia buscamos el json
             'weight0':data.get('weight'),
             'order':data.get('order'),
             'type':'Profesor',
             'photo':data.get('sprites').get('other').get('official-artwork').get('front_default'),
             }
    return render_template('pokemon.html', pokemon=pokemon)

@app.route("/home1")
def home1():
    return render_template('detalle.html')


@app.route("/insert")
def insert():
    new_pokemon='ditto'

    if new_pokemon:
        obj=Pokemon(name=new_pokemon, )


if __name__=='__main__':
    app.run(debug=True)
    

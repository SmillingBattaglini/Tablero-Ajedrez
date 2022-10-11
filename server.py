
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def tablero():
    return render_template('index.html', num = 8, numero = 8, color1 = 'red', color2 = 'black')

@app.route('/4')
def tablero1():
    return render_template('index.html', num = 4, numero= 4 ,color1 = 'purple', color2 = 'peachpuff')

@app.route('/table/<int:num>/<int:numero>')
def tablero2(num, numero):
    numero = int(numero)
    return  render_template('index.html', num = num, numero = numero, color1 = 'blue', color2= 'yellow')


@app.route('/table/<int:numero>/<int:num>/<string:color1>/<string:color2>') 
def tablero3(numero, num, color1, color2):
    return  render_template('index.html', numero = numero, num = num, color1 = color1, color2 = color2) 



if __name__=="__main__":
    app.run(debug=True)
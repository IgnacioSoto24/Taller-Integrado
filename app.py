from flask import Flask, render_template
from datos import videojuegos

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/juegos')
def lista_juegos():
    return render_template('juegos.html', juegos=videojuegos)

@app.route('/juego/<slug>')
def detalle_juego(slug):
    juego = next((j for j in videojuegos if j['slug'] == slug), None)
    return render_template('detalle.html', juego=juego)

if __name__ == '__main__':
    app.run(debug=True)
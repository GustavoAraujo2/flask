from estudo import app
from flask import render_template

@app.route('/')
def home():
    usuario = 'Gustavo'
    idade = 22

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)
@app.route('/login/')
def login():
    return render_template('login.html')
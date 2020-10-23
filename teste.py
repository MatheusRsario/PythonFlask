from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def raiz():
    return '<h1>hellow world</h1>'

@app.route('/2')
def raiz2():
    return '<input type="number"> <input type="submit" value="enviar">'

@app.route('/3/<nome>')
def raiz3(nome):
    r = {
        'numero': 18,
        'nome': nome
        }
    return jsonify(r)

@app.route('/4')
def raiz4():
    return render_template('index.html')


app.run(debug=True)
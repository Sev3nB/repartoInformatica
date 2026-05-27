import json
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

def carica_dati(jsonFile):
    try:
        with open(jsonFile, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/progetti')
def progetti():
    sezioni_pagina = carica_dati("progetti.json")
    return render_template('progetti.html', sezioni=sezioni_pagina)

@app.route('/competizioni')
def competizioni():
    competizioni = carica_dati("competizioni.json")
    return render_template('competizioni.html', competizioni=competizioni)

@app.route('/competizione/<int:comp_id>')
def dettaglio(comp_id):
    competizioni = carica_dati("competizioni.json")

    gara = next((item for item in competizioni if item["id"] == comp_id), None)

    if gara is None:
        abort(404)

    return render_template('dettaglio_comp.html', gara=gara)

@app.route("/contatti")
def contatti():
    return render_template("contatti.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
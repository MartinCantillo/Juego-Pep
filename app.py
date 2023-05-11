from flask import Flask, request, jsonify, json, render_template
#importo las dependencias de trabajo
from config.db import app, bd



@app.route("/", methods=['GET'])
def index():
    nombre= "Loggin"
    return render_template('Login.html')

@app.route("/Registro", methods=['GET'])
def registrar():
    nombre= "registrar"
    return  render_template('Registro.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)
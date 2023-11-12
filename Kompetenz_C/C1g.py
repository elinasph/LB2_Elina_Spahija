# Ursprüngliche Flask-Funktion
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/berechne', methods=['POST'])
def berechne():
    data = request.json
    operation = data.get('operation')
    x = data.get('x', 0)
    y = data.get('y', 0)

    if operation == 'addieren':
        ergebnis = x + y
    elif operation == 'subtrahieren':
        ergebnis = x - y
    elif operation == 'multiplizieren':
        ergebnis = x * y
    elif operation == 'dividieren':
        ergebnis = x / y if y != 0 else 'Division durch Null!'
    else:
        ergebnis = 'Unbekannte Operation'

    return jsonify({'ergebnis': ergebnis})

if __name__ == '__main__':
    app.run(debug=True)






# Refaktorisierte Flask-Funktion
from flask import Flask, request, jsonify

app = Flask(__name__)

def addiere(x, y):
    return x + y

def subtrahiere(x, y):
    return x - y

def multipliziere(x, y):
    return x * y

def dividiere(x, y):
    return x / y if y != 0 else 'Division durch Null!'

@app.route('/c1g', methods=['POST'])
def berechne():
    data = request.json
    operation = data.get('operation')
    x = data.get('x', 0)
    y = data.get('y', 0)

    operationen = {
        'addieren': addiere,
        'subtrahieren': subtrahiere,
        'multiplizieren': multipliziere,
        'dividieren': dividiere
    }
    ergebnis_funktion = operationen.get(operation, lambda a, b: 'Unbekannte Operation')
    ergebnis = ergebnis_funktion(x, y)
    return jsonify({'ergebnis': ergebnis})

if __name__ == '__main__':
    app.run(debug=True)


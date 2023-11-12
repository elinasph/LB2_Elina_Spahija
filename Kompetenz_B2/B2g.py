from flask import Flask, request, jsonify

app = Flask(__name__)

# Definieren einiger grundlegender mathematischer Funktionen
def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def multiplizieren(x, y):
    return x * y

def dividieren(x, y):
    return x / y if y != 0 else 'Division durch Null!'

# Funktion, die eine mathematische Operation ausführt
def ausfuehren_operation(oper, x, y):
    return oper(x, y)

@app.route('/b2g', methods=['GET'])
def berechne():
    data = request.json
    operation = data.get('operation')
    x = data.get('x')
    y = data.get('y')

    operationen = {
        'addieren': addieren,
        'subtrahieren': subtrahieren,
        'multiplizieren': multiplizieren,
        'dividieren': dividieren
    }

    # Wählen der entsprechenden Funktion basierend auf der Anfrage
    if operation in operationen:
        ergebnis = ausfuehren_operation(operationen[operation], x, y)
        return jsonify({'Ergebnis': ergebnis})
    else:
        return jsonify({'Fehler': 'Unbekannte Operation'})

if __name__ == '__main__':
    app.run(debug=True)

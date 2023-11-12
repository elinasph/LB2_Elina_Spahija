from flask import Flask, request
from functools import reduce

app = Flask(__name__)

@app.route('/b4e', methods=['GET'])
def datenanalyse():
    # Eine Liste von Zahlen aus den Query-Parametern extrahieren und in Integer umwandeln
    nummern = request.args.getlist('nummer', type=int)

    # Map: Jede Zahl in der Liste quadrieren
    quadriert = map(lambda x: x**2, nummern)

    # Filter: Nur Zahlen behalten, die größer als 10 sind
    über_zehn = filter(lambda x: x > 10, nummern)

    # Reduce: Summe aller quadrierten Zahlen berechnen
    summe_quadriert = reduce(lambda x, y: x + y, map(lambda x: x**2, nummern), 0)

    return {
        "Original": nummern,
        "Quadriert": list(quadriert),
        "Über Zehn": list(über_zehn),
        "Summe der Quadrate": summe_quadriert
    }

if __name__ == '__main__':
    app.run(debug=True)



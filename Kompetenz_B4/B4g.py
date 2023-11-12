from flask import Flask, request
from functools import reduce

app = Flask(__name__)

@app.route('/b4g', methods=['GET'])
def verarbeite_liste():
    # Eine Liste von Zahlen aus den Query-Parametern extrahieren und in Integer umwandeln
    nummern = request.args.getlist('nummer', type=int)

    # Map: Jede Zahl in der Liste quadrieren
    quadriert = map(lambda x: x**2, nummern)

    # Filter: Nur gerade Zahlen behalten
    gerade_nummern = filter(lambda x: x % 2 == 0, nummern)

    # Reduce: Summe aller Zahlen in der Liste berechnen
    summe = reduce(lambda x, y: x + y, nummern, 0)

    return {
        "Original": nummern,
        "Quadriert": list(quadriert),
        "Gerade Nummern": list(gerade_nummern),
        "Summe": summe
    }

if __name__ == '__main__':
    app.run(debug=True)

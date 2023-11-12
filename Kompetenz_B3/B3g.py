from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/quadrat', methods=['POST'])
def quadrat_berechnen():
    data = request.json
    zahl = data.get('zahl')
    quadrat = lambda x: x * x
    ergebnis = quadrat(zahl)
    return jsonify({'quadrat': ergebnis})

@app.route('/grossbuchstaben', methods=['POST'])
def zu_grossbuchstaben():
    data = request.json
    text = data.get('text')
    in_grossbuchstaben = lambda s: s.upper()
    ergebnis = in_grossbuchstaben(text)
    return jsonify({'grossbuchstaben': ergebnis})

if __name__ == '__main__':
    app.run(debug=True)



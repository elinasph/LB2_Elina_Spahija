from flask import Flask, request, jsonify
from functools import reduce

app = Flask(__name__)

@app.route('/b4f', methods=['POST'])
def verarbeite_daten():
    data = request.json
    zahlen = data.get('zahlen', [])

    # Verwendung von map, filter und reduce
    quadriert = map(lambda x: x**2, zahlen)
    gefiltert = filter(lambda x: x > 10, quadriert)
    summe = reduce(lambda x, y: x + y, gefiltert, 0)

    return jsonify({'ergebnis': summe})

if __name__ == '__main__':
    app.run(debug=True)

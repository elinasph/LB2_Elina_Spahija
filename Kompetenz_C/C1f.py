# Ursprüngliche Flask-Funktion
from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a + b
    return f"Das Ergebnis von {a} + {b} ist {result}"

if __name__ == '__main__':
    app.run(debug=True)






# Refaktorisierte Flask-Funktion
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def addiere_zahlen():
    erste_zahl = request.args.get('erste_zahl', type=int)
    zweite_zahl = request.args.get('zweite_zahl', type=int)

    if erste_zahl is None or zweite_zahl is None:
        return jsonify({"error": "Bitte geben Sie beide Zahlen an."}), 400

    ergebnis = erste_zahl + zweite_zahl
    return jsonify({
        "erste_zahl": erste_zahl,
        "zweite_zahl": zweite_zahl,
        "ergebnis": ergebnis
    })

if __name__ == '__main__':
    app.run(debug=True)

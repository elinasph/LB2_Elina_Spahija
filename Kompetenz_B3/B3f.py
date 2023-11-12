from flask import Flask, request

app = Flask(__name__)

@app.route('/b3f', methods=['GET'])
def berechne():
    # Ein Lambda-Ausdruck, der drei Argumente nimmt und eine Berechnung durchführt
    operation = lambda x, y, z: (x + y) * z

    # Werte aus den Query-Parametern der Anfrage extrahieren
    x = request.args.get('x', default=0, type=int)
    y = request.args.get('y', default=0, type=int)
    z = request.args.get('z', default=1, type=int)

    # Lambda-Ausdruck mit den extrahierten Werten ausführen
    ergebnis = operation(x, y, z)
    return f"Das Ergebnis der Berechnung ist: {ergebnis}"

if __name__ == '__main__':
    app.run(debug=True)

    
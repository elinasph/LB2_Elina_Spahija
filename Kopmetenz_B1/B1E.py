from flask import Flask, request, jsonify

app = Flask(__name__)

# Funktion zum Einlesen der Daten
def lese_daten(daten):
    # Hier könnte eine tatsächliche Logik zum Einlesen und Konvertieren von Daten stehen
    return [int(x) for x in daten.split(',')]

# Funktion zur Durchführung grundlegender statistischer Berechnungen
def berechne_statistiken(daten):
    mean = sum(daten) / len(daten)
    median = sorted(daten)[len(daten) // 2]
    return {'mittelwert': mean, 'median': median}

@app.route('/b1e', methods=['GET'])
def daten_analyse():
    daten = request.json.get('daten')
    verarbeitete_daten = lese_daten(daten)
    statistiken = berechne_statistiken(verarbeitete_daten)
    return jsonify(statistiken)

if __name__ == '__main__':
    app.run(debug=True)



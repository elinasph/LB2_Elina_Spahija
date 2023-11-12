# Ursprüngliche Flask-Funktion
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def analyse():
    data = request.json
    text = data.get('text', '')

    # Umständliche Logik zur Textanalyse
    zeichen_count = len(text)
    wort_count = len(text.split())
    durchschnitt_wortlaenge = sum(len(wort) for wort in text.split()) / len(text.split()) if wort_count > 0 else 0

    ergebnis = {
        'zeichen_count': zeichen_count,
        'wort_count': wort_count,
        'durchschnitt_wortlaenge': durchschnitt_wortlaenge
    }

    return jsonify(ergebnis)

if __name__ == '__main__':
    app.run(debug=True)





# Refaktorisierte Flask-Funktion
from flask import Flask, request, jsonify

app = Flask(__name__)

def zaehle_zeichen(text):
    return len(text)

def zaehle_woerter(text):
    return len(text.split())

def berechne_durchschnittliche_wortlaenge(text):
    worte = text.split()
    return sum(len(wort) for wort in worte) / len(worte) if worte else 0

@app.route('/analyse', methods=['POST'])
def analyse():
    data = request.json
    text = data.get('text', '')

    ergebnis = {
        'zeichen_count': zaehle_zeichen(text),
        'wort_count': zaehle_woerter(text),
        'durchschnitt_wortlaenge': berechne_durchschnittliche_wortlaenge(text)
    }

    return jsonify(ergebnis)

if __name__ == '__main__':
    app.run(debug=True)

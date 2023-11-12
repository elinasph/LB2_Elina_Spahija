from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sortiere_nach', methods=['POST'])
def sortiere_nach():
    data = request.json
    liste = data.get('liste', [])
    schlüssel = data.get('schlüssel')
    umgekehrt = data.get('umgekehrt', False)

    # Verwendung eines Lambda-Ausdrucks für das Sortieren
    sortierte_liste = sorted(liste, key=lambda x: x.get(schlüssel), reverse=umgekehrt)

    return jsonify(sortierte_liste)

if __name__ == '__main__':
    app.run(debug=True)


# Für Postman
{
  "liste": [{"name": "Anna", "alter": 28}, {"name": "Lukas", "alter": 24}, {"name": "Sophie", "alter": 31}],
  "schlüssel": "alter"
}


from flask import Flask

app = Flask(__name__)

# Erstellen eines Closures für einen Zähler
def zaehler_erzeugen():
    count = 0
    def zaehler():
        nonlocal count
        count += 1
        return count
    return zaehler

# Initialisieren des Zählers
mein_zaehler = zaehler_erzeugen()

@app.route('/b2e', methods=['GET'])
def zaehlen():
    zaehlerstand = mein_zaehler()
    return f"Zählerstand: {zaehlerstand}"

if __name__ == '__main__':
    app.run(debug=True)



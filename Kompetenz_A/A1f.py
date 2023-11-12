from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/a1f', methods=['GET'])
def immutable_demo():
    # Ein unveränderliches Tuple
    immutable_tuple = (1, 2, 3)

    # Versuch, das Tuple zu ändern (würde in einem Fehler resultieren)
    # immutable_tuple[0] = 4

    # Unveränderlicher String
    immutable_string = "Hello, World!"

    # Versuch, den String zu ändern (würde in einem Fehler resultieren)
    # immutable_string[0] = "h"

    return jsonify({
        "Immutable Tuple": immutable_tuple,
        "Immutable String": immutable_string
    })

if __name__ == '__main__':
    app.run(debug=True)



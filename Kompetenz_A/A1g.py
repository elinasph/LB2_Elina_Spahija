from flask import Flask, jsonify

app = Flask(__name__)


def addiere(a, b):
    return a + b


@app.route('/a1g', methods=['GET'])
def addiere_page():
    result = addiere(1, 2)
    return jsonify(str(result))


if __name__ == '__main__':
    app.run(debug=True)



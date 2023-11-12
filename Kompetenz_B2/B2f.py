from flask import Flask

app = Flask(__name__)

def höherwertige_funktion(funktion):
    def wrapper(*args, **kwargs):
        result = funktion(*args, **kwargs)
        return f"Das Ergebnis ist: {result}"
    return wrapper

def verdoppeln(x):
    return x * 2

@app.route('/b2f', methods=['GET'])
def verdoppeln_route(nummer):
    verdoppeln_wrapped = höherwertige_funktion(verdoppeln)
    return verdoppeln_wrapped(nummer)

if __name__ == '__main__':
    app.run(debug=True)



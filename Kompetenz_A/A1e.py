from flask import Flask, jsonify

app = Flask(__name__)

class SumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        return sum(self.numbers)

def calculate_sum_procedural(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_sum_functional(numbers):
    return sum(numbers)

@app.route('/a1e', methods=['GET'])
def calculate_sum_route():
    numbers = [1, 2, 3, 4, 5]

    oo_calculator = SumCalculator(numbers)
    oo_sum = oo_calculator.calculate_sum()

    procedural_sum = calculate_sum_procedural(numbers)

    functional_sum = calculate_sum_functional(numbers)

    return jsonify({
        "Object-Oriented Sum": oo_sum,
        "Procedural Sum": procedural_sum,
        "Functional Sum": functional_sum
    })

if __name__ == '__main__':
    app.run(debug=True)



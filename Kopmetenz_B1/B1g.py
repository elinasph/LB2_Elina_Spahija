from flask import Flask, request, jsonify

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@app.route('/b1g', methods=['GET'])
def sort_list():
    data = request.json
    unsorted_list = data.get('numbers', [])
    sorted_list = bubble_sort(unsorted_list)
    return jsonify(sorted_list)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def poisson_probability(lambda_val, k):
    """
    Calculate the Poisson probability P(X = k)
    :param lambda_val: Mean (λ) - float
    :param k: Number of occurrences - int
    :return: Probability P(X = k) - float
    """
    try:
        lambda_val = float(lambda_val)
        k = int(k)
        if lambda_val < 0 or k < 0:
            return {"error": "λ and k must be non-negative."}
        prob = (math.pow(lambda_val, k) * math.exp(-lambda_val)) / math.factorial(k)
        return {"result": round(prob, 6)}
    except ValueError:
        return {"error": "Invalid input. λ must be a float and k must be an integer."}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    lambda_val = data.get('lambda')
    k = data.get('k')
    result = poisson_probability(lambda_val, k)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

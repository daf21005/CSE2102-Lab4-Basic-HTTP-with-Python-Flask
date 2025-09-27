from flask import Flask, request, jsonify

# AI given within the lab instructions
def trial_division(n):
    factors = []
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd numbers up to sqrt(n)
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2

    if n > 1:
        factors.append(n)
    return factors

def trial_division_prime_checker(n):
    factors = trial_division(n)
    # If the factors list contains only n itself, it's a prime
    if len(factors) == 1 and factors[0] == n:
        return factors
    # properly include 1 as a factor for composite numbers as following the lab instructions
    result = [1]
    result.extend(factors)
    return result

app = Flask(__name__)

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']


@app.route("/factors/<int:inINT>")
def get_factors(inINT):
    factors = trial_division_prime_checker(inINT)
    return jsonify(factors)


if __name__ == "__main__":
   # im being suggested to include port=5000, debug=True in the run method
   # ask professor if needed
   app.run(host='0.0.0.0')
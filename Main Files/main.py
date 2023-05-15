from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/math", methods=['POST'])
def meth_operation():
    if (request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1 - num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1 * num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1 / num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + " is " + str(r)

        return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)

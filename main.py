from flask import Flask, render_template, request
from controllers.calculator_controller import CalculatorController

app = Flask(__name__)

controller = CalculatorController()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        result = controller.calculate(
            operation,
            num1,
            num2
        )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
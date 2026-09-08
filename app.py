from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            y = [
                float(request.form["w1"]),
                float(request.form["w2"]),
                float(request.form["w3"]),
                float(request.form["w4"]),
                float(request.form["w5"])
            ]

            X = [[1], [2], [3], [4], [5]]

            model = LinearRegression()
            model.fit(X, y)

            result = {
                "slope": model.coef_[0],
                "intercept": model.intercept_,
                "week6": model.predict([[6]])[0],
                "week7": model.predict([[7]])[0]
            }
        except ValueError:
            result = {"error": "Please enter valid numbers."}

    return render_template("index.html", result=result)

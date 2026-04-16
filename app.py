from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def password():

    if request.method == "POST":

        password = request.form["password"]

        if len(password) >= 6:
            return "Parol to‘g‘ri"
        else:
            return "Parol juda qisqa"

    return render_template("index.html")

app.run(debug=True)

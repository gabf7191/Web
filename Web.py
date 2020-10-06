from flask import Flask, redirect,url_for, request ,render_template, session


app = Flask(__name__)
#app.secret_key = "hola"


@app.route("/")
def home():
    return render_template("Main.html")

@app.route("/Prensas")
def Prensas():
    return render_template("Prensas.html")


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        if user == "expandir":
            return redirect(url_for("Andreani"))
        else:
            return render_template("login.html", text = "Password Incorrecta")
    else:
        return render_template("login.html", text ="")

@app.route ("/Cv")
def Cv():
    return render_template("Cv.html")

@app.route ("/Andreani")
def Andreani():
    return render_template("Andreani.html")

@app.route ("/Map")
def Map():
    return render_template("Map.html")


if __name__ == "__main__":
    app.run(debug= True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido a la aplicación"

@app.route("/saludo")
def saludo():
    mensaje = "Bienvenido a la aplicación"
    return render_template("saludo.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
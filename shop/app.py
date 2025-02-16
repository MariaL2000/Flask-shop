from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def principal():
    return render_template("index.html")


@app.route("/accesor")
def accesorios():
    return render_template("accesorios.html")


@app.route("/libros")
def libros():
    return render_template("libros.html")


@app.route("/comida")
def comida():
    return render_template("comida.html")


@app.route("/ropa")
def ropa():
    return render_template("ropa.html")


IMAGES_FOLDER = os.path.join("static", "img", "acces")


# Datos de ejemplo para los elementos de la tienda
productos = {
    "bandoleras": {
        "nombre": "Bandoleras",
        "precio": "$300",
        "imagen": "static/img/acces/bandoleras.jpg",
    },
    "felpas": {
        "nombre": "felpas",
        "precio": "$20",
        "imagen": "static/img/acces/felpas.jpg",
    },
    "pellizcos": {
        "nombre": "pellizcos",
        "precio": "$280",
        "imagen": "static/img/pellizc.jpg",
    },
}


@app.route("/buscar", methods=["POST"])
def buscar():
    query = request.form.get("query").lower()
    resultados = []

    # Buscar en los productos
    for key, producto in productos.items():
        if query in key:
            resultados.append(producto)
    return render_template("resultados.html", resultados=resultados)


if __name__ == "__main__":
    app.run(debug=True)

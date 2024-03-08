# app.py
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB("caminhos.json")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/novo")
def novo2():
    return render_template("novo.html")
    


@app.route("/novo" , methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        id = request.form.get("id")
        nome = request.form.get("nome")
        coordenadas = request.form.get("coordenadas")
        db.insert({"id": id,"nome": nome, "coordenadas": coordenadas})

    return render_template("index.html")


@app.route("/listar_caminhos")
def listar():
    posts = db.all()
    return render_template("caminhos.html",posts=posts)

@app.route("/buscar_caminho")
def buscar():
    return render_template("buscar-caminho.html")

@app.route("/pegar_caminho", methods=["GET", "POST"])
def listar_by_id():
    id = request.form.get("id")
    caminhos = db.get(id == 'id')
    return render_template("caminho.html",caminhos = caminhos)


    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
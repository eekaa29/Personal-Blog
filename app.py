from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://eekaa_29:Ekaitz-2003@curso-espinoza.y0obi.mongodb.net/")
app.db = cliente.BlogPersonal

entradas = [entrada for entrada in app.db.Contenido.find({})]

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        titulo = request.form.get("title")
        contenido_entrada = request.form.get("entry")
        fecha_formato = datetime.datetime.today().strftime("%d-%m-%Y") 
        parametros= {"titulo": titulo,
                     "contenido": contenido_entrada,
                     "fecha": fecha_formato}
        entradas.append(parametros)
        app.db.Contenido.insert_one(parametros)
    return render_template("index.html", entradas= entradas)


if __name__ == "__main__":
    app.run()


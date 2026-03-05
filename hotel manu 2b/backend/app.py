import os
from flask import Flask, send_from_directory

# caminho da pasta p dois pontos mandam isso a 1 pasta atras onde esta o front.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

#pasta frontend
FRONTEND_DIR = os.path.join(BASE_DIR,"frontend")

# pasta static (css)
STATIC_DIR= os.path.join(BASE_DIR, "static")

app = Flask(__name__, static_folder=STATIC_DIR,static_url_path="/" + STATIC_DIR)

@app.route("/")
def home ():
    return send_from_directory(FRONTEND_DIR,"index.html")


@app.route("/")
def consulta_page ():
    return send_from_directory(FRONTEND_DIR,"consulta.html")


@app.route("/")
def alterar_page ():
    return send_from_directory(FRONTEND_DIR,"alterar.html")


app.run()




































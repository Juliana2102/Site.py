from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'Primeiro-site'
mysql = MySQL(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/quem_somos")
def informações():
    return "Somos um canal de doação focado em conectar doadores a receptores e assim facilitar o modo como as doações são destinadas, fazendo a ponte para que as pessoas recebam o que de fato precisam."

@app.route("/quero_receber")
def receptores():
    return "Aqui você pode escolher quais são suas necessidades e aguardar um doador"

@app.route("/query_doar")
def doadores():
    return "Aqui você apoia um receptor e faz sua doação"

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome_completo = request.form["nome_completo"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        senha = request.form["senha"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (nome_completo, email, telefone, senha) VALUES (%s, %s, %s, %s)", (nome_completo, email, telefone, senha))
        mysql.connection.commit()
        cur.close()
        return "Cadastro realizado com sucesso"
    else:
        return render_template("cadastro.html")

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import psycopg2
from datetime import datetime
#from pytz import timezone

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# configurar o banco de dados

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Impacta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Hair2you(db.Model):
    ra = db.Column(db.Integer, primary_key=True, nullable=True)
    nome = db.Column(db.String(50), nullable=True, unique=True)
    email = db.Column(db.String(50), nullable=True)
    logradouro = db.Column(db.String(50), nullable=True)
    numero = db.Column(db.String(5), nullable=True)
    cep = db.Column(db.String(10), nullable=True)
    complemento = db.Column(db.String(20))


db.create_all()

 


@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')



@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('index.html')


@app.route("/validar")   
def validar():
    return render_template('menu.html')



@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if request.method == "POST":
        aluno = Hair2you(ra = request.form['ra'],
                        nome = request.form['nome'],
                        email = request.form['email'], 
                        logradouro = request.form['endereco'], 
                        numero = request.form['numero'],
                        cep = request.form['cep'],
                        complemento = request.form['complemento'])
        
        db.session.add(aluno)
        db.session.commit()
        return render_template('login.html') 
    

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')       
    

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')
    

@app.route('/menu')
def menu():
    return render_template('menu.html')




## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True)
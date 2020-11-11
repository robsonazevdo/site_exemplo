from flask import Flask, render_template, request, jsonify,  redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
 
from flask_login import LoginManager
from flask_login import login_user, logout_user,login_required

from forms import LoginForm







app = Flask(__name__)


# configurar o banco de dados

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Impacta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your secret key'
db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)

@lm.user_loader
def load_user(id):
    return Hair2you.query.filter_by(id=id).first()

class Hair2you(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    logradouro = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(5), nullable=False)
    cep = db.Column(db.String(10), nullable=True)
    complemento = db.Column(db.String(20))
    senha = db.Column(db.String(128), nullable=False)

    def __init__(self, nome, email, logradouro, numero, cep, complemento, senha ):
           
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento
        self.senha = senha

    @lm.user_loader
    def load_user(id):
        return Hair2you.query.filter_by(id=id).first()


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def s_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


    def __repr__(self):
        return  self.nome

    

@app.route('/inicio')
@app.route('/', methods=['GET', 'POST'])
def inicio():
   formu = LoginForm()
   if formu.validate_on_submit():
      
       u = Hair2you.query.filter_by(email=formu.email.data).first()
    
       if u and u.senha == formu.senha.data:
           login_user(u)
           return render_template("logado.html", aluno=Hair2you.query.all())
       else:
           flash("login inválido")

      
   return render_template('login.html', formu=formu)


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')



@app.route('/users', methods=['GET', 'POST'])
def aluno():
    if request.method == "POST":
        aluno = Hair2you(nome = request.form['nome'],
                        email = request.form['email'], 
                        logradouro = request.form['endereco'], 
                        numero = request.form['numero'],
                        cep = request.form['cep'],
                        complemento = request.form['complemento'], 
                        senha = request.form['senha'])
        
        db.session.add(aluno)
        db.session.commit()
        return render_template('login.html') 


@app.route("/validar")   
def validar():
    
    return render_template('menu.html')


@app.route("/logout")
@login_required
def logout():
    flash('logout')
    logout_user()
    return redirect(url_for('inicio'))


@app.route('/logado')
def logado():
    return render_template('logado.html')       
    

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')
    

@app.route('/menu')
def menu():
    return render_template('menu.html')




## Para rodar o projeto em desenvolvimento

db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
    
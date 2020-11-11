from flask import Flask, render_template, request, jsonify,  redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy
 
from flask_login import LoginManager
from flask_login import login_user

from forms import LoginForm







app = Flask(__name__)


# configurar o banco de dados

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Impacta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'your secret key'
db = SQLAlchemy(app)




lm = LoginManager()
lm.init_app(app)

class Hair2you(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    logradouro = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(5), nullable=False)
    cep = db.Column(db.String(10), nullable=True)
    complemento = db.Column(db.String(20))
    senha = db.Column(db.String(128), nullable=False)

    @lm.user_loader
    def load_user(user_id):
        return Hair2you.get(user_id)

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

    def __init__(self,name, email, senha, logradouro, numero, cep, complemento ):
       
        self.name = name
        self.email = email
        self.senha = senha
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento


    



@app.route('/inicio', methods=['GET', 'POST'])
@app.route('/')
def inicio():
   form = LoginForm()
   
   if form.validate_on_submit(): 
         
       u = Hair2you.query.filter_by(username=form.username.data).fist()
       if u and u.senha == form.password.data:
           login_user(u)
           print('logado')
       else:
            print("nao deu")
         
   return render_template('login.html', form=form)


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')




@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if request.method == "POST":
        aluno = Hair2you(senha = request.form['senha'],
                        nome = request.form['nome'],
                        email = request.form['email'], 
                        logradouro = request.form['endereco'], 
                        numero = request.form['numero'],
                        cep = request.form['cep'],
                        complemento = request.form['complemento'])
        

        db.session.add(aluno)
        db.session.commit()
        return render_template('login.html') 


@app.route("/validar")   
def validar():
    
    
    return render_template('menu.html')

    


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

db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
    
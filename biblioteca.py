from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'fsoy5u34'

@app.route('/')
def atividade():
    return render_template('atividade.html')

@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')

    if len(dao.login(login, senha)) > 0:
        session['login'] = login
        return render_template('paginaPrincipal.html')
    else:
        return render_template('atividade.html', msg='Usuário ou senha incorretos')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    nome = request.form.get('nome')
    contato = request.form.get('contato')
    contatofamiliar = request.form.get('contatofamiliar')
    endereco = request.form.get('endereco')
    bairro = request.form.get('bairro')
    cep = request.form.get('cep')
    sexo = request.form.get('sexo')
    email = request.form.get('email')
    senha = request.form.get('senha')

    if dao.inserir_user(nome, contato, contatofamiliar, endereco, bairro, cep, sexo, email, senha):
        msgm = "Usuário Cadastrado Com Sucesso"
        return render_template('atividade.html', ok=msgm)

    else:
        msgm = "Usuário Já Cadastrado"
        return render_template('atividade.html', erro=msgm)

@app.route('/mostrarpaginacadastro')
def mostre_pag_cadastro():
    return render_template('cadastro.html')

@app.route('/mostrarpaginaprincipal')
def pag_principal():
    return render_template('paginaPrincipal.html')

@app.route('/livroslidos')
def lidos():
    if 'login' in session:
        livros = dao.listar_livros(session['login'])
        return render_template('mostrarLivros.html', lista=livros)

    else:
        return render_template('atividade.html')

@app.route('/cad_livros', methods=['POST'])
def cadlivroslidos():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    editora = request.form.get('editora')
    login = session['login']

    if dao.inserir_livros(titulo, autor, editora, login):
        return redirect(url_for('lidos'))
    else:
        return render_template('salvarlivros.html')

@app.route('/pagcadastrolivros')
def listarlivros():
    return render_template('salvarlivros.html')

if __name__ == '__main__':
    app.run(debug=True)
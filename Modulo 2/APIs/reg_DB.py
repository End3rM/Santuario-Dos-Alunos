from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

# -----------------------------
# CRIA O BANCO CASO NÃO EXISTA
# -----------------------------
def init_db():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS aulas (
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   tipo TEXT ,
                   data TEXT,
                   horario TEXT
                   
                   )''')
    conn.commit()
    conn.close()

init_db()
alunis=['gabrire','maria']

# -----------------------------
# ROTA PRINCIPAL (SELECT)
# -----------------------------
@app.route('/')
def index():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()  # lista de tuplas (id, nome, idade)
    conn.close()

    return render_template('Index_DB.html', alunos=alunos)


# -----------------------------
# ROTA PARA CADASTRAR ALUNO
# -----------------------------
@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    nome = request.form['nome']
    idade = request.form['idade']

    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    conn.close()

    return "<h2>Aluno cadastrado! <a href='/'>Voltar</a></h2>"
            
                   


app.run(debug=True)
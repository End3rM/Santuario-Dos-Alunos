from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conene():
    conn =  sqlite3.connect('bancoQualquer.bd')
    methods = conn.cursor()
    methods.execute('''
                    
                    CREATE TABLE alunos (
                    id integer primary key ,
                    nome text,
                    idade text ,
                    peso_kg text
                    

                    )
                    
                    
                    
                    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('register.html',variavel=NomedoObjeto)

@app.route('/adicionar',methods=['POST'])
def adicionar():
    nome= request.form['nome']
    idade = request.form['idade']
    # telefone=request.form['telefone']
    # id=request.form['id']
    email=request.form['email']
    # RG=request.form['RG']

   
    return redirect(url_for('index'))

app.run(debug=True)
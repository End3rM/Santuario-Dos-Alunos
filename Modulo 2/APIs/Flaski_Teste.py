from flask import Flask,render_template, request, redirect ,url_for
app = Flask(__name__) 

aluno=[{
   'Name':'Gabriel',
   'Age':26,
   'Telephone':'(11)01234-6789'
},{
   'Name':'Yasmim A.',
   'Age':18,
   'Telephone':'(11)95397-2857'
}]


@app.route('/')
def index():
    return render_template('Index_Teste.html', alunos=aluno)

@app.route('/adicionar',methods=['POST'])
def adicionar():
   Name = request.form ['Name']
   Age = request.form ['Age']
   Telephone = request.form ['Telephone']

   aluno.append({'Name':Name,'Age':Age,'Telephone':Telephone})
   return redirect(url_for('index'))

app.run(debug=True)
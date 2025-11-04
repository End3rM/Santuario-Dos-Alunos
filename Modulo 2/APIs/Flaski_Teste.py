from flask import Flask,render_template, request, redirect 
app = Flask(__name__) 

aluno=[{
   'Name':'Gabriel',
   'Age':26,
   'Telephone':'(11)01234-6789'
},{
   'Name':'Gabriel',
   'Age':26,
   'Telephone':'(11)01234-6789'
}]


@app.route('/teste')
def home():
    return render_template('Index_Teste.html',pessoa=aluno)

app.run(debug=True)

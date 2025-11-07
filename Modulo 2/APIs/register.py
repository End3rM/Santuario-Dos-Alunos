from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


NomedoObjeto = [
    {
'id':22,
'Nome':'gabriel',
'Idade':22,
'Email':'seila@gmail',
'RG':12212
},
    {
'id':22,
'Nome':'gabriel',
'Idade':22,
'Email':'seila@gmail',
'RG':12212
}
]

@app.route('/')
def index():
    return render_template('register.html',variavel=NomedoObjeto)

app.run()
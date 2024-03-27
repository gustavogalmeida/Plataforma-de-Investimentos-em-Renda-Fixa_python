from flask import render_template, request, redirect
from app import app
from app import models

modalidade_lista = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modalidades')
def modalidades():
    return render_template('modalidades.html',
                           modalidades_lista = modalidade_lista,
                           titulo='Lista de modalidades - Plataforma de investimentos')

@app.route('/gravar_modalidade', methods=['POST',])
def gravar_modalidade():
    descricao = request.form['descricao']
    tipo = request.form['tipo_group']
    if 'permite_resgate_automatico' in request.form:
        resgate = 'Permite'
    else:
        resgate = "Não permitido"
    prazo_minimo = request.form['prazo_minimo']
    prazo_maximo = request.form['prazo_maximo']

    modalidade = models.Modalidades(descricao, tipo, resgate,
                                    prazo_minimo, prazo_maximo)
    
    modalidade_lista.append(modalidade)

    return redirect('/modalidades')

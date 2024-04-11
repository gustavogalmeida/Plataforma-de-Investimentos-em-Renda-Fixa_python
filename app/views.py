from flask import render_template, request, redirect, session, flash, url_for
from app import app
from app import models

modalidade_lista = []

@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/modalidades')
def modalidades():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você precisa estar conectado para acessar este recurso!')
        return redirect (url_for('login'))       
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

    modalidade = models.Modalidades(nome=descricao, tipo=tipo, resgate_automatico=resgate,
                                    prazo_minimo=prazo_minimo, prazo_maximo=prazo_maximo)
    
    modalidade_lista.append(modalidade)

    return redirect(url_for('modalidades'))

@app.route('/login')
def login():
    return render_template('login.html', titulo='Faça seu login para continuar')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        flash('Bem vindo(a), ' + session['usuario_logado'] + '!')
        return redirect(url_for('index'))
    else:
        flash('Por gentileza, verifique suas credênciais.')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário desconectado com sucesso!')
    return redirect (url_for('login'))
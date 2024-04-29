from flask import render_template, request, redirect, session, url_for
from app import app, db
from app import models, helpers

modalidade_lista = []

@app.route('/login')
def login():
    return render_template('login.html', titulo_navegador="Login - Plataforma de Investimentos")

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect (url_for('login'))

@app.route('/')
def index():
    return render_template('index.html', titulo_navegador="Plataforma de Investimentos"), 200

@app.route('/simulacao', methods=['POST', 'GET'])
def simulacao():
    simulacoes_lista = models.Simulacao.query.order_by(models.Simulacao.id)

    if request.method=='POST':
        valor_aplicado = request.form['valor']
        dias = request.form['dias']
        cdi_pago = request.form['cdi']

        cdi_com_sobras = helpers.calcula_cdi_considerando_sobras(cdi_pago)
        rentabilidade_valor = helpers.calcula_rentabilidade_periodo_valor(dias, valor_aplicado, cdi_pago)
        valor_sobras = helpers.calcula_valor_sobras(valor_aplicado)
        rentabilidade_bruta_valor = helpers.calcula_rentabilidade_bruta_valor(valor_sobras, rentabilidade_valor)
        rentabilidade_bruta_porcentagem_aa = helpers.calcula_rentabilidade_bruta_porcentagem_aa(rentabilidade_bruta_valor, valor_aplicado)
        saldo_total = helpers.calcula_saldo_total(rentabilidade_bruta_valor, valor_aplicado)
        return render_template('simulacao.html', 
                            simulacoes_lista=simulacoes_lista,
                            valor_aplicado=valor_aplicado,
                            dias=dias,
                            rentabilidade_paga=rentabilidade_valor, 
                            cdi=cdi_pago,
                            cdi_considerando_sobras=cdi_com_sobras,
                            valor_sobras=valor_sobras,
                            rentabilidade_bruta_valor=rentabilidade_bruta_valor,
                            saldo_total=saldo_total,
                            rentabilidade_bruta_porcentagem_aa=rentabilidade_bruta_porcentagem_aa,
                            titulo_navegador="Simulação - Plataforma de Investimentos") 
    return render_template('simulacao.html', simulacoes_lista=simulacoes_lista, titulo_navegador="Plataforma de Investimentos") 

@app.route('/salvar_simulacao', methods=['POST', ])
def salvar_simulacao():
    descricao = request.form['descricao']
    valor_aplicado = request.form['valor_aplicado']
    cdi = request.form['cdi']
    cdi_sobras = request.form['cdi_considerando_sobras']
    dias = request.form['dias']
    rentabilidade_bruta = request.form['rentabilidade_bruta_valor']
    saldo_total = request.form['saldo_total']

    nova_simulacao = models.Simulacao(descricao=descricao, valor_aplicado=valor_aplicado, cdi=cdi, cdi_sobras=cdi_sobras, dias=dias, rentabilidade_bruta=rentabilidade_bruta, saldo_total=saldo_total)

    db.session.add(nova_simulacao)
    db.session.commit()

    return redirect(url_for('simulacao'))

@app.route('/excluir_simulacao/<int:id>')
def excluir_simulacao(id):
    models.Simulacao.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('simulacao'))

@app.route('/modalidades')
def modalidades():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect (url_for('login'))       
    return render_template('modalidades.html',
                           modalidades_lista = modalidade_lista)

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

@app.route('/politica')
def politica():
    return render_template('politica.html', titulo_navegador="Politica - Plataforma de Investimentos")

@app.route('/manual')
def manual():
    return render_template('manual.html', titulo_navegador="Manual - Plataforma de Investimentos")

@app.route('/dicas')
def dicas():
    return render_template('/dicas.html', titulo_navegador="Dicas - Plataforma de Investimentos")

@app.route('/ferramentas')
def ferramentas():
    return render_template('/ferramentas.html', titulo_navegador="Ferramentas - Plataforma de Investimentos")

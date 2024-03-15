from flask import  render_template
from app import app

@app.route('/modalidades')
def modalidades():
    modalidades_lista = ['RDC', 'LCA', 'LCI']
    return render_template('modalidades_lista.html',
                           modalidades_lista = modalidades_lista,
                           titulo='Lista de modalidades - Plataforma de investimentos')
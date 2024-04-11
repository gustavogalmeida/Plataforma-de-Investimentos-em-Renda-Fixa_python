from __main__ import db

class Modalidades(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(30), nullable=False)
    resgate_automatico = db.Column(db.String(15), nullable=False)
    prazo_minimo = db.Column(db.Integer, nullable=False)
    prazo_maximo = db.Column(db.Integer, nullable=False)
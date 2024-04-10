from __main__ import db

class Modalidades:
    def __init__(self, descricao: str, tipo: str, resgate_automatico: str,
                 prazo_minimo: int, prazo_maximo: int):
        self.descricao = descricao
        self.tipo = tipo
        self.resgate_automatico = resgate_automatico 
        self.prazo_minimo = prazo_minimo
        self.prazo_maximo = prazo_maximo

class Modalidades(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(30), nullable=False)
    resgate_automatico = db.Column(db.String(15), nullable=False)
    prazo_minimo = db.Column(db.Integer, nullable=False)
    prazo_maximo = db.Column(db.Integer, nullable=False)
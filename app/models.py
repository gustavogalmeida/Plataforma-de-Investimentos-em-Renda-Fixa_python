from app import db

class Modalidades(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(30), nullable=False)
    resgate_automatico = db.Column(db.String(15), nullable=False)
    prazo_minimo = db.Column(db.Integer, nullable=False)
    prazo_maximo = db.Column(db.Integer, nullable=False)

class Usuarios(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(70), nullable=False)
    senha = db.Column(db.String(30), nullable=False)

class Simulacao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(30), nullable=False)
    valor_aplicado = db.Column(db.Float, nullable=False)
    cdi = db.Column(db.Float, nullable=False)
    cdi_sobras = db.Column(db.Float, nullable=False)
    dias = db.Column(db.Integer, nullable=False)
    rentabilidade_bruta = db.Column(db.Integer, nullable=False)
    saldo_total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
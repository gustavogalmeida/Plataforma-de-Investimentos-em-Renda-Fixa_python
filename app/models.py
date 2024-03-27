class Modalidades:
    def __init__(self, descricao: str, tipo: str, resgate_automatico: str,
                 prazo_minimo: int, prazo_maximo: int):
        self.descricao = descricao
        self.tipo = tipo
        self.resgate_automatico = resgate_automatico 
        self.prazo_minimo = prazo_minimo
        self.prazo_maximo = prazo_maximo
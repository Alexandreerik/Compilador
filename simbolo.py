class Simbolo:
    def __init__(self, tipo, linha):
        self.tipo = tipo
        self.linha = linha

class SimboloCaracteristica:

    def __init__(self, tipo, linha, qtdParam, listParam):
        self.tipo = tipo
        self.linha = linha
        self.qtdParam = qtdParam
        self.listParam = listParam
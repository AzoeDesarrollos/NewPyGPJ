from backend.globales import abrir_arma, abrir_armadura


class ObjetoCombate:
    precio = 0
    tipo = None
    req = None

    def __init__(self, data):
        self.precio = data['precio']
        self.tipo = data['tipo']
        self.req = data['Dote']


class Arma(ObjetoCombate):
    critico = None
    danio_med = None
    danio_peq = None

    def __init__(self, nombre):
        data = abrir_arma(nombre)
        super().__init__(data)
        self.critico = data['Crítico']
        self.danio_med = data['Mediana']
        self.danio_peq = data['Pequeña']


class Armadura(ObjetoCombate):
    ca = 0
    dex = 0
    pen = 0
    v20 = 0
    v30 = 0

    def __init__(self, nombre):
        data = abrir_armadura(nombre)
        super().__init__(data)
        self.ca = data["Bono_CA"]
        self.dex = data["Bono_max_des"]
        self.pen = data['Penalizador']
        self.v20 = data['Velocidad_20']
        self.v30 = data['Velocidad_30']

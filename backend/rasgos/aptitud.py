from globales import abrir_dominio


class Aptitud:
    nombre = ''

    def __init__(self, name):
        self.nombre = name


class Dominio(Aptitud):
    def __init__(self, nombre):
        super().__init__(nombre)
        data = abrir_dominio(nombre)
        self.aptitudes = [i for i in data['Aptitudes']]
        self.conjuros = [i for i in data['Conjuros']]

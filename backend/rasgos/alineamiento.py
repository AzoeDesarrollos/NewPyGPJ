class Alineamiento:
    eje_legal = ''
    eje_moral = ''

    def __init__(self, ejes):
        self.eje_legal, self.eje_moral = ejes.split(' ')

    def validar(self, clase):
        pass

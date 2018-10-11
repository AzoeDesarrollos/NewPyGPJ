class Salvacion:
    _base = 0
    _mod = 0
    _magia = 0

    def __init__(self, nombre, valor):
        self.name = nombre
        self.abreviatura = nombre[:3].upper()
        self.abr = self.abreviatura
        self._base = valor

    @property
    def value(self):
        return round(self._base+self._mod+self._magia)

    def __str__(self):
        return '%(n)s %(v)d' % {'n': self.name, "v": self.value}

    def __repr__(self):
        return 'Salvacion.' + '%(n)s %(v)d' % {'n': self.abr, "v": self.value}

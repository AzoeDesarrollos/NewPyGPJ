class Salvacion:
    _base = 0
    _mod = 0
    _magia = 0

    def __init__(self, pj, nombre: str, car: str):
        self._pj = pj
        self.name = nombre
        self.abreviatura = nombre[:4].title()
        self.abr = self.abreviatura
        self._base = getattr(pj.clase, 'ts_'+nombre.lower())
        self._mod = getattr(pj, car.lower())

    @property
    def value(self):
        return round(self._base.value+self._mod.mod+self._magia)

    def __str__(self):
        return 'TS {} {:+}'.format(self.name, self.value)

    def __repr__(self):
        return 'Salvacion.' + '%(n)s %(v)d' % {'n': self.abr, "v": self.value}

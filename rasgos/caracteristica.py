from math import floor


class Caracteristica:
    name = ''
    abreviatura = ''
    abr = abreviatura
    value = 0

    def __init__(self, nombre):
        self.name = nombre
        self.abreviatura = nombre[:3].upper()
        self.abr = self.abreviatura

    @property
    def mod(self):
        return floor((self.value - 10) / 2)

    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, **kwargs):
        valor = 0
        for key in ['racial', 'base']:
            if key in kwargs:
                valor += kwargs[key]

        self.value = valor

    def __ge__(self, other):
        assert type(other) is int
        return self.value >= other

    def __le__(self, other):
        assert type(other) is int
        return self.value <= other

    def __str__(self):
        return '%(n)s %(v)d (%(m)+d)' % {'n': self.name, "v": self.value, "m": self.mod}

    def __repr__(self):
        return 'Caracteristica.' + '%(n)s %(v)d' % {'n': self.abr, "v": self.value}

from globales import HABILIDADES


class Habilidad:
    _rangos = 0
    _mod_caracteristica = 0
    _mod_sinergia = 0
    _mod_racial = 0
    _mod_objeto = 0
    _mod_dote = 0
    _pen_armadura = 0

    name = ''
    modifier = ''
    penalty_factor = 0
    trained = False
    synergies = None

    def __init__(self, name):
        data = HABILIDADES[name]
        self.name = name
        self.modifier = data['Modificador']
        self.penalty_factor = data['Penalizador']
        self.trained = data['SoloEntrenada']
        self.synergies = data['Sinergias']

    @property
    def value(self):
        rng = self._rangos
        c = self._mod_caracteristica
        s = self._mod_sinergia
        r = self._mod_racial
        o = self._mod_objeto
        d = self._mod_dote
        pen = self._pen_armadura
        return rng+c+s+r+o+d-pen
    
    def bon_sinergia(self):
        return self._rangos > 5

    def __iadd__(self, other):
        assert type(other) is int
        self._rangos += other
        return self

    def __isub__(self, other):
        assert type(other) is int
        self._rangos -= other
        return self

    def __gt__(self, other):
        return self._rangos > other

    def __lt__(self, other):
        return self._rangos < other

    def __eq__(self, other):
        return self._rangos == other

    def __ne__(self, other):
        return self._rangos != other

    def __len__(self):
        return self.value

    def __str__(self):
        return '%(n)s %(v)+d' % {'n': self.name, "v": self.value}

    def __repr__(self):
        return 'Habilidad.' + '%(n)s %(c)d %(s)d %(r)d %(o)d %(d)d %(p)d' % {'n': self.name,
                                                                             "c": self._mod_caracteristica,
                                                                             "s": self._mod_sinergia,
                                                                             "r": self._mod_racial,
                                                                             "o": self._mod_objeto,
                                                                             "d": self._mod_dote,
                                                                             "p": self._pen_armadura
                                                                             }

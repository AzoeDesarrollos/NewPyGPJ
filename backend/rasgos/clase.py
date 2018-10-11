from backend.globales import abrir_clase
from backend.globales.data import ARMAS, ARMADURAS as ARMDS


class Clase:
    idiomas = None
    alineamientos = None
    competencias = None

    def __init__(self, name):
        data = abrir_clase(name)
        self.nombre_de_clase = name
        self.nivel_de_clase = 1
        self.abr = data['Abreviatura']
        self.alineamientos = self.cargar_alineamientos(data['Alineamientos'])
        self.ataque_base = AtaqueBase(data['AtaqueBase'])
        self.ts_reflejos = SalvacionBase('Reflejos', data['Salvaciones']['Reflejos'])
        self.ts_fortaleza = SalvacionBase('Fortaleza', data['Salvaciones']['Fortaleza'])
        self.ts_voluntad = SalvacionBase('Voluntad', data['Salvaciones']['Voluntad'])
        self.habilidades_claseas = [i for i in data['HabilidadesClaseas']]
        self.idiomas = [i for i in data['Idiomas_Adicionales']]
        self.competencias = {
            'armas': self.cargar_competencias_armas(data['Competencias']['Armas']),
            'armaduras': self.cargar_competencias_armaduras(data['Competencias']['Armaduras']),
            'escudos': self.cargar_competencias_escudos(data['Competencias']['Escudos'])
        }
        self.abr_conj = self.abr.title()+' '+str(self.nivel_de_clase)

    def __repr__(self):
        return 'Clase '+self.nombre_de_clase

    def __str__(self):
        return self.nombre_de_clase+' '+str(self.nivel_de_clase)+'º'

    @staticmethod
    def cargar_alineamientos(data):
        sintax = {'Cualquiera no legal': ['Neutral Bueno', 'Neutral', 'Neutral Maligno',
                                          'Caótico Bueno', 'Caótico Neutral', 'Neutral Maligno'],
                  'Cualquiera Neutral': ['Legal Neutral', 'Neutral Bueno', 'Neutral',
                                         'Neutral Maligno', 'Caótico Neutral'],
                  'Cualquiera': ['Legal Bueno', 'Legal Neutral', 'Legal Maligno',
                                 'Neutral Bueno', 'Neutral', 'Neutral Maligno',
                                 'Caótico Bueno', 'Caótico Neutral', 'Caótico Maligno'],
                  'Cualquiera Legal': ['Legal Bueno', 'Legal Neutral', 'Legal Maligno']}
        if data in sintax:
            return sintax[data]

        else:  # 'Legal Bueno' in sintax = False
            return data

    @staticmethod
    def cargar_competencias_armas(data):
        compt = []
        for item in data:
            if item == 'Sencillas':
                compt.extend([arma for arma in ARMAS if ARMAS[arma]['Dote'] == 'Competencia con arma (sencilla)'])
            elif item == 'Marciales':
                compt.extend([arma for arma in ARMAS if ARMAS[arma]['Dote'] == 'Competencia con arma (marcial)'])
            else:
                compt.append(item)
        compt.sort()
        return compt

    @staticmethod
    def cargar_competencias_armaduras(data):
        compt = []
        e = compt.extend
        for item in data:
            if item in ('Ligeras', 'Intermedias', 'Pesadas'):
                e([armd for armd in ARMDS if ARMDS[armd]['Dote'] == 'Competencia con armadura ('+item[:-1].lower()+')'])
            else:
                compt.append(item)

        compt.sort()
        return compt

    @staticmethod
    def cargar_competencias_escudos(data):
        compt = []
        e = compt.extend
        for item in data:
            if item == 'Todos':
                e([armd for armd in ARMDS if ARMDS[armd]['Dote'] == 'Competencia con escudo'])
            else:
                compt.append(item)

        compt.sort()
        return compt


class NamedValue:
    value = 0
    name = ''

    def __init__(self, nombre, data):
        self.name = nombre
        self.value = eval(data)

    def __iadd__(self, other):
        assert type(other) is int
        self.value += other
        return self


class AtaqueBase(NamedValue):
    def __init__(self, data):
        super().__init__('Ataque Base', data)

    def __repr__(self):
        return 'Ataque Base {:+}'.format(self.value)

    def __str__(self):
        # devuelve los múltiples ataques por ataque base alto automáticamente
        return '/'.join(['{:+}'.format(self.value - i) for i in range(0, 16, 5) if self.value - i > 0])


class SalvacionBase(NamedValue):
    def __repr__(self):
        return 'Salvacion Base '+self.name+' ('+str(self.value)+')'

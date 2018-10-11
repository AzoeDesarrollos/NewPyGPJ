from backend.globales import abrir_clase
from backend.globales.data import ARMAS, ARMADURAS as ARMDS


class Clase:
    habilidades = None
    idiomas = None
    alineamientos = None
    competencias = None

    def __init__(self, name):
        data = abrir_clase(name)
        self.nombre = name
        self.abr = data['Abreviatura']
        self.alineamientos = self.cargar_alineamientos(data['Alineamientos'])
        self.ataque_base = eval(data['AtaqueBase'])
        self.reflejos = eval(data['Salvaciones']['Reflejos'])
        self.fortaleza = eval(data['Salvaciones']['Fortaleza'])
        self.voluntad = eval(data['Salvaciones']['Voluntad'])
        self.habilidades = [i for i in data['HabilidadesClaseas']]
        self.idiomas = [i for i in data['Idiomas_Adicionales']]
        self.competencias = {
            'armas': self.cargar_competencias_armas(data['Competencias']['Armas']),
            'armaduras': self.cargar_competencias_armaduras(data['Competencias']['Armaduras']),
            'escudos': self.cargar_competencias_escudos(data['Competencias']['Escudos'])
        }

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
        return sintax[data]

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
            elif item == 'Pavés':
                compt.append('Escudo pavés')
            else:
                compt.append(item)

        compt.sort()
        return compt

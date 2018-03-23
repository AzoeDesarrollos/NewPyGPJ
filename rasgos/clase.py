from globales import abrir_clase


class Clase:
    habilidades = None
    idiomas = None

    def __init__(self, name):
        data = abrir_clase(name)
        self.nombre = name
        self.abr = data['Abreviatura']
        self.alineamientos = data['Alineamientos']
        self.ataque_base = eval(data['AtaqueBase'])
        self.reflejos = eval(data['Salvaciones']['Reflejos'])
        self.fortaleza = eval(data['Salvaciones']['Fortaleza'])
        self.voluntad = eval(data['Salvaciones']['Voluntad'])
        self.habilidades = []
        for clasea in data['HabilidadesClaseas']:
            self.habilidades.append(clasea)
        self.idiomas = []

        for idioma in data['Idiomas_Adicionales']:
            self.idiomas.append(idioma)

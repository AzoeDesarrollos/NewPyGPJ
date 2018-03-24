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
        self.habilidades = [i for i in data['HabilidadesClaseas']]
        self.idiomas = [i for i in data['Idiomas_Adicionales']]

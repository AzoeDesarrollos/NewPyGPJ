from globales import abrir_raza


class Raza:
    habilidades = None
    idiomas = None
    tipo = 'Humanoide'

    def __init__(self, name):
        data = abrir_raza(name)
        self.nombre = name
        self.tamanio = data['Tamaño']
        self.velocidad = data['Velocidad']
        self.subtipo = data['Subtipo']
        self.clasepredilecta = data['Clase predilecta']
        self.idiomas = [i for i in data['Idiomas_Automáticos']]
        self.idiomas_adicionales = [i for i in data['Idiomas_Adicionales']]

from backend.globales import abrir_raza


class Raza:
    habilidades = None
    idiomas = None
    tipo = 'Humanoide'

    def __init__(self, name):
        data = abrir_raza(name)
        self.nombre: str = name
        self.tamanio = data['Tamaño']
        self.velocidad = data['Velocidad']
        self.subtipo = data['Subtipo']
        self.clasepredilecta = data['Clase predilecta']
        self.idiomas = [i for i in data['Idiomas_Automáticos']]
        self.idiomas_adicionales = [i for i in data['Idiomas_Adicionales']]
        self.ajustes_caracteristicas = data['Ajustes']
        self.habilidades_raciales = self.cargar_habilidades_raciales(data['Especial'], data['Aptitudes'])

    @staticmethod
    def cargar_habilidades_raciales(especial, aptitudes):
        habs = []
        for aptitud in especial:
            if 'Habilidad Racial' in aptitud:
                hab = aptitud.split(':')[1]
                mod = aptitudes[aptitud]['Valor']
                habs.append({'Habilidad': hab, "Bono": mod})
        return habs

    def __repr__(self):
        return 'Raza ' + self.nombre

    def __str__(self):
        return self.nombre.capitalize()

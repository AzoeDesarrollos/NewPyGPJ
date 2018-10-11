from backend.globales import abrir_dote


class Dote:
    def __init__(self, nombre):
        self.nombre = nombre
        data = abrir_dote(nombre)
        self.descripcion = data['Descripcion']
        self.reqs = [i for i in data["Requisitos"] if "Requisitos" in data]
        self.efectos = [i for i in data["Efecto"] if "Efecto" in data]

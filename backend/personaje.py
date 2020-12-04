from backend.rasgos import Raza, Clase, Caracteristica, Salvacion


class Personaje:
    raza = None
    clase = None
    rangos_hab = None
    objetos = None

    def __init__(self, raza, clase, puntuaciones):
        self.raza = Raza(raza)
        self.clase = Clase(clase)

        self.fuerza = Caracteristica(self, 'Fuerza', puntuaciones.get('Fuerza', 10))
        self.destreza = Caracteristica(self, 'Destreza', puntuaciones.get('Destreza', 10))
        self.constitucion = Caracteristica(self, 'Constitución', puntuaciones.get('Constitución', 10))
        self.inteligencia = Caracteristica(self, 'Inteligencia', puntuaciones.get('Inteligencia', 10))
        self.sabiduria = Caracteristica(self, 'Sabiduría', puntuaciones.get('Sabiduría', 10))
        self.carisma = Caracteristica(self, 'Carisma', puntuaciones.get('Carisma', 10))

        self.fortaleza = Salvacion(self, 'Fortaleza', 'Constitucion')
        self.reflejos = Salvacion(self, 'Reflejos', 'Destreza')
        self.voluntad = Salvacion(self, 'Voluntad', 'Sabiduria')

    def __repr__(self):
        return 'Personaje ' + self.raza.nombre + ' ' + str(self.clase)

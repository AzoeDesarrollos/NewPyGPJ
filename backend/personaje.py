from backend.rasgos import Raza, Clase, Caracteristica, Salvacion


class Personaje:
    raza = None
    tipo = None
    subtipo = None
    tamanio = None
    velocidad = None
    idiomas = None

    clase = None

    def __init__(self, raza, clase):
        self.raza = Raza(raza)
        self.clase = Clase(clase)
        self.tamanio = self.raza.tamanio
        self.velocidad = self.raza.velocidad
        self.tipo = self.raza.nombre
        self.subtipo = self.raza.subtipo
        self.idiomas = self.raza.idiomas

        self.fuerza = Caracteristica('Fuerza')
        self.fuerza += self.raza.ajustes_caracteristicas.get('Fuerza', 0)
        self.destreza = Caracteristica('Destreza')
        self.destreza += self.raza.ajustes_caracteristicas.get('Destreza', 0)
        self.constitucion = Caracteristica('Constitución')
        self.constitucion += self.raza.ajustes_caracteristicas.get('Constitución', 0)
        self.inteligencia = Caracteristica('Inteligencia')
        self.inteligencia += self.raza.ajustes_caracteristicas.get('Inteligencia', 0)
        self.sabiduria = Caracteristica('Sabiduría')
        self.sabiduria += self.raza.ajustes_caracteristicas.get('Sabiduría', 0)
        self.carisma = Caracteristica('Carisma')
        self.carisma += self.raza.ajustes_caracteristicas.get('Carisma', 0)

        self.fortaleza = Salvacion('Fortaleza', self.constitucion.mod)
        self.reflejos = Salvacion('Reflejos', self.destreza.mod)
        self.voluntad = Salvacion('Voluntad', self.sabiduria.mod)

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

        self.fortaleza = Salvacion('Fortaleza', self.clase.ts_fortaleza, self.constitucion)
        self.reflejos = Salvacion('Reflejos', self.clase.ts_reflejos, self.destreza)
        self.voluntad = Salvacion('Voluntad', self.clase.ts_voluntad, self.sabiduria)

        self.ataque_base = self.clase.ataque_base

    def __repr__(self):
        return 'Personaje '+self.raza.nombre+' '+str(self.clase)

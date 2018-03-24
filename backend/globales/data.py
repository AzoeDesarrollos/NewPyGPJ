from .util import abrir_json


HABILIDADES = abrir_json('data/habilidades.json')
DOTES = abrir_json('data/dotes.json')
IDIOMAS = abrir_json('data/idiomas.json')
DOMINIOS = abrir_json('data/dominios.json')
CONJUROS = abrir_json('data/conjuros.json')
ARMAS = abrir_json('data/armas.json')
ARMADURAS = abrir_json('data/armaduras.json')


def abrir_clase(name):
    return abrir_json('data/clases/'+name+'.json')


def abrir_raza(name):
    return abrir_json('data/razas/'+name+'.json')


def abrir_dote(name):
    return DOTES[name]


def abrir_habilidad(name):
    return HABILIDADES[name]


def abrir_conjuro(name):
    return CONJUROS[name]


def abrir_dominio(name):
    return DOMINIOS[name]


def abrir_arma(name):
    return ARMAS[name]


def abrir_armadura(name):
    return ARMADURAS[name]

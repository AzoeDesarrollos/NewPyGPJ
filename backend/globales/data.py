from .util import abrir_json

root = 'backend/data/'
HABILIDADES = abrir_json(root+'habilidades.json')
DOTES = abrir_json(root+'dotes.json')
IDIOMAS = abrir_json(root+'idiomas.json')
DOMINIOS = abrir_json(root+'dominios.json')
CONJUROS = abrir_json(root+'conjuros.json')
ARMAS = abrir_json(root+'armas.json')
ARMADURAS = abrir_json(root+'armaduras.json')


def abrir_clase(name):
    return abrir_json(root+'clases/'+name+'.json')


def abrir_raza(name):
    return abrir_json(root+'razas/'+name+'.json')


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

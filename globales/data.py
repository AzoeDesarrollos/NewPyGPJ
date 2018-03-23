from .util import abrir_json


HABILIDADES = abrir_json('data/habilidades.json')
DOTES = abrir_json('data/dotes.json')
IDIOMAS = abrir_json('data/idiomas.json')
DOMINIOS = abrir_json('data/dominios.json')
CONJUROS = abrir_json('data/conjuros.json')


def abrir_clase(name):
    return abrir_json('data/clases/'+name+'.json')

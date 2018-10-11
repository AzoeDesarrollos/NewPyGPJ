import json
import sys
import pygame
from os import getcwd, path


def abrir_json(archivo, encoding='utf-8'):
    with open(path.join(getcwd(), archivo), encoding=encoding) as file:
        return json.load(file)


def guardar_json(nombre, datos):
    with open(nombre, mode='w', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=2, separators=(',', ':'), sort_keys=True)


def salir():
    pygame.quit()
    sys.exit()

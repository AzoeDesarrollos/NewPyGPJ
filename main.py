from frontend.globales import EventHandler, WidgetHandler, Renderer
from backend.globales.util import abrir_json

config = abrir_json('config.json')

while True:
    EventHandler.process()
    WidgetHandler.update()
    Renderer.update()

from .globales import COLOR_BOX, ANCHO, ALTO, WidgetHandler, Renderer
from .widgets import BaseWidget
from pygame import Surface


class Window(BaseWidget):
    def __init__(self):
        super().__init__()
        self.image = Surface((ANCHO, ALTO))
        self.image.fill(COLOR_BOX)
        self.rect = self.image.get_rect()

        Renderer.add_widget(self)
        WidgetHandler.add_widget(self)

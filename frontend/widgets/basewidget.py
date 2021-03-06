from frontend.globales import WidgetHandler, Renderer, COLOR_BOX, COLOR_TEXTO
from pygame.sprite import Sprite
from pygame import font


class BaseWidget(Sprite):
    active = False
    enabled = False
    selected = False
    is_visible = False
    layer = 0

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if self.parent is not None:
            self.layer = self.parent.layer + 1

    @staticmethod
    def crear_fuente(size, underline=False, bold=False):
        f = font.SysFont('Verdana', size, bold=bold)
        f.set_underline(underline)
        return f

    def on_keydown(self, key):
        pass

    def on_keyup(self, key):
        pass

    def on_mousebuttondown(self, event):
        pass

    def on_mousebuttonup(self, event):
        pass

    def on_mousemotion(self, rel):
        pass

    def on_mouseover(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def select(self):
        pass

    def deselect(self):
        pass

    def update(self):
        pass

    def show(self):
        self.is_visible = True
        Renderer.add_widget(self)
        WidgetHandler.add_widget(self)

    def hide(self):
        self.is_visible = False
        Renderer.del_widget(self)
        WidgetHandler.del_widget(self)

    def kill(self) -> None:
        super().kill()
        Renderer.del_widget(self)
        WidgetHandler.del_widget(self)

    def write(self, text, fuente, bg=COLOR_BOX, **kwargs):
        render = fuente.render(text, True, COLOR_TEXTO, bg)
        render_rect = render.get_rect(**kwargs)
        self.image.blit(render, render_rect)

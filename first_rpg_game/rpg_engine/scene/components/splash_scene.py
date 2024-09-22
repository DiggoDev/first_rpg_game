from pygame import MOUSEBUTTONDOWN

from first_rpg_game.rpg_engine.graphics.fonts import get_default_sys_font, FontType, FontSize

from .. import Scene
from ...helpers.coordinates_helper import get_center_coords

default_font = get_default_sys_font(FontType.TEXT, FontSize.LARGE)


class SplashScene(Scene):
    def __init__(self, engine, text, next_scene_key, pos=None,
                 font=default_font, text_color=(255, 255, 255)) -> None:
        super().__init__(engine)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.next_scene_key = next_scene_key
        self.text_surface = self.font.render(self.text, True, self.text_color)
        if pos:
            self.pos = pos
        else:
            self.pos = get_center_coords(self.text_surface.get_size(), self.screen.get_size())

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                self.engine.set_active_scene(self.next_scene_key)

    def render(self):
        self.screen.blit(self.text_surface, self.pos)

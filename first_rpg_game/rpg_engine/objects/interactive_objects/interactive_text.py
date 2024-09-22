from pygame import Rect
from pygame.font import SysFont
from typing import Tuple

from first_rpg_game.rpg_engine.graphics.colors import BLACK
from first_rpg_game.rpg_engine.graphics.fonts import get_default_font, FontType
from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject

default_font = get_default_font(FontType.TEXT)


class InteractiveText(InteractiveObject):
    def __init__(self, pos: Tuple[int, int], text: str, text_size=64) -> None:
        font = SysFont(default_font, text_size)
        text_color = BLACK
        self.surface = font.render(text, True, text_color)
        size = self.surface.get_size()
        shape = Rect(*pos, *size)
        super().__init__(shape)

    def render(self, screen):
        screen.blit(self.surface, [self.shape.x, self.shape.y])

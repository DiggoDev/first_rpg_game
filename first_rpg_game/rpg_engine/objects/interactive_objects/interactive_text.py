from pygame import Rect
from pygame.font import SysFont
from typing import Tuple

from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject


class InteractiveText(InteractiveObject):
    def __init__(self, pos: Tuple[int, int], text: str, text_size=64) -> None:
        font = SysFont('Arial', text_size)
        text_color = (255, 255, 255)
        self.surface = font.render(text, True, text_color)
        size = self.surface.get_size()
        shape = Rect(*pos, *size)
        super().__init__(shape)

    def render(self, screen):
        screen.blit(self.surface, [self.shape.x, self.shape.y])

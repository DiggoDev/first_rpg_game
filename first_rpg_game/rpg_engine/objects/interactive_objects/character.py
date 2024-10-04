from pygame import Rect

from first_rpg_game.rpg_engine.graphics.fonts import get_default_sys_font, FontType, FontSize
from first_rpg_game.rpg_engine.helpers.images_helper import load_image
from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject
from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_object_types import InteractiveObjectTypes

default_sys_font = get_default_sys_font(FontType.BUTTON, FontSize.MEDIUM)


class Character(InteractiveObject):

    def __init__(self, shape: Rect, width, height, x, y, image_name) -> None:
        shape.x = x
        shape.y = y
        self.image = load_image(f'{image_name}.png', (width, height))
        super().__init__(shape)
        self.type = InteractiveObjectTypes.CHARACTER

    def render(self, screen):
        screen.blit(self.image, [self.shape.x, self.shape.y])

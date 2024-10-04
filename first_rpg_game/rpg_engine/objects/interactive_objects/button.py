from pygame import Rect

from first_rpg_game.rpg_engine.graphics.colors import BLACK
from first_rpg_game.rpg_engine.graphics.fonts import get_default_sys_font, FontType, FontSize
from first_rpg_game.rpg_engine.helpers.images_helper import load_image
from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject
from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_object_types import InteractiveObjectTypes

default_sys_font = get_default_sys_font(FontType.BUTTON, FontSize.MEDIUM)


class Button(InteractiveObject):
    text_padding = 10

    def __init__(self, x, y, text) -> None:
        font = default_sys_font

        self.text_surface = font.render(text, True, BLACK)
        self.button_image = load_image('menu_button.png',
                                       (self.text_surface.get_width() + self.text_padding,
                                        self.text_surface.get_height() + self.text_padding))
        shape = Rect(x, y, self.button_image.get_width(), self.button_image.get_height())
        super().__init__(shape)
        self.type = InteractiveObjectTypes.BUTTON
        self.text_pos = [self.shape.x + (self.text_padding / 2), self.shape.y + (self.text_padding / 2)]

    def render(self, screen):
        screen.blit(self.button_image, [self.shape.x, self.shape.y])
        screen.blit(self.text_surface, [self.text_pos[0], self.text_pos[1]])

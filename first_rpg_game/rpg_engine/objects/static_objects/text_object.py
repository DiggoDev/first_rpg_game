from first_rpg_game.rpg_engine.objects import Object
from first_rpg_game.rpg_engine.graphics.colors import BLACK
from first_rpg_game.rpg_engine.graphics.fonts import FontSize, FontType, get_default_sys_font

default_sys_font = get_default_sys_font(FontType.TEXT, FontSize.MEDIUM)


class TextObject(Object):
    def __init__(self, text, pos, text_color=BLACK, font=default_sys_font):
        self.text_color = text_color
        self.text = text
        self.font = font

        self.pos = pos

        self.text_surface = self.font.render(self.text, True, self.text_color)

    def render(self, screen):
        screen.blit(self.text_surface, self.pos)

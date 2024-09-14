from pygame import K_BACKSPACE, Rect, draw

from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject
from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_object_types import InteractiveObjectTypes

from ...graphics.colors import BLACK, WHITE


class InputField(InteractiveObject):
    def __init__(self, x, y, width, height, font, text_color=BLACK, bg_color=WHITE,
                 border_color=BLACK, border_width=2) -> None:
        shape = Rect(x, y, width, height)
        self.color = bg_color
        self.border_color = border_color
        self.text_color = text_color
        self.border_width = border_width
        self.text = ''
        self.font = font
        self.active = False  # Tracks if the input field is active (focused)

        super().__init__(shape)
        self.type = InteractiveObjectTypes.INPUT_FIELD
        self.on_key_down_fn = self._on_key_down_fn

    def on_click(self) -> None:
        self.active = True

    def on_key_down(self, event_key, event_unicode) -> None:
        self.on_key_down_fn(event_key, event_unicode)

    def render(self, screen):
        # Draw the input field
        draw.rect(screen, self.border_color, self.shape, self.border_width)
        draw.rect(screen, self.color, self.shape.inflate(-self.border_width*2, -self.border_width*2))

        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.shape.x + 5, self.shape.y +
                                   (self.shape.height - text_surface.get_height()) // 2))

    def _on_key_down_fn(self, event_key, event_unicode):
        self.text
        if event_key == K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += event_unicode

from pygame import MOUSEBUTTONDOWN, KEYDOWN, K_BACKSPACE
from pygame.event import Event
from pygame.sysfont import SysFont

from first_rpg_game.rpg_engine.objects.interactive_objects.input_field import InputField
from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_object_types import InteractiveObjectTypes
from first_rpg_game.rpg_engine.scene import Scene


class NewGameScene(Scene):
    def __init__(self, engine, player):
        super().__init__(engine)
        self.interactive_objects = []
        font = SysFont('Arial', 32)
        self.interactive_objects.append(InputField(100, 100, 200, 100, font))

    def handle_event(self, event: Event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                active_index = -1
                for index in range(len(self.interactive_objects)):
                    obj = self.interactive_objects[index]
                    if obj.shape.collidepoint(mouse_x, mouse_y):
                        active_index = index
                        obj.on_click()
                for index in range(len(self.interactive_objects)):
                    if index != active_index:
                        obj = self.interactive_objects[index]
                        if obj.active is True:
                            obj.active = False

        if event.type == KEYDOWN:
            for obj in self.interactive_objects:
                if obj.type == InteractiveObjectTypes.INPUT_FIELD and obj.active:
                    if event.key == K_BACKSPACE:
                        obj.text = obj.text[:-1]
                    else:
                        obj.text += event.unicode

    def render(self):
        for obj in self.interactive_objects:
            obj.render(self.screen)

from typing import List, TypedDict, Callable, Dict

from pygame import KEYDOWN, MOUSEBUTTONDOWN
from pygame.event import Event

from first_rpg_game.rpg_engine.objects.interactive_objects.button import Button
from first_rpg_game.rpg_engine.objects.interactive_objects.input_field import InputField
from first_rpg_game.rpg_engine.objects.static_objects.text_object import TextObject
from first_rpg_game.rpg_engine.scene import Scene
from first_rpg_game.rpg_engine.graphics.fonts import DEFAULT_FONT


class FormItem(TypedDict):
    label: str
    input_type: str


class FormScene(Scene):
    def __init__(self, engine, title: str, items: List[FormItem], submit_text: str,
                 submit_action: Callable[[Dict], None]):
        super().__init__(engine)
        self.title = title

        self.form_rows = []
        font = DEFAULT_FONT

        self.form_item_objects = []

        for item in items:
            label = item['label']
            # input_type = item['input_type']

            label_text = TextObject(label, (0, 100))
            input_field = InputField(200, 100, 200, 50, font)
            self.form_item_objects.append({'label': label_text, 'input': input_field})

        self.submit = Button(200, 500, submit_text)
        self.submit_action = submit_action

        def my_submit_fn():
            payload = {}
            for obj in self.form_item_objects:
                label = obj['label'].text
                value = obj['input'].text
                payload[label] = value
                submit_action(payload)

        self.submit.set_on_click(my_submit_fn)

    def handle_event(self, event: Event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.submit.shape.collidepoint(mouse_x, mouse_y):
                self.submit.on_click()
        elif event.type == KEYDOWN:
            for obj in self.form_item_objects:
                obj['input'].on_key_down(event.key, event.unicode)

    def render(self):
        # Render form input rows
        for obj in self.form_item_objects:
            obj['label'].render(self.screen)
            obj['input'].render(self.screen)

        # Render submit button
        self.submit.render(self.screen)

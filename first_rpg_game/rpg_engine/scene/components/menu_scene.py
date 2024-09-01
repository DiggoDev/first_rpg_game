from pygame import MOUSEBUTTONDOWN
from pygame.event import Event
from typing import List, Callable, Any, Dict

from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject
from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_text import InteractiveText

from .. import Scene
from ...helpers.coordinates_helper import get_center_coords


# Define the type for an individual item
Action = Callable[[], Any]
ActionItem = Dict[str, Action]

# Define the type for a list of such
ActionItemList = List[ActionItem]


class MenuScene(Scene):
    def __init__(self, engine, items: ActionItemList) -> None:
        super().__init__(engine)

        y_padding = 20

        self.interactive_objects: List[InteractiveObject] = []

        items_size = len(items)

        first_item = items.pop(0)

        first_obj = InteractiveText([0, 0], first_item['title'])
        first_obj.set_on_click(first_item['action'])

        # Get full height by adding sizes of all items + paddings. Will be used to centralize item pos
        full_height = (first_obj.shape.size[1] * items_size) + (y_padding * (items_size - 1))
        first_x, first_y = get_center_coords([first_obj.shape.size[0], full_height], self.screen.get_size())

        first_obj.move(first_x, first_y)
        self.interactive_objects.append(first_obj)

        for i in range(len(items)):
            prev_obj = self.interactive_objects[i]
            y = prev_obj.shape.y + prev_obj.shape.size[1] + y_padding
            obj = InteractiveText([first_x, y], items[i]['title'])
            obj.set_on_click(items[i]['action'])
            self.interactive_objects.append(obj)

    def handle_event(self, event: Event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for obj in self.interactive_objects:
                    if obj.shape.collidepoint(mouse_x, mouse_y):
                        obj.on_click()

    def render(self):
        for obj in self.interactive_objects:
            obj.render(self.screen)

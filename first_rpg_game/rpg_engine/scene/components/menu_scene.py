from pygame import MOUSEBUTTONDOWN, Surface, Rect
from pygame.event import Event
from pygame.font import SysFont
from typing import List, Callable, Any, Dict, Tuple

from .. import Scene
from ...helpers.coordinates_helper import get_center_coords


# Define the type for an individual item
Action = Callable[[], Any]
ActionItem = Dict[str, Action]

# Define the type for a list of such
ActionItemList = List[ActionItem]


class MenuScene(Scene):
    def __init__(self, engine, items: ActionItemList, start_pos=None, y_padding=20,
                 font=SysFont('Arial', 64), text_color=(255, 255, 255)) -> None:
        super().__init__(engine)
        self.font = font
        self.text_color = text_color

        self.text_surfaces: List[Surface] = []
        self.text_rect_and_actions: List[Tuple[Rect, Action]] = []
        item_size = None
        self.y_padding = y_padding

        y = 0
        for item in items:
            item_surface = self.font.render(item['title'], True, self.text_color)
            self.text_surfaces.append(item_surface)
            if not item_size:
                item_size = item_surface.get_size()
                self.start_pos = get_center_coords(item_size, self.screen.get_size())
                self.y_size = item_size[1]
                y = self.start_pos[1]

            y_size = item_size[1]
            item_rect = Rect(self.start_pos[0], y, item_size[0], y_size)
            self.text_rect_and_actions.append([item_rect, item['action']])
            y = y + y_size + y_padding

        if start_pos:
            self.start_pos = start_pos
        else:
            self.start_pos = get_center_coords(item_size, self.screen.get_size())

    def handle_event(self, event: Event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for rect_and_action in self.text_rect_and_actions:
                    rect, action = rect_and_action
                    if rect.collidepoint(mouse_x, mouse_y):
                        action()

    def render(self):
        start_pos_x = self.start_pos[0]
        start_pos_y = self.start_pos[1]
        y_padding = self.y_padding

        y = start_pos_y

        for rect in self.text_surfaces:
            p = [start_pos_x, y]
            self.screen.blit(rect, p)
            y = y + self.y_size + y_padding

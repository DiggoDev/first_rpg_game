from pygame import Surface
from pygame.font import SysFont
from typing import List, Callable, Any, Dict

from .. import Scene
from ...helpers.coordinates_helper import get_center_coords


# Define the type for an individual item
ActionItem = Dict[str, Callable[[], Any]]

# Define the type for a list of such
ActionItemList = List[ActionItem]


class MenuScene(Scene):
    def __init__(self, engine, items: ActionItemList, start_pos=None, y_padding=20,
                 font=SysFont('Arial', 64), text_color=(255, 255, 255)) -> None:
        super().__init__(engine)
        self.font = font
        self.text_color = text_color

        self.text_surfaces: List[Surface] = []
        item_size = None
        for item in items:
            item_surface = self.font.render(item['title'], True, self.text_color)
            self.text_surfaces.append(item_surface)
            if not item_size:
                item_size = item_surface.get_size()
            # TODO do action
            # item.action()
        self.y_padding = y_padding
        self.y_size = item_size[1]
        if start_pos:
            self.start_pos = start_pos
        else:
            self.start_pos = get_center_coords(item_size, self.screen.get_size())

    def render(self):
        start_pos_x = self.start_pos[0]
        start_pos_y = self.start_pos[1]
        y_padding = self.y_padding

        y = start_pos_y

        for surf in self.text_surfaces:
            p = [start_pos_x, y]
            self.screen.blit(surf, p)
            y = y + self.y_size + y_padding

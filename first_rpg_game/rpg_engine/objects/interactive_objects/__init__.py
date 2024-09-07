from pygame import Rect, Surface
from typing import Callable

from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_object_types import InteractiveObjectTypes


class InteractiveObject:
    def __init__(self, shape: Rect) -> None:
        self.shape = shape
        self.on_click_fn = None
        self.on_key_down_fn = None
        self.type: InteractiveObjectTypes = InteractiveObjectTypes.DEFAULT

    def set_on_click(self, fn: Callable[[], None]) -> None:
        self.on_click_fn = fn

    def set_on_key_down(self, fn: Callable[[str], None]) -> None:
        self.on_key_down_fn = fn

    def on_click(self) -> None:
        if self.on_click_fn:
            self.on_click_fn()

    def on_key_down(self, event_key) -> None:
        if self.on_key_down_fn:
            self.on_key_down_fn(event_key)

    def move(self, x: float, y: float) -> None:
        self.shape = self.shape.move(x, y)

    def render(self, screen: Surface) -> None:
        pass

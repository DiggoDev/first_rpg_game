from pygame import Rect, Surface
from typing import Callable


class InteractiveObject:
    def __init__(self, shape: Rect) -> None:
        self.shape = shape
        self.on_click_fn = None

    def set_on_click(self, fn: Callable[[], None]) -> None:
        self.on_click_fn = fn

    def on_click(self) -> None:
        self.on_click_fn()

    def move(self, x: float, y: float) -> None:
        self.shape = self.shape.move(x, y)

    def render(self, screen: Surface) -> None:
        pass

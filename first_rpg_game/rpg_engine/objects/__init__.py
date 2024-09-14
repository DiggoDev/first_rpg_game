from pygame import Rect, Surface


class Object:
    def __init__(self, shape: Rect) -> None:
        self.shape = shape

    def move(self, x: float, y: float) -> None:
        self.shape = self.shape.move(x, y)

    def render(self, screen: Surface) -> None:
        pass

from pygame import Rect, Surface, Vector2


class Object:
    def __init__(self, shape: Rect) -> None:
        self.shape = shape

    def move(self, x: float, y: float) -> None:
        self.shape = self.shape.move(x, y)

    def move_vector(self, v: Vector2) -> None:
        self.shape = self.shape.move(v.x, v.y)

    def pre_render(self) -> None:
        pass

    def render(self, screen: Surface) -> None:
        pass

    def post_render(self) -> None:
        pass

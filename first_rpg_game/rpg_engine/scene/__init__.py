from pygame import Surface
from pygame.event import Event

# from first_rpg_game.rpg_engine import RpgEngine


class Scene:

    def __init__(self, engine) -> None:
        self.engine = engine
        self.screen: Surface = engine.screen

    def on_start(self):
        pass

    def handle_event(self, event: Event):
        pass

    def pre_render(self):
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("purple")
        return

    def render(self):
        pass

    def post_render(self):
        return

    def on_end(self):
        pass

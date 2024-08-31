from pygame import Surface


class Scene:

    def __init__(self, engine) -> None:
        self.screen: Surface = engine.screen

    def on_start(self):
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

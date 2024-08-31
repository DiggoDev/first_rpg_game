from first_rpg_game.rpg_engine.scene.components.splash_scene import SplashScene
from ..rpg_engine import RpgEngine
from .scene_keys import SceneKeys


class Game:
    def __init__(self) -> None:
        title = 'First rpg game'
        self.engine = RpgEngine()

        splash_scene = SplashScene(self.engine, title)

        self.engine.add_scene(SceneKeys.SPLASH, splash_scene)
        self.engine.set_active_scene(SceneKeys.SPLASH)

    def start(self):
        self.engine.run()

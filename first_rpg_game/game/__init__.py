from first_rpg_game.game.scenes.start_menu_scene import StartMenuScene
from first_rpg_game.rpg_engine.scene.components.splash_scene import SplashScene
from ..rpg_engine import RpgEngine
from .scene_keys import SceneKeys


class Game:
    def __init__(self) -> None:
        title = 'First rpg game'
        self.engine = RpgEngine()

        splash_scene = SplashScene(self.engine, title, SceneKeys.START_MENU)

        self.engine.add_scene(SceneKeys.SPLASH, splash_scene)
        self.engine.set_active_scene(SceneKeys.SPLASH)

        start_menu_scene = StartMenuScene(self.engine)
        self.engine.add_scene(SceneKeys.START_MENU, start_menu_scene)

    def start(self):
        self.engine.run()

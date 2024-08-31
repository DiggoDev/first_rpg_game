from first_rpg_game.rpg_engine.scene.components.menu_scene import MenuScene
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

        start_menu_scene = MenuScene(self.engine, [
            {'title': 'New Game', 'action': lambda: print("Action 1 executed")},
            {'title': 'Load Game', 'action': lambda: print("Action 2 executed")},
            {'title': 'Quit Game', 'action': lambda: print("Action 3 executed")},
        ])
        self.engine.add_scene(SceneKeys.START_MENU, start_menu_scene)

    def start(self):
        self.engine.run()

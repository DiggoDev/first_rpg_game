from first_rpg_game.game.scene_keys import SceneKeys
from first_rpg_game.rpg_engine.scene.components.splash_scene import SplashScene


class TmpGameScene(SplashScene):
    def __init__(self, engine) -> None:
        super().__init__(engine, 'Game', SceneKeys.START_MENU)

from first_rpg_game.game.map import Map
from first_rpg_game.game.player import Player
from first_rpg_game.game.scenes.game_scene import GameScene
from first_rpg_game.game.scenes.new_game_scene import NewGameScene
from first_rpg_game.game.scenes.start_menu_scene import StartMenuScene
from first_rpg_game.rpg_engine.scene.components.splash_scene import SplashScene
from ..rpg_engine import RpgEngine
from .scene_keys import SceneKeys


class Game:
    def __init__(self) -> None:
        title = 'First rpg game'
        self.engine = RpgEngine()

        # Game objects
        player = Player('')
        map = Map()

        # Scenes
        splash_scene = SplashScene(self.engine, title, SceneKeys.START_MENU)
        start_menu_scene = StartMenuScene(self.engine)
        game_scene = GameScene(self.engine, map, player)
        new_game_scene = NewGameScene(self.engine, player)

        self.engine.add_scene(SceneKeys.SPLASH, splash_scene)
        self.engine.add_scene(SceneKeys.START_MENU, start_menu_scene)
        self.engine.add_scene(SceneKeys.GAME, game_scene)
        self.engine.add_scene(SceneKeys.NEW_GAME, new_game_scene)

        self.engine.set_active_scene(SceneKeys.SPLASH)

    def start(self):
        self.engine.run()

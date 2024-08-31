from first_rpg_game.game.scene_keys import SceneKeys
from first_rpg_game.rpg_engine.scene.components.menu_scene import MenuScene


class StartMenuScene(MenuScene):
    def __init__(self, engine) -> None:
        items = [
            {'title': 'New Game', 'action': self.start_new_game},
            {'title': 'Load Game', 'action': lambda: print("Action 2 executed")},
            {'title': 'Quit Game', 'action': self.quit_game},
        ]
        super().__init__(engine, items)

    def start_new_game(self):
        self.engine.set_active_scene(SceneKeys.GAME)

    def quit_game(self):
        self.engine.stop()

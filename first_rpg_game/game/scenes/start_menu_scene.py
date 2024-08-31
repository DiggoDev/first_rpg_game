from first_rpg_game.rpg_engine.scene.components.menu_scene import MenuScene


class StartMenuScene(MenuScene):
    def __init__(self, engine) -> None:
        items = [
            {'title': 'New Game', 'action': lambda: print("Action 1 executed")},
            {'title': 'Load Game', 'action': lambda: print("Action 2 executed")},
            {'title': 'Quit Game', 'action': self.quit_game},
        ]
        super().__init__(engine, items)

    def quit_game(self):
        self.engine.stop()

from first_rpg_game.game.player import Player
from first_rpg_game.rpg_engine.scene.components.form_scene import FormScene


class NewGameScene(FormScene):
    def __init__(self, engine, player: Player):
        title = 'Create Player'
        super().__init__(engine, title, [{'label': 'Name', 'input_type': 'str'}], 'Create', self.on_submit)
        self.player = player

    def on_submit(self, payload):
        self.player.name = payload['Name']
        print('submit clicked')

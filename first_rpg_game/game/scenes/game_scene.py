from first_rpg_game.game.map import Map
from first_rpg_game.game.player import Player
from first_rpg_game.rpg_engine.scene import Scene


class GameScene(Scene):
    def __init__(self, engine, map: Map, player: Player) -> None:
        super().__init__(engine)
        self.map = map
        self.player = player
        if self.player.current_location is None:
            self.player.current_location = map.locations.START_LOCATION

    def render(self):
        match self.player.current_location:
            # Start location renders
            case self.map.locations.START_LOCATION:
                self.screen.fill('green')

        pass

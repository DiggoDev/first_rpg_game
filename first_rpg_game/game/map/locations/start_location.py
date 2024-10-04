from first_rpg_game.game.map.locations import LocationNames
from first_rpg_game.game.player import Player


class StartLocation:
    def __init__(self, engine, player: Player) -> None:
        self.name = LocationNames.START_LOCATION

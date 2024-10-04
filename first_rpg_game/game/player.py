from first_rpg_game.rpg_engine.objects.interactive_objects.character import Character


class Player:
    def __init__(self, name):
        self.name = name
        self.current_location = None
        self.character = None

    def set_character(self, character: Character):
        self.character = character

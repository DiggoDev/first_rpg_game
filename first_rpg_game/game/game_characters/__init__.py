from first_rpg_game.rpg_engine.objects.interactive_objects.character import Character


class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.current_location = None
        self.character = None
        # Attributes
        self.max_speed = 5
        self.acceleration = 0.5
        # Current attributes
        self.move_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
        }

    def set_character(self, character: Character):
        self.character = character
        self.character.acceleration = self.acceleration
        self.character.max_speed = self.max_speed

    def move(self):
        self.character.move_vector(self.velocity)

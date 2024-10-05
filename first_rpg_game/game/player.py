from first_rpg_game.rpg_engine.objects.interactive_objects.character import Character


class Player:
    # Attributes
    max_speed = 5
    acceleration = 0.5
    # Current attributes
    move_directions = {
        'left': False,
        'right': False,
        'up': False,
        'down': False,
    }

    def __init__(self, name):
        self.name = name
        self.current_location = None
        self.character = None

    def set_character(self, character: Character):
        self.character = character
        self.character.acceleration = self.acceleration
        self.character.max_speed = self.max_speed

        # Set input
        self.character.set_on_key_down(self._on_key_down)
        self.character.set_on_key_up(self._on_key_up)

    def _on_key_down(self, key, unicode):
        match unicode:
            case 'a':
                self.character.move_directions['left'] = True
            case 'd':
                self.character.move_directions['right'] = True
            case 'w':
                self.character.move_directions['up'] = True
            case 's':
                self.character.move_directions['down'] = True

        # self.character.move(new_x, new_y)

    def _on_key_up(self, key, unicode):
        match unicode:
            case 'a':
                self.character.move_directions['left'] = False
            case 'd':
                self.character.move_directions['right'] = False
            case 'w':
                self.character.move_directions['up'] = False
            case 's':
                self.character.move_directions['down'] = False

    def move(self):
        self.character.move_vector(self.velocity)

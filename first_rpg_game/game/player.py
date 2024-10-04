from first_rpg_game.rpg_engine.objects.interactive_objects.character import Character


class Player:
    def __init__(self, name):
        self.name = name
        self.current_location = None
        self.character = None

    def set_character(self, character: Character):
        self.character = character

        # Set input
        self.character.set_on_key_down(self._on_key_down)

    def _on_key_down(self, key, unicode):
        new_x = 0
        new_y = 0
        speed = 5
        match unicode:
            case 'a':
                new_x -= speed
            case 'd':
                new_x += speed
            case 'w':
                new_y -= speed
            case 's':
                new_y += speed

        self.character.move(new_x, new_y)

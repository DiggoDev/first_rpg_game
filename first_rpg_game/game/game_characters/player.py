from first_rpg_game.game.game_characters import GameCharacter
from first_rpg_game.rpg_engine.objects.interactive_objects.character import Character


class Player(GameCharacter):

    def set_character(self, character: Character):
        super().set_character(character)

        # Set input
        self.character.set_on_key_down(self._on_key_down)
        self.character.set_on_key_up(self._on_key_up)

    def _on_key_down(self, key, unicode):
        match unicode:
            case 'a':
                self.character.movement_left(True)
            case 'd':
                self.character.movement_right(True)
            case 'w':
                self.character.movement_up(True)
            case 's':
                self.character.movement_down(True)

        # self.character.move(new_x, new_y)

    def _on_key_up(self, key, unicode):
        match unicode:
            case 'a':
                self.character.movement_left(False)
            case 'd':
                self.character.movement_right(False)
            case 'w':
                self.character.movement_up(False)
            case 's':
                self.character.movement_down(False)

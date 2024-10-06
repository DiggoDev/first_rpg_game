from pygame.sprite import Group

from first_rpg_game.game.enemies.enemy import Enemy


class Enemies(Group):
    def add(self, *sprites: list[Enemy]):
        super().add(*sprites)

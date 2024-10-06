from first_rpg_game.game.enemies.enemy import Enemy


class RedEnemy(Enemy):
    def __init__(self, x, y) -> None:
        super().__init__('enemy', 32, 32, x, y)

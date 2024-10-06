# from pygame import KEYDOWN, KEYUP
from pygame.event import Event
from pygame.sprite import Group

from first_rpg_game.game.enemies.red_enemy import RedEnemy
from first_rpg_game.game.map import Map
# from first_rpg_game.game.game_characters.player import Player
from first_rpg_game.rpg_engine.scene import Scene


class GameScene(Scene):
    def __init__(self, engine, map: Map, player) -> None:
        super().__init__(engine)
        self.map = map
        self.player = player
        self.all_sprites = Group()
        self.all_sprites.add(self.player)

        self.add_enemy()

    def pre_render(self):
        self.player.pre_render()
        pass

    def render(self):
        match self.player.current_location:
            # Start location renders
            case self.map.locations.START_LOCATION:
                self.screen.fill('green')

        # self.player.character.render(self.screen)
        self.all_sprites.draw(self.screen)

        pass

    def post_render(self):
        self.player.post_render()

    def handle_event(self, event: Event):
        self.player.handle_event(event)

    def add_enemy(self):
        # Create enemy
        enemy = RedEnemy(100, 100)
        self.all_sprites.add(enemy)

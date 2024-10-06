from pygame import KEYDOWN, KEYUP, Rect
from pygame.event import Event

from first_rpg_game.game.game_characters.enemy import Enemy
from first_rpg_game.game.map import Map
from first_rpg_game.game.game_characters.player import Player
from first_rpg_game.rpg_engine.objects.interactive_objects.character import Character
from first_rpg_game.rpg_engine.scene import Scene


class GameScene(Scene):
    def __init__(self, engine, map: Map, player: Player) -> None:
        super().__init__(engine)
        self.map = map
        self.player = player
        self.enemies: list[Enemy] = []

        self.add_enemy()

    def pre_render(self):
        self.player.character.pre_render()
        for enemy in self.enemies:
            enemy.character.pre_render()

    def render(self):
        match self.player.current_location:
            # Start location renders
            case self.map.locations.START_LOCATION:
                self.screen.fill('green')

        self.player.character.render(self.screen)
        for enemy in self.enemies:
            enemy.character.render(self.screen)

        pass

    def post_render(self):
        self.player.character.post_render()
        for enemy in self.enemies:
            enemy.character.post_render()

    def handle_event(self, event: Event):
        if event.type == KEYDOWN:
            self.player.character.on_key_down(event.key, event.unicode)
        elif event.type == KEYUP:
            self.player.character.on_key_up(event.key, event.unicode)

    def add_enemy(self):
        # Create enemy
        enemy = Enemy('Enemy')
        enemy_char = Character(Rect(0, 0, 36, 36), 36, 36, 200, 200, 'enemy')
        enemy.set_character(enemy_char)
        self.enemies.append(enemy)

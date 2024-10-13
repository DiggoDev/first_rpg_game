from pygame.event import Event
from pygame import KEYDOWN, KEYUP, Vector2


from first_rpg_game.rpg_engine.config import get_window_size
from first_rpg_game.rpg_engine.sprites.image_sprite import ImageSprite
from first_rpg_game.rpg_engine.sprites.controllable_sprite import ControllableSprite
from first_rpg_game.rpg_engine.sprites.movable import Movable


class Player(ImageSprite, Movable, ControllableSprite):
    def __init__(self, x, y):
        super().__init__('player', 32, 32, x, y)
        super().init_controllable_sprite()
        self.name = ''
        self.current_location = None
        self.velocity = Vector2(0, 0)
        self.max_speed = 5
        self.acceleration = 0.5

    def handle_event(self, event: Event) -> None:
        key_down = None
        if event.type == KEYDOWN:
            key_down = True
        elif event.type == KEYUP:
            key_down = False

        if key_down is not None:
            match event.unicode:
                case 'a':
                    self.movement_left(key_down)
                case 'd':
                    self.movement_right(key_down)
                case 'w':
                    self.movement_up(key_down)
                case 's':
                    self.movement_down(key_down)

    def pre_render(self) -> None:
        accelerate_directions: list[str] = []
        decelerate_directions: list[str] = []

        accelerate_x = False
        accelerate_y = False

        for key in self.move_directions:
            if self.move_directions[key] is True:
                accelerate_directions.append(key)
                if key in ['left', 'right']:
                    accelerate_x = True
                if key in ['up', 'down']:
                    accelerate_y = True
            else:
                decelerate_directions.append(key)

        if 'left' in accelerate_directions and 'right' in accelerate_directions and self.direction_prio_x:
            if self.direction_prio_x == 'left':
                accelerate_directions.remove('right')
            else:
                accelerate_directions.remove('left')

        if 'up' in accelerate_directions and 'down' in accelerate_directions and self.direction_prio_y:
            if self.direction_prio_y == 'up':
                accelerate_directions.remove('down')
            else:
                accelerate_directions.remove('up')

        self.accelerate_in_directions(accelerate_directions)

        if accelerate_x is False:
            self.decelerate_x()

        if accelerate_y is False:
            self.decelerate_y()

        self.move(self.velocity.x, self.velocity.y)

    def post_render(self) -> None:
        self.move_if_out_of_bounds()

    def accelerate_in_directions(self, directions: list[str]):
        new_x = self.velocity.x
        new_y = self.velocity.y

        if 'left' in directions:
            new_x = max(-self.max_speed, new_x - self.acceleration)

        if 'right' in directions:
            new_x = min(self.max_speed, new_x + self.acceleration)

        if 'up' in directions:
            new_y = max(-self.max_speed, new_y - self.acceleration)

        if 'down' in directions:
            new_y = min(self.max_speed, new_y + self.acceleration)

        self.velocity = Vector2(new_x, new_y)

    def decelerate_x(self):
        new_x = self.velocity.x
        if new_x > 0:
            new_x = max(0, new_x - self.acceleration)
        elif new_x < 0:
            new_x = min(0, new_x + self.acceleration)

        self.velocity.x = new_x

    def decelerate_y(self):
        new_y = self.velocity.y
        if new_y > 0:
            new_y = max(0, new_y - self.acceleration)
        elif new_y < 0:
            new_y = min(0, new_y + self.acceleration)

        self.velocity.y = new_y

    def move_if_out_of_bounds(self):
        size = get_window_size()
        rect = self.rect
        velocity = self.velocity
        acceleration = self.acceleration
        bounce_val_x = (rect.width / 8)
        bounce_val_y = (rect.height / 8)
        if rect.x < 0:
            rect.x = bounce_val_x
            velocity.x = acceleration
        elif (rect.x + rect.width) > size[0]:
            rect.x = size[0] - rect.width - bounce_val_x
            velocity.x = -acceleration
        if rect.y < 0:
            rect.y = bounce_val_y
            velocity.y = acceleration
        elif (rect.y + rect.height) > size[1]:
            rect.y = size[1] - rect.height - bounce_val_y
            velocity.y = -acceleration


# def _on_key_down(self, key, unicode):
#         match unicode:
#             case 'a':
#                 self.character.movement_left(True)
#             case 'd':
#                 self.character.movement_right(True)
#             case 'w':
#                 self.character.movement_up(True)
#             case 's':
#                 self.character.movement_down(True)

#         # self.character.move(new_x, new_y)

#     def _on_key_up(self, key, unicode):
#         match unicode:
#             case 'a':
#                 self.character.movement_left(False)
#             case 'd':
#                 self.character.movement_right(False)
#             case 'w':
#                 self.character.movement_up(False)
#             case 's':
#                 self.character.movement_down(False)

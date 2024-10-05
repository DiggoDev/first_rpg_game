from pygame import Rect, Vector2

from first_rpg_game.rpg_engine.config import get_window_size
from first_rpg_game.rpg_engine.graphics.fonts import get_default_sys_font, FontType, FontSize
from first_rpg_game.rpg_engine.helpers.images_helper import load_image
from first_rpg_game.rpg_engine.objects.interactive_objects import InteractiveObject
from first_rpg_game.rpg_engine.objects.interactive_objects.interactive_object_types import InteractiveObjectTypes

default_sys_font = get_default_sys_font(FontType.BUTTON, FontSize.MEDIUM)


class Character(InteractiveObject):
    velocity = Vector2(0, 0)
    acceleration = 0.1
    max_speed = 0.1
    move_directions = {
        'left': False,
        'right': False,
        'up': False,
        'down': False,
    }
    direction_prio_x = ''
    direction_prio_y = ''

    def __init__(self, shape: Rect, width, height, x, y, image_name) -> None:
        shape.x = x
        shape.y = y
        self.image = load_image(f'{image_name}.png', (width, height))
        super().__init__(shape)
        self.type = InteractiveObjectTypes.CHARACTER

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

        self.move_vector(self.velocity)

    def render(self, screen):
        screen.blit(self.image, [self.shape.x, self.shape.y])

    def post_render(self) -> None:
        self.move_if_out_of_bounds()

    def update_velocity(self, new_velocity):
        # Add the new velocity increment to the current velocity
        self.velocity += new_velocity

    def movement_left(self, move: bool):
        if move is True:
            if self.move_directions['right'] is True:
                self.direction_prio_x = 'left'
            self.move_directions['left'] = True
        else:
            self.move_directions['left'] = False

    def movement_right(self, move: bool):
        if move is True:
            if self.move_directions['left'] is True:
                self.direction_prio_x = 'right'
            self.move_directions['right'] = True
        else:
            self.move_directions['right'] = False

    def movement_up(self, move: bool):
        if move is True:
            if self.move_directions['down'] is True:
                self.direction_prio_y = 'up'
            self.move_directions['up'] = True
        else:
            self.move_directions['up'] = False

    def movement_down(self, move: bool):
        if move is True:
            if self.move_directions['up'] is True:
                self.direction_prio_y = 'down'
            self.move_directions['down'] = True
        else:
            self.move_directions['down'] = False

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
        bounce_val_x = (self.shape.width / 8)
        bounce_val_y = (self.shape.height / 8)
        if self.shape.x < 0:
            self.shape.x = bounce_val_x
            self.velocity.x = self.acceleration
        elif (self.shape.x + self.shape.width) > size[0]:
            self.shape.x = size[0] - self.shape.width - bounce_val_x
            self.velocity.x = -self.acceleration
        if self.shape.y < 0:
            self.shape.y = bounce_val_y
            self.velocity.y = self.acceleration
        elif (self.shape.y + self.shape.height) > size[1]:
            self.shape.y = size[1] - self.shape.height - bounce_val_y
            self.velocity.y = -self.acceleration

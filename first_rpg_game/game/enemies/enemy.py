from pygame.sprite import Sprite

from first_rpg_game.rpg_engine.helpers.images_helper import load_image


class Enemy(Sprite):
    def __init__(self, image_name, width, height, x, y) -> None:
        super().__init__()
        self.image = load_image(f'{image_name}.png', (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

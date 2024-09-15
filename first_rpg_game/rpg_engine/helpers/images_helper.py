import os
from pygame import image, transform

from first_rpg_game.rpg_engine.config import images_path


def load_image(path, new_size=None):
    image_path = os.path.join(images_path, path)
    image_surface = image.load(image_path)
    if new_size is not None:
        image_surface = transform.scale(image_surface, new_size)

    return image_surface

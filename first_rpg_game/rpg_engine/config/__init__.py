import os
import pygame

# Paths

# Assets paths
_assets_path = os.path.join('assets')
images_path = os.path.join(_assets_path, 'images')
# Cache paths
_cache_path = os.path.join('cache')
saves_path = os.path.join(_cache_path, 'saves')


def init():
    os.makedirs(saves_path, exist_ok=True)


def get_window_size():
    return pygame.display.get_window_size()

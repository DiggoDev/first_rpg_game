import pygame
from typing import Dict

from first_rpg_game.rpg_engine.scene import Scene

from .engine_settings import engine_settings


class RpgEngine:
    def __init__(self, settings={}) -> None:
        self.settings = engine_settings | settings

        screen_settings = self.settings['screen']
        self.screen = pygame.display.set_mode((screen_settings['width'], screen_settings['height']))
        self.clock = pygame.time.Clock()

        self.debug = self.settings['debug']

        self.scenes: Dict[str, Scene] = {}
        self.active_scene_key = None

    def run(self):
        self.running = True
        clock = self.clock
        fps = self.settings['fps']
        while self.running:
            scene = self.get_active_scene()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                scene.handle_event(event)

            # fill the screen with a color to wipe away anything from last frame
            scene.pre_render()

            # RENDER YOUR GAME HERE
            scene.render()

            scene.post_render()

            # flip() the display to put your work on screen
            pygame.display.flip()

            if self.debug['show_fps']:
                # Get FPS
                current_fps = clock.get_fps()
                print(f"FPS: {current_fps:.2f}")

            clock.tick(fps)  # limits FPS to 60

        pygame.quit()

    def stop(self):
        self.running = False

    def get_active_scene(self):
        return self.scenes[self.active_scene_key]

    def set_active_scene(self, key: str):
        if (self.active_scene_key):
            self.get_active_scene().on_end()

        self.active_scene_key = key
        self.get_active_scene().on_start()

    def add_scene(self, key: str, scene: Scene):
        if key in self.scenes:
            raise Exception('Scenes already have a scene with key ' + key)

        self.scenes[key] = scene

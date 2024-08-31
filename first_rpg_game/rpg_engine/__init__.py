import pygame

from .engine_settings import engine_settings

pygame.init()


class RpgEngine:
    def __init__(self, settings={}) -> None:
        self.settings = engine_settings | settings

        screen_settings = self.settings['screen']
        self.screen = pygame.display.set_mode((screen_settings['width'], screen_settings['height']))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        screen = self.screen
        clock = self.clock
        fps = self.settings['fps']
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(fps)  # limits FPS to 60

        pygame.quit()

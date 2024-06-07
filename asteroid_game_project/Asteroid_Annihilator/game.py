# imports pygame module

import pygame

# creates the AsteroidAnnihilator class

class AsteroidAnnihilator:

    # the constructor

    def __init__(self):

        # for pygame initialization

        self._init_pygame()

        # creates a display surface of 800 pixels width and 600 pixels height

        self.screen = pygame.display.set_mode((800, 600))

    # main loop for every frame
    
    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    # one-time initialization of pygame

    def _init_pygame(self):

        # calls pygame.init for its feautures

        pygame.init()

        #sets the caption of this Pygame programme

        pygame.display.set_caption("Asteroid Annihilator")

    def _handle_input(self):
        pass

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0,0,255))
        pygame.display.flip()
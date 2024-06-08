from .Figura import Figura

import pygame

class Circulo(Figura):
    def __init__(self, params):
        super().__init__('CIRCULO', params)

    def draw(self, screen, color, font):
        pygame.draw.circle(screen, color, self.params['vertex'], int(self.params['radio']), 2)
        pygame.draw.circle(screen, color, self.params['vertex'], 5)
        self.show_coordinates(screen, font, self.params['vertex'])

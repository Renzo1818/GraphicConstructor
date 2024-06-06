from .Figura import Figura

import pygame

class Cuadrado(Figura):
    def __init__(self, params):
        super().__init__('CUADRADO', params)

    def draw(self, screen, color, font):
        pygame.draw.rect(screen, color, (*self.params['vertex'], int(self.params['ancho']), int(self.params['ancho'])), 2)
        vertices = [
            (self.params['vertex'][0], self.params['vertex'][1]),
            (self.params['vertex'][0] + self.params['ancho'], self.params['vertex'][1]),
            (self.params['vertex'][0], self.params['vertex'][1] + self.params['ancho']),
            (self.params['vertex'][0] + self.params['ancho'], self.params['vertex'][1] + self.params['ancho'])
        ]
        for vx, vy in vertices:
            pygame.draw.circle(screen, color, (vx, vy), 5)
            self.show_coordinates(screen, font, (vx, vy))

from .Figura import Figura

import pygame

class Triangulo(Figura):
    def __init__(self, params):
        super().__init__('TRIANGULO', params)

    def draw(self, screen, color, font):
        x, y = self.params['vertex']
        width = self.params['ancho']
        height = self.params['alto']
        points = [(x, y), (x + width / 2, y - height), (x + width, y)]
        pygame.draw.polygon(screen, color, points, 2)
        for vx, vy in points:
            pygame.draw.circle(screen, color, (vx, vy), 5)
            self.show_coordinates(screen, font, (vx, vy))

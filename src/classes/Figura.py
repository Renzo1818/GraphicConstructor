import pygame

class Figura:
    def __init__(self, tipo, params):
        self.tipo = tipo
        self.params = params

    def draw(self, screen, color, font):
        pass

    def show_coordinates(self, screen, font, vertex):
        label = font.render(f"({vertex[0]}, {vertex[1]})", True, (0, 0, 0))
        screen.blit(label, (vertex[0] + 5, vertex[1] - 15))

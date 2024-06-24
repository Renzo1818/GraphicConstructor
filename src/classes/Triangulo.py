from .Figura import Figura

import matplotlib.pyplot as plt

class Triangulo(Figura):
    def __init__(self, params):
        super().__init__('TRIANGULO', params)

    def draw(self, ax):
        vertices = [list(vertex) for vertex in self.params['vertex']]  # Convertir vértices a lista de listas
        triangle = plt.Polygon(vertices, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_artist(triangle)

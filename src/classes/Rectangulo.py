from .Figura import Figura

import matplotlib.pyplot as plt

class Rectangulo(Figura):
    def __init__(self, params):
        super().__init__('RECTANGULO', params)

    def draw(self, ax):
        vertex = self.params['vertex'][0]
        x, y = vertex[0], vertex[1]
        ancho = self.params['ancho']
        alto = self.params['alto']
        rect = plt.Rectangle((x, y), ancho, alto, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_artist(rect)

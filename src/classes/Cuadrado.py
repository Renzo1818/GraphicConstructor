from .Figura import Figura

import matplotlib.pyplot as plt

class Cuadrado(Figura):
    def __init__(self, params):
        super().__init__('CUADRADO', params)

    def draw(self, ax):
        vertex = self.params['vertex'][0]
        x, y = vertex[0], vertex[1]
        lado = self.params['ancho']
        square = plt.Rectangle((x, y), lado, lado, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_artist(square)

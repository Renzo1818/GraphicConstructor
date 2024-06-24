from .Figura import Figura

import matplotlib.pyplot as plt

class Circulo(Figura):
    def __init__(self, params):
        super().__init__('CIRCULO', params)

    def draw(self, ax):
        vertex = self.params['vertex'][0]
        x, y = vertex[0], vertex[1]
        radio = self.params['radio']
        circle = plt.Circle((x, y), radio, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_artist(circle)


import pygame
import sys


from ..classes.Circulo import Circulo
from ..classes.Rectangulo import Rectangulo
from ..classes.Cuadrado import Cuadrado
from ..classes.Triangulo import Triangulo

from src.Parser.GraphLangParser import GraphLangParser
from src.Parser.GraphLangVisitor import GraphLangVisitor

class CustomVisitor(GraphLangVisitor):
    def __init__(self):
        pass

    def visitImprimir(self, ctx:GraphLangParser.ImprimirContext):
        return self.visitChildren(ctx)
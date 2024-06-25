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
        self.variables = {}
        self.shapes = {}
        self.scene = {}
        self.scene_invocada = False
        self.width = 800
        self.height = 600
        self.transformations = {}

    def visitSentenciaFor(self, ctx:GraphLangParser.SentenciaForContext):
        # Evaluación de la inicialización
        self.visit(ctx.declaracionVariable())
        
        # Evaluación de la condición de continuación
        while self.visit(ctx.expresionComparativa()):
            # Ejecución del bloque
            self.visit(ctx.bloque())
            
            # Evaluación de la expresión de actualización
            self.visit(ctx.declaracionIncremental())

        return None
    
    # Regla sentenciaWhile
    def visitSentenciaWhile(self, ctx: GraphLangParser.SentenciaWhileContext):
        condicion = self.visit(ctx.expresion())  # Visitamos la expresión de la condición
        while condicion:
            self.visit(ctx.bloque())  # Visitamos el bloque del while
            condicion = self.visit(ctx.expresion())  # Evaluamos la condición nuevamente al final del bloque
        return None
from ..classes.Circulo import Circulo
from ..classes.Rectangulo import Rectangulo
from ..classes.Cuadrado import Cuadrado
from ..classes.Triangulo import Triangulo

from src.Parser.GraphLangParser import GraphLangParser
from src.Parser.GraphLangVisitor import GraphLangVisitor

import matplotlib.pyplot as plt
import copy

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
    
    # Regla declaracionIncremental
    def visitDeclaracionIncremental(self, ctx: GraphLangParser.DeclaracionIncrementalContext):
        variable_name = ctx.ID().getText()
        increment_operator = ctx.opIncrementales().getText()
        if increment_operator == '++':
            self.variables[variable_name] += 1
        elif increment_operator == '--':
            self.variables[variable_name] -= 1
        return None
    
    # Regla opIncrementales
    def visitOpIncrementales(self, ctx: GraphLangParser.OpIncrementalesContext):
        return ctx.getText()
    
    # Bloque
    def visitBloque(self, ctx: GraphLangParser.BloqueContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return None
    
    def render_scene(self):
        if not self.scene_invocada:
            print("Error: No se ha declarado una escena para renderizar.")
            return

        # Definir los límites del plano cartesiano
        x_min, x_max = -50, 50
        y_min, y_max = -50, 50

        # Crear la figura y los ejes
        fig, ax = plt.subplots(figsize=(self.width / 100, self.height / 100), dpi=100)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_aspect('equal')
        ax.grid()

        for shape_id, shape in self.scene.items():
            shape.draw(ax)
            if isinstance(shape, Triangulo):  # Verificar si la forma es un triángulo
                ax.text(shape.params['vertex'][0][0], shape.params['vertex'][0][1], shape_id, fontsize=12)
            else:  # Para las demás formas, imprimir el identificador en cada vértice
                if shape.params.get('vertex'):  # Verificar si la forma tiene vértices definidos
                    for vertex in shape.params['vertex']:
                        ax.text(vertex[0], vertex[1], shape_id, fontsize=12)

        plt.axis('equal')
        plt.show()
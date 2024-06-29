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
    
    # Expresión
    def visitExpresion(self, ctx: GraphLangParser.ExpresionContext):
        if ctx.opLogico():
            resultado = self.visit(ctx.expresionComparativa(0))  # Empezamos con la primera expresión
            operadores = ctx.opLogico()  # Lista de operadores lógicos
            comparativas = ctx.expresionComparativa()  # Lista de expresiones comparativas

            # Iteramos sobre los operadores y expresiones comparativas restantes
            for i in range(1, len(comparativas)):
                derecha = self.visit(comparativas[i])
                op = operadores[i - 1].getText()  # Operador correspondiente
                if op == '&&':
                    resultado = resultado and derecha
                elif op == '||':
                    resultado = resultado or derecha
            return resultado
        else:
            return self.visit(ctx.expresionComparativa(0))
        

    # Expresión Comparativa
    def visitExpresionComparativa(self, ctx: GraphLangParser.ExpresionComparativaContext):
        izquierda = self.variables[ctx.ID().getText()]
        derecha = int(ctx.ENTERO().getText())
        op = ctx.opComparacion().getText()
        if op == '==':
            return izquierda == derecha
        elif op == '!=':
            return izquierda != derecha
        elif op == '>':
            return izquierda > derecha
        elif op == '<':
            return izquierda < derecha
        elif op == '>=':
            return izquierda >= derecha
        elif op == '<=':
            return izquierda <= derecha
        
    def visitDeclaracionVariable(self, ctx: GraphLangParser.DeclaracionVariableContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
        operador = ctx.opAsignacion().getText()
        valor_ctx = ctx.literal()
        valor = self.visitLiteral(valor_ctx)

        if operador == '=':
            self.declarar_variable(tipo, nombre, valor)
        else:
            print(f"Error: Operador de asignación no válido '{operador}' en línea {ctx.start.line}")

        return self.visitChildren(ctx)
    
    def visitLiteral(self, ctx:GraphLangParser.LiteralContext):
        literal_text = ctx.getText()
        if ctx.ENTERO():
            return int(literal_text)
        elif ctx.DECIMAL():
            return float(literal_text)
        elif literal_text == 'verdadero':
            return True
        elif literal_text == 'falso':
            return False
        elif ctx.CADENA():
            return literal_text[1:-1]
        else:
            print(f"Error: Literal no reconocido '{literal_text}' en línea {ctx.start.line}")
            return None    
        
    def declarar_variable(self, tipo, nombre, valor):
        if tipo in ['ENTERO', 'DECIMAL', 'BOOLEANO', 'CADENA']:
            if tipo == 'ENTERO':
                if not isinstance(valor, int):
                    raise Exception(f"Error: El valor '{valor}' no es un entero válido para la variable '{nombre}'")
                self.variables[nombre] = int(valor)
            elif tipo == 'DECIMAL':
                if not isinstance(valor, float):
                    raise Exception(f"Error: El valor '{valor}' no es un decimal válido para la variable '{nombre}'")
                self.variables[nombre] = float(valor)
            elif tipo == 'BOOLEANO':
                if not isinstance(valor, bool):
                    raise Exception(f"Error: El valor '{valor}' no es un booleano válido para la variable '{nombre}'")
                self.variables[nombre] = bool(valor)
            elif tipo == 'CADENA':
                if not isinstance(valor, str):
                    raise Exception(f"Error: El valor '{valor}' no es una cadena válida para la variable '{nombre}'")
                self.variables[nombre] = str(valor)
        else:
            raise Exception(f"Error: Tipo de variable no válido '{tipo}' en la declaración de '{nombre}'")


    def visitExpresionAritmetica(self, ctx: GraphLangParser.ExpresionAritmeticaContext):
        variable_name = ctx.ID().getText()
        operador = ctx.opAsignacion().getText()

        # Procesar la expresión aritmética completa
        valor = self.eval_expresion_aritmetica_detalle(ctx.expresionAritmeticaDetalle())
        
        if valor is not None:
            if variable_name in self.variables:
                tipo_variable = type(self.variables[variable_name])
                if tipo_variable == int:
                    valor = int(valor)
                elif tipo_variable == float:
                    valor = float(valor)
                else:
                    print(f"Error: Tipo de variable no compatible para la variable '{variable_name}' en línea {ctx.start.line}")
                    return

                if operador == '=':
                    self.variables[variable_name] = valor
                else:
                    print(f"Error: Operador de asignación no válido '{operador}' en línea {ctx.start.line}")
            else:
                print(f"Error: La variable '{variable_name}' no está definida en línea {ctx.start.line}")
        else:
            print(f"Error: Valor no válido para la operación en línea {ctx.start.line}")

        return self.visitChildren(ctx)

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
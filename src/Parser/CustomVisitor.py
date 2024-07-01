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

      def eval_expresion_aritmetica_detalle(self, ctx: GraphLangParser.ExpresionAritmeticaDetalleContext):
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def apply_operator(operands, operator):
            right = operands.pop()
            left = operands.pop()
            if operator == '+':
                operands.append(left + right)
            elif operator == '-':
                operands.append(left - right)
            elif operator == '*':
                operands.append(left * right)
            elif operator == '/':
                operands.append(left / right)

        # Convert expression to postfix notation (RPN)
        output = []
        operators = []
        
        numeros = [float(n.getText()) for n in ctx.numero()]
        operadores = [o.getText() for o in ctx.opAritmetico()]

        # Intercalamos los números y operadores en una lista
        intercalados = []
        for i in range(len(numeros)):
            intercalados.append(numeros[i])
            if i < len(operadores):
                intercalados.append(operadores[i])

        for token in intercalados:
            if isinstance(token, float):
                output.append(token)
            else:
                while operators and precedence(operators[-1]) >= precedence(token):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        # Evaluate RPN expression
        operands = []
        for token in output:
            if isinstance(token, float):
                operands.append(token)
            else:
                apply_operator(operands, token)

        return operands[0]

    def convertir_tipo(self, variable_name):
        if variable_name in self.variables:
            valor = self.variables[variable_name]
            tipo = type(valor)
            if tipo == int:
                if isinstance(valor, float) and valor.is_integer():
                    self.variables[variable_name] = int(valor)
            elif tipo == float:
                self.variables[variable_name] = float(valor)
            elif tipo == bool:
                self.variables[variable_name] = bool(valor)
            elif tipo == str:
                self.variables[variable_name] = str(valor)

    
    def visitImprimir(self, ctx: GraphLangParser.ImprimirContext):
        valor = ctx.literal().getText() if ctx.literal() else self.variables.get(ctx.ID().getText(), None)
        if valor is not None:
            print(valor)
        else:
            print(f"Error: La variable '{ctx.ID().getText()}' no está definida en línea {ctx.start.line}")
        return self.visitChildren(ctx)

    def visitDeclaracionForma(self, ctx: GraphLangParser.DeclaracionFormaContext):
        shape_id = ctx.ID().getText()
        shape = {'id': shape_id, 'type': None, 'params': {}}

        for child in ctx.definicionForma():
            if child.tipoForma():
                shape['type'] = child.tipoForma().getText()
            elif 'radio:' in child.getText():
                shape['params']['radio'] = int(child.numero().getText())
            elif 'ancho:' in child.getText():
                shape['params']['ancho'] = int(child.numero().getText())
            elif 'alto:' in child.getText():
                shape['params']['alto'] = int(child.numero().getText())
            elif 'vertex:' in child.getText():
                vertices = []
                for vertex_ctx in child.vertex():
                    x = int(vertex_ctx.numero(0).getText())
                    y = int(vertex_ctx.numero(1).getText())
                    vertices.append((x, y))
                shape['params']['vertex'] = vertices

        if shape['type'] == 'CIRCULO':
            self.shapes[shape_id] = Circulo(shape['params'])
        elif shape['type'] == 'RECTANGULO':
            self.shapes[shape_id] = Rectangulo(shape['params'])
        elif shape['type'] == 'CUADRADO':
            self.shapes[shape_id] = Cuadrado(shape['params'])
        elif shape['type'] == 'TRIANGULO':
            self.shapes[shape_id] = Triangulo(shape['params'])

        # Suponiendo que `shape` es tu diccionario
        for key, value in shape.items():
            print(f"{key}: {value}")

        return None

    
    def visitDeclaracionTransformacion(self, ctx: GraphLangParser.DeclaracionTransformacionContext):
        transform_id = ctx.ID().getText()
        transformations = {}

        for child in ctx.definicionTransformacion():
            if child.getChild(0).getText() == 'trasladar:':
                translation_values = [
                    int(child.numero(0).getText()),
                    int(child.numero(1).getText())
                ]
                shape_id = child.ID().getText()
                transformations[shape_id] = {'type': 'TRASLACION', 'params': translation_values}

                # Crear una nueva figura con las propiedades modificadas
                if shape_id in self.shapes:
                    original_shape = self.shapes[shape_id]

                    # Imprimir los atributos de original_shape para verificar
                    print(f"Original shape ID: {shape_id}")
                    print(f"Original shape details: {original_shape.__dict__}")

                    new_shape = copy.deepcopy(original_shape)
                    if 'vertex' in new_shape.params:
                        new_shape.params['vertex'] = [
                            (vertex[0] + translation_values[0], vertex[1] + translation_values[1])
                            for vertex in new_shape.params['vertex']
                        ]
                        self.shapes[transform_id] = new_shape
                        print(f"Figura {shape_id} trasladada a nueva figura {transform_id} con vértices {new_shape.params['vertex']}")
                    else:
                        print(f"Error: La forma '{shape_id}' no tiene un atributo 'vertex' en params.")
                else:
                    print(f"Error: Forma '{shape_id}' no encontrada.")

        if transformations:
            self.transformations[transform_id] = transformations
           

        return None

 def visitDeclaracionEscena(self, ctx: GraphLangParser.DeclaracionEscenaContext):
        formas_ids_nodes = ctx.ID()  # Obtiene los nodos de ID
        formas = {}

        # Itera sobre los nodos de ID para obtener los IDs como cadenas
        for shape_id_node in formas_ids_nodes:
            shape_id = shape_id_node.getText()  # Obtiene el texto del nodo como cadena
            if shape_id in self.shapes:
                formas[shape_id] = self.shapes[shape_id]
            else:
                print(f"Error: Forma '{shape_id}' no encontrada en línea {ctx.start.line}")

        self.scene = formas
        self.scene_invocada = True

        # Renderiza la escena después de construirla
        self.render_scene()

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

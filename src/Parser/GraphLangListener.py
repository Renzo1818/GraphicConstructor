# Generated from src/utils/GraphLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GraphLangParser import GraphLangParser
else:
    from GraphLangParser import GraphLangParser

# This class defines a complete listener for a parse tree produced by GraphLangParser.
class GraphLangListener(ParseTreeListener):

    # Enter a parse tree produced by GraphLangParser#programa.
    def enterPrograma(self, ctx:GraphLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#programa.
    def exitPrograma(self, ctx:GraphLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#declaraciones.
    def enterDeclaraciones(self, ctx:GraphLangParser.DeclaracionesContext):
        pass

    # Exit a parse tree produced by GraphLangParser#declaraciones.
    def exitDeclaraciones(self, ctx:GraphLangParser.DeclaracionesContext):
        pass


    # Enter a parse tree produced by GraphLangParser#sentencia.
    def enterSentencia(self, ctx:GraphLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#sentencia.
    def exitSentencia(self, ctx:GraphLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#declaracionVariable.
    def enterDeclaracionVariable(self, ctx:GraphLangParser.DeclaracionVariableContext):
        pass

    # Exit a parse tree produced by GraphLangParser#declaracionVariable.
    def exitDeclaracionVariable(self, ctx:GraphLangParser.DeclaracionVariableContext):
        pass


    # Enter a parse tree produced by GraphLangParser#declaracionIncremental.
    def enterDeclaracionIncremental(self, ctx:GraphLangParser.DeclaracionIncrementalContext):
        pass

    # Exit a parse tree produced by GraphLangParser#declaracionIncremental.
    def exitDeclaracionIncremental(self, ctx:GraphLangParser.DeclaracionIncrementalContext):
        pass


    # Enter a parse tree produced by GraphLangParser#imprimir.
    def enterImprimir(self, ctx:GraphLangParser.ImprimirContext):
        pass

    # Exit a parse tree produced by GraphLangParser#imprimir.
    def exitImprimir(self, ctx:GraphLangParser.ImprimirContext):
        pass


    # Enter a parse tree produced by GraphLangParser#declaracionForma.
    def enterDeclaracionForma(self, ctx:GraphLangParser.DeclaracionFormaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#declaracionForma.
    def exitDeclaracionForma(self, ctx:GraphLangParser.DeclaracionFormaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#declaracionTransformacion.
    def enterDeclaracionTransformacion(self, ctx:GraphLangParser.DeclaracionTransformacionContext):
        pass

    # Exit a parse tree produced by GraphLangParser#declaracionTransformacion.
    def exitDeclaracionTransformacion(self, ctx:GraphLangParser.DeclaracionTransformacionContext):
        pass


    # Enter a parse tree produced by GraphLangParser#declaracionEscena.
    def enterDeclaracionEscena(self, ctx:GraphLangParser.DeclaracionEscenaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#declaracionEscena.
    def exitDeclaracionEscena(self, ctx:GraphLangParser.DeclaracionEscenaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#estructuraControl.
    def enterEstructuraControl(self, ctx:GraphLangParser.EstructuraControlContext):
        pass

    # Exit a parse tree produced by GraphLangParser#estructuraControl.
    def exitEstructuraControl(self, ctx:GraphLangParser.EstructuraControlContext):
        pass


    # Enter a parse tree produced by GraphLangParser#sentenciaIf.
    def enterSentenciaIf(self, ctx:GraphLangParser.SentenciaIfContext):
        pass

    # Exit a parse tree produced by GraphLangParser#sentenciaIf.
    def exitSentenciaIf(self, ctx:GraphLangParser.SentenciaIfContext):
        pass


    # Enter a parse tree produced by GraphLangParser#sentenciaWhile.
    def enterSentenciaWhile(self, ctx:GraphLangParser.SentenciaWhileContext):
        pass

    # Exit a parse tree produced by GraphLangParser#sentenciaWhile.
    def exitSentenciaWhile(self, ctx:GraphLangParser.SentenciaWhileContext):
        pass


    # Enter a parse tree produced by GraphLangParser#sentenciaFor.
    def enterSentenciaFor(self, ctx:GraphLangParser.SentenciaForContext):
        pass

    # Exit a parse tree produced by GraphLangParser#sentenciaFor.
    def exitSentenciaFor(self, ctx:GraphLangParser.SentenciaForContext):
        pass


    # Enter a parse tree produced by GraphLangParser#bloque.
    def enterBloque(self, ctx:GraphLangParser.BloqueContext):
        pass

    # Exit a parse tree produced by GraphLangParser#bloque.
    def exitBloque(self, ctx:GraphLangParser.BloqueContext):
        pass


    # Enter a parse tree produced by GraphLangParser#expresion.
    def enterExpresion(self, ctx:GraphLangParser.ExpresionContext):
        pass

    # Exit a parse tree produced by GraphLangParser#expresion.
    def exitExpresion(self, ctx:GraphLangParser.ExpresionContext):
        pass


    # Enter a parse tree produced by GraphLangParser#expresionComparativa.
    def enterExpresionComparativa(self, ctx:GraphLangParser.ExpresionComparativaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#expresionComparativa.
    def exitExpresionComparativa(self, ctx:GraphLangParser.ExpresionComparativaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#expresionOperacional.
    def enterExpresionOperacional(self, ctx:GraphLangParser.ExpresionOperacionalContext):
        pass

    # Exit a parse tree produced by GraphLangParser#expresionOperacional.
    def exitExpresionOperacional(self, ctx:GraphLangParser.ExpresionOperacionalContext):
        pass


    # Enter a parse tree produced by GraphLangParser#expresionAritmetica.
    def enterExpresionAritmetica(self, ctx:GraphLangParser.ExpresionAritmeticaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#expresionAritmetica.
    def exitExpresionAritmetica(self, ctx:GraphLangParser.ExpresionAritmeticaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#tipo.
    def enterTipo(self, ctx:GraphLangParser.TipoContext):
        pass

    # Exit a parse tree produced by GraphLangParser#tipo.
    def exitTipo(self, ctx:GraphLangParser.TipoContext):
        pass


    # Enter a parse tree produced by GraphLangParser#tipoForma.
    def enterTipoForma(self, ctx:GraphLangParser.TipoFormaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#tipoForma.
    def exitTipoForma(self, ctx:GraphLangParser.TipoFormaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#definicionForma.
    def enterDefinicionForma(self, ctx:GraphLangParser.DefinicionFormaContext):
        pass

    # Exit a parse tree produced by GraphLangParser#definicionForma.
    def exitDefinicionForma(self, ctx:GraphLangParser.DefinicionFormaContext):
        pass


    # Enter a parse tree produced by GraphLangParser#definicionTransformacion.
    def enterDefinicionTransformacion(self, ctx:GraphLangParser.DefinicionTransformacionContext):
        pass

    # Exit a parse tree produced by GraphLangParser#definicionTransformacion.
    def exitDefinicionTransformacion(self, ctx:GraphLangParser.DefinicionTransformacionContext):
        pass


    # Enter a parse tree produced by GraphLangParser#opAsignacion.
    def enterOpAsignacion(self, ctx:GraphLangParser.OpAsignacionContext):
        pass

    # Exit a parse tree produced by GraphLangParser#opAsignacion.
    def exitOpAsignacion(self, ctx:GraphLangParser.OpAsignacionContext):
        pass


    # Enter a parse tree produced by GraphLangParser#opAritmetico.
    def enterOpAritmetico(self, ctx:GraphLangParser.OpAritmeticoContext):
        pass

    # Exit a parse tree produced by GraphLangParser#opAritmetico.
    def exitOpAritmetico(self, ctx:GraphLangParser.OpAritmeticoContext):
        pass


    # Enter a parse tree produced by GraphLangParser#opIncrementales.
    def enterOpIncrementales(self, ctx:GraphLangParser.OpIncrementalesContext):
        pass

    # Exit a parse tree produced by GraphLangParser#opIncrementales.
    def exitOpIncrementales(self, ctx:GraphLangParser.OpIncrementalesContext):
        pass


    # Enter a parse tree produced by GraphLangParser#opLogico.
    def enterOpLogico(self, ctx:GraphLangParser.OpLogicoContext):
        pass

    # Exit a parse tree produced by GraphLangParser#opLogico.
    def exitOpLogico(self, ctx:GraphLangParser.OpLogicoContext):
        pass


    # Enter a parse tree produced by GraphLangParser#opComparacion.
    def enterOpComparacion(self, ctx:GraphLangParser.OpComparacionContext):
        pass

    # Exit a parse tree produced by GraphLangParser#opComparacion.
    def exitOpComparacion(self, ctx:GraphLangParser.OpComparacionContext):
        pass


    # Enter a parse tree produced by GraphLangParser#literal.
    def enterLiteral(self, ctx:GraphLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by GraphLangParser#literal.
    def exitLiteral(self, ctx:GraphLangParser.LiteralContext):
        pass


    # Enter a parse tree produced by GraphLangParser#numero.
    def enterNumero(self, ctx:GraphLangParser.NumeroContext):
        pass

    # Exit a parse tree produced by GraphLangParser#numero.
    def exitNumero(self, ctx:GraphLangParser.NumeroContext):
        pass



del GraphLangParser